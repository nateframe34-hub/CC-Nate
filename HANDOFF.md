# Handoff State

> Real-time handoff document. Updated whenever work happens, decisions get made, or items complete.
> Read this at session start BEFORE doing anything else (after CLAUDE.md).

**Last Updated:** 2026-05-04
**Active Brand:** Tallow Cream
**Project Phase:** Purchase campaign live on B7C1, engagement campaign retired, scaling decision pending performance review

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

Engagement campaign turned OFF. B7C1 single-ad purchase campaign at $10/day. Last ~1.5 days: $18.15 spent, $97.58 CPM (good, half the cooked BM's $200-450), 8.60% CTR (exceptional), 16 clicks, 8 LPVs, 1 ATC, 1 InitiateCheckout, 0 purchases on this Portfolio specifically (brand has 9 lifetime sales across prior accounts). Funnel signals upstream of checkout are healthy. The 0-purchase reading is on a sample of n=1 IC — meaningless statistically. Scaling decision: GO, but at $25-30/day instead of $10 → $40 (3x is aggressive enough to feel meaningful without 4x learning-reset risk). Add B9C3 alongside B7C1 in the same ad set to give CBO options.

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
| Business Portfolio | OPERATIONAL — not restricted | None | Standard ad operations. Verify new virtual Visa Debit attached as payment method. |
| Pixel | CREATED + CONNECTED to Portfolio | Pending: confirm Shopify connection so conversions track when purchase ads launch | Verify pixel fires on Shopify PDP, ATC, and checkout. Test event firing in Events Manager before purchase ads go live. |
| Engagement campaign | TURNED OFF (date unconfirmed) | None | Final stats unknown — need to capture before fully retiring the work stream. Page warmup work it did is preserved in Julie's page activity. |
| Purchase campaign B7C1 | SPENDING — 0 purchases YET ON THIS PORTFOLIO ($18.15 spend, 1 ATC + 1 IC), but brand has 9 lifetime sales across other accounts | None blocking | Funnel signals healthy: 8.6% CTR, 50% click-to-LPV, 12.5% LPV-to-ATC, 100% ATC-to-IC. The 0 purchase reading is within-Portfolio only and based on n=1 InitiateCheckout. Brand-level conversion economics already proven. |
| Pixel value attribution | NEEDS VERIFICATION | None blocking but should fix before scaling | Run Test Events with a real test purchase to confirm `value` parameter is set on Purchase event. Critical for AOV-based optimization (especially when BOGO 50% goes live). |
| Scaling decision | GO — moderate scale | None | Given 9-sale brand validation + healthy funnel signals on fresh Portfolio + CPM is half what cooked BM was: scaling is supportable. Right amount: $10 → $25-30/day (2.5-3x, aggressive but defensible). Add B9C3 alongside B7C1 in same ad set to give CBO options. Watch CPMs for 2-3 days for learning-phase reset signs. Re-evaluate $40+ once that data comes in. |
| Batch 12 testing (Invisible Woman, locked-formula rebuilds) | QUEUED — start after B7C1+B9C3 stabilizes | Don't overlap with current scale + B9C3 add | Plan: launch B12 in a NEW ad set (same campaign or new campaign) at $10-15/day after Phase 1 data settles. Tests whether locked-formula skeleton reproduces with new hooks (Hairdresser, Pond's nostalgia, Daughter Sent It). Compare against B7C1+B9C3 baseline. |
| Batch 13 testing (Photo Avoider sub-sub-avatar) | QUEUED — start after B12 data | Different test variable than B12 (avatar fit, not formula fit) | Plan: launch B13 in its own test structure 5-7 days after B12 data starts coming in. This is testing whether the Photo Avoider sub-avatar converts, not whether the formula works (B12 answers that). |
| Checkout funnel investigation | LOW PRIORITY — sample too small to act on | None | n=1 IC abandon is statistical noise, not a problem signal. Implement abandoned cart email when feasible (recovers 5-15% of future cart abandoners), but don't troubleshoot a non-existent issue based on 1 data point. |
| Manual Julie replies | High volume incoming | Comment volume may exceed reply bandwidth | At $0.02 CPE the campaign is generating 250-350 engagements/day. Reply selectively — focus on most engaged commenters / longest comments. Not every comment needs a Julie reply. |
| Purchase test campaign (B7C1) | DECIDED, launching | None | Launch as a separate campaign with purchase objective, $10/day budget, B7C1 (She Used Pond's) as the only ad, broad audience, Advantage+ Placements, optimize for Purchase event. New pixel, NOT cooked BM's pixel. Verify pixel firing on Shopify (PDP/ATC/Checkout/Purchase) before launch. |
| Personal FB profile health | UNAFFECTED | None | Safe per Nate. |
| Banned-BM cleanup track | Running in parallel | None | BBB / Competition Bureau Canada filing for ~$180 refund still pending; doesn't block forward progress. |
| Portfolio admin redundancy | Personal FB + cooked BM both added as backup admins | None | Standard redundancy practice — gives multiple access paths if primary admin ever gets locked out. "Cooked BM" = original underperforming-CPM BM (not banned), still operational. |
| Operational hygiene of imported assets | Cooked BM brings old assets (page, pixel, audiences) into Portfolio scope | None active | Don't reuse the cooked BM's pixel or audiences in the new ad campaigns — those carry the old auction baggage. Treat the cooked BM as admin-redundancy only; build new ad accounts/audiences/pixel inside the new Portfolio. |
| Abandoned cart email | Copy drafted, awaiting implementation | Needs Shopify Email editor configuration | Paste brand-voice copy from chat into Shopify Email draft; verify Baseline → tallow brand name override |
| BOGO 50% offer (live) | Spreadsheet committed; Shopify implementation pending | Default Shopify pricing doesn't support BOGO; needs Shopify Functions or app | Configure when ads resume — also update PDP messaging + cart upsell |
| Ad creative for new BM | 10 ads written, awaiting BM | New BM not yet live | Launch sequence TBD: B11 (CPM diagnostic), B12 C2/C3, B13 (Photo Avoider × 3), B14 (Retinol Burnout × 3) |
| Email sequence (post-cart-email-1) | Not started | Email 1 not yet live | Email 2 (24h, story-form) + Email 3 (72h, soft urgency) drafts queued |

---

## Recent Decisions (Last 14 Days)

- **2026-05-04** — Testing roadmap for B12/B13 sequenced AFTER current scale + B9C3 add stabilizes. Don't overlap multiple changes (scale to $30 + add B9C3 + test new batches = three simultaneous variables = no clean attribution). Phase 1: scale + B9C3 today. Phase 2: B12 in 2-5 days once Phase 1 settles. Phase 3: B13 5-7 days after B12 data starts coming in.
- **2026-04-27** — B7C1 (She Used Pond's) selected as the lead purchase-ad test on the new Portfolio. Rationale: B7C1 likely has the most lifetime sales among the 4 converters now (2 prior + portion of the 4 banned-BM unattended sales = ~3-4 total), cleanest click-to-LPV funnel historically (multiple 100% days), cheapest engagement signal of the converters ($209-240 CPM range), and the generational-mirror hook is the broadest Invisible Woman avatar trigger (almost every woman 45+ has a mother memory). Recent unattended-conversion data on the banned BM is the most relevant signal for how converters behave on a fresh-Portfolio environment, and B7C1 had that data.
- **2026-04-27** — Purchase test will launch as a SEPARATE campaign with purchase objective, NOT by switching the engagement campaign's objective. Both campaigns run in parallel — engagement at $5/day continues, purchase test at $10/day on B7C1.
- **2026-04-27** — Personal Facebook account + cooked BM (the original high-CPM but operational BM, NOT the Apr 23 banned one) both added to Portfolio as backup admins. Rationale: redundancy — if the primary admin (the fresh FB account that created the Portfolio) ever gets locked out, the personal FB and the cooked BM both retain admin paths to pause campaigns. Standard redundancy practice. Note for future sessions: don't reuse the cooked BM's pixel or audiences in the new Portfolio's ads — those carry the old auction baggage. Cooked BM is admin-redundancy only.
- **2026-04-27** — Working Business Portfolio acquired (status: not restricted). Pixel created and connected to Portfolio. Engagement campaign launching imminently. Earlier-Apr-27 banned Portfolio attempt no longer blocking.
- **2026-04-27** — Methodology of fresh FB account per new BM stays. Approach has worked for the previous 3 BMs and now this 4th one. Earlier-Apr-27 failure was an outlier within a working pattern.
- **2026-04-26** — BM warmup resumed despite billing crisis still being technically open. Decision basis: old card numbers killed (banned BM can no longer charge), new virtual Visa Debit ready for new BM, refund process for past charges runs in parallel and doesn't block forward progress. Trade-off accepted: refund of ~$180 bleed is paperwork, not a blocker.
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

- **2026-04-27** — Engagement campaign LAUNCHED. Day-1 performance: $5 CPM, $0.02 cost per engagement. Validates fresh-Portfolio hypothesis at engagement level (40-90x CPM improvement vs old BM, ~10-25x vs Apr 21 fresh BM).
- **2026-04-27** — Personal FB + cooked BM added to Portfolio as backup admins (defensive redundancy).
- **2026-04-27** — Working Business Portfolio acquired (status: not restricted)
- **2026-04-27** — Pixel created and connected to Portfolio
- **2026-04-26** — New BM created (third BM since brand launch — first was old BM, second was Apr 21 fresh BM that got banned Apr 23)
- **2026-04-26** — New partner page created (pending confirmation: presumed to be Julie Brennan's page per `tallow-cream/partner-page/Partner_Page_Identity.md`)
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

### Active
- Is the pixel connected to Shopify (firing on PDP, ATC, checkout, purchase) so conversions track when purchase ads launch? Verify in Events Manager before purchase ads go live. NOTE: use the NEW pixel created today, not the cooked BM's old pixel.
- Vocabulary clarification logged: "cooked BM" in Nate's vocabulary = the original high-CPM-but-operational BM from before Apr 21, NOT the Apr 23 banned BM. Distinct things. Both exist; only the Apr 23 one is contaminated.
- Is the new virtual Visa Debit attached as the payment method on the working Portfolio (NOT any of the killed card numbers)?
- Is the engagement campaign creative the pet-photo prompt per `Follower_Warmup_Campaign.md`, or product-aware? Should be pet-photo for cheapest delivery + cleanest BM warmup signal.
- Vocabulary check: in Nate's setup, what's the distinction between "BM" and "Business Portfolio"? Meta uses these interchangeably; Nate treats them as related but distinct. Worth pinning down so HANDOFF.md uses consistent language.

### Existing
- Will Meta refund post-ban charges via BBB or Competition Bureau Canada? (Filing pending, no response yet.)
- Total banned-BM spend at end-of-bleed: estimated ~$180 but exact figure unknown until card declines stop charges or refund process surfaces it.
- BOGO 50% Shopify implementation path: Shopify Functions vs third-party app. Unresolved (independent of BM problem — can proceed regardless).
- B11 launch sequencing when a non-banned BM exists: solo first to isolate avatar variable, or stack with reactivated B5C1/B7C1/B9C3?
- Brand name on Shopify emails: header currently says "Baseline" but product is tallow. Single store / dual brands or separate stores? Affects abandoned cart email branding fix.

---

## Pause / Resume Conditions

**Status: ACTIVE — engagement campaign launching imminently.**

- Working Business Portfolio operational (not restricted)
- Pixel created and connected
- Engagement campaign launching now per `Follower_Warmup_Campaign.md`
- Personal Facebook activity continuing at normal pace

**Things to gate before purchase ads launch (do NOT skip):**
1. Engagement campaign hits $50 spend target (4-5 days at $5-7/day per warmup plan)
2. Pixel confirmed firing on Shopify (PDP / ATC / Checkout / Purchase events) — verify in Events Manager
3. Portfolio confirmed in good standing (no Meta restrictions / warnings showing on Account Quality)
4. Payment method = new virtual Visa Debit, NOT any of the killed card numbers
5. BOGO 50% offer implemented in Shopify so purchase ads have the new offer to point to (or decision to launch with current $49.99 single SKU and add BOGO later)

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
