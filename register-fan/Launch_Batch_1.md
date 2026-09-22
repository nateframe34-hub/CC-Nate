# Launch Batch 1 — SA1, All Angles

**Created:** 2026-09-22 · **Restructured 2026-09-22 (founder call)**
**Reads against:** `Brand_Mastery.md`, `Offer_Structure.md`, `Format_Angle_Map.md`, `Launch_Plan.md`.

> **Structure correction.** An earlier version of this file sequenced an angle test and then a format test, on the grounds that $600 split nine ways yields under one purchase per cell. **That was wrong, because it costed each ad as its own budget line.** With the **ad set as the angle** and three ads inside it, the angle receives the full ad-set budget and Meta allocates impressions between the three formats itself. Angle, format and (when extended) sub-avatar are all testable in one campaign.

---

## 1. Architecture

**One campaign. ABO. Each ad set is an ANGLE. Each ad set holds 3 ads: 1 native + 2 non-native.**

```
CAMPAIGN — Register Fan | SA1 | Purchase | ABO
│
├── AD SET 1 — Angle A3: "You don't need a contractor"      $20/day
│     ├── Ad 1  Native long-form                    [persona page]
│     ├── Ad 2  Solution Exaggeration (typographic)  [brand page]
│     └── Ad 3  Minimal Us vs Them — vs the quote    [brand page]
│
├── AD SET 2 — Angle A1: "You were right about the room"    $20/day
│     ├── Ad 1  Native long-form                    [persona page]
│     ├── Ad 2  Duct-run diagram (explanatory)       [brand page]
│     └── Ad 3  This Is Not [The Product] (reframe)  [brand page]
│
└── AD SET 3 — Angle A2: "Don't heat the whole house"       $20/day
      ├── Ad 1  Native long-form                    [persona page]
      ├── Ad 2  Two-panel thermometer (documentary)  [brand page]
      └── Ad 3  Relatable Hook (typographic)         [brand page]
```

**$60/day. 7 days = $420.** Reserve $180 of the $600 cap for extending whatever wins.

### Why this reads three things at once

| Level | Where it is read | Mechanism |
|---|---|---|
| **Angle** | **Between ad sets** | Each angle accumulates ~$140 over 7 days — the full ad-set budget, not a ninth of the campaign |
| **Format** | **Within each ad set** | Meta concentrates delivery on the creative it predicts will perform. That concentration *is* the format answer |
| **Sub-avatar** | **Add ad sets** | Same pattern. Batch 2 adds SA6 / SA2 / SA3 ad sets alongside the SA1 winner |

---

## 2. Config

| Setting | Value | Why |
|---|---|---|
| Budget | **ABO, $20/day per ad set** | Protected budget per angle. **Not CBO** — CBO concentrates spend on first-hour noise, which produced this account's worst reads |
| Optimisation | Purchase | Nothing upstream is worth optimising toward on a $100 product |
| Audience | Broad, US, no interest stacking | Post-Andromeda the creative sorts the audience. Interest targeting on a new pixel just shrinks the pool |
| Placements | Advantage+ | **Except the three native ads — exclude right column.** It cannot render primary text, so a native there serves an image with no argument attached. The non-natives keep every placement; that coverage is why they exist |
| Duration | 7 days minimum | Do not judge before day 4 |
| Ads per ad set | **3, all live at launch** | **Never add a fourth mid-flight — it resets learning for the whole ad set** |

---

## 3. The honest caveats on this design

Neither of these is a reason to change it. Both are reasons to read the results correctly.

**⚠️ We will be learning-limited the entire time.** Meta wants ~50 conversions per ad set per week to exit learning. At $20/day against a $56 CAC ceiling, the ceiling is ~2-3 purchases per ad set per week at best. **Every result from this batch is directional, not statistically settled.** That is normal and acceptable for a first read — it is not acceptable as a basis for declaring a winner and scaling hard.

**⚠️ The format read is a delivery-preference read, not a clean conversion comparison.** Meta typically concentrates 70-90% of an ad set's spend on one creative within a couple of days. That answers *"which format does Meta serve cheaply for this angle"* — genuinely useful, since delivery cost is the thing that killed the last product. It does **not** establish that the other two formats convert worse; they may simply never have been given the impressions. If a format read matters enough later, isolate it in its own ABO.

