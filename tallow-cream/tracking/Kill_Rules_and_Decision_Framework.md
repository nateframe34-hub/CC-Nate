# Kill Rules & Decision Framework — Tallow Launch

> **Purpose:** Hard rules for when to kill, scale, or iterate on ads. Built from NMN postmortem learnings.
> **Updated:** June 2026 — added the governing 2× Breakeven CPA kill rule (founder decision 2026-06-29).

---

## ★ GOVERNING KILL RULE — 2× IDEAL SCALING CAC (revised 2026-07-17, supersedes 2× Breakeven) ★

**Ideal Scaling CAC: $20.** Target CPA to trigger aggressive budget increases, well under the $33 breakeven, leaving real margin for reinvestment (the $10 per-order gift card cost applies to repeat orders, not this first-purchase CAC, but still worth the buffer). Aspirational but not fantasy, the account has already hit $11.35 CPA once (B19C2, 2026-06-28).

**Kill rule, founder-locked 2026-07-17: kill at 2× Ideal Scaling CAC = ~$40 in spend with no purchase.** Tighter than the prior 2× breakeven ($66) line. Flagged once for the record: $40 sits closer to B17C1's actual lifetime mean CPA ($31.30) than the old $66 line did, which per the variance math below means a somewhat higher false-kill rate on genuine winners mid-dry-stretch than the account's June analysis targeted. Founder's explicit call, made with that tradeoff known: faster capital turnover and stricter batch discipline are worth more right now than the marginal risk of occasionally killing a real winner early. **This is the rule going forward, not a soft suggestion.**

**The math:**
- Price: $49.99 | COGS: ~$17.01 | Breakeven CPA ≈ $33 (reference only, no longer the kill anchor)
- Ideal Scaling CAC: $20 | **2× Ideal Scaling CAC = ~$40 (the kill line)**

**The rule:**
> Once an ad accumulates **~$40 in spend with no purchase**, kill it.

**Counter definition (so it doesn't misfire):**
- The $40 counter measures **spend since the ad's last purchase.** A brand-new ad measures from launch.
- **Each purchase resets the counter to $0.** This protects proven converters (e.g. B9C3/B17C1) that have dead stretches but reset every time they sell, while still killing genuine losers that never convert.
- Applies per-ad (per creative), not per-campaign.

**Worked examples (current ads):**
- B19C2 (whiteboard winner): converted at $11.35 → counter reset, nowhere near $40. SAFE.
- B19C3: ~$45-50 cumulative, no purchase → already past the new $40 line. Kill.
- Dead urgency cells (B17C2/C4): near-zero delivery, kill on the separate "concluded test" basis, not this rule.

**The variance math this rule is trading off (kept for reference):** purchases arrive lumpy (Poisson-ish), not evenly. An ad's average spend-between-sales ≈ its CPA. Even a genuinely PROFITABLE ad routinely has dry gaps of 1.5-2× its mean CPA as normal variance. At B17C1's real $31.30 mean CPA, a $40 kill line is only ~1.3× that mean, tighter than the ~2× mean gap the June analysis found necessary to hold the false-kill rate near 10-15%. Founder's decision accepts a higher false-kill rate on individual proven converters in exchange for faster overall batch turnover and a harder discipline against dead spend. Watch: if a real converter (B17C1-caliber) gets killed on a dry stretch and would have reset on the next day's sale, that's this tradeoff manifesting, not a bug in the rule.

---

## ★ TWO REGIMES — Unproven Ads vs Proven Converters (locked 2026-06-30) ★

The 2× ($40) no-purchase line answers ONE question: *"has this ad shown it CAN convert?"* It is the right tool ONLY for **unproven ads** (zero conversions, still measuring from launch). Once an ad has converted a few times, the flat trip-wire is the wrong tool — switch to judging it on rolling economics.

**Regime A — UNPROVEN ad (0 lifetime purchases):** use the 2× line. Spend $40 from launch with no purchase → KILL. (Applies now to: B19C3, B20 C1/C2/C3 once delivering.)

**Regime B — PROVEN converter (has converted, ~breakeven or better):** do NOT use the flat no-purchase line. Judge on **rolling CPA/ROAS + opportunity cost.** A proven converter at/under breakeven is a (thin) winner — don't murder it into a vacuum on a dry stretch. Two triggers to retire it:
1. **Economic decay:** rolling CPA over a meaningful window (e.g. last ~10 purchases, or last ~$200 spend) climbs and stays above breakeven ($33) → it has stopped being profitable, wind it down.
2. **Opportunity cost (the important one for format migration):** retire it when a cheaper-CPM format proves a BETTER CPA. Don't kill it for losing money (it isn't) — replace it when something earns more per dollar. Trading up, not cutting into a vacuum.

**Worked example — B17C1 (B9C3 verbatim native), as of 2026-06-29:** lifetime $125.19 spend, 4 purchases, $199.96 revenue → **CPA $31.30, ROAS 1.60x gross, +$6.73 net over the run.** Just under breakeven = marginal winner. BUT native CPM is capped (~$180) while whiteboard delivers $19-160, so B17C1's ceiling is low by format. Decision: do NOT kill on the rule (it's profitable + under $40 since last sale, though closer to the line now than under the old $66 threshold); CAP its budget, let B20 take growth dollars, and **retire it the moment a whiteboard cell banks a purchase at ≤ ~$31 CPA** (beats it). Opportunity-cost trigger, not a loss trigger.

