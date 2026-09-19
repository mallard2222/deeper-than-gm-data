# GM Bootstrap Handoff
**Status:** prepared (partial — league settings retrieval in flight)  
**Generated (UTC):** 2026-09-19T02:14:24Z  
**Prepared by:** Grok Bot  
**Audience:** Andrew + Codex / Deeper Than GM Work app

---

## 1. Current instructions, workflows, files, routines — and conflicts

### Operating instructions now in force (this conversation)
- Roles: Grok Bot = research/gather/recommend; Deeper Than GM Work app = reconciled state/models; Andrew = approve consequential actions.
- Evidence tiers: verified league facts / analytical judgments / unverified signals — keep separate with sources.
- Approval boundary: research OK; no waivers/FAAB/lineups/trades/publishes/deletes without specific approval. Always ask before roster moves (already standing rule).
- Bootstrap: do **not** enable new schedules or external writes until workflow proposed, tested once, and approved.
- Do not mix leagues; use stable league identifiers.
- Work app URL is illustrative / not a connected production GM; do not treat UI signals as evidence.

### Pre-existing Grok Bot workflows (before this handoff)
1. **Yahoo browser session** on bot computer: signed-in Fantasy Football for `ogdru22@yahoo.com` (session established 2026-09-18 evening CT after VPN-related login failures; password never stored in chat).
2. **League scout** (one-shot, 2026-09-18 ~20:33–20:42 CT): standings, all-team roster snapshots, FA WR scan, Week 2 matchup brief for Deeper Than.
3. **Approved lineup change** (2026-09-18 ~20:55–20:58 CT): Golden → W/T flex; Collins → bench. Yahoo “All changes saved.” Evidence: `/workspace/vaqueros-week2-final.png`.
4. **Drop/waiver/trade monitoring ask** (user): pervasive monitor — led to routine creation (see conflict).

### Active / paused routines
| Routine | Folder | Schedule | Status | Notes |
|---------|--------|----------|--------|-------|
| Deeper Than GM desk | `deeper-than-gm-desk` | Mon–Sat 08:00 America/Chicago | **PAUSED** during bootstrap | Created earlier tonight for drop/waiver/trade monitoring. Conflicts with bootstrap §6 (“do not enable new schedules… during this bootstrap”). Paused pending Andrew approval of new handoff workflow. Never successfully run yet. |

### Relevant files on bot computer (not overwritten)
| Path | Kind | Retrieved / written |
|------|------|---------------------|
| `/workspace/vaqueros-week2-final.png` | Evidence | 2026-09-18 ~20:58 CT |
| `/workspace/vaq-*.png`, `league*.png`, `standings*.png`, `big-roster*.png`, `players*.png`, `wr.yml`, team `*.yml`, `fullsnap.yml` | Raw scout artifacts (Yahoo DOM/screenshots) | 2026-09-18 ~20:33–20:55 CT |
| `/workspace/deeper-than-gm/` | New research tree for this integration (additive) | this handoff |

### Conflicts with these bootstrap instructions
1. **Routine schedule** — already created + was enabled → **paused** to comply with bootstrap. Needs explicit re-enable after workflow approval.
2. **Prior GM posture** — earlier tonight Grok Bot acted as sole “in-season GM”; new model splits research (Grok) vs reconciled state (Work app). No overwrite of Work app; Grok will submit sourced observations rather than treat chat conclusions as league state of record.
3. **Sleeper mis-ID** — briefly mislabeled Deeper Than as Sleeper based on mobile UI resemblance; corrected. Yahoo is source of truth for both leagues.
4. **Incomplete formal research files** — scout lived in chat + ad-hoc `/workspace` dumps, not schema-versioned batches. This handoff starts the structured store without deleting prior dumps.

---

## 2. Connected platforms and data sources

| Source | Connection type | Status | Latest successful retrieval |
|--------|-----------------|--------|----------------------------|
| Yahoo Fantasy (browser session) | Bot Chrome profile, interactive | Connected (session live as of lineup save) | **2026-09-18 ~20:58 CT** (lineup save confirm) |
| Yahoo Fantasy API / MCP connector | Plugin search | **None installed / none found** | n/a |
| 1Password Shared with Grok Bot | Credential fill | **Not connected** | n/a |
| Deeper Than GM Work app (`https://deeper-than-gm.ogdru22.chatgpt.site`) | HTTPS GET probe | **401 Sign in required** (unreachable anonymously) | Probe **2026-09-18 ~21:13 CT** |
| Public web (injury/news) | WebSearch | Available | Collins Grade 1 notes **2026-09-18 ~20:48 CT** |
| Sleeper | — | Not used for these leagues | n/a |

---

## 3. Current league data accessible vs missing

### League identifiers (do not mix)
| Display name | Stable id | Yahoo league id | Team | Role |
|--------------|-----------|-----------------|------|------|
| Deeper Than | `yahoo-ff-668216` | 668216 | Vaqueros (team path `/f1/668216/8`) | **Main / priority** |
| Castle Hills FFL | unknown | unknown | — | Renewal card seen; not managed |