---

## 4. The metric ladder

Governs every kill decision. Reading a metric before its threshold is how money buys false confidence.

| Cumulative spend | Readable | Still noise |
|---|---|---|
| $0-25 | CPM (directional) | Everything else |
| ~$40 | **CTR** — first real signal | CPC, LPV, downstream |
| $60-90 | **CPC**, LPV, cost per LPV | ATC, purchases |
| $150+ | ATC rate | Purchase rate |
| $250+ | Purchase rate, CAC | — |

**Per ad set, $140 over 7 days.** So by the end of the run CTR, CPC and cost-per-LPV are readable at the angle level; ATC is marginal; purchase rate is not. **Judge angles on cost per landing-page view and CTR, with purchases as a tiebreak and as evidence for Question 1.**

---

## 5. Kill rules

| Level | Signal | Threshold | Action |
|---|---|---|---|
| **Ad** | CTR under 1.0% | at $40 ad spend | Pause the ad, leave the ad set running |
| **Ad set** | 0 purchases | at $140 (full run) | Angle does not advance |
| **Ad set** | Cost per LPV 2× the best ad set | at $90 | Angle does not advance |
| **Campaign** | CPC above $4.00 on every ad set | at ~$250 total | **Stop.** The economics do not close at any price we can charge |
| **Campaign** | Hard cap | **$600** | Does not move. Extending "for one more read" is how tallow reached $2,000 |

**Guard:** if all three ad sets die on CTR, do **not** conclude SA1 is wrong. Nine ads across three registers failing together points at the offer, the page or the product — not at the avatar. Check the PDP before writing off the research.

---

## 6. What "can we sell this on Meta" looks like

Set before spending so it cannot move afterwards.

| Outcome | Read |
|---|---|
| **3+ purchases, blended CAC under $56.15** | ✅ Product sells. Fund Batch 2 from it |
| **1-2 purchases**, CAC above room | 🟡 Alive, economics unproven. Extend the winning ad set with the $180 reserve |
| **0 purchases, healthy CTR and cost per LPV** | 🟠 **Creative works, page or offer doesn't.** Fix the PDP or the price — do not rewrite ads |
| **0 purchases, CTR under 1% across all nine** | 🔴 Wrong avatar or wrong product. Re-check the page first, then stop |
| **CPC above $4 everywhere** | 🔴 Stop |

---

## 7. Batch 2 — the sub-avatar test

Same architecture, ad set = sub-avatar, each carrying its own best-evidenced angle:

| Ad set | Sub-avatar | Angle |
|---|---|---|
| Control | **SA1** | Batch 1's winning angle + winning format |
| 2 | **SA6** — Fixing It For Someone Else | *"You keep checking that room."* ⚠️ Strictest claim rules in the project — temperature and not-checking only, never risk or safety |
| 3 | **SA2** — the bedroom | The space-heater beat |
| 4 | **SA3** — renters | The landlord quote *(gated: confirm the unit is reversible)* |

Funded by Batch 1, not from this $600.

---

## 8. Prerequisites

| # | Item | Blocks | Status |
|---|---|---|---|
| 1 | **Store + PDP** | **Everything** | ❌ Scrapped 2026-09-17, needs rebuild |
| 2 | **Brand page + BM, warmed** | Everything | ❌ Not started. Last BM was banned as a suspected bot |
| 3 | **Category name** | PDP, domain, copy | ❌ Open founder decision |
| 4 | **Persona page** | **The 3 native ads only** | ❌ Not started |
| 5 | Cold-side verbatim | Copy quality | 🟡 Thin but workable |
| 6 | Two thermometers | Ad set 3, Ad 2 | 🟢 $20 |

**If the persona page is not ready at launch:** run 2-ad ad sets and treat the natives as a separate later campaign. **Do not inject them mid-flight** — that resets learning across all three ad sets and costs more than the natives are worth in week one.

**The critical path is the store, not the creative.** All six non-native ads can be produced in a day. None of them can run without somewhere to send the click.

---

## 9. Schedule

7 days of spend plus a possible reserve extension ≈ **10-12 days**. Starting within the week finishes **early-to-mid October, ahead of the Q4 CPM ramp** (mid-Oct onward). Every day of prep past that is paid for in auction price.
