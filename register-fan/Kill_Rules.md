# Kill Rules — Register Fan (Evenroom)

**Set 2026-09-23, BEFORE any spend. Founder call.**
**These are hard. They do not move mid-flight. Moving a kill rule after seeing the data is how tallow reached ~$2,000 on a product that should have stopped at $600.**

---

## THE FOUR RULES

| # | Rule | Action |
|---|---|---|
| **1** | **No purchase intent at $300 spend** | **KILL THE PRODUCT** |
| **2** | Purchase intent present, but no purchases | **In-depth evaluation → one fix → bounded retest** |
| **3** | Above **2× ROAS** *(see §3 — the real number is higher)* | **Scale budget, keep testing** |
| **4** | Above **$3 CPC** after $50+ on a single ad | **Evaluate, possibly kill the ad** |

---

## §1 — "Purchase intent" must be defined before it can be enforced

Rule 1 is the most consequential rule here and the term at its centre is undefined. Defining it now, so the $300 decision is arithmetic rather than a judgement call made while staring at a losing campaign.

**Purchase intent = Add to Cart OR Initiate Checkout.** Landing page views do not count — a click is interest, not intent.

> ### 🚨 ADS MANAGER DOUBLE-COUNTS ATC
> Per `CLAUDE.md`: **Adds to Cart display at 2× the real number.** A screenshot showing 6 ATC means **3 actual**. This has caught the account before. **Halve every displayed ATC figure before applying any rule below.** Impressions, clicks, LPVs, checkouts and purchases all read true — only ATC is affected.

**The $300 gate, stated in numbers:**

| At $300 cumulative spend | Verdict |
|---|---|
| **0 real ATC and 0 checkouts initiated** | 🔴 **KILL THE PRODUCT.** No ambiguity |
| **1-2 real ATC, 0 checkouts** | 🔴 **Kill.** Two carts across $300 is noise, not intent |
| **3+ real ATC, or 1+ checkout initiated** | 🟡 Intent exists → **Rule 2** |

**Why $300 is a good number:** it's 3× the sale price and roughly 5× the single-unit CAC room ($56.15). If five CACs of spend produces not one person who got as far as a cart, the problem is the product or the market, not the creative.

**Relationship to the $600 cap:** $300 is the *early* gate and it binds first. **$600 remains the outer cap** and also does not move. Passing the $300 gate buys the second $300, not an open budget.

---

## §2 — Intent but no purchases: the evaluation, bounded

This is the rule most likely to leak money, because "evaluate and fix" has no natural end. It gets a ceiling and a sequence.

**Diagnose in this order — the first one that's broken is the one to fix:**

| Check | If broken | Fix |
|---|---|---|
| 1. Cost per LPV vs CPC | Big gap → clicks aren't loading | Page speed, mobile render |
| 2. **LPV → ATC** | Low → **the PDP isn't selling** | Offer, price, the fit step, the mechanism section |
| 3. **ATC → Checkout** | Low → sticker shock at shipping, or the size selector is confusing | Shipping presentation, selector UX |
| 4. **Checkout → Purchase** | Low → payment, trust, or the guarantee | Checkout config, trust signals |

**Hard constraints on the fix-and-retest:**

- **ONE fix at a time.** Two changes at once and the retest tells you nothing.
- **Retest budget: $150 maximum**, drawn from the $600 cap — not on top of it.
- **One retest cycle only.** If a second fix is needed, the product is not being killed by a fixable thing; it's being kept alive by hope.
- **If the fix is the price**, that is a real finding and it changes the economics doc, not just the test.

**The most likely diagnosis, stated in advance:** healthy CTR and cost per LPV with no ATC means **the page or the offer is wrong, not the ads.** Do not rewrite creative in that scenario.

---

## §3 — ⚠️ 2× ROAS is NOT the scale threshold. The real number is higher.

Rule 3 as written would have us scaling into a loss on bundle-heavy days. The arithmetic:

| | Revenue | Contribution | **Breakeven ROAS** |
|---|---|---|---|
| **Single** ($89.99 + $9.95) | $99.94 | $56.15 | **1.78×** |
| **2-Pack** ($159.99) | $159.99 | $73.87 | **2.17×** |

**At exactly 2.0× ROAS:**
- A single earns about **+$6** per order.
- A 2-pack **loses about $6** per order.

