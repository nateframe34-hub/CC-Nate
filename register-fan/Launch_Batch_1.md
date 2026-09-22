# Launch Batch 1 — SA1, All Angles

**Created:** 2026-09-22
**Reads against:** `Brand_Mastery.md` (avatars, claim rules), `Offer_Structure.md` (price, kill rules), `Format_Angle_Map.md` (format × angle), `Launch_Plan.md` (Q4 clock).

---

## 1. What this batch can and cannot answer

The four stated goals, checked against the money available.

| # | Question | Answerable? |
|---|---|---|
| 1 | **Can we sell this product to Meta consumers at all?** | ✅ **Yes — this is the one that matters and the one $600 can answer.** |
| 2 | Which sub-avatar is most profitable? | ❌ **Not in this batch.** A batch that only runs SA1 cannot compare SAs. Needs Batch 2 |
| 3 | Which angle has the highest ROAS? | ⚠️ **Not on ROAS.** Answerable on *upper-funnel* signal in this batch; ROAS needs volume we won't have |
| 4 | Which format does the winning angle respond to? | ⚠️ **Only after 3 is settled**, and only if we don't split the budget nine ways |

### The arithmetic that forces this

$600 ÷ 9 cells = **$66 per cell.** At a hypothetical $2 CPC that is ~33 clicks. At any plausible conversion rate, **under one purchase per cell.**

> **You cannot rank anything on ROAS at one purchase per cell.** Tallow was killed partly for judging decisions on exactly this kind of sample. Nine cells at once would produce nine numbers that all look meaningful and none of which are.

**So: sequence, don't parallelise.** Stage 1 isolates angle. Stage 2 isolates format on the surviving angle. Each stage gets enough per cell to read something real.

---

## 2. The metric ladder — what is readable at what spend

This governs every kill decision. Reading a metric before its threshold is how money gets wasted on false confidence.

| Cumulative spend / cell | What becomes readable | What is still noise |
|---|---|---|
| $0-25 | **CPM** (directional) | Everything else |
| ~$40 | **CTR** — the first real signal | CPC, LPV, everything downstream |
| $60-90 | **CPC**, LPV, cost per LPV | ATC, purchases |
| $150+ | **ATC rate** | Purchase rate |
| $250+ / cell | Purchase rate, CAC | — |

**Consequence: Stage 1 is decided on CTR and CPC, not on purchases.** Purchases in Stage 1 are a bonus signal — if one arrives, it is evidence for Question 1, not evidence that its angle won.

---

## 3. Stage 1 — the ANGLE test

**Variable isolated: angle. Format held constant.**

**Format held constant: Statement static (G)** — one line of plain high-contrast type, no image.

Why this one as the control:
- It is the most **neutral** carrier available. The image contributes nothing, so the angle is genuinely the only variable.
- It costs minutes to produce, so all three cells are identical in production quality — no cell wins on craft.
- It needs **no product, no persona page, no supplier photography.** Nothing blocks it.
- It carries in **every placement**, including right column.

### The three cells

| Cell | Angle | Line on the image | Evidence |
|---|---|---|---|
| **B1C1** | **SA1-A3 — You don't need a contractor** ⭐ | **"Two screws and an outlet. Not $3,400."** | **Strongest.** *"$3-4,000"*, *"quoted over 3k"*, *"That seems rather high and I don't like the broad range"* |
| **B1C2** | **SA1-A1 — You were right; here's what nobody told you** | **"The last room on the duct run gets whatever's left."** | Good. Self-diagnosis quotes + the contested vent-closing advice |
| **B1C3** | **SA1-A2 — Don't heat the whole house for one room** | **"You turned the thermostat up for one room. Again."** | ⚠️ **Weak — this angle is MINE, not theirs.** No quote found of anyone complaining about over-conditioning. Running it *because* it's unevidenced: if it wins, my inference was right; if it loses, we stop guessing |

**Config:** ABO, **$12.50/day per cell**, Purchase optimisation, broad, US, Advantage+ placements. Not CBO — CBO concentrates spend on first-hour noise, which produced this account's worst reads.

**Duration: 5 days.** 3 cells × $12.50 × 5 = **$187.50.**

### Stage 1 decision rules

| Signal | Threshold | Action |
|---|---|---|
| CTR | under **1.0%** at $40 spend | Kill the cell |
| CTR | clear leader by **1.5×** over the others | That angle advances |
| CPC | above **$4.00** on every cell after the full $187.50 | **Stop the whole batch.** The economics do not close at any price we can charge |
| **All three die on CTR** | — | ⚠️ **Do not conclude "SA1 is dead."** Conclude "plain type may be too weak a carrier." Re-run the best angle in a second register (two-panel thermometer) before writing off the avatar |

