# Kill Rules & Decision Framework — Tallow Launch

> **Purpose:** Hard rules for when to kill, scale, or iterate on ads. Built from NMN postmortem learnings.
> **Updated:** April 2026 (pre-launch)

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