Because the bundle carries a lower margin percentage, **2× ROAS is profitable on singles and loss-making on bundles** — and we intend to push the bundle hard.

### Corrected thresholds

| Blended ROAS | Meaning | Action |
|---|---|---|
| Below **1.8×** | Losing money on any mix | Do not scale. Diagnose |
| **1.8× – 2.2×** | Breakeven-ish, mix-dependent | **Hold budget. Keep testing.** Do not scale |
| **Above 2.25×** | Profitable on any mix | ✅ **Scale** |
| Above 3× | Comfortably profitable | Scale faster |

**Better still, judge on CAC, not ROAS.** ROAS hides the mix; CAC doesn't. **Scale when blended CAC sits below the contribution for the mix actually being sold** — $56.15 single, $73.87 bundle. If both numbers are available, CAC is the one to trust.

### Scaling mechanics, so scaling doesn't kill the winner

- **No more than +20-30% to an ad set's budget per 48 hours.** Larger jumps re-enter learning and can destroy the performance being scaled.
- **Never add a new ad to a winning ad set.** Duplicate the ad set instead.
- **Re-check after every increase.** Performance at $20/day frequently does not survive $60/day; that is information, not failure.

### ⚠️ ROAS at day 7 is provisional

Returns are not in it. On a ~$100 electrical product with a size step, returns will not be zero — the incumbent's reviews are dominated by fitment and setup errors. **Treat any ROAS figure as provisional until the 60-day return window has meaningfully elapsed**, and do not fund a MOQ off a number that hasn't survived returns.

**Attribution:** use Meta's default 7-day click / 1-day view and state it anywhere ROAS is recorded. Comparing numbers across different windows is a silent error.

---

## §4 — $3 CPC after $50 on an ad

**Trigger:** any single ad above **$3.00 CPC** at **$50+ of that ad's own spend** → evaluate.

**Evaluate means diagnose, because CPC has two very different causes:**

| Pattern | Cause | Action |
|---|---|---|
| **High CPM, healthy CTR** (>1.5%) | Auction cost, not creative failure | The creative is working. Look at audience and placement before killing. **This was tallow's actual problem** — B17C1 had a 5.81% CTR and still cost $4.46/click |
| **Normal CPM, low CTR** (<1%) | Creative isn't landing | **Kill the ad.** This is a real creative failure |
| **Both bad** | Wrong audience or wrong offer | Kill the ad, and look hard at the ad set |

**Context for the $3 number:** at $3 CPC we need a **5.3% click→purchase** to break even on a single. Tallow's best was 3.42%. So $3 is not a soft ceiling — it's close to the edge of workable, and $4 is past it.

**⚠️ One practical limit.** Meta concentrates most of an ad set's spend on one creative within a couple of days, so **the other two ads in an ad set may never reach $50 and cannot be judged by this rule.** An ad that never got spend hasn't failed — it was never tested. Do not record it as a losing format.

---

## §5 — Rules that were missing

**No kill decisions before day 4**, except catastrophic (zero delivery, policy rejection, a broken link). Ad sets are in learning; days 1-3 are noise, and CBO-style first-hour noise produced this account's worst historical reads.

**If all ad sets fail together, suspect the page, not the avatar.** Nine ads across three visual registers do not fail for one creative reason. Check the PDP before writing off the research.

**Check the link before every launch.** A broken or mis-pathed link produces a perfect imitation of "the market rejected us."

---

## §6 — The decision table, one page

| Condition | Verdict |
|---|---|
| $300 spend, <3 real ATC and 0 checkouts | 🔴 **KILL PRODUCT** |
| $300 spend, 3+ real ATC or 1+ checkout, 0 purchases | 🟡 **Rule 2** — one fix, $150 retest, one cycle |
| Any ad, $50+ spend, CPC >$3 | 🟠 Diagnose via CPM/CTR split → kill or keep |
| Blended ROAS <1.8× | 🟠 Do not scale |
| Blended ROAS 1.8-2.25× | 🟡 Hold, keep testing |
| Blended ROAS >2.25×, or CAC < contribution | 🟢 **Scale +20-30% / 48h** |
| $600 cumulative | 🔴 **Hard cap. Stop.** |

---

**Signed off before spend, 2026-09-23.** Any change to these numbers must be dated, reasoned and written here *before* the data that would motivate it — not after.
