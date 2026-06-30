# Feedback Loop: Batch 17: Urgency Isolation Test

**Batch:** 17 (4-cell ABO: C1 Control / B9C3 verbatim, C2 Same-Morning Grind, C3 Cost-Bleed, C4 Closing Window)
**Test variable:** Does adding an urgency mechanism lift the proven B9C3 One-Jar angle above its baseline?
**Window:** 2026-06-16 → 2026-06-30 (13 days, $20/day re-warming budget → CBO)
**Status:** Concluded. C1 is the only surviving cell; C2/C3/C4 are dead or killed.
**Verdict:** Urgency variants did NOT lift the angle. The verbatim control (no urgency mechanism) is the only cell that ever converted. B9C3's proven skeleton is durable; the urgency layer added nothing and in two cases (C3, C4) actively underperformed the control on the metric that matters (purchases).

---

## Performance Summary (lifetime, by cell)

| Cell | Mechanism | Lifetime Spend | Purchases | Revenue | CPA | ROAS | Fate |
|---|---|---|---|---|---|---|---|
| **C1 Control** | B9C3 verbatim, no urgency | $125.19 | **4** | $199.96 | **$31.30** | **1.60x** | Still active, only proven converter |
| **C4 Closing Window** | Recoverability/garden metaphor urgency | ~$19.96 | 0 | $0 | n/a | n/a | Starved to death (never got budget after Day 1) |
| **C3 Cost-Bleed** | Sales-math/receipts urgency | ~$46.36 | 0 | $0 | n/a | n/a | Killed by founder before Day 6 |
| **C2 Same-Morning Grind** | Daily-grind urgency | ~$8.40 | 0 | $0 | n/a | n/a | Never found a real auction; dead weight throughout |

**Account total B17 spend:** ~$200 across 13 days. **4 purchases, all on C1.** Zero purchases on any urgency variant despite C3 and C4 each getting meaningful delivery (C3 especially: $46+ spent with strong CTR at points and never closed).

---

## Step 1: Hypothesis

### Why C1 (the control) worked, ranked most to least confident

**1. The proven skeleton is genuinely durable, not a fluke (HIGH CONFIDENCE).** C1 is verbatim B9C3: the same object-discovery hook, five-character chain, and husband-notice close documented as the account's strongest ad since April. It converted 4 times across this batch (Day 4, Day 6 ×2, Day 10) in completely different delivery conditions (re-warming budget, ABO, then CBO). That's not luck: that's a structurally sound ad doing what it's always done.

**2. Bursty-but-real conversion pattern, consistent with prior B9C3 behavior (HIGH CONFIDENCE).** Days 7-9 were dry ($15.33, $5.66, $10.65 spent, zero purchases), then Day 10 converted at $6.65 for 7.52x ROAS: the best single-cell ROAS of the entire test. This matches the exact bursty pattern documented in the original B9C3 feedback loop (Apr 14 yes, Apr 16 no, Apr 21 yes). The ad doesn't convert linearly; it converts in clusters. Reinforces that the 2x-breakeven kill rule (not a flat no-purchase line) is the correct tool for judging it.

**3. Meta's algorithm self-corrected toward the converter (MEDIUM-HIGH CONFIDENCE).** Day 5 was the first day C1 led spend (61% of account): directly after the Day 4 purchase. By Day 6 it was eating 97% of budget. This is the auction recognizing a working signal and reallocating without any manual intervention. Good evidence the CBO/ABO system is functioning correctly once it has a real purchase signal to learn from.

**4. High CTR ceiling when delivery is fresh (MEDIUM CONFIDENCE).** Day 6 hit 15% CTR, Day 10 hit 22.22% CTR: both well above the account's typical 3-9% range. These spikes correlate with the days it converted. Possibly the algorithm narrows to a hot pocket right before/during a purchase cluster, then drifts back to broader (cooler) delivery afterward (Day 7: CTR dropped to 2.35% on the very next day).

### Why C2, C3, C4 (the urgency cells) did NOT work, ranked most to least confident

**1. C2 (Same-Morning Grind) never got a real auction test (HIGH CONFIDENCE: this is an "unproven," not "disproven" angle).** Zero delivery for 4 consecutive days at launch, and every day after that was starved to $0-2.51. Total lifetime spend ~$8.40 across 13 days. This is a structural ABO/CBO starvation failure, not a creative failure. We learned nothing about whether "same-morning grind" urgency works as a mechanism: we only learned Meta's auction never gave it a fair look once C1 had a purchase signal to chase.

**2. C3 (Cost-Bleed) is the cleanest disproof: it got real delivery and still didn't close (HIGH CONFIDENCE).** This is the one urgency cell that actually got tested. Day 2: 81% of account spend, 15% CTR, 1 IC: looked promising. But that IC never converted, and the pattern repeated: Day 4 a NEW ATC, 0 checkouts. By Day 5 Meta had already started de-prioritizing it in favor of C1. Across ~$46 of real spend with real clicks and real top-of-funnel engagement, it produced zero purchases. The "sales-math wearing the buyer's receipts as a costume" framing (customer-eyes agent's original prediction) generated curiosity (clicks) but apparently didn't survive contact with the PDP or the actual buying decision: consistent with the broader account-wide low-ATC-rate problem, not specific to this cell's compliance risk.

