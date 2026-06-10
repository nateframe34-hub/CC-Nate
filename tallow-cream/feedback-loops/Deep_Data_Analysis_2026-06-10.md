# Deep Data Analysis: What The Spend Data Actually Says

**Date:** 2026-06-10
**Inputs:** Ad_Performance_Tracker.csv (73 logged rows, Apr 8 to Apr 21), Ad_Test_Variables_Tracker.csv (46 ads), Converter_Pattern_Synthesis.md, Killed_Batch_Failure_Analysis.md, Tallow_Brand_Growth_Sheet.csv, HANDOFF sales snapshot.
**Purpose:** Determine from the data what has actually worked, what has actually been tested vs what only LOOKS tested, and what the highest-priority next test is.

---

## PART 1: The Funnel Data, Disaggregated By Ad

The councils kept saying "the funnel is broken" from the aggregate (high CTR, near-zero ATC). The aggregate hides the real finding. The PDP is a CONSTANT: every ad lands on the same page. So if some ads convert their landing-page views and others convert none, the variance is in the AD, not the page.

### Tracked LPV-to-purchase by ad (all logged days combined)

| Ad | Tracked LPVs | ATCs | Purchases | LPV→Purchase | CPA when it converted |
|---|---|---|---|---|---|
| **B9C3 One Jar** | 12 | 2 | **2** | **~17%** | $10.82 (old BM), $26.54 (fresh BM) |
| B5C1 Husband Noticed | 15 | 1-2 | 1 | ~7% (but **0/12 on fresh BM**) | $21.21 (old BM, Apr 10) |
| B7C1 She Used Pond's | 23 | 1 | 0 tracked | **0%** (2 sales pre-tracker) | unknown (pre-tracker) |
| B10C3 Maintenance | 5 | 0 | 0 | 0% | n/a |
| B2C2 All The Same | 4 | 0 | 0 | 0% | n/a |
| May B7C1 $10/day run | few | 1 | 0 | 0% | n/a |

### What this means

1. **The funnel is not uniformly broken. It closes for exactly one ad.** B9C3 converted its LPVs at roughly 17% across TWO different BM environments (old and fresh). Every purchase it generated came in under CPA $27 against a $32.98 contribution margin ($49.99 minus $17.01 COGS). When B9C3 converts, it is unit-profitable.

2. **High CTR is anti-signal when it comes without ATCs.** B5C1's fresh-BM day is the cleanest demonstration in the whole dataset: $53 CPM, 48.39% CTR, 15 clicks, 12 LPVs, ZERO add-to-carts. The ad is a recognition machine: women click because they feel seen, then bounce because feeling seen is not a reason to pay $49.99. B7C1 is the same pattern softened: 19.51% CTR, 11 LPVs, 1 ATC, 0 purchases, and its comment section fills with the Pond's objection (the ad hands them a cheaper alternative inside its own story).

3. **B9C3's CTR is LOWER than B5C1's and B7C1's (13.79% vs 19.5-48%), and it converts anyway.** Fewer clicks, but intent-loaded clicks. The object-discovery hook (a jar on a near-empty counter, what is it?) attracts solution-curious clickers. The recognition hooks (husband noticed / mother's photo) attract feel-seen clickers. Curiosity clicks buy. Recognition clicks don't.

### The Core Desire read, straight from the funnel

Map each converter's identity payoff to the funnel result:

| Ad | Payoff type | Core Desire it serves | Funnel result |
|---|---|---|---|
| B9C3 | "The not-carrying" (relief, skin handled, one jar) | **v2: skin cooperates again** | Converts repeatedly, both BMs |
| B3C2 | "Get the right bucket" (control, practical anger) | v2-adjacent (control/cost) | Converted (at $19.99) |
| B5C1 | "It's the Tuesday" (being seen by husband) | v1: be seen again | 1 old-BM sale, then 12 LPV / 0 ATC fresh BM |
| B7C1 | "Doing what mother did" (inheritance/validation) | v1-adjacent | Clicks and LPVs forever, 1 ATC, won't close |

The funnel data independently validates the Core Desire v2 decision. Relief/control payoffs close. Validation payoffs get cheap clicks that don't close. We locked v2 on theory in May; the spend data agrees with it. This is the strongest cross-confirmation in the dataset.

---

## PART 2: What Has ACTUALLY Been Tested (the honest audit)

This is the part that changes the picture most. **A test only counts if the ad got enough delivery to fail on its merits.** Applying the tracker's own thresholds (50+ impressions for engagement claims, meaningful spend):

