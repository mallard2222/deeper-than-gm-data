#!/usr/bin/env python3
"""Weekly usage table for Deeper Than (yahoo-ff-668216) roster + candidates.

Public data only (no Yahoo login). Sources (nflverse-data GitHub releases):
  stats_player/stats_player_week_<season>.csv  -> targets, carries, target_share
  snap_counts/snap_counts_<season>.csv          -> offense snaps / snap pct (PFR-derived)
  pbp/play_by_play_<season>.csv.gz              -> red-zone targets / carries (yardline_100 <= 20)
Routes run are not published in nflverse -> always null.

Usage:
  python3 build_usage_table.py --season 2026 --through-week 9 \
      --players grok/tools/usage_players_yahoo-ff-668216.csv \
      --out grok/intel/yahoo-ff-668216/2026/usage/usage-2026-W01-W09.csv [--cache /tmp/nflverse]

Rules: one row per tracked player per week. If a player has no nflverse record that week
(bye, inactive, injured, not yet in league, etc.) the numeric fields are left empty (null)
and record_status says which source had nothing. Nothing is inferred or zero-filled.
"""
import argparse, os, urllib.request, datetime
from zoneinfo import ZoneInfo
import pandas as pd

BASE = "https://github.com/nflverse/nflverse-data/releases/download"
def urls(season):
    return {
        "stats": f"{BASE}/stats_player/stats_player_week_{season}.csv",
        "snaps": f"{BASE}/snap_counts/snap_counts_{season}.csv",
        "pbp": f"{BASE}/pbp/play_by_play_{season}.csv.gz",
        "players": f"{BASE}/players/players.csv",
    }

def fetch(url, cache):
    os.makedirs(cache, exist_ok=True)
    path = os.path.join(cache, os.path.basename(url))
    if not os.path.exists(path):
        urllib.request.urlretrieve(url, path)
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=2026)
    ap.add_argument("--through-week", type=int, required=True)
    ap.add_argument("--from-week", type=int, default=1)
    ap.add_argument("--players", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache", default="/tmp/nflverse")
    a = ap.parse_args()
    collected_at = datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%dT%H:%M:%S%z")
    U = urls(a.season)
    tracked = pd.read_csv(a.players, dtype=str)
    stats = pd.read_csv(fetch(U["stats"], a.cache), low_memory=False)
    stats = stats[stats.season_type == "REG"]
    snaps = pd.read_csv(fetch(U["snaps"], a.cache), low_memory=False)
    snaps = snaps[snaps.game_type == "REG"]
    players = pd.read_csv(fetch(U["players"], a.cache), low_memory=False, dtype=str)
    pbp = pd.read_csv(fetch(U["pbp"], a.cache), low_memory=False,
                      usecols=["season_type", "week", "posteam", "yardline_100", "play_type",
                               "receiver_player_id", "rusher_player_id", "two_point_attempt",
                               "qb_kneel", "pass_attempt", "rush_attempt", "sack"])
    pbp = pbp[(pbp.season_type == "REG")]
    rz = pbp[(pbp.yardline_100 <= 20) & (pbp.two_point_attempt != 1) & pbp.play_type.isin(["pass", "run"])]  # excludes no_play (penalty-nullified)
    rz_t = rz[(rz.pass_attempt == 1) & (rz.sack != 1) & rz.receiver_player_id.notna()] \
        .groupby(["week", "receiver_player_id"]).size()
    rz_c = rz[(rz.rush_attempt == 1) & (rz.qb_kneel != 1) & rz.rusher_player_id.notna()] \
        .groupby(["week", "rusher_player_id"]).size()
    pfr = players.set_index("gsis_id")["pfr_id"].to_dict()
    weeks_present = set(stats.week.unique())
    rows = []
    for _, p in tracked.iterrows():
        g = p.gsis_id
        for wk in range(a.from_week, a.through_week + 1):
            st = stats[(stats.player_id == g) & (stats.week == wk)]
            sn = snaps[(snaps.pfr_player_id == pfr.get(g)) & (snaps.week == wk)] if pfr.get(g) else snaps.iloc[0:0]
            status = []
            if wk not in weeks_present:
                status.append("week_not_in_source")
            if st.empty: status.append("no_stats_row")
            if sn.empty: status.append("no_snap_row")
            team = (st.team.iloc[0] if not st.empty else (sn.team.iloc[0] if not sn.empty else None))
            opp = (st.opponent_team.iloc[0] if not st.empty else (sn.opponent.iloc[0] if not sn.empty else None))
            has_game = (not st.empty) or (not sn.empty)
            def v(df, col):
                return None if df.empty or pd.isna(df[col].iloc[0]) else df[col].iloc[0]
            rows.append({
                "season": a.season, "week": wk, "group": p.group, "player_name": p.player_name,
                "position": p.position, "gsis_id": g, "pfr_id": pfr.get(g),
                "yahoo_player_id": p.yahoo_player_id if isinstance(p.yahoo_player_id, str) else None,
                "team": team, "opponent": opp,
                "snaps": v(sn, "offense_snaps"),
                "snap_pct": None if sn.empty or pd.isna(sn.offense_pct.iloc[0]) else round(float(sn.offense_pct.iloc[0]), 3),
                "routes": None,
                "targets": v(st, "targets"),
                "target_share": None if st.empty or pd.isna(st.target_share.iloc[0]) else round(float(st.target_share.iloc[0]), 3),
                "carries": v(st, "carries"),
                # red-zone counts only when the player has a game record that week; 0 = played, no RZ work
                "rz_targets": int(rz_t.get((wk, g), 0)) if has_game else None,
                "rz_carries": int(rz_c.get((wk, g), 0)) if has_game else None,
                "record_status": "ok" if not status else ";".join(status),
                "source": "nflverse-data releases: stats_player_week_%d.csv (targets/carries/target_share); snap_counts_%d.csv (offense snaps/pct, PFR); play_by_play_%d.csv.gz (RZ = yardline_100<=20, excl. 2pt/sacks/kneels/no-plays); routes not published" % (a.season, a.season, a.season),
                "collected_at": collected_at,
            })
    out = pd.DataFrame(rows)
    for c in ["snaps", "targets", "carries", "rz_targets", "rz_carries"]:
        out[c] = out[c].astype("Int64")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    out.to_csv(a.out, index=False)
    print(f"wrote {len(out)} rows -> {a.out}")

if __name__ == "__main__":
    main()
