#!/usr/bin/env python3
"""Weekly usage table for Deeper Than (yahoo-ff-668216) roster + candidates.

Public data only (no Yahoo login). Sources (nflverse-data GitHub releases):
  stats_player/stats_player_week_<season>.csv  -> targets, carries, target_share
  snap_counts/snap_counts_<season>.csv          -> offense snaps / snap pct (PFR-derived)
  pbp/play_by_play_<season>.csv.gz              -> red-zone targets / carries (yardline_100 <= 20)
  schedules/games.csv                           -> game final status (pbp coverage check)
Routes run are not published in nflverse -> always null.
Every run revalidates each cached source (conditional GET). Per-source retrieval time, ETag,
Last-Modified and sha256 are written to the CSV and to <out>-sources.json; built_at is separate.
Red-zone zeros are only written for games whose play-by-play coverage is verified complete.

Usage:
  python3 build_usage_table.py --season 2026 --through-week 9 \
      --players grok/tools/usage_players_yahoo-ff-668216.csv \
      --out grok/intel/yahoo-ff-668216/2026/usage/usage-2026-W01-W09.csv [--cache /tmp/nflverse]

Rules: one row per tracked player per week. If a player has no nflverse record that week
(bye, inactive, injured, not yet in league, etc.) the numeric fields are left empty (null)
and record_status says which source had nothing. Nothing is inferred or zero-filled.
"""
import argparse, os, urllib.request, urllib.error, datetime, hashlib, json, shutil
from zoneinfo import ZoneInfo
import pandas as pd

BASE = "https://github.com/nflverse/nflverse-data/releases/download"
def urls(season):
    return {
        "stats": f"{BASE}/stats_player/stats_player_week_{season}.csv",
        "snaps": f"{BASE}/snap_counts/snap_counts_{season}.csv",
        "pbp": f"{BASE}/pbp/play_by_play_{season}.csv.gz",
        "players": f"{BASE}/players/players.csv",
        "games": f"{BASE}/schedules/games.csv",
    }

def _now():
    return datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%dT%H:%M:%S%z")

