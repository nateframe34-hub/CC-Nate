# Project Context — Baseline NMN + Tallow Cream

> This file ensures every new Claude session has full context. Read this first before asking Nate to repeat himself.

## Active Focus

**Tallow Cream is the active brand.** All current paid advertising, BM warmup, ad creative work, and session activity is on tallow. Baseline NMN exists in this repo but is dormant — no active campaigns or recent work. If a request is ambiguous, assume tallow.

## ⚠️ MANDATORY READ FOR ANY TALLOW AD WORK

Before writing, briefing, or reviewing ANY tallow cream ad, you MUST read BOTH:
1. **`/home/user/CC-Nate/tallow-cream/Brand_Mastery.md`** : the master reference (added 2026-07-06). Sub-avatars (desire + experience + emotion, NOT demographics), angles with tested/untested status, market sophistication (Stage 5 market / Stage 3-4 niche), awareness levels, and the ranked unique mechanisms. Every new ad must state its sub-avatar, angle, awareness level, and sophistication response from this doc. It supersedes the old `avatars/` profiles for ad creation.
2. **`/home/user/CC-Nate/tallow-cream/Tallow_Ad_Creative_Principles.md`** : the locked creative/compliance principles.

These supersede general copywriting advice. Skipping them produces ads that don't convert and waste spend.

Key principles (covered in detail in that file):
1. Targeting happens at the CREATIVE level post-Andromeda, not audience targeting
2. The IMAGE is the scroll-stop — equal craft to the copy
3. Sub-sub-avatars (specific shared experiences) beat broad avatars
4. The 10-element converter skeleton is locked — every element required
5. Specific banned phrases for compliance (no menopause, no anti-aging, no skincare-industry language)

---

## Brand 1 — Tallow Cream (ACTIVE)

**Product:** Whipped Tallow & Honey Balm. 4 ingredients (tallow, manuka honey, olive oil, calendula). $49.99 launch price (anchor $59.99). 60-day money-back guarantee. Free shipping.

**Status:** Ads currently paused. The BM was banned (Meta flagged it as a bot, not a content/compliance issue). Nate is warming up a new BM — personal account activity first, then BM + partner page creation, then engagement campaign warmup, then purchase ads. Ads will resume once warmup is complete.

**Pre-pause performance:** 4 converters identified (B3C2, B5C1, B7C1, B9C3). Closest to "winner" status: B9C3 The Counter With One Thing. None of the 4 has hit the winner bar yet (sustained 2+ ROAS over 3 days). See `tallow-cream/feedback-loops/Converter_Pattern_Synthesis.md` for the working pattern. **"Invisible Woman" is RETIRED, structurally wrong, do not use it for tallow.** It was the old demographic-identity avatar label these converters were originally written under. It has been superseded by the desire-first SA-numbered system in `Brand_Mastery.md`. B9C3/B17C1 specifically has been remapped: SA2 The Product Graveyard is the lead angle, SA4 The Tight-by-Noon is the habit-cessation mid-beat, SA3 The Unnoticed is the close. See `tallow-cream/feedback-loops/B17C1_Deep_Analysis_Why_It_Works.md` for the full breakdown.