### Genuinely tested and FAILED (real negative results, trust these)
- **Thesis/intellectual hooks** (B2C2: $38 spend, 4 LPV 0 ATC). Argument attracts evaluators, not buyers.
- **Husband-notice VARIANTS** (B6: wordless touch, unposed photo, generic compliment). All three lost to the skin-specific verbal original. The comment content is load-bearing.
- **Urgency in the HOOK** (B4: internal deadline, disgust/harm, calendar deadline). All failed, but two of three failures are confounded: B4C2 was a compliance bomb ($1,000 CPM penalty) and B4C3 was a hyper-narrow calendar anchor. The clean lesson is "urgency as the opener fails." NOT "urgency fails."
- **Short NMN-style functional ads** (B8). Falsified: no CPM benefit, no engagement.
- **Homesteader Mom avatar** (B10: $116-184 CPMs, 5 LPV 0 ATC on its best ad). Avatar didn't escape the auction or convert.
- **Compliance violations** (menopause, doctor-endorser, disgust, active-harm). Each one priced out by Meta within hours. Settled law.
- **Recognition-lane intent** (B5C1 fresh BM, B7C1 both BMs). Tested with real traffic. Earns clicks, doesn't earn carts.

### Killed but NEVER ACTUALLY TESTED (9 of 15 "failed" ads)
B1C1, B1C3, B2C1, B2C3, B4C3, B5C2, B5C3, B6C1, B6C2 all died with under $2-8 of spend and under 50 impressions. CBO starved them at birth. Their hooks failed to earn delivery (which IS information), but their bodies, angles, and structures were never read by a single meaningful sample of humans. The kill list overstates what we know. B2C1 "Cow Fat" in particular had the best CPM in its batch ($65) and died of CBO starvation, not rejection.

### NEVER tested at all (the actual frontier)
1. **Any ad with a protected budget.** Every single data point in this account's history comes from CBO, which starved 9 ads to death and concentrated 69% of spend on whichever ad had purchase signal. We have NEVER run an ad in its own ad set with a guaranteed daily budget. The Converter_Pattern_Synthesis specced exactly this test for B9C3 in April ("$25-40/day, 5 consecutive days, own ad set") and it never ran. **This is the single largest untested variable in the account, and it is a test-STRUCTURE variable, not a copy variable.**
2. **The narrative Urgency Anchor** (v2 skeleton element 11: urgency woven mid-story, not in the hook). Written into B16C2/B16C3. Never launched. The B4 failure does not cover this; B4 tested urgency as the opener.
3. **The offer.** Every sale ever made was a single jar at $49.99 on the same PDP (plus one accidental $19.99). BOGO is built and never been live. Offer-side "buy now" urgency: never tested.
4. **Price.** The one $19.99 sale converted on the structurally weakest converter (B3C2). That is a loud hint that price elasticity exists, and it has never been deliberately probed.
5. **Chain depth as a variable.** B9C3 is the ONLY launched ad with a 3-layer authority chain (narrator → Elaine → Aunt Winnie, 39 years of proof). Its uniqueness is confounded: object hook + chain depth 3 + decades-proof + relief payoff all travel together in one ad. We do not know which is load-bearing. B15C3 (Old Notebook, also chain depth 3) is written and would isolate this, but is parked.
6. **Per-use cost mention in a full-price ad.** Only B3C2 had it (converted, but at discount). B15C1 has it, parked.
7. **An advertorial / pre-sell bridge.** Never built, never tested.

---

## PART 3: The CPM Question Is Largely Answered, Stop Re-Solving It

Old BM: $200-450 CPMs. Fresh BM (Apr 21): B5C1 $53, B7C1 $123, account CPC $0.61 vs $2.71-6.36. Same ads, 2-8x cheaper. The fresh-campaign duplicate test (Apr 14) had already ruled out campaign-level causes. Conclusion: the CPM problem was account/BM-level and the fresh environment fixed most of it. B9C3's $552 CPM on Apr 21 is a CBO-concentration artifact (Meta paying premium to find buyers for the only ad with purchase signal), not a creative penalty.

Implication: auction-escape strategies (avatar pivots, ancestral reframes, category camouflage) were designed to solve a problem the fresh BM mostly solved. They are no longer the priority. The priority is conversion intent, where the data above points.

---

## PART 4: The Highest-Priority Next Test

### What the data demands

Combining Part 1 (only the relief-payoff One-Jar configuration closes), Part 2 (the two biggest untested levers are protected budgets and the narrative urgency anchor), and the founder's locked direction (one core desire, urgency worth testing, B16):

**TEST: B16 head-to-head, restructured as ABO (protected budgets), with the BOGO live on the PDP.**

Three changes from the current B16 plan, each forced by the data:

**1. ABO, not CBO. Each ad gets its own ad set with a fixed budget.** This is non-negotiable on the data: CBO has invalidated or contaminated every test this account has ever run (9 ads starved to death, budget concentration on the incumbent converter). If B16 runs CBO, B16C1 (the proven benchmark) will eat the budget by day 3 and we will learn nothing about the urgency anchor. Protected budgets are how we finally buy a clean read.