def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def fetch(url, cache, manifest, offline=False):
    """Revalidate every run with a conditional GET (If-None-Match / If-Modified-Since).
    200 -> re-downloaded; 304 -> cached copy confirmed current by the server.
    Records per-source retrieval/validation time, ETag, Last-Modified, sha256 and the result.
    If the network fails, the cached copy is used but flagged `stale_unvalidated` with its
    original retrieval time (it never inherits the build time)."""
    os.makedirs(cache, exist_ok=True)
    name = os.path.basename(url)
    path = os.path.join(cache, name)
    meta_path = path + ".meta.json"
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) and os.path.exists(path) else {}
    rec = {"source": name, "url": url}
    req = urllib.request.Request(url, headers={"User-Agent": "deeper-than-usage/1.1"})
    if meta.get("etag"):
        req.add_header("If-None-Match", meta["etag"])
    if meta.get("last_modified"):
        req.add_header("If-Modified-Since", meta["last_modified"])
    try:
        if offline:
            raise OSError("offline mode")
        with urllib.request.urlopen(req, timeout=120) as r:
            tmp = path + ".part"
            with open(tmp, "wb") as f:
                shutil.copyfileobj(r, f)
            os.replace(tmp, path)
            meta = {"etag": r.headers.get("ETag"), "last_modified": r.headers.get("Last-Modified"),
                    "retrieved_at": _now()}
            rec["result"] = "downloaded_200"
    except urllib.error.HTTPError as e:
        if e.code == 304 and meta:
            meta["etag"] = e.headers.get("ETag") or meta.get("etag")
            meta["last_modified"] = e.headers.get("Last-Modified") or meta.get("last_modified")
            rec["result"] = "not_modified_304"
        elif meta:
            rec["result"] = f"stale_unvalidated (HTTP {e.code})"
        else:
            raise
        meta["validated_at"] = _now() if e.code == 304 else meta.get("validated_at")
    except (urllib.error.URLError, OSError) as e:
        if not meta:
            raise
        rec["result"] = f"stale_unvalidated ({type(e).__name__}: {e})"
    if rec["result"] == "downloaded_200":
        meta["validated_at"] = meta["retrieved_at"]
    meta["sha256"] = _sha256(path)
    json.dump(meta, open(meta_path, "w"), indent=1)
    rec.update({"source_retrieved_at": meta.get("retrieved_at"), "source_validated_at": meta.get("validated_at"),
                "etag": meta.get("etag"), "last_modified": meta.get("last_modified"), "sha256": meta["sha256"]})
    manifest.append(rec)
    return path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", type=int, default=2026)
    ap.add_argument("--through-week", type=int, required=True)
    ap.add_argument("--from-week", type=int, default=1)
    ap.add_argument("--players", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--cache", default="/tmp/nflverse")
    ap.add_argument("--offline", action="store_true", help="skip network; cached files flagged stale_unvalidated")
    a = ap.parse_args()
    built_at = _now()
    manifest = []
    U = urls(a.season)
    tracked = pd.read_csv(a.players, dtype=str)
    stats = pd.read_csv(fetch(U["stats"], a.cache, manifest, a.offline), low_memory=False)
    stats = stats[stats.season_type == "REG"]
    snaps = pd.read_csv(fetch(U["snaps"], a.cache, manifest, a.offline), low_memory=False)
    snaps = snaps[snaps.game_type == "REG"]
    players = pd.read_csv(fetch(U["players"], a.cache, manifest, a.offline), low_memory=False, dtype=str)
    pbp = pd.read_csv(fetch(U["pbp"], a.cache, manifest, a.offline), low_memory=False,
                      usecols=["game_id", "desc", "game_seconds_remaining", "season_type", "week", "posteam", "yardline_100", "play_type",
                               "receiver_player_id", "rusher_player_id", "two_point_attempt",
                               "qb_kneel", "pass_attempt", "rush_attempt", "sack"])
    pbp = pbp[(pbp.season_type == "REG")]
    games = pd.read_csv(fetch(U["games"], a.cache, manifest, a.offline), low_memory=False)
    games = games[(games.season == a.season) & (games.game_type == "REG")].set_index("game_id")
    # play-by-play coverage per game: plays for both teams, END GAME / clock 0, and schedule says final
    cov = {}
    for gid, gp in pbp.groupby("game_id"):
        teams = set(gp.posteam.dropna().unique())
        sched = games.loc[gid] if gid in games.index else None
        expected = {sched.home_team, sched.away_team} if sched is not None else set()
        ended = bool(gp.desc.astype(str).str.contains("END GAME").any() or (gp.game_seconds_remaining.min() == 0))
        final = sched is not None and pd.notna(sched.home_score) and pd.notna(sched.away_score)
        if sched is None:
            cov[gid] = "pbp_game_not_in_schedule"
        elif expected and not expected.issubset(teams):
            cov[gid] = "pbp_partial_missing_team"
        elif not ended:
            cov[gid] = "pbp_partial_not_through_final"
        elif not final:
            cov[gid] = "schedule_not_final"
        else:
            cov[gid] = "complete"
    rz = pbp[(pbp.yardline_100 <= 20) & (pbp.two_point_attempt != 1) & pbp.play_type.isin(["pass", "run"])]  # excludes no_play (penalty-nullified)
    rz_t = rz[(rz.pass_attempt == 1) & (rz.sack != 1) & rz.receiver_player_id.notna()] \
        .groupby(["week", "receiver_player_id"]).size()
    rz_c = rz[(rz.rush_attempt == 1) & (rz.qb_kneel != 1) & rz.rusher_player_id.notna()] \
        .groupby(["week", "rusher_player_id"]).size()
    pfr = players.set_index("gsis_id")["pfr_id"].to_dict()
    weeks_present = set(stats.week.unique())
    src = {m["source"]: m for m in manifest}
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
            gid = (st.game_id.iloc[0] if not st.empty else (sn.game_id.iloc[0] if not sn.empty else None))
            if not has_game:
                pbp_cov = "no_game_record"
            elif gid is None or pd.isna(gid):
                pbp_cov = "game_id_unknown"
            else:
                pbp_cov = cov.get(gid, "pbp_game_missing")
            rz_ok = pbp_cov == "complete"
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
                "game_id": gid,
                # 0 only when pbp coverage for that game is verified complete; otherwise null
                "rz_targets": int(rz_t.get((wk, g), 0)) if rz_ok else None,
                "rz_carries": int(rz_c.get((wk, g), 0)) if rz_ok else None,
                "pbp_coverage": pbp_cov,
                "record_status": "ok" if not status else ";".join(status),
                "source": "nflverse-data releases: stats_player_week_%d.csv (targets/carries/target_share); snap_counts_%d.csv (offense snaps/pct, PFR); play_by_play_%d.csv.gz (RZ = yardline_100<=20, excl. 2pt/sacks/kneels/no-plays); routes not published" % (a.season, a.season, a.season),
                "stats_retrieved_at": src["stats_player_week_%d.csv" % a.season]["source_retrieved_at"],
                "snaps_retrieved_at": src["snap_counts_%d.csv" % a.season]["source_retrieved_at"],
                "pbp_retrieved_at": src["play_by_play_%d.csv.gz" % a.season]["source_retrieved_at"],
                "sources_validation": ";".join(f"{m['source']}={m['result']}" for m in manifest),
                "built_at": built_at,
            })
    out = pd.DataFrame(rows)
    for c in ["snaps", "targets", "carries", "rz_targets", "rz_carries"]:
        out[c] = out[c].astype("Int64")
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    out.to_csv(a.out, index=False)
    man_path = os.path.splitext(a.out)[0] + "-sources.json"
    json.dump({"built_at": built_at, "season": a.season, "weeks": [a.from_week, a.through_week],
               "players_file": a.players, "sources": manifest,
               "pbp_game_coverage": {k: v for k, v in sorted(cov.items())}}, open(man_path, "w"), indent=1)
    print(f"wrote {len(out)} rows -> {a.out}; manifest -> {man_path}")
    for m in manifest:
        print(m["source"], m["result"], m["source_retrieved_at"])

if __name__ == "__main__":
    main()
