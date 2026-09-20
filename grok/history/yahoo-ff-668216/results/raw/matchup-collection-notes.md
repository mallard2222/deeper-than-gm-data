# Deeper Than matchup collection notes

Collection date: 2026-09-19 (UTC-5)

## Completed
- 2023, Yahoo league 69639: 64 Final records, weeks 1–16. Weeks 1–6 were pre-existing and untouched; weeks 7–16 appended. Regular weeks 7–14 plus championship/consolation weeks 15–16.
- 2022, Yahoo league 59165: 64 Final records, weeks 1–16. Regular weeks 1–14 plus championship/consolation weeks 15–16.
- 2026, Yahoo league 668216: 4 Final records, week 1 only. Week 2 was visibly marked “In progress” and was not captured.

## Not yet collected
Remaining requested seasons after the historical collection below: 2017=122934, 2016=79234, 2015=1044, 2014=76443, 2013=11558. No placeholder matchup records were created.

## Rate limits / safety
No HTTP 999/429 block was encountered during this run. Pages were loaded slowly with several-second waits. No Yahoo writes, lineup changes, claims, or trades were performed.

## Evidence
- 2022: `results/evidence/2022/week1-final.png`, `results/evidence/2022/week16-final.png`
- 2023: `results/evidence/2023/week15-brackets.png`, `results/evidence/2023/week16-final.png`
- 2026: `results/evidence/2026/week1-final.png`

Scores are the first displayed values on Yahoo matchup cards; adjacent displayed values are projections and were excluded.

## Historical collection completed (this run)
- 2021, Yahoo league 771925: 64 Final records, weeks 1-16. Regular weeks 1-14; championship/consolation brackets weeks 15-16. Files: `results/matchups/2021-matchups.jsonl`, `results/identities/2021-teams.json`. Evidence: `results/evidence/2021/week1-final.png`, `results/evidence/2021/week16-final.png`.
- 2020, Yahoo league 26564: 64 Final records, weeks 1-16. Regular weeks 1-14; championship/consolation brackets weeks 15-16. Files: `results/matchups/2020-matchups.jsonl`, `results/identities/2020-teams.json`. Evidence: `results/evidence/2020/week1-final.png`, `results/evidence/2020/week16-final.png`.
- 2019, Yahoo league 56453: 64 Final records, weeks 1-16. Regular weeks 1-14; championship/consolation brackets weeks 15-16. Files: `results/matchups/2019-matchups.jsonl`, `results/identities/2019-teams.json`. Evidence: `results/evidence/2019/week1-final.png`, `results/evidence/2019/week16-final.png`.

For these seasons Yahoo's supplied `/f1/<id>/schedule?week=N` path returned a problem/404, so the equivalent read-only archived league standings Matchups route was used: `/<year>/f1/<id>?module=standings&lhst=matchups&matchup_week=N`. No Yahoo writes, lineup changes, claims, or trades were performed. No HTTP 999/429 encountered. Matchup scores are the first displayed final values; adjacent projection values were excluded.

- 2018, Yahoo league 16765: 64 Final records, weeks 1-16. Regular weeks 1-14; championship/consolation brackets weeks 15-16. Files: `results/matchups/2018-matchups.jsonl`, `results/identities/2018-teams.json`. Evidence: `results/evidence/2018/week1-final.png`, `results/evidence/2018/week16-final.png`.

Remaining requested historical seasons not collected in this run: 2017 (league 122934), 2016 (79234), 2015 (1044), 2014 (76443), 2013 (11558).

## 2017–2016 collection attempt (stopped on Yahoo rate limit)
- 2017, Yahoo league 122934: 64 Final records, weeks 1–16. Regular weeks 1–14 (56 records), championship/consolation brackets weeks 15–16 (8 records). Files: `results/matchups/2017-matchups.jsonl`, `results/identities/2017-teams.json`. Evidence: `results/evidence/2017/week15-brackets.png`.
- 2016, Yahoo league 79234: 60 Final records, weeks 1–15 only. Regular weeks 1–14 (56 records), championship/consolation brackets week 15 (4 records). Week 16 was not collected. Files: `results/matchups/2016-matchups.jsonl`, `results/identities/2016-teams.json`.
- Route used: archived read-only standings Matchups UI, `/<year>/f1/<league_id>?module=standings&lhst=matchups&matchup_week=N`, which displayed `Final results`. Scores are the first displayed values on each matchup card; adjacent values are projections and were excluded.
- Yahoo returned HTTP 999 while loading 2016 week 16 (`https://football.fantasysports.yahoo.com/2016/f1/79234?matchup_week=16&module=matchups&lhst=matchups`). Per instructions, collection stopped immediately. No Yahoo writes, lineup changes, claims, or trades were performed.

## 2016–2013 continuation attempt (stopped on Yahoo rate limit)
- Cool-down was honored before retrying 2016 week 16 via the archived read-only standings Matchups route.
- Yahoo returned HTTP 999 immediately for `https://football.fantasysports.yahoo.com/2016/f1/79234?module=standings&lhst=matchups&matchup_week=16`.
- Per instructions, stopped immediately; no retries, no Yahoo writes, lineup changes, claims, or trades.
- No new matchup or identity files were created for 2016 week 16, 2015 (league 1044), 2014 (league 76443), or 2013 (league 11558). Existing 2016 file remains 60 records for weeks 1–15, with no duplicates.
- Evidence screenshots were not captured for this blocked attempt.

## Saturday evening cool-down resume (2026-09-19 ~19:09 America/Chicago) — still blocked
- Finite routine "Resume Deeper Than matchup scrape" fired after intentional weekend cool-down.
- Opened read-only archived Matchups URL for 2016 week 16 (league 79234): `https://football.fantasysports.yahoo.com/2016/f1/79234?module=standings&lhst=matchups&matchup_week=16`
- Yahoo returned plain-text **Request denied** (HTTP 999-class rate limit). Stopped immediately; no retries; no Yahoo writes.
- No new matchup rows appended. `2016-matchups.jsonl` remains 60 records (weeks 1–15). 2015/2014/2013 not attempted after the block.
- Evidence: `results/evidence/2016/week16-request-denied-2026-09-19.webp`
- Next plan: longer cool-down (24–48h), single-page probe of 2016 W16 only, then 2015→2014→2013 if clear. Finite Saturday resume routine deleted after this run.
