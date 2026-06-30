# Feedback Loop: Batch 19: Whiteboard Format CPM Test

**Batch:** 19 (3-cell: C1 Greasy/Shiny objection-buster, C2 Water vs Tallow mechanism, C3 Delayed Results timeline)
**Test variable:** Does the static whiteboard diagram format escape the saturated native long-form auction bucket and deliver at a lower CPM, and does it convert?
**Window:** 2026-06-24 → 2026-06-30 (7 days; first 4 days starved in a shared campaign, then relaunched in an isolated $10/day campaign 6/28-6/30)
**Status:** Concluded. C2 is the format's proof-of-concept winner and remains active. C1 and C3 are both killed.
**Verdict:** The whiteboard FORMAT hypothesis is confirmed: but only conditionally. Cheap CPM is creative-specific, not format-wide. The mechanism/comparison diagram (C2) is a genuine winner on CPM AND conversion. The timeline diagram (C3) proved the opposite failure mode from B17's urgency cells: it bought cheap, engaged clicks that never converted. C1 never got tested at all due to a structural starvation bug.

---

## Performance Summary (lifetime, by cell)

| Cell | Diagram type | Lifetime Spend | Best CPM | Purchases | CPA | Fate |
|---|---|---|---|---|---|---|
| **C2 Water vs Tallow** | Mechanism/comparison diagram | ~$12.38 | **$19.07** (low: $76.69 high) | **1** | **$11.35** | Active, only whiteboard converter, format's CPM star |
| **C3 Delayed Results** | Results timeline | $17.86 (cumulative, final slice) | $162-270 | 0 | n/a | Killed (2x-breakeven rule, correctly) |
| **C1 Greasy/Shiny** | Objection-buster comparison | $0.00 | n/a (never delivered) | 0 | n/a | Killed (never got an at-bat, starved) |

**Critical structural note:** Days 1-4 (Jun 24-27), B19 was in the SAME campaign as B17C1 (the proven native converter). It spent **$0.00 across all 4 days**: Meta routed 100% of budget to the known converter. The format hypothesis was completely untestable until B19 was moved to its own isolated $10/day campaign on Jun 28. This single structural fix is what made the rest of the test possible.

**Same-day CPM comparison (the core proof point, Jun 28):** B19C2 $76.69 CPM vs. B17C1 native $187.81 CPM, same account, same day. Whiteboard format delivered at ~41% of native cost. By Jun 29, B19C2 dropped further to **$19.07 CPM**: a single creative beating the entire account's historical CPM range by 5-10x.

---

## Step 1: Hypothesis

### Why C2 (Water vs Tallow) worked, ranked most to least confident

**1. The mechanism-as-diagram IS the sales argument, with no translation loss (HIGH CONFIDENCE).** C2 visualizes the exact water-evaporates-vs-fat-absorbs mechanism that has been the converting core of B9C3 and every native winner since April. Unlike the urgency cells in B17 (which bolted a NEW mechanism onto a proven angle), C2 took an ALREADY-PROVEN piece of reasoning and changed only its delivery format (diagram vs. paragraph). Lower risk, and the result shows it: it's the only whiteboard cell to convert, on its very first real day of delivery (Jun 28, $11.35 CPA, 4.40x ROAS).

**2. Dwell time is the likely CPM mechanism (HIGH CONFIDENCE, matches the principle already documented in `Whiteboard_Ad_Format_Principles.md`).** C2 is a richer diagram that rewards reading (two labeled columns, molecule icons, a bottom-line payoff). C3 (the cell that failed) is a quick-scan timeline: readable in under a second. The CPM gap between them (C2 consistently $19-77, C3 consistently $162-270) lines up almost exactly with "how long does this make someone stop and look." This is the same mechanism Meta's classifier appears to reward across the cross-niche examples studied (Neuro-Ignite, PowerPeak, Javvy) before this batch was built.

**3. Format genuinely escapes the saturated native auction bucket (HIGH CONFIDENCE on the CPM claim specifically).** Same account, same day, same audience pool, more than 2x CPM difference between C2 and native B17C1. This isn't a different audience finding a cheaper pocket: it's the same Meta account being classified differently because the creative LOOKS different (real photographed whiteboard, hand-drawn marker, no brand polish: per the format principles doc). Strong, clean evidence the format itself (not just the angle) carries CPM value.

### Why C3 (Delayed Results) did NOT work, ranked most to least confident

**1. Cheap clicks that never converted: the same failure mode as B17's urgency cells, but worse (HIGH CONFIDENCE).** Jun 29: 11.00% CTR, 11 clicks, 10 LPV (91% click-to-LPV): genuinely excellent top-of-funnel numbers. Zero ATCs. The final killed slice (Jun 30) shows the cumulative damage: $270.61 CPM, 1.52% CTR, $17.86 CPC: a creative that had clearly exhausted whatever audience pocket was responding to it. This is the cheap-clicks-don't-convert pattern called out by the Avatar Council, now observed twice in two different batches (B17C3/C4 and B19C3): worth treating as a real account-level pattern, not a one-off.

