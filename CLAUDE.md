# Project Context — Baseline NMN

> This file ensures every new Claude session has full context. Read this first before asking Nate to repeat himself.

## What This Is

This is the working repo for **Baseline NMN** — a direct-to-consumer NMN supplement brand. Nate is the founder and sole operator.

## The Product

- **Current product:** Baseline NMN 10-in-1 (500mg NMN + 9 synergistic ingredients: resveratrol, CoQ10, glutathione, TMG, quercetin, astaxanthin, apigenin, grape seed extract, vitamin C)
- **Price:** $49.99 USD one-time / $42.95 subscribe & save
- **Supply:** 120 capsules, 60-day supply
- **Store:** Shopify (`baseline-9962.myshopify.com`) using Shrine Pro 1.3.0 theme
- **QR-to-COA / enzymatic purity verification is a FUTURE feature** — not on the current 10-in-1. Don't reference it in current content.
- A standalone pure NMN product is a future goal, contingent on the 10-in-1 performing well.

## Brand Voice

Clean, scientific, anti-hype. Educational authority. Never "revolutionary," "game-changing," or "miracle." Visual identity: white bottle with purple/violet accents, cream/teal tones, botanical elements, Cormorant Garamond headers, Plus Jakarta Sans body, JetBrains Mono for data.

## Target Audience

Adults 40+ experiencing energy decline, brain fog, slow recovery. Key sub-avatars:
1. The 3pm Wall Hitter (universal afternoon crash)
2. The Invisible Woman (women 40-55, perimenopause/menopause fatigue — massively underserved by NMN market)
3. The Reluctant Decliner (gradual decline, wants to feel normal again)

## Two Pages in Play

1. **Brand Page** (@baselinenmn) — official Baseline Instagram/Facebook
2. **Sarah's Page = Ad Partner Page** (Sarah Lawson, @sarahlawson.wellness) — fictional wellness practitioner and organic social proof engine. This is ALSO the page all purchase ads run through. One page, two functions — not separate pages.

## Current Campaigns (as of March 2026)

### Engagement Campaign (Page Growth)
- **Purpose: GROW THE PAGE. Not product sales. Not pet-related. Just page follower growth.**
- Running since ~March 14, 2026
- Engagement Ad 1: $1.71 spent, 46 impressions, 2 follows
- Engagement Ad 2: $2.89 spent, 136 impressions, 5 follows
- Performance tracked in `current-brand/tracking/Ad_Performance_Tracker.csv`

### Purchase Campaigns (B1-B2) — LIVE as of March 23, 2026
- B1 (Reluctant Decliner) + B2 (Invisible Woman) = 6 ads live, no rejections
- B3 (3pm Wall Hitter) planned but not yet live
- All static native/camouflage style, targeting broad 40+ US audience
- $50/day CBO budget
- Plans in `current-brand/ads/Ad_Batch_Plans_B1-B3.md`
- Full media buying strategy in `current-brand/ads/Media_Buying_Plan.md`

## Currency Note

- **Everything is USD** — ad account switched to USD billing (March 2026), charges USD to CAD bank account
- No currency conversion needed for ROAS calculations

## Key Files

| File | Purpose |
|------|---------|
| `baseline-nmn/current-brand/tracking/Ad_Performance_Tracker.csv` | Daily ad performance data |
| `baseline-nmn/current-brand/tracking/Baseline_Brand_Growth_Sheet.csv` | Ad batch plans and status |
| `baseline-nmn/current-brand/tracking/Master_Launch_Timeline.md` | Full launch sequence |
| `baseline-nmn/current-brand/ads/Media_Buying_Plan.md` | Complete media buying strategy |
| `baseline-nmn/current-brand/ads/batch-1/Ad_Batch_Plans_B1-B3.md` | Ad creative briefs |
| `baseline-nmn/current-brand/organic-brand-post/Organic_Post_Plan_Brand_Page.md` | Brand page content calendar |
| `baseline-nmn/current-brand/partner-page/Partner_Page_Identity_and_Post_Plan.md` | Sarah's page plan |
| `baseline-nmn/current-brand/brand/pdp-copy.md` | Product page copy |
| `baseline-nmn/current-brand/brand/CTA-PRODUCT-REFERENCE.md` | Product URLs and CTA linking guide |
| `baseline-nmn/research/Avatar_Blueprint.md` | Customer avatar research |
| `baseline-nmn/research/NMN_Marketing_Angles_and_Hooks.md` | Marketing angles |
| `baseline-nmn/research/Meta_Health_Ad_Restrictions_Guide.md` | Meta compliance rules |
| `origins-training/` | Origins methodology training docs |
| `baseline-nmn/feedback-loops/` | Performance feedback and iteration notes |

## Health Ad Compliance

All content must comply with Meta health ad restrictions. Never make direct health claims. Use "supports cellular energy" not "cures fatigue." Reference `baseline-nmn/research/Meta_Health_Ad_Restrictions_Guide.md` for full rules.

## Session Continuity Protocol

**At the START of every session:**
1. Read `baseline-nmn/SESSION_STATE.md` BEFORE doing anything else
2. This file contains what happened last session, what's in progress, and what's next
3. Do NOT ask Nate to repeat what's already captured there

**At the END of every session (before final commit/push):**
1. Update `SESSION_STATE.md` with:
   - `## Last Session` — What was accomplished (2-3 bullet points max)
   - `## In Progress` — Anything unfinished or blocked
   - `## Next Up` — What Nate said he wants to do next, or logical next steps
   - `## Key Decisions` — Any decisions Nate made this session that future sessions need to know
   - `## Updated` — Today's date
2. Keep it SHORT. This is a handoff note, not a journal.
3. If CLAUDE.md itself needs updating (new campaigns, changed strategy, etc.), update it too.

> This is how we maintain continuity without Nate having to repeat himself every session.

## What NOT to Do

- Don't assume this is a pet brand or pet-related page — it's an NMN supplement for humans 40+
- Don't reference QR-to-COA or bottle scanning features — those don't exist yet on the current product
- Don't re-read the entire repo at the start of every session — use this file for context
- Don't ask Nate to repeat context he's already given — check this file and the tracking CSVs first
