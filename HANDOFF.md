# Handoff State

> Real-time handoff document. Updated whenever work happens, decisions get made, or items complete.
> Read this at session start BEFORE doing anything else (after CLAUDE.md).

**Last Updated:** 2026-04-27
**Active Brand:** Tallow Cream
**Project Phase:** Pre-relaunch — BM warmup paused pending billing crisis resolution

---

## Update Protocol (read this if you are Claude)

Three concrete triggers — update HANDOFF.md inline, NOT at end of session:

1. **Starting work on something** → add a row to "Active Work Streams" with state + next action
2. **Making a decision / coming up with something** → add a dated entry to "Recent Decisions" with the rationale
3. **Completing something** → move from "Active Work Streams" to "Recently Completed" with outcome

**Pre-response check:** Before responding to a user message, if the previous turn contained a decision, work-state change, or completion → update HANDOFF.md as part of the response.

**Tied to commits:** Every commit that changes content (ad copy, offer sheet, feedback file, etc.) should also include a HANDOFF.md update reflecting the change. No commit goes out without HANDOFF.md being current.

The reason the old `SESSION_STATE.md` went stale (Apr 16 → Apr 27 with no update during an active period) is that "update at end of session" is a fuzzy trigger. Real-time triggers fix that.

---

## Right Now

Tallow ads paused. Banned BM (banned Apr 23 at 2am) still spending $40/day on B5C1 + B7C1 — generated 4 sales since the ban (good signal at ~$45 CPA, 1.11x gross ROAS) but unrecoverable money is bleeding. New BM warmup paused at end of Day 2/3 of personal Facebook account activity until the billing crisis is resolved. RBC card replacement underway: new virtual Visa Debit obtained, credit card shipping (5-7 business days). BOGO 50% offer locked in (replaces Ritual + Transformation in offer sheet, Apr 27). Abandoned cart email rewrite drafted in brand voice, awaiting Shopify implementation.

---

## What to Read Right Now (Dynamic — current active work)

For the work currently in flight, the relevant files are:

1. `HANDOFF.md` (this file) — current state
2. `CLAUDE.md` — project context, both-brand framing
3. `tallow-cream/Tallow_Ad_Creative_Principles.md` — locked creative rules
4. `tallow-cream/offers/Offer_Planning_Sheet.csv` — BOGO 50% recently added (Apr 27)
5. `tallow-cream/feedback-loops/Converter_Pattern_Synthesis.md` — what's working across the 4 early converters
6. `tallow-cream/partner-page/Partner_Page_Identity.md` — Julie Brennan identity (paused but still relevant)

If/when ads resume, also pull the active batch's copy + feedback files.

---

## Active Work Streams

| Stream | State | Blocker | Next Action |
|---|---|---|---|
| Banned BM billing crisis | In progress | Meta chatbot refuses human escalation | File BBB / Competition Bureau Canada complaint to start refund track |
| RBC card replacement | In progress | Physical credit card in mail (~5-7 business days) | Virtual Visa Debit obtained; new credit card # available digitally; old numbers killed via fraud framing (no Visa Account Updater push) |
| BM #3 warmup | PAUSED | Billing crisis must resolve first | End of Day 2/3 personal account warmup completed; resume when bleed confirmed stopped + alt payment locked in |
| Personal FB activity | Continuing at low baseline | None | 5-10 min/day of normal activity to preserve warmup credit during pause |
| Abandoned cart email | Copy drafted, awaiting implementation | Needs Shopify Email editor configuration | Paste brand-voice copy from chat into Shopify Email draft; verify Baseline → tallow brand name override |
| BOGO 50% offer (live) | Spreadsheet committed; Shopify implementation pending | Default Shopify pricing doesn't support BOGO; needs Shopify Functions or app | Configure when ads resume — also update PDP messaging + cart upsell |
| Ad creative for new BM | 10 ads written, awaiting BM | New BM not yet live | Launch sequence TBD: B11 (CPM diagnostic), B12 C2/C3, B13 (Photo Avoider × 3), B14 (Retinol Burnout × 3) |
| Email sequence (post-cart-email-1) | Not started | Email 1 not yet live | Email 2 (24h, story-form) + Email 3 (72h, soft urgency) drafts queued |

