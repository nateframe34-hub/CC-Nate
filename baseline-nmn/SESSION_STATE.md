# Session State — Tallow Cream Launch

## Status: ACTIVE — Batch 10 LIVE (First New-Avatar CPM Test)

Product is live. Whipped Tallow & Honey Balm. $49.99 launch price. **4 total sales to date:** B3C2 ($19.99 discount error), B5C1 ($49.99 — first full-price), B7C1 ×2 ($99.98). Zero sales since April 12.

## Last Session (April 14, 2026)

- **Batch 10 LAUNCHED** — first ad set targeting a new sub-avatar (The Homesteader Mom, Sub-Avatar #6) after 9 batches of Invisible Woman ads stuck at $150-400 CPMs. Dual-axis test: validates CPM-reduction hypothesis AND tests three angles in parallel.
  - B10C1 Two Lives — Kitchen/Bathroom Gap angle
  - B10C2 For The Kids First — Child Gateway angle
  - B10C3 Maintenance — Permission to Care for Yourself angle (strongest ad in project library per review)
- **All 3 B10 ads written under the validated Homesteader Mom research.** Body formula locked: Solution-Aware, accidental discovery, peer-adjacent non-medical authority, water-vs-oil mechanism compressed to ~60 words (she's already philosophically pre-sold), household-utility close (NOT husband-notice). 10/10 density, full compliance.
- **Image prompts rewritten for scroll-stop realism** — each tied to a specific story moment (ingredient-list read at kitchen table, balm applied to kid's inner elbow at bathtime, hand hesitating over $38 jar at farmers market). All three now specify iPhone-candid aesthetic, real working hands, mundane environmental details, zero brand logos.
- **Homesteader Mom deep research COMPLETE.** Sub-Avatar 6 doc polished with validated angles, competitive landscape (Toups & Co is Jill Winger–endorsed incumbent; Primally Pure has Ballerina Farm endorsement + known FTC issue), 72 verbatim-sourced quotes, banned-language list of 16 phrases. Brand voice reference built.
- **4 candidate sub-avatars drafted as hypothesis docs** (pending Batch 10 CPM data):
  - Sub-Avatar 7 Carnivore Woman (Tier 1 — next in research queue if B10 validates)
  - Sub-Avatar 8 Postpartum Mom (Tier 1 — tied with Carnivore)
  - Sub-Avatar 9 Tween Daughter's Mom (Tier 2 — Sephora-kids cultural moment)
  - Sub-Avatar 10 Clean Eater (Tier 2 — flagged "avatar vs. angle" for research to determine)
- **B1-B6 feedback loops written.** 12 per-ad postmortems in `tallow-cream/feedback-loops/`. Identified converter formula: Solution Aware + accidental discovery + peer-adjacent authority + water-vs-oil mechanism at 50-60% + husband-notice close (for Invisible Woman) or household-utility close (for Homesteader).

## In Progress

- **B10 delivery data pending** — 48-72 hour window to validate the CPM-reduction hypothesis. Homesteader Mom lives in "parenting/homesteading/natural living" Meta audience classification; projected $30-100 CPM range based on research.
- **Stream idle timeout issue on Anthropic API** — Opus 4.6 [1M] and Sonnet both hitting it during long native-ad writing tasks. Workaround: pre-resolve the story skeleton in prompts so model doesn't trigger extended thinking; write to disk via Write tool rather than rendering in chat. Report filed with Anthropic pending.
- **Shopify PDP is COMPLIANT (confirmed April 14)** — Nate pushed the rewritten liquid files to Shopify Custom Liquid blocks when they were originally written. PDP non-compliance is RULED OUT as a CPM driver. Remaining upstream CPM candidates: Account Quality Score, Page Quality (Sarah Lawson page), Pixel fragmentation (NMN→tallow training carryover), Avatar pocket bias (pixel learned only on Invisible Woman conversions).

## Next Up

- **Monitor B10 CPMs for 48-72 hours.** Key questions:
  - Do Homesteader-targeted ads deliver at $30-100 CPM (validates avatar-saturation hypothesis)?
  - Do any of the 3 angles convert at full price?
  - Does B10C3 Maintenance (strongest ad written to date) outperform its siblings?
- **If B10 validates CPM hypothesis:** commission deep research for Sub-Avatar 7 Carnivore Woman OR Sub-Avatar 8 Postpartum Mom. Both are Tier 1.
- **If B10 fails (CPMs stay $150+):** avatar isn't the bottleneck. Investigate upstream: pixel classification, Shopify product categorization, fresh-campaign duplicate test with the 3 converters (B3C2 + B5C1 + B7C1).
- **Shopify PDP liquid files still need to be pushed live** — files are updated in repo for Meta 2026 compliance but haven't been pasted into Custom Liquid blocks yet. This may be contributing to upstream CPM pressure.

## Key Decisions This Session

- **Batch 10 is the first new-avatar test in the project.** Every prior batch (B1-B9) targeted Sub-Avatar #5 (The Invisible Woman). B10 is the strategic pivot.
- **Husband-notice close is NOT universal.** Works for Invisible Woman (grieving invisibility). For Homesteader Mom, household-utility close (one jar for four family members) outperforms because it bypasses self-spending guilt.
- **"Safe enough to eat" is the north-star phrase for the Homesteader avatar.** Used in B10C3 as specified. Origin: Emilie Toups (Toups & Co Organics).
- **16 phrases are banned-list for Homesteader ads.** Not stylistic preferences — trust-terminators. Includes "all-natural," "clean beauty," "anti-aging as lead," "radiant/glowing/luminous/dewy," "luxury," "revolutionary." Enforced in all three B10 ads.
- **B10C3 Maintenance is the strongest ad in the project library.** Self-spending-guilt backstory, Aunt Pat as peer-adjacent authority, mirror-wince unexpected discovery, stewardship close ("Not vanity. Maintenance."). Template for future Carnivore / Postpartum ads if avatar hypothesis validates.
- **Research queue discipline: one avatar at a time.** Don't commission Tier 2 research until Tier 1 produces usable data. Don't commission Tier 1 until Batch 10 validates the CPM hypothesis.

## Campaign Architecture (April 14)

- **Active ads:** B7C1 She Used Pond's (keep — 2 prior full-price sales), B5C1 Husband Noticed v2 (keep — first full-price sale)
- **B9 ad set** (processing → active): B9C1 Chart On The Wall, B9C2 Softer, B9C3 One Jar
- **B10 ad set** (LIVE — new avatar): B10C1 Two Lives, B10C2 For The Kids First, B10C3 Maintenance
- **Killed:** All of B1, B2, B3, B4, B6 (individual ads), B8 (entire batch — NMN-mirror hypothesis falsified)

## Key Files (Tallow)

| File | Purpose |
|------|---------|
| `tallow-cream/tracking/Ad_Performance_Tracker.csv` | Daily ad performance |
| `tallow-cream/tracking/Tallow_Brand_Growth_Sheet.csv` | Batch plans + status |
| `tallow-cream/tracking/Kill_Rules_and_Decision_Framework.md` | Hard/soft kill rules |
| `tallow-cream/avatars/invisible-woman/` | Primary validated avatar (definition + deep research + brand voice) |
| `tallow-cream/avatars/homesteader-mom/` | Active Batch 10 avatar (definition + deep research + brand voice) |
| `tallow-cream/avatars/carnivore-woman/` | Sub-Avatar 7 hypothesis draft (Tier 1, research pending) |
| `tallow-cream/avatars/postpartum-mom/` | Sub-Avatar 8 hypothesis draft (Tier 1, research pending) |
| `tallow-cream/avatars/tween-daughter-mom/` | Sub-Avatar 9 hypothesis draft (Tier 2) |
| `tallow-cream/avatars/clean-eater/` | Sub-Avatar 10 hypothesis draft (Tier 2 — avatar vs. angle TBD) |
| `tallow-cream/feedback-loops/` | Per-ad postmortems for B1-B6 |
| `tallow-cream/ads/batch-10/copy/` | Current live batch (Homesteader Mom test) |
| `.claude/skills/native-ad-writer/` | Native ad writing skill (compliance + density + Homesteader brand voice) |

## Updated
2026-04-14