**2. A timeline is a weaker "teach me something" hook than a mechanism (MEDIUM-HIGH CONFIDENCE).** Per the whiteboard format principles, the format's persuasion mode is curiosity/learning, not recognition. A results timeline ("week 1: nothing, week 4: results") promises an outcome but doesn't actually teach a mechanism: there's no "oh, I get it now" moment the way there is with water-vs-fat. It may generate curiosity-clicks ("will this actually work for me by week 4?") without building the logical case that makes someone trust the product enough to add to cart. This matches hypothesis #1 in HANDOFF's ATC brainstorm (ads build narrow curiosity without building broad desire).

**3. Possible mismatch between the dwell-time CPM reward and actual buying-readiness (MEDIUM CONFIDENCE).** C3's 12.12% CTR on Jun 28 was nearly as strong as C2's eventual numbers, and its CPM started reasonably (cold-start $186, comparable to C2's early reads). But the conversion never followed. This raises a genuine open question: is Meta's classifier rewarding "people who stop and read" without that necessarily correlating with "people who are close to buying"? If true, this would mean dwell-time-optimized creative could systematically attract engaged-but-not-ready traffic: worth testing directly in a future batch rather than assuming dwell time always predicts purchase intent.

### Why C1 (Greasy/Shiny) is inconclusive, not a real finding

**Zero delivery for the entire test (HIGH CONFIDENCE this is a structural failure, not a creative failure).** $0.00 spend, 0 impressions, start to finish. CBO routed 100% of budget to C2 (once it proved itself) and C3 (which kept getting tested despite never converting, likely because of its strong CTR signal misleading the algorithm). C1: built specifically to address the #1 pre-purchase objection in the category (greasiness/shine), per the Amazon review research: never got a single impression to test that thesis. This is the exact same starvation failure pattern as B17C2 (Same-Morning Grind).

---

## Step 2: Action - What Changes Going Forward

### Keep

- **C2 (Water vs Tallow) stays active and becomes the new house template for whiteboard creative.** It's the best CPM+conversion combination on the account right now ($11.35 CPA beats even C1 native's $31.30 lifetime CPA). Future whiteboard cells should default to mechanism/comparison diagrams over timelines.
- **Isolated-campaign-from-launch discipline.** This batch is the second consecutive case (after B17) where a shared campaign with a known converter completely starved new tests. Already corrected mid-batch here (Jun 28 fix): confirm this is now standard practice for every future test launch, not just a one-time fix.
- **The whiteboard format itself as a CPM lever for proven angles.** B20 (Counter Math, Money Math, Label Test: all proven angles in this format) is the direct, correct next step and is already in motion.

### Change

- **Don't trust CTR/LPV alone as a leading indicator anymore: require it to convert within a defined spend window.** C3 had excellent top-funnel metrics for days before it was killed. The 2x-breakeven kill rule worked exactly as designed here (correctly killed it), but earlier recognition of the cheap-clicks-don't-convert pattern (now confirmed twice, B17 and B19) should make us faster to be skeptical of "great CTR, no ATC" cells going forward: watch them closer and sooner rather than waiting the full rule out passively.
- **Build a real test for C1 (Greasy/Shiny) before concluding anything about objection-busting diagrams.** It has zero data. Re-run it in its OWN isolated ad set/campaign, not pooled with anything that has prior purchase signal, so it gets a fair read this time.
- **Investigate whether dwell-time-rewarded creative systematically attracts low-purchase-intent traffic.** This is a new, untested hypothesis raised by C3's failure pattern. Worth a deliberate test: build two whiteboard cells with similar topics but deliberately different dwell profiles (quick-scan vs. rich-read) and track LPV→ATC specifically, not just CTR/CPM.

### Test Next

- **B20 is the direct next step and is already live**: proven angles (One-Jar counter math, cost-comparison, label comparison) rebuilt in the C2-style mechanism/comparison diagram format. Watch whether they replicate C2's CPM+conversion combo or whether C2 was partly a lucky early-mover result.
- **Re-test C1 Greasy/Shiny in isolation.** The objection it targets (greasiness/shine) is the #1 pre-purchase fear in the category per review research: too important to leave untested due to a delivery bug.
- **Feed this into the ATC% diagnosis (HANDOFF TODO #2) alongside the B17 feedback loop.** Two independent batches (B17's C3/C4, B19's C3) now show the same pattern: ads that generate strong clicks/LPVs but zero ATCs. This is no longer cell-specific noise: it's a recurring account-level signal that something between LPV and ATC (the PDP, the offer, trust-at-decision-point) is the more likely root cause than weak top-of-funnel creative. The creative is, if anything, doing its job too well relative to what happens after the click.

---

*Feedback loop completed 2026-06-30. Source: `Ad_Performance_Tracker.csv` B19 rows (2026-06-24 through 2026-06-30) + `Whiteboard_Ad_Format_Principles.md`. Template: `origins-training/origins-notes/origins-_-feedback-loops.docx`.*