---

## Recent Decisions (Last 14 Days)

- **2026-04-27** — BOGO 50% replaces Ritual + Transformation bundles ($74.99, $42.94 margin, 57.27%, 1.75 BE ROAS). Rationale: both old bundles had zero sales since launch; "save $X" framing reads as upsell, "buy one get one half off" reads as deal. Same economic outcome, much stronger psychology. BOGO 40% reserved as future price-test variant.
- **2026-04-27** — Get new card numbers from RBC with fraud framing (NOT routine reissue) so Visa Account Updater doesn't push new card to banned BM. Virtual Visa Debit and credit card both replaced. Old numbers killed.
- **2026-04-27** — Pause new BM warmup until billing crisis resolved. Resume conditions defined (3-point checklist).
- **2026-04-27** — Abandoned cart email = BRAND voice, not Julie peer voice. The brand speaks once they're past the ad and into the brand's email funnel. Frame as "your jar is held in your cart," not "your order is ready to ship" (latter risks trust + ESP policy issues).
- **2026-04-27** — HANDOFF.md created at repo root, replaces stale `baseline-nmn/SESSION_STATE.md`. Update protocol baked into CLAUDE.md.
- **2026-04-25** — `CLAUDE.md` restructured to lead with tallow as active brand, NMN as dormant. Two clean brand sections (Brand 1 ACTIVE / Brand 2 DORMANT). Old framing had it inverted.
- **2026-04-25** — Sarah Lawson partner page references purged from repo, replaced with Julie Brennan throughout.
- **2026-04-25** — `Converter_Pattern_Synthesis.md` created. Documents what 4 early converters share (4/4 + 3/4 elements) and what's unique to each. Framed as working hypothesis from small sample (4 ads, ~6 sales at the time).
- **2026-04-16** — Batch 10 (Homesteader Mom) killed. CPMs $116-184 — directionally lower than Invisible Woman ads ($200-450) but not the dramatic drop the avatar-saturation hypothesis predicted. 0 conversions on 5 LPVs.
- **2026-04-14** — Fresh-campaign duplicate test (B5C1 + B7C1 + B9C3 in clean campaign) ruled out campaign-level pixel poisoning. CPM problem confirmed upstream of campaign — pixel/page/account/product level.

---

## Recently Completed

- **2026-04-27** — `tallow-cream/offers/Offer_Planning_Sheet.csv` updated: BOGO 50% added, Ritual + Transformation removed (commit `54e68b2`)
- **2026-04-27** — RBC virtual Visa Debit number replaced; old number killed
- **2026-04-25** — `tallow-cream/feedback-loops/Converter_Pattern_Synthesis.md` published (commit `b27766d`)
- **2026-04-25** — `CLAUDE.md` restructure published (commit `b27766d`)
- **2026-04-25** — `tallow-cream/feedback-loops/batch-7/B7C1_She_Used_Ponds_Feedback.md` + `tallow-cream/feedback-loops/batch-9/B9C3_The_Counter_With_One_Thing_Feedback.md` published (commit `d972733`)

---

## Sales Snapshot

- **Lifetime sales:** 9 (~$419.91 revenue, average ~$46.66/sale due to one $19.99 discount-error sale)
- **Estimated lifetime spend:** ~$730 across old BM + fresh BM (Apr 21) + banned BM (Apr 23-27)
- **Lifetime gross ROAS:** ~0.58x
- **Most recent unattended period (banned BM, Apr 23-27):** ~$180 spend, 4 sales = $199.96 revenue, ~1.11x gross ROAS, ~$45 CPA
- **Converters identified (4):** B3C2 ($19.99 discount error), B5C1 ($49.99 + recent unattended), B7C1 (×2 + recent unattended), B9C3 (×2)
- **Closest to "winner":** B9C3 (4.62x ROAS Apr 14, 1.88x fresh BM Apr 21). No ad has yet hit sustained 2+ ROAS over 3 days.
- **Validation state:** Product = validated. Conversion mechanic = validated. Avatar (Invisible Woman) = validated. Unit economics = NOT YET (still net-negative lifetime). Scalability beyond Invisible Woman = NOT YET TESTED. Repeat purchase / LTV = NO DATA.

