# Session State — Tallow Cream Launch

## Status: ACTIVE — Launching Batch 5 (CPM Reduction Test)

Product is live. Whipped Tallow & Honey Balm. $49.99 launch price. 1 sale so far (B3C2, $19.99 due to discount error — since fixed).

## Last Session (April 9, 2026)

- **Got first sale** via B3C2 "Water On A Hole" — customer intended to buy at full price ($49.99), got $19.99 due to discount misconfiguration (fixed)
- **Diagnosed high CPMs** as the critical bottleneck. Account running $143-$368 CPMs across most ads. B1C2 "Husband Noticed" is the outlier at $11-15 CPM but CBO starves it.
- **Root cause analysis:** Compared NMN ads (low CPMs) to tallow ads (high CPMs) and found: NMN had explicit compliance rules (no menopause, no "your body" diagnostic claims, no symptom words) that tallow ads abandoned entirely. Also: tallow ads averaged 5 density elements vs the course's Doctor Ad at 10.
- **Updated native-ad-writer skill** with three new rule layers:
  1. **Compliance + readability** (`compliance-and-readability.md`) — 6 middle-ground rules, vocabulary swap table, 6th-grade reading level, pre-write and post-write checklists
  2. **Element density** (`element-density.md`) — 10-element Doctor Ad stack with 8/10 minimum rule, binary counting rubric
  3. Both integrated into SKILL.md workflow (Steps 4, 5, 6, 9) and self-audit-checklist.md
- **Rewrote PDP sections** for Meta compliance — Section 2 (minor), Section 3 (manuka honey medical claims removed), Section 4 (complete rewrite — removed "Your skin isn't dry. It's starving," menopause, 60% stat, all diagnostic claims), Section 6 (removed "damaged"), Section 7 (replaced 6 of 10 reviews — removed psoriasis cure claims, pediatric eczema claim, anti-aging fine-lines claims, anti-medical framing), Section 9 (minor), Section 10 (minor)
- **Wrote Batch 4** (3 ads testing urgency mechanisms) — B4C1 "30-Day Mirror" (calm resolve), B4C2 "I Wanted To Throw Up" (active harm — KILLED at $1000 CPM), B4C3 "Six Weeks From Saturday" (external deadline). B4C2 taught us: active-harm / anti-competitor framing is a separate Meta penalty category not covered in original compliance rules.
- **Wrote Batch 5** (3 ads testing CPM reduction via element density) — B5C1 "Husband Noticed v2" (external dialogue, 10/10 density), B5C2 "I Haven't Told Anyone" (confession opener, 10/10 density), B5C3 "I Gave Up On Moisturizer" (time reversal, 10/10 density). All at 1,400-1,600 words, compliant, 6th-grade reading level.
- **Kill list for B5 launch:** Kill B3C2, B2C3, B3C1, B3C3, B1C1, B2C1, B1C2 (7 ads). Keep B4C1 and B4C3. Launch B5 ad set at $30/day alongside B4 ad set.

## In Progress
- **B5 launch imminent** — all 3 ads written, creatives generated (B5C3 ghost-rings image is excellent, B5C2 coffee mug is clean, B5C1 needs label blur on jar)
- **B4C1 showing promising early signal** — $70 CPM, 15.38% CTR, $0.46 CPC on 13 impressions. Best engagement numbers in the account. Keep running alongside B5.
- **PDP rewrites need to be pushed to Shopify** — liquid files are updated in repo but need to be pasted into Shopify Custom Liquid blocks. Meta's PDP crawler will take 12-24h to refresh after changes go live.

## Next Up
- Push PDP liquid files to Shopify (Sections 2, 3, 4, 6, 7, 9, 10)
- Launch B5 ad set ($30/day, 3 ads)
- Kill the 7 ads listed above
- Monitor B5 CPMs vs B4 CPMs over 48-72 hours — this is the density hypothesis test
- If B5 CPMs come in at $30-70: density + compliance works. Iterate on conversion mechanisms.
- If B5 CPMs stay at $150+: problem is upstream (account-level or PDP) and we need different levers.
- B4C3 Six Weeks — watch for one more day. Kill at $15+ spend with 0 clicks.

## Key Decisions This Session
- **Product IS tallow cream** — not researching new products. Committed.
- **Compliance rules make copy STRONGER, not weaker** — the middle-ground framework keeps emotional punch while passing Meta's scanner
- **Element density is the structural gap** — our best ads had 5 elements, course reference has 10. B5 aims for 10/10 on all three ads.
- **The "husband noticed" hook is the proven CPM winner** — B1C2 at $11.50 CPM was 3-30x cheaper than everything else. B5C1 densifies this exact hook to test if density adds conversion depth.
- **Active-harm framing is a separate Meta penalty** — B4C2 hit $1000 CPM despite being otherwise compliant. "Your cream is making it worse" ≠ "your cream isn't working." Added to compliance awareness but not yet formalized as Rule 7.
- **Kill aggressively, test cleanly** — clearing the entire old CBO to give B5 a clean runway

## Campaign Architecture (After Kills)
- **B4 ad set** (~$30/day): B4C1 30-Day Mirror + B4C3 Six Weeks
- **B5 ad set** (~$30/day): B5C1 Husband Noticed v2 + B5C2 I Haven't Told Anyone + B5C3 I Gave Up
- **Total daily budget:** ~$60
- **Off:** B1C1, B1C2, B1C3, B2C1, B2C2, B2C3, B3C1, B3C2, B3C3, B4C2

## Key Files (Tallow)
| File | Purpose |
|------|---------|
| `tallow-cream/tracking/Ad_Performance_Tracker.csv` | Daily ad performance |
| `tallow-cream/tracking/Tallow_Brand_Growth_Sheet.csv` | Batch plans + status |
| `tallow-cream/tracking/Kill_Rules_and_Decision_Framework.md` | Hard/soft kill rules |
| `tallow-cream/avatars/sub-avatars/Sub_Avatar_5_The_Invisible_Woman.md` | Primary avatar |
| `tallow-cream/avatars/Avatar_Language_Research.md` | Verbatim customer language |
| `tallow-cream/store/store-liquid/` | PDP section liquid files (updated for compliance) |
| `tallow-cream/ads/batch-5/copy/` | Current batch ad copy |
| `.claude/skills/native-ad-writer/` | Native ad writing skill (updated with compliance + density) |

## Updated
2026-04-09