**Launch queue (written, awaiting new BM):** B11 Working Hands Man (CPM diagnostic), B12 C2/C3 (Pond's nostalgia + Daughter Sent It), B13 Photo Avoider (3 ads), B14 Retinol Burnout (3 ads).

**Partner page:** Julie Brennan (@juliebrennan.page, 48, Fort Collins, CO, office manager at a small civil engineering firm). Native/camouflage ad infrastructure — runs all purchase ads. Full identity in `tallow-cream/partner-page/Partner_Page_Identity.md`.

**Brand voice:** Real-woman, dry humor, self-deprecating, never spa/luxe/clean-beauty language. Voice rules enforced in every ad — see `Tallow_Ad_Creative_Principles.md` for the banned-phrase list.

**Avatars:** the account now runs on `Brand_Mastery.md`'s desire-first SA-numbered sub-avatars, NOT the old demographic labels ("Invisible Woman," "Homesteader Mom," "Working Hands Man" are all retired naming, kept only as historical batch-name references). SA2 The Product Graveyard, SA3 The Unnoticed, and SA4 The Tight-by-Noon are the account's validated converting angles (see the CPM Reduction/Converter analysis in `tallow-cream/feedback-loops/`). SA6 The Sun-Lived is activated for B26+. SA8 The Fast-Loser is researched, B27 candidate. See `tallow-cream/avatars/` for retired demographic profiles (kept as language research only) and `Brand_Mastery.md` for the current system.

---

## Brand 2 — Baseline NMN (DORMANT)

**Product:** Baseline NMN 10-in-1 (500mg NMN + 9 synergistic ingredients: resveratrol, CoQ10, glutathione, TMG, quercetin, astaxanthin, apigenin, grape seed extract, vitamin C). $49.99 USD one-time / $42.95 subscribe & save. 120 capsules, 60-day supply. Shopify (`baseline-9962.myshopify.com`) on Shrine Pro 1.3.0 theme.

**Status:** No active campaigns. Last activity logged was March 2026 (engagement campaign for page growth + purchase batches B1-B2). Brand is on pause while tallow gets attention.

**QR-to-COA / enzymatic purity verification is a FUTURE feature** — not on the current 10-in-1. Don't reference it in current content.

**Brand voice:** Clean, scientific, anti-hype. Educational authority. Never "revolutionary," "game-changing," or "miracle." Visual identity: white bottle with purple/violet accents, cream/teal tones, botanical elements, Cormorant Garamond headers, Plus Jakarta Sans body, JetBrains Mono for data.

**Brand page:** @baselinenmn on Instagram/Facebook.

**NMN sub-avatars (for reference if NMN reactivates):**
1. The 3pm Wall Hitter (universal afternoon crash)
2. The Invisible Woman (women 40-55, perimenopause/menopause fatigue — different framing than the tallow Invisible Woman)
3. The Reluctant Decliner (gradual decline, wants to feel normal again)

A standalone pure NMN product is a future goal, contingent on the 10-in-1 performing well.

---

## Currency

Everything is USD. Ad account switched to USD billing March 2026 (charges USD to CAD bank account). No currency conversion needed for ROAS calculations.

---

## ⚠️ Ads Manager Data Quirk — ATC is DOUBLE-COUNTED

**Adds to cart in Meta Ads Manager display at 2x the real number.** A screenshot showing 2 ATC means 1 actual add-to-cart. Always halve the displayed ATC figure before logging it to `Ad_Performance_Tracker.csv`, before using it in any funnel analysis, and before drawing conclusions about ATC-to-checkout drop-off rates.

This has caught us more than once — it makes the ATC→checkout stage look far leakier than it actually is. Only ATC is affected; impressions, clicks, landing page views, checkouts initiated, and purchases all read true.

---

## Key Files

### Tallow (active)

| File | Purpose |
|------|---------|
| `tallow-cream/Tallow_Ad_Creative_Principles.md` | Locked creative principles — MANDATORY read for any ad work |
| `tallow-cream/tracking/Ad_Performance_Tracker.csv` | Daily ad performance |
| `tallow-cream/tracking/Tallow_Brand_Growth_Sheet.csv` | Batch plans + status |
| `tallow-cream/tracking/Kill_Rules_and_Decision_Framework.md` | Hard/soft kill rules (may need recalibration for fresh-BM CPMs) |
| `tallow-cream/avatars/` | Retired demographic-avatar profiles (language research only, superseded by `Brand_Mastery.md`'s SA-numbered system for ad creation) |
| `tallow-cream/feedback-loops/` | Per-ad postmortems |
| `tallow-cream/feedback-loops/Converter_Pattern_Synthesis.md` | Cross-cutting analysis of what the 4 early converters share |
| `tallow-cream/ads/batch-N/copy/` | Ad copy by batch (B1-B14) |
| `tallow-cream/partner-page/Partner_Page_Identity.md` | Julie Brennan identity + content plan |
| `tallow-cream/partner-page/Follower_Warmup_Campaign.md` | Pet-photo engagement campaign for new-BM warmup |
| `tallow-cream/store/copy/` | PDP copy (v2 is current; PDP is compliant per Apr 14 confirmation) |
| `tallow-cream/offers/` | Offer roadmap (launch + future bundles) |

### NMN (dormant)

| File | Purpose |
|------|---------|
| `baseline-nmn/current-brand/tracking/Ad_Performance_Tracker.csv` | NMN ad performance (last activity March 2026) |
| `baseline-nmn/current-brand/tracking/Baseline_Brand_Growth_Sheet.csv` | NMN batch plans |
| `baseline-nmn/current-brand/tracking/Master_Launch_Timeline.md` | NMN launch sequence |
| `baseline-nmn/current-brand/ads/Media_Buying_Plan.md` | NMN media buying strategy |
| `baseline-nmn/current-brand/ads/batch-1/Ad_Batch_Plans_B1-B3.md` | NMN ad creative briefs |
| `baseline-nmn/current-brand/organic-brand-post/Organic_Post_Plan_Brand_Page.md` | NMN brand page content calendar |
| `baseline-nmn/current-brand/brand/pdp-copy.md` | NMN product page copy |
| `baseline-nmn/current-brand/brand/CTA-PRODUCT-REFERENCE.md` | NMN product URLs and CTA linking guide |
| `baseline-nmn/research/Avatar_Blueprint.md` | NMN customer avatar research |
| `baseline-nmn/research/NMN_Marketing_Angles_and_Hooks.md` | NMN marketing angles |
| `baseline-nmn/research/Meta_Health_Ad_Restrictions_Guide.md` | Meta compliance rules (applies to both brands) |
| `baseline-nmn/feedback-loops/` | NMN performance feedback |

### Shared

| File | Purpose |
|------|---------|
| `baseline-nmn/SESSION_STATE.md` | Cross-brand session handoff (file lives in baseline-nmn/ for historical reasons but currently covers tallow work) |
| `origins-training/` | Origins methodology training docs |

---

## Health Ad Compliance

All content must comply with Meta health ad restrictions. Never make direct health claims.

- **Tallow:** No menopause/perimenopause, no anti-aging, no medical claims. Specific banned phrases enforced — see `tallow-cream/Tallow_Ad_Creative_Principles.md`.
- **NMN:** "Supports cellular energy" not "cures fatigue." See `baseline-nmn/research/Meta_Health_Ad_Restrictions_Guide.md`.

---

## Session Continuity Protocol

**At the START of every session — read in this order:**
1. `CLAUDE.md` (this file) — project context
2. `HANDOFF.md` (repo root) — current state, active work streams, recent decisions, open questions, pause/resume conditions
3. `tallow-cream/Tallow_Ad_Creative_Principles.md` — locked creative rules (mandatory before any tallow ad work)
4. Then any tier-specific reading per HANDOFF.md's "Required Reading" section, based on the work that's coming next

Do NOT ask Nate to repeat context already captured in those files.

**HANDOFF.md update protocol — three triggers, REAL-TIME, NOT end-of-session:**

Update HANDOFF.md inline as work happens, not at the end. Three concrete triggers:
1. **Starting work on something** → add a row to "Active Work Streams" with state and next action
2. **Making a decision / coming up with something** → add a dated entry to "Recent Decisions" with the rationale
3. **Completing something** → move from "Active Work Streams" to "Recently Completed" with outcome

**Pre-response check:** Before responding to a user message, if the previous turn contained a decision, work-state change, or completion → update HANDOFF.md AS PART OF the response.

**Tied to commits:** Every commit that changes content (ad copy, offer sheet, feedback file, etc.) should also include a HANDOFF.md update reflecting the change. This is the mechanical enforcement — no commit goes out with HANDOFF.md stale.

> The reason the previous `SESSION_STATE.md` (now deleted) went stale (Apr 16 → Apr 27 with no update during an active period) is that "update at end of session" is a fuzzy trigger that gets skipped. Real-time triggers tied to concrete events fix that.

---

## What NOT to Do

- Don't assume "this project" means NMN — tallow is the active brand. NMN is dormant.
- Don't reference QR-to-COA / bottle scanning for NMN — that's a future feature, not on the current product
- Don't apply NMN brand voice to tallow ads, or vice versa — they're different voices for different audiences
- Don't use "Invisible Woman" for TALLOW, that label is retired and structurally wrong, tallow runs on `Brand_Mastery.md`'s SA-numbered desire-first system now (SA2/SA3/SA4 for the proven converting angles). NMN (dormant) still uses its own separate "Invisible Woman" naming (energy/fatigue framing) in its own avatar system, that's a different brand's terminology and not affected by this correction, don't confuse the two.
- Don't re-read the entire repo at the start of every session — use this file for context
- Don't ask Nate to repeat context he's already given — check this file, SESSION_STATE.md, and the tracking CSVs first