That last row is the guard against the biggest risk in this design: a neutral control format is neutral in both directions.

---

## 4. Stage 2 — the FORMAT test

**Variable isolated: format. Angle held constant — whichever survived Stage 1.**

Three registers, deliberately far apart so no two can be taxed by the same familiarity:

| Cell | Format | Register | Needs |
|---|---|---|---|
| **B1C4** | **Native long-form** | Story | ⚠️ **Persona page** |
| **B1C5** | **Two-panel thermometer** *(or duct diagram if Angle 2 won)* | Documentary / explanatory | Two $10 thermometers |
| **B1C6** | **This Is Not [The Product]** — *"This isn't a fan for the room. It's a fan for the vent."* | Reframe / typographic | Type + a vent photo |

**Config:** identical to Stage 1. **5 days, $187.50.**

**Note:** B1C4 excludes right-column placement — it cannot render primary text, and a native there delivers an image with no argument attached.

### Stage 2 decision rules

Same CTR and CPC gates, **plus** the first real look at the funnel: cost per LPV and ATC rate. Still not ROAS — $62.50 per cell does not buy a purchase-rate read.

---

## 5. Reserve — ~$225

Whatever survives Stage 2 gets the remaining budget in a single cell at $25-50/day for 5-7 days. **This is the only cell in the entire plan that gets enough spend to say anything about CAC**, and it is the one that answers Question 1 properly.

---

## 6. What "can we sell this on Meta" actually looks like

The honest bar, stated before spending so it can't be moved afterwards:

| Outcome | Read |
|---|---|
| **2+ purchases at CAC under $56.15** in the reserve cell | ✅ **Yes.** Product sells. Proceed to Batch 2 (avatar comparison) |
| **1 purchase**, CAC above room | 🟡 Inconclusive but alive. The mechanism works; economics unproven |
| **0 purchases, healthy CTR and CPC** | 🟠 **The creative works and the offer or page doesn't.** Fix the PDP or the price, not the ads |
| **0 purchases, CTR under 1% throughout** | 🔴 Creative or avatar is wrong. Re-test in another register before killing the product |
| **CPC above $4 across every cell** | 🔴 **Stop.** No price we can charge closes this |

**Hard cap: $600. It does not move.** Extending "for one more read" is the documented mechanism by which tallow reached $2,000.

---

## 7. Batch 2 — Question 2 (which SA is most profitable)

Cannot run before Batch 1 answers Question 1. Design, for the record:

Hold the **winning format** constant. Vary **avatar**, using each one's best-evidenced angle:

| Cell | Avatar | Angle |
|---|---|---|
| — | **SA1** | Batch 1 winner (the control) |
| — | **SA6** — Fixing It For Someone Else | *"You keep checking that room."* Strictest claim rules in the project |
| — | **SA2** — the bedroom | The space-heater beat |
| — | **SA3** — renters | The landlord quote *(gated on confirming the unit is reversible)* |

Funded by Batch 1's result, not from this $600.

---

## 8. Prerequisites

| # | Item | Blocks | Status |
|---|---|---|---|
| 1 | Brand page + BM, warmed | Everything | ❌ Not started. Last BM was banned as a suspected bot — warmup history matters |
| 2 | Store + PDP | Everything | ❌ PDP scrapped 2026-09-17, needs rebuild |
| 3 | Category name | PDP, domain, copy | ❌ Open founder decision |
| 4 | Cold-side research verbatim | Copy quality | 🟡 Thin; Stage 1 lines are usable without it |
| 5 | Persona page | **Stage 2 B1C4 only** | ❌ Not started — **Stage 1 is not blocked by this** |
| 6 | Two thermometers | B1C5 | 🟢 $20 |

**The critical path is the store, not the creative.** All three Stage 1 cells can be produced in an afternoon; none of them can run without somewhere to send the click.

---

## 9. Schedule against the Q4 clock

Meta CPMs ramp from mid-October. Today is 22 September.

| | |
|---|---|
| Stage 1 | 5 days, $187.50 |
| Stage 2 | 5 days, $187.50 |
| Reserve | 5-7 days, ~$225 |
| **Total** | **~17 days of spend** |

Starting inside the next week finishes around **10-14 October — just ahead of the ramp.** Every day of prep past that is paid for in auction price, so the store and the brand page are worth doing fast and plainly rather than well.