**2. The core matchup is C1 vs C3. C2 is the optional third cell.**
- **B16C1** (B9C3 exact): the proven control. 17% LPV→purchase, CPA $10.82-26.54, the bar.
- **B16C3** (One Who Should Have Fallen Apart): same One-Jar avatar, same counter image lane, but rebuilt with v2 relief framing + the narrative urgency anchor. C1 vs C3 is a true single-cluster A/B: same avatar, same visual, different skeleton generation. **This one matchup answers the most valuable open question in the account: does v2 + narrative urgency beat the configuration that already converts?**
- **B16C2** (Quiet House) is the husband-noticed lane rebuilt on v2 + urgency. The data is stacked against this lane (B5C1: 12 LPV 0 ATC fresh BM; B6: all variants falsified; B1C2: 0 sales). Running it answers "can the recognition lane convert when re-anchored to relief + urgency," which is a legitimate question, but it is third in line for budget. At $50/day: either run 2 cells at $25/day (faster, cleaner signal on the question that matters most) or 3 cells at $16-17/day (slower everywhere, but tests the lane rescue too). Founder's call. The data leans 2-cell.

**3. BOGO live before launch, with the pixel value verified by one test purchase.** This adds the offer-side "buy now" lever to the same launch without adding an ad-level variable (both cells see the same offer). Sequencing stays: native discount in admin first, then the liquid block, then one real test purchase to verify cart math + Purchase-with-value.

### Decision metrics (locked before launch so there is no mid-test rationalizing)

- **Primary: LPV→ATC and LPV→Purchase rate per cell.** This is where every non-B9C3 ad has died, so it is the metric the test exists to move. The bar: B9C3's historical ~17% LPV→purchase.
- **Secondary: CPA vs the $32.98 contribution margin.** Anything under ~$30 CPA is unit-profitable; under $20 is scale-ready.
- **NOT primary: CTR.** This account has proven CTR is a vanity metric. A 48% CTR produced zero dollars. Do not let a high-CTR cell win on CTR.
- **Volume reality at $50/day:** ~$700/fortnight, roughly 14-25 orders if things work. Minimum 10 combined orders before declaring a winner; below that, extend rather than lock.
- **Read the answers as:** C3 ≥ C1 on LPV→purchase = v2 + urgency anchor validated, becomes the skeleton for all future variants. C1 > C3 = the urgency anchor is not the lever; the next swing is proof-depth isolation (see queue below). Both below 0.8 ROAS at day 21 with the BOGO live = the problem is offer/price, jump to Test B in the queue.

### The test queue after this one (test, test, test)

Each subsequent test isolates the next-biggest untested lever, in order of expected information value:

| # | Test | Lever isolated | Trigger |
|---|---|---|---|
| **A** | B16 C1 vs C3, ABO, BOGO live | Narrative urgency + v2 skeleton vs proven control | NOW (after warmup gates + Tier 1 funnel fixes) |
| **B** | Offer/price test: winner of A with BOGO-prominent vs single-jar framing (or a $39.99 price probe) | The offer. The $19.99 accident says price moves this buyer; never deliberately tested | If A produces a winner that's under 2x ROAS, or both cells stall |
| **C** | Proof-depth test: winner's skeleton with chain-depth 3 + decades-proof (Winnie-style) vs chain-depth 1 | Is the 3-layer/39-years authority chain B9C3's secret weapon? B15C3 is pre-written for this | After A locks a skeleton |
| **D** | Hook-lane expansion: 2-3 new object-discovery hooks (not recognition hooks) on the winning skeleton | Scale the curiosity-click lane that converts; abandon recognition hooks for cold traffic | After A or C produces a 2x+ ROAS ad |
| **E** | Advertorial bridge vs direct-to-PDP on the winner | Post-click message match | Once a winner is spending consistently |

### What we STOP doing (the data has spoken)

- **Stop running recognition-payoff hooks at cold traffic.** Husband-noticed and mother's-photo earn the cheapest clicks in the account and close nothing. If the lane comes back, it comes back as a retargeting layer, not a cold-traffic prospector.
- **Stop solving the CPM problem.** The fresh BM solved most of it. The bottleneck moved to intent.
- **Stop trusting CBO to run experiments.** CBO is for scaling a known winner, not for testing. Every test from now on is ABO/protected budget until we have a winner to scale.
- **Stop counting starved ads as failed angles.** 9 of the 15 "killed" ads were never tested. Their angle inventory (Cow Fat especially) stays on the shelf for the Phase 4 variant pool, not in the graveyard.

---

## One-Line Answer

**The data says the only configuration that converts is the One-Jar relief-payoff ad, the two biggest things we have never tested are protected budgets and the narrative urgency anchor, so the highest-priority test is B16 C1-vs-C3 run as ABO at $25/day per cell with BOGO live, judged on LPV→purchase against B9C3's 17% bar, with CTR explicitly demoted to a vanity metric.**

---

*Analysis: 2026-06-10. Update when B16 produces 14 days of data.*