---

## The 3 NMN Mistakes We're Not Repeating

1. **Letting CBO bleed money on bad ads.** We let some NMN ads spend $40-60 with zero ATCs. That's dead money.
2. **Not killing ads fast enough at high CPMs.** B1C2 and B2C1 hit $100+ CPMs and we kept them alive too long.
3. **Confusing CTR with conversion.** B3C3 hit 10.56% CTR with 0 purchases. Engagement ≠ buying intent.

---

## Hard Kill Rules

These are non-negotiable. If any of these trigger, kill the ad immediately. No exceptions.

| Rule | Trigger | Action |
|---|---|---|
| **Budget Bleed** | $50 spend, 0 purchases | HARD KILL |
| **CPM Death Spiral** | CPM > $80 for 24+ hours | HARD KILL (Meta has decided your ad is bad) |
| **Zero Engagement** | $20 spent, < 0.5% CTR | HARD KILL (creative is invisible) |
| **High CTR No ATC** | $30 spent, > 3% CTR but 0 ATC | KILL — landing page mismatch or wrong audience |
| **CPC Spike** | CPC > $2.00 sustained for 24h | KILL — audience exhaustion |

---

## Soft Kill Rules

These are warning signs. Watch them. Kill if they don't improve in 24 hours.

| Rule | Trigger | Action |
|---|---|---|
| Spend Without ATC | $30 spent, 0 ATC | WATCH — kill at $40 if no movement |
| Below Average CTR | CTR < 1% after 24 hours | WATCH — iterate hook within 24h |
| Above Target CPC | CPC > $1.50 | WATCH — likely audience problem |
| Single ATC No Purchase | 1 ATC, 0 purchase, $40+ spend | WATCH — checkout abandonment investigation |

---

## Scale Rules

These are green lights. Scale immediately when these hit.

| Rule | Trigger | Action |
|---|---|---|
| **First Purchase** | First purchase at < $40 CPA | Increase budget 25% next day |
| **Sustained ROAS** | ROAS > 2.0 across 5+ purchases | Increase budget 50% |
| **Strong CTR + ATC** | CTR > 2%, ATC rate > 5% | Worth more spend, audience is hot |
| **Low CPA** | CPA < $25 | Scale aggressively, this is a winner |

---

## Daily Check-In Protocol

**At 9am EST every day:**

1. Pull yesterday's stats from Meta Ads Manager (not real-time, wait for attribution to settle)
2. Log to `Ad_Performance_Tracker.csv` — every active ad gets a row
3. Check each ad against kill/soft kill rules
4. Make kill decisions BEFORE checking what made money (avoid rationalization)
5. Update `Tallow_Brand_Growth_Sheet.csv` if you launched a new batch

---

## Launch Week Budget Caps

| Day | Daily Cap | Notes |
|---|---|---|
| Day 1-2 | $50/day | Pure data collection. No optimization decisions yet. |
| Day 3-5 | $75/day | Apply soft kills, double down on early winners |
| Day 6-7 | $100/day if ROAS > 1.0, otherwise back to $50 | First profitability check |
| Day 8-14 | Scale based on ROAS | If ROAS < 0.8 by day 10 — STOP, audit creative |

**Total launch budget: $500 max for the first 7 days.** Hard cap. Don't go over.

---

## The "Two-Week Truth" Rule

If the brand has not generated:
- **At least 5 purchases**
- **At ROAS > 0.8 (cost recovery basis)**
- **By day 14**

Then the problem is NOT the ads. The problem is the offer, the product, or the PDP. Stop iterating creative and audit upstream.

---

## What We Track (and Why)

| Metric | Why It Matters |
|---|---|
| **CPM** | Tells you if Meta likes your creative |
| **CTR** | Tells you if your hook works |
| **CPC** | Tells you cost of getting attention |
| **LPV (Landing Page Views)** | Tells you if clicks are actually loading the page |
| **ATC Rate (LPV → ATC)** | Tells you if your PDP converts |
| **ATC → Checkout** | Tells you if checkout is broken |
| **Checkout → Purchase** | Tells you if pricing/payment friction is killing sales |
| **CPA (Cost per Purchase)** | Tells you actual unit economics |
| **ROAS** | Tells you if you're profitable |

---

## Target Benchmarks (First 14 Days)

| Metric | Target | Acceptable | Kill Zone |
|---|---|---|---|
| CPM | $20-40 | $40-60 | $60+ |
| CTR | > 2% | 1-2% | < 1% |
| CPC | < $1.50 | $1.50-2.00 | > $2.00 |
| LPV → ATC | > 3% | 2-3% | < 2% |
| ATC → Purchase | > 30% | 20-30% | < 20% |
| CPA | < $30 | $30-45 | > $45 |
| ROAS | > 1.5 | 1.0-1.5 | < 1.0 |

---

## Critical Reminders

1. **Don't fall in love with a "good" CTR if there are no purchases.** The NMN B3C3 lesson.
2. **Don't optimize creative if PDP/offer is the problem.** Diagnose upstream first.
3. **Kill ads at the rule, not at your gut.** Rules exist because gut overrides cost money.
4. **Track everything daily.** Weekly tracking misses death spirals.
5. **Don't launch new batches while old ones are bleeding.** Fix what's running first.

---

*Built from Baseline NMN postmortem learnings — March 2026*