### Verified / observed for `yahoo-ff-668216` (as of 2026-09-18 evening CT scout — **not** a full settings pull yet)
**Verified league facts (from Yahoo UI / screenshots; settings page pending):**
- 8 teams; Week 2 of 2026 season
- Vaqueros 0-1-0, 7th; PF 141.20; waiver budget shown **$100** remaining (implies FAAB — exact rules TBD from settings)
- Matchup vs Big Balls (Brad / “4th”); live proj ~131.14 vs ~170.29 at scout time; Big Balls already had Allen + Amon-Ra scores
- Starting structure observed on roster: **2 QB**, RB, RB, WR, WR, TE, **W/T**, **W/R**, K, DEF — **no IDP slots observed** on this roster
- User-stated format assumptions (await settings confirm): 8 teams, 2QB, full PPR, 6 pt all TDs, 4 playoff teams

**Analytical (not league-of-record):**
- Drop ranking offered: Concepcion Jr. weakest, then Marks
- Trade ideas floated (Nix+Golden; LaPorta packages) — hypotheses only

**Missing (must retrieve before FAAB/trade execution advice):**
- Complete scoring table (PPR value, pass TD, bonuses)
- Official roster maxima, IR/NA, bench size
- Waiver type details (FAAB min bid, process day/time, continuous vs weekly)
- Trade review/veto/deadline
- Keeper rules
- Playoff week numbers / tiebreakers
- Canonical Yahoo player IDs for all rostered players
- Transaction history export
- Current FA list freshness after lineup change


## 4. Integration capabilities (verified vs possible)

| Capability | Verified? | Notes |
|------------|-----------|-------|
| Write structured files on bot disk | **Verified** | `/workspace/deeper-than-gm/**` |
| Attach / deliver files in chat to Andrew | **Verified** | SendToUser attachments |
| Outbound HTTPS GET | **Verified** | `curl`/`urllib`; Work app returns **401** without auth |
| Outbound HTTPS POST to Work app | **Possible, not verified** | Not attempted (bootstrap: no external writes) |
| Remote MCP to Work app | **Not present** | No plugin/MCP found |
| Shared storage with Codex/Work app | **Unknown** | Needs Andrew/Codex to define (e.g. repo, Drive, webhook) |
| Yahoo official API | **Not connected** | Browser scrape/session only |
| Persist credentials in chat | **Forbidden** | Use 1Password Shared vault or box sign-in handoff |

---

## 5. Recommended smallest working integration

**Phase 0 (this handoff) — prepared:** file-based exchange on Grok Bot disk + chat delivery. No Work app write.

**Smallest working loop (propose — needs your approval before enabling):**
1. Grok Bot maintains `/workspace/deeper-than-gm/batches/batch_<id>.json` (schema below) + human brief markdown.
2. Andrew (or Codex with access) copies/pulls the batch into Deeper Than GM for quarantine review (`status: quarantined`).
3. After Andrew approves a recommendation in chat, Grok Bot may execute on Yahoo (lineup/waiver/trade) under the standing permission rule.
4. **Do not** POST to the Work app until Codex publishes an authenticated ingest contract and a one-shot test is approved.

**What Andrew / Codex must complete:**
1. Share how Codex/Work app should **read** batches (manual paste, shared git repo path, signed webhook URL, or MCP). Prefer read-of-files or authenticated HTTPS ingest — not anonymous public POST.
2. Confirm auth path for `https://deeper-than-gm.ogdru22.chatgpt.site` (401 today) if Grok Bot should ever open it in-browser for read-only UI checks (illustrative only until verified).
3. Align JSON schema (`schema_version`) and reject/accept rules for `quarantined` signals.
4. Explicitly approve re-enabling any schedule (replacing paused routine) after one dry-run batch is accepted.
5. Optional: connect 1Password “Shared with Grok Bot” for Yahoo to reduce login friction (no passwords in chat).

---

## 6. Sourced signals (initial batch)

See `batches/batch_20260919T021500Z_bootstrap.json`. Up to five signals included only where sources exist. All `status: quarantined`.

Gap note: full FA waiver board + complete settings not yet in this file; settings agent in flight at handoff draft time.

---

## 7. Copyable summary for Codex

```
GM BOOTSTRAP HANDOFF — Grok Bot → Deeper Than GM
League main: yahoo-ff-668216 (Yahoo Deeper Than / Vaqueros)
Work app URL: https://deeper-than-gm.ogdru22.chatgpt.site → probed 401 anonymous (not production-connected)
Yahoo access: browser session on Grok Bot computer; last success ~2026-09-18 20:58 CT (Golden start / Collins bench saved)
No Yahoo MCP; no 1Password vault connected
Existing Mon–Sat 08:00 CT routine PAUSED for bootstrap compliance (never ran)
Artifact root: /workspace/deeper-than-gm/ (additive; prior scout dumps retained under /workspace/*.png|yml)
Proposed exchange: human brief + schema_versioned JSON batches with signals[].status=quarantined; NO outbound POST until contract + one approved test
Standing rule: Andrew approves all consequential Yahoo actions
Missing: full settings scrape (in progress), FAAB process rules, keeper/playoff detail, stable player IDs, Work app auth/ingest
```
