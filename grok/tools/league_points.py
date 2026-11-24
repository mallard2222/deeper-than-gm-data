#!/usr/bin/env python3
"""Compute Deeper Than (yahoo-ff-668216) league-scored fantasy points per NFL player-week
from public nflverse data. Scoring = Yahoo settings captured 2026-11-10 (W10 settings.json):
pass 25 yd/pt, 4 pass TD, INT -2; rush/rec 10 yd/pt, 6 TD; 0.5 PPR; 2PT 2; fumble lost -2;
return TD 6. K: FG 0-39=3, 40-49=4, 50+=5; miss 0-19 -2, 20-29 -1 (30+ misses 0); PAT 1, PAT miss -1.
DEF: sack 1, INT 2, fumble rec 2, TD 6, safety 2, block 2, points-allowed tiers 15/10/8/4/0/-5/-10.
DEF points-allowed uses the opponent's final score from games.csv (APPROXIMATION: Yahoo may
exclude points the opponent scored via its own defense/ST; flagged as approx).
Output: CSV with one row per (yahoo_player_id or team DEF, week). Missing = empty, never zero-filled.
"""
import argparse, pandas as pd, numpy as np

def off_points(r):
    g = lambda c: (r.get(c) if pd.notna(r.get(c)) else 0)
    p = g('passing_yards')/25 + 4*g('passing_tds') - 2*g('passing_interceptions')
    p += g('rushing_yards')/10 + 6*g('rushing_tds') + g('receiving_yards')/10 + 6*g('receiving_tds')
    p += 0.5*g('receptions') + 2*(g('passing_2pt_conversions')+g('rushing_2pt_conversions')+g('receiving_2pt_conversions'))
    p += 6*g('special_teams_tds')
    p -= 2*(g('rushing_fumbles_lost')+g('receiving_fumbles_lost')+g('sack_fumbles_lost'))
    k = 3*(g('fg_made_0_19')+g('fg_made_20_29')+g('fg_made_30_39')) + 4*g('fg_made_40_49') + 5*(g('fg_made_50_59')+g('fg_made_60_'))
    k += -2*g('fg_missed_0_19') - 1*g('fg_missed_20_29') + g('pat_made') - g('pat_missed')
    return round(p + k, 2)

def pa_pts(pa):
    if pd.isna(pa): return np.nan
    for hi, pts in [(0,15),(6,10),(13,8),(20,4),(27,0),(34,-5)]:
        if pa <= hi: return pts
    return -10

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cache', default='/workspace/nflverse-cache')
    ap.add_argument('--season', type=int, default=2026)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    s = pd.read_csv(f'{a.cache}/stats_player_week_{a.season}.csv', low_memory=False)
    s = s[s.season_type == 'REG']
    s['league_pts'] = s.apply(off_points, axis=1)
    ids = pd.read_csv(f'{a.cache}/db_playerids.csv', low_memory=False)[['gsis_id','yahoo_id']].dropna()
    ids['yahoo_id'] = ids.yahoo_id.astype(int)
    s = s.merge(ids.drop_duplicates('gsis_id'), left_on='player_id', right_on='gsis_id', how='left')
    out = s[['player_id','yahoo_id','player_display_name','position','team','opponent_team','week','league_pts',
             'targets','receptions','receiving_yards','carries','rushing_yards','passing_yards','passing_tds',
             'rushing_tds','receiving_tds','target_share']].rename(columns={'player_id':'gsis_id'})
    out['kind'] = 'player'
    # DEF
    t = pd.read_csv(f'{a.cache}/stats_team_week_{a.season}.csv', low_memory=False)
    t = t[t.season_type == 'REG']
    gm = pd.read_csv(f'{a.cache}/games.csv'); gm = gm[(gm.season == a.season) & (gm.game_type == 'REG')]
    sc = pd.concat([gm.assign(team=gm.home_team, pa=gm.away_score)[['week','team','pa']],
                    gm.assign(team=gm.away_team, pa=gm.home_score)[['week','team','pa']]])
    t = t.merge(sc, on=['week','team'], how='left')
    f = lambda c: t[c].fillna(0) if c in t else 0
    t['league_pts'] = (f('def_sacks') + 2*f('def_interceptions') + 2*f('fumble_recovery_opp') + 6*(f('def_tds')+f('special_teams_tds'))
                       + 2*f('def_safeties') + 2*(f('def_punt_blocks')+f('def_fg_blocks')+f('def_pat_blocks')) + t.pa.map(pa_pts)).round(2)
    d = t[['team','opponent_team','week','league_pts','pa']].copy()
    d['kind'] = 'DEF_approx'; d['player_display_name'] = d.team + ' DEF'; d['position'] = 'DEF'
    out = pd.concat([out, d], ignore_index=True)
    out.to_csv(a.out, index=False)
    print('rows', len(out), 'weeks', sorted(out.week.unique()))
main()
