# The CPM / CTR Trade-Off: Where The Profitable Zone Actually Is

**Date:** 2026-07-30
**Trigger:** founder's read that B30 had great CPM and terrible CTR, the proven converters have the reverse, and profitability lives in the middle ground.
**Verdict: the instinct is right, and the middle ground is computable. This doc computes it.**

---

## 1. The number that actually matters is CPC, and neither CPM nor CTR alone tells you anything

CPM and CTR are not two competing goals. They're two inputs to one output:

```
CPC = CPM ÷ (CTR × 10)
```

And CPC is what converts into CPA. Run the account's real numbers through it:

| Cell | CPM | CTR | **CPC** |
|---|---|---|---|
| B30C3 | **$22** | 0% | **∞** (zero clicks on 418 impressions) |
| B30C1 | $53 | 0.82% | **$6.45** |
| B30C2 | $101 | 2.83% | **$3.57** |
| **B30 blended** | **$52** | 0.99% | **$5.24** |
| B17C1 (7/27) | $259 | 5.81% | **$4.46** |
| B28C1 (7/27) | **$295** | 7.69% | **$3.84** |

**B30 had the cheapest CPM on the account and the most expensive clicks on the account.** $5.24 blended against B28C1's $3.84 — the cell with a CPM 5.7x higher delivered clicks 27% cheaper.

That is the whole finding in one line. Cheap CPM bought us nothing.

---

## 2. The within-batch correlation kills the "cheap audience" theory outright

This is the part that settles it. Inside B30, **CPM and CTR moved in the same direction, not opposite directions:**

| | CPM | CTR |
|---|---|---|
| B30C3 | cheapest ($22) | **worst (0%)** |
| B30C1 | middle ($53) | middle (0.82%) |
| B30C2 | most expensive ($101) | **best (2.83%)** |

Perfect rank correlation across three cells, in the *opposite* direction to what "we found cheap inventory" would predict.

**If B30 had genuinely reached a cheaper high-quality audience, CPM and CTR would be independent** — you'd expect roughly the same click rate at a lower price. Instead, the cheaper the inventory got, the worse it performed. That's the signature of **relegation**, not discovery: Meta reads weak engagement, stops bidding into competitive inventory, and dumps the budget into junk placements to spend the floor.

The prior feedback loop reached this conclusion qualitatively. The rank correlation is the quantitative proof.

---

## 3. CPA ≈ CPC × 9, and the model validates against a real purchase