---

## Open Questions

- Will Meta refund post-ban charges via BBB or Competition Bureau Canada? (Filing pending, no response yet.)
- Total banned-BM spend at end-of-bleed: estimated ~$180 but exact figure unknown until card declines stop charges or refund process surfaces it.
- BOGO 50% Shopify implementation path: Shopify Functions vs third-party app (BOGO+, Shop Quantity Breaks, etc.). Unresolved.
- B11 (Working Hands Man) launch sequencing when new BM goes live: solo first to isolate avatar variable, or stack with reactivated B5C1/B7C1/B9C3 for budget efficiency?
- Personal Facebook account access — is `business.facebook.com/billing` reachable directly even though the BM is banned? Worth a 5-min test to potentially bypass the chatbot escalation problem.
- Brand name on Shopify emails: header currently says "Baseline" but product is tallow. Single store / dual brands or separate stores? Affects abandoned cart email branding fix.

---

## Pause / Resume Conditions

**Currently paused:** New BM creation, new partner page setup on the new BM, engagement campaign warmup, purchase ads.

**Continuing at low baseline:** Personal Facebook account activity (5-10 min/day) to preserve warmup credit during pause.

**Resume new BM warmup when ALL of:**
1. Bank confirms recurring authorization revoked on both cards in writing (or charges declining is observable)
2. Banned-BM bleed confirmed stopped (Meta auto-suspends after card declines, or BBB confirms cancellation)
3. Alternate payment method for new BM is locked in (likely the new virtual Visa Debit or new credit card once delivered)

---

## Required Reading (For Any New Session)

### Tier 1 — Always Read (in this order)
1. `CLAUDE.md` — project context, both-brand framing, what NOT to do
2. `HANDOFF.md` (this file) — current state, active work, decisions, blockers
3. `tallow-cream/Tallow_Ad_Creative_Principles.md` — locked creative rules (mandatory before any ad work)

### Tier 2 — Read If Doing Ad Creative Work
- `tallow-cream/feedback-loops/Converter_Pattern_Synthesis.md` — what's working across converters
- `tallow-cream/tracking/Ad_Performance_Tracker.csv` — last 30 rows for recent performance
- The specific batch's existing ads (`tallow-cream/ads/batch-N/copy/`) + any feedback files (`tallow-cream/feedback-loops/batch-N/`)
- `tallow-cream/tracking/Kill_Rules_and_Decision_Framework.md` — when to kill what

### Tier 3 — Read If Doing Avatar / Research Work
- `tallow-cream/avatars/Avatar_Blueprint.md` — full sub-avatar roster
- The specific avatar folder (`tallow-cream/avatars/<avatar-name>/`) including Definition + Deep Research + Brand Voice Reference
- `tallow-cream/avatars/Avatar_Language_Research.md` — language patterns

### Tier 4 — Read If Doing Offer / Store Work
- `tallow-cream/offers/Offer_Planning_Sheet.csv` — current offer matrix (BOGO 50% live as of Apr 27)
- `tallow-cream/offers/Competitive_Offer_Research.md` — competitor positioning
- `tallow-cream/store/copy/PDP_Copy_v2.md` — current PDP copy
- `tallow-cream/store/copy/PDP_Swipe_Analysis.md` — competitive PDP teardowns

### Tier 5 — Read If Doing Partner Page / Julie Brennan Work
- `tallow-cream/partner-page/Partner_Page_Identity.md` — Julie's full identity
- `tallow-cream/partner-page/Follower_Warmup_Campaign.md` — engagement campaign warmup plan

### Tier 6 — Read If Working on NMN (Currently Dormant)
- `baseline-nmn/current-brand/tracking/` — last activity logged March 2026
- `baseline-nmn/research/Avatar_Blueprint.md`
- `baseline-nmn/research/Meta_Health_Ad_Restrictions_Guide.md` — applies to both brands

### Skip Unless Explicitly Asked
- `origins-training/` — methodology training docs (reference only, not for active work)
- Old batch copy / feedback for killed batches (B1-B4, B6, B8, B10) — unless studying failure patterns