**3. C4 (Closing Window) showed the single best engagement-per-impression signal in the batch and STILL never converted (MEDIUM-HIGH CONFIDENCE).** Day 1: 15.28% CTR, the only ATC of the day, lowest CPM in the batch at points ($108-170). The customer-eyes agent predicted this cell would feel "weightless / floated by": the early CTR contradicted that. But it never got sustained budget (Meta abandoned it after Day 1), so the one ATC it generated never had a chance to compound into a purchase pattern. This is the most ambiguous result in the batch: was it killed too early by the algorithm before it could prove out, or did the high compliance-risk garden/recoverability metaphor simply not survive the decision-making moment the way the engagement metrics suggested it would? Genuinely unknown: this cell has the least data of the three urgency variants.

**4. Pattern across all three: urgency mechanisms generate curiosity-clicks that don't survive to purchase (MEDIUM CONFIDENCE, ties to the account-wide ATC% problem).** All three urgency cells, when they got any delivery at all, showed CTR at or above C1's typical range. None converted. This is consistent with the broader hypothesis already logged in HANDOFF's ATC brainstorm: ads can build curiosity/clicks without building the deeper desire/trust needed to actually buy. Urgency framing in particular may be especially prone to this: it creates a reason to look NOW without necessarily building the underlying case for the product itself.

---

## Step 2: Action - What Changes Going Forward

### Keep

- **B9C3 verbatim as the default control in every future batch.** It is the only angle in the account with a multi-month track record of repeat conversion across different BMs, budgets, and campaign structures (Apr → Jun). Every new batch should run it as a benchmark cell unless/until something beats its $31.30 lifetime CPA.
- **The 2x-breakeven (not flat no-purchase) kill rule for proven converters.** C1's bursty pattern (dry Days 7-9, converts Day 10) is exactly the variance the rule was designed to tolerate. A flat line would have killed it mid-streak.

### Change

- **Never launch a new test angle in the same ABO/CBO as a known converter again.** This is the single biggest structural lesson from B17. C2 never got a fair test. C3 and C4 got partial reads only because the converter (C1) hadn't yet produced its first purchase signal: once it did (Day 4 on), the algorithm correctly abandoned the urgency cells, which is right FOR THE ALGORITHM but wrong FOR US if we wanted clean reads on all 4 cells. **Going forward: untested angles get their own isolated budget/campaign from day one** (this lesson was already partially learned and applied to B19/B20, which launched in separate campaigns).
- **Stop testing "urgency as a layer on top of a proven angle" as the next lever.** Three independent urgency mechanisms (daily-grind, cost-math, closing-window) all failed to convert despite at least two of them getting real delivery. This is a reasonably strong signal that urgency-bolted-onto-B9C3 is not the unlock. Don't run a 4th urgency variant without a new theory for why it would behave differently.
- **Re-examine C3 and C4's specific compliance/tone risk separately from "did urgency work."** Both ranked high on the customer-eyes agent's pre-launch risk read. It's possible the issue isn't "urgency doesn't work" but "these two specific executions of urgency read as inauthentic/salesy in a way that breaks the peer-confession voice the rest of B9C3 relies on." Worth a copy post-mortem against `Tallow_Ad_Creative_Principles.md` Principle 5 (voice rules) before fully closing the book on urgency as a category.

### Test Next

- **C2 (Same-Morning Grind) deserves a real, isolated test before being called dead.** It never got a fair auction read. If urgency gets revisited at all, this is the one to re-run first, in its own ad set/budget from day one.
- **C4 (Closing Window) is the most interesting "maybe" in the batch.** Best engagement signal, killed by starvation not by failure. If there's appetite to revisit urgency, give this one a real budget floor for at least 3-4 days before judging it.
- **Apply the B17 structural lesson directly to B20 and beyond:** every new angle test gets isolated budget from launch. (Already done for B19/B20: confirm this discipline holds for whatever comes after.)
- **Feed this into the ATC% diagnosis (HANDOFF TODO #2):** B17 adds a data point: urgency-driven clicks (C3, C4) did not convert at a higher rate than the baseline's clicks. This weakens "we need more urgency" as a fix for the ATC leak and strengthens hypotheses further down the funnel (PDP, offer, trust-at-decision-point) as the more likely culprits. Cross-reference against the B19 feedback loop before concluding.

---

*Feedback loop completed 2026-06-30. Source: `Ad_Performance_Tracker.csv` B17 rows (2026-06-16 through 2026-06-30) + `Kill_Rules_and_Decision_Framework.md` two-regime kill logic. Template: `origins-training/origins-notes/origins-_-feedback-loops.docx`.*