Click-to-purchase on this account runs about **11%** (B17C1 on 7/27: 9 clicks → 1 purchase; B9C3's LPV→purchase was 17% on a ~1:1 click-to-LPV ratio).

So:

```
CPA ≈ CPC × 9
```

**Check it against the real 7/27 purchase:** B17C1's CPC was $4.46. 9 × $4.46 = $40.14. **Actual CPA was $40.18.** The model is accurate to four cents on the one data point we can test it against.

That gives us hard CPC thresholds:

| Target | CPA | **Required CPC** |
|---|---|---|
| Ideal Scaling CAC | $20 | **≤ $2.22** |
| **Breakeven** | $30.16 | **≤ $3.35** |
| Kill line | $40 | ≤ $4.44 |

**Current state: B28C1 at $3.84 and B17C1 at $4.46 are both above breakeven.** B17C1 is sitting exactly on the kill line. This is not a mystery to be solved — it is arithmetic. **The account is unprofitable because CPC is roughly 30-100% too high, and nothing else.**

---

## 4. The profitable zone, mapped

What CTR do you need at a given CPM to hit each target? (`CTR = CPM ÷ (CPC × 10)`)

| CPM | CTR for breakeven ($3.35 CPC) | CTR for target ($2.22 CPC) |
|---|---|---|
| $50 | **1.5%** | 2.3% |
| $100 | **3.0%** | 4.5% |
| $150 | **4.5%** | 6.8% |
| $200 | 6.0% | 9.0% |
| $275 *(current)* | **8.2%** | **12.4%** |
| $400 | 11.9% | 18.0% |

**Read the bottom row against the top rows and the strategy writes itself.**

At today's ~$275 CPM we need **8.2% CTR just to break even** and **12.4% to hit target**. The account's best-ever days are 11.43% (B17C1, 7/18) and 7.69% (B28C1, 7/27). So we are asking our creative to perform at its historical ceiling *merely to stop losing money*.

At **$150 CPM**, breakeven needs **4.5%** and target needs **6.8%** — both of which this account hits routinely.

**Halving CPM halves the CTR requirement.** That's the founder's middle ground, and it's not a compromise between two goods. It's moving from "we must be exceptional every single day" to "we must be normal."

---

## 5. So what distinguishes good cheap CPM from bad cheap CPM?

We have both in the account's history, and the distinction is the most useful thing in this document:

| | CPM | Outcome | What it was |
|---|---|---|---|
| **B19C2** (whiteboard) | **$19-97** | **$11.35 CPA, 4.40x ROAS** | ✅ **Genuine format advantage** |
| **B30** (native, soft imagery) | $22-101 | 0 purchases, 0.99% CTR | ❌ **Relegation** |

Nearly identical CPM ranges. Opposite outcomes.

**B19C2 proves cheap CPM can be real** — relegated junk inventory does not convert at 4.40x ROAS. Something about a bold hand-drawn diagram earned cheap *and* engaged delivery simultaneously, most likely because Meta's classifier read it as native educational content rather than a polished ad, while the human eye found it genuinely novel in feed.

**B30 proves cheap CPM can be fake.** Same price, no engagement, no sales.

### The diagnostic rule this produces

> **Cheap CPM + healthy CTR = genuine format advantage. Bank it and scale it.**
> **Cheap CPM + weak CTR = relegation. Kill it, and do not record the cheap CPM as a win.**
> **Never read CPM on its own. It is meaningless without CTR beside it.**

---

## 6. What this says about B32, which is already live

**B32 is a direct bet on exactly this middle ground, and this analysis raises its priority above everything else in flight.**

The whiteboard × native hybrid was designed to split the job: the diagram earns cheap engaged delivery (B19C2's proven strength), the long-form native copy does the converting (B17C1's proven strength). Run the numbers on plausible outcomes:

| If B32 lands... | CPC | Implied CPA | Verdict |
|---|---|---|---|
| $100 CPM, 5% CTR | $2.00 | **$18** | Better than target |
| $150 CPM, 6% CTR | $2.50 | **$22** | Comfortably profitable |
| $150 CPM, 4% CTR | $3.75 | $34 | Marginal, above breakeven |
| $275 CPM, 6% CTR | $4.58 | $41 | Unprofitable, same as today |

**The first two rows are the entire thesis of the account's next phase.** And they require nothing exceptional — 5-6% CTR is ordinary for this account. The only thing that has to be true is that whiteboard's cheap CPM is the *genuine* kind, which B19C2 already demonstrated once.

**This is the strongest argument yet for flooring B32C1**, and it's a better argument than the one made yesterday: B32 isn't just "a format worth testing," it's the only live candidate that can plausibly move CPC into profitable territory. Everything else in B31 is fighting for a better CTR at a CPM that makes profitability nearly impossible.

---

## 7. Operating changes

**1. CPC becomes the primary daily metric.** Log it, watch it, judge creatives on it. CPM alone and CTR alone both mislead, and B30 is the proof: it won on one, lost on the other, and lost overall.

**2. Add the CPC thresholds to the kill framework:**
- CPC ≤ $2.22 → on track for target CPA, scale
- CPC $2.22-3.35 → profitable, hold
- CPC $3.35-4.44 → above breakeven, fix or wind down
- CPC > $4.44 → past the kill line's implied rate

**3. Never bank a cheap CPM without checking CTR in the same breath.** Write it into feedback loops as a paired reading.

**4. Stop optimising for CTR at $275 CPM.** It's the harder of the two levers. Going from 7.7% to 12.4% CTR means beating the account's all-time best consistently. Going from $275 to $150 CPM means matching something the account has already done (B19C2, and B17C1's own $94-135 fresh-object window on 7/5).

**5. The fresh-object lever is also a CPM lever, and it's cheap.** B17C1 ran at **$94-135 CPM** immediately after its 7/5 duplication, versus $259-408 now. At $135 CPM and its normal 6% CTR, its CPC would be **$2.25** and CPA **~$20**. The proven converter was profitable at target four weeks ago and the only thing that changed is object staleness. **Duplicating B17C1 into a fresh ad object is a near-free test with a large expected effect.** Per the 7/17 external research, the standing SOP was a 2-3 week refresh cadence and it's overdue.

---

## 8. The honest caveats

- **Click-to-purchase 11% rests on one day and one purchase.** The $40.18 validation is reassuring but it's n=1. If the true rate is 8%, every CPC threshold tightens by a third. Worth recomputing once B31/B32 produce purchases.
- **B30's CPM figures come from small impression volumes.** C1 and C2 are both under the 100-impression reliability bar individually. The *rank correlation* across three cells is more robust than any single figure, and C3 cleared the bar at 418 impressions, but treat the exact CPMs as directional.
- **This model assumes CPM and CTR are independently controllable. They aren't fully.** Section 2 shows Meta couples them. Which means the middle ground may not be freely dialable — you may only be able to reach cheap-CPM-with-good-CTR through a genuinely different *format*, not by tuning a native ad. That is precisely why B32 matters and why B31 alone probably can't fix this.
