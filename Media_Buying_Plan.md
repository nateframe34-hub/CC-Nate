# Baseline NMN — Complete Media Buying & Launch Plan

---

## PART 1: PRE-LAUNCH INFRASTRUCTURE (Build Before You Spend $1)

### PDP First vs. Landing Page First: Go Straight to PDP

**Verdict: Launch with PDP. Skip the standalone landing page for now.**

Why:

1. **You already have PDP copy mapped to Shrine Pro sections** — it's ready to build. A landing page would require additional copy, design, and a separate funnel.
2. **PDP builds your store's credibility.** When people click an ad, they want to see a real brand with a real store, not a single-page squeeze site. For a trust-first brand like Baseline, this matters more than conversion rate optimization on day one.
3. **PDP gives you infrastructure.** Cart abandonment flows, upsells, subscription options, cross-sell potential — all native to Shopify. A landing page isolates the customer from all of that.
4. **Landing pages are a Phase 2 play.** Once you know which avatar + angle wins, you build a dedicated landing page around that specific winner. Right now you're testing — you need flexibility, not a locked-in funnel.

**What your PDP needs before launch:**
- All Shrine Pro sections populated with your copy
- 3-tier Bundle & Save (Starter / Protocol / Transformation) live and functional
- Free shipping threshold set at $59+
- Subscription option visible but not forced
- Mobile-optimized (80%+ of Meta traffic is mobile)
- Page load under 3 seconds
- Product images (use your image generation prompts to produce these)

---

## PART 2: COMPARE AT PRICE STRATEGY

### Set Your "Compare At" Price to $89 for the 120ct Hero SKU

| SKU | Selling Price | Compare At Price | Perceived Savings | Why This Number |
|-----|--------------|-----------------|-------------------|-----------------|
| 60ct (The Starter) | $49 | $59 | Save $10 (17%) | Anchors against low-end competitors; modest enough to be believable |
| 120ct (The Protocol) | $69 | $89 | Save $20 (22%) | $89 is where PartiQlar and mid-premium brands sit for 60-day supply |
| 2x 120ct (The Transformation) | $119 | $178 | Save $59 (33%) | 2x the compare-at of a single 120ct; the math checks out visually |

**Rules:**
- Compare-at must be a price you could *believably* charge. $89 for a 60-day NMN supply is within market range (PartiQlar = $86, GenuinePurity = $80).
- Never set compare-at more than 40% above selling price — it looks fake.
- Shopify will show the strikethrough price automatically. Don't add additional "SALE" language — it cheapens the brand.

---

## PART 3: CAMPAIGN STRUCTURE (Meta Ads)

### Your Instinct Is Right — Here's the Refined Version

```
CAMPAIGN: Baseline NMN — Avatar Discovery (CBO)
├── Budget: $150-$250 CAD/day
├── Optimization: Purchases
├── Attribution: 7-day click, 1-day view
│
├── AD SET 1: Batch 1 — The Reluctant Decliner
│   ├── Targeting: Broad (40+, your geo)
│   ├── Creative 1: B1C1 "Late Night Search History"
│   ├── Creative 2: B1C2 "Trajectory Note"
│   └── Creative 3: B1C3 "Honest Post"
│
├── AD SET 2: Batch 2 — The 3pm Wall Hitter
│   ├── Targeting: Broad (35+, your geo)
│   ├── Creative 1: B2C1 "Coffee Chaos vs NMN Calm"
│   ├── Creative 2: B2C2 "Spike vs Baseline Graph"
│   └── Creative 3: B2C3 "Cells Then vs Now"
│
├── AD SET 3: Batch 3 — The Burned Supplement Buyer
│   ├── Targeting: Broad (35+, your geo)
│   ├── Creative 1: B3C1 "Star Rating Card"
│   ├── Creative 2: B3C2 "Reddit-Style Comment"
│   └── Creative 3: B3C3 "Multi-Review Collage"
│
├── AD SET 4: Batch 4 — The Exhausted Parent
│   ├── Targeting: Broad (35-55, your geo)
│   ├── Creative 1: B4C1 "Maybe Later"
│   ├── Creative 2: B4C2 "Leftovers"
│   └── Creative 3: B4C3 "Guilt Cycle"
│
└── AD SET 5: Batch 5 — The Invisible Woman
    ├── Targeting: Broad (40-55, Female, your geo)
    ├── Creative 1: B5C1 "Anti-Aging Reframe"
    ├── Creative 2: B5C2 "Doctor Dismissal"
    └── Creative 3: B5C3 "Body Didn't Betray You"
```

### Why CBO (Not ABO)

- CBO lets Meta allocate spend toward whichever ad set is converting. You're not guessing which avatar wins — you're letting the algorithm tell you.
- With $150-$250/day across 5 ad sets, CBO will naturally starve the losers and feed the winners within 3-5 days.
- You're right that these ad sets won't individually exit learning phase — and that's fine. The goal here is **signal, not scale.**

### Body Copy Per Ad

Each creative runs with **2 body copy variants** (already written in your batches doc). So each ad set has 3 creatives × 2 body copies = **6 ad variations per ad set, 30 total ads in the campaign.**

This is a lot. Meta will aggressively allocate to the top performers. That's exactly what you want.

### Headlines

Use the 2 headlines per batch that you already have. Pair each headline with each body copy. Meta will auto-rotate.

---

## PART 4: BATCH LAUNCH SEQUENCE

### Launch All 5 Batches Simultaneously — Day 1

**Do NOT stagger batches.** Here's why:

1. **You don't know which avatar converts until you test.** Launching Batch 1 first because it's "broadest" is a hypothesis, not a fact. Let the data speak.
2. **CBO is designed for simultaneous testing.** It will automatically allocate budget to the winner. Staggering defeats the purpose.
3. **Time is money.** At $200/day, every week of staggered testing is $1,400 spent without full data. Launch all 5, get signal in 7 days.

### The 7-Day Rule

- **Do not touch anything for 7 days.** No pausing ads, no adjusting budgets, no killing "underperformers" at day 3. Meta's algorithm needs 50 conversion events to optimize. At $200/day you'll need roughly 7 days to accumulate enough data.
- Exception: if an ad is spending >40% of budget with zero purchases by day 5, you can kill that specific ad (not the ad set).

---

## PART 5: READING THE DATA & BUILDING YOUR CHAMPION AD SET

### Week 1 (Days 1-7): Observation Only

Track these metrics daily but change NOTHING:

| Metric | What It Tells You | Where to Find It |
|--------|-------------------|-------------------|
| Spend distribution by ad set | Which avatar Meta thinks converts | Ads Manager → Breakdown by ad set |
| CTR (link click-through rate) | Which hook stops the scroll | Ad-level metrics |
| CPC (cost per link click) | Efficiency of getting to PDP | Ad-level metrics |
| Add to Cart rate | Which angle creates purchase intent | Shopify analytics + Meta pixel |
| Cost per Purchase | Which avatar actually buys | Ad-level metrics |
| ROAS | Which avatar is profitable | Ad-level metrics |

### Week 2 (Days 8-14): First Cuts

**Kill criteria** (apply to individual ads, not ad sets):
- CTR below 0.8% after $50+ spend → the hook isn't working
- CPC above $5 CAD after $50+ spend → the creative isn't resonating
- No purchases after $75+ spend → the angle isn't converting

**Keep criteria:**
- Any ad with a purchase at <$50 CAD CPA → promising
- Any ad with CTR >1.5% → strong hook, worth iterating on
- Any ad set receiving >25% of CBO budget → Meta is finding conversions there

### Week 2-3: Build the Champion Ad Set

Once you have clear signal on which sub-avatar and angle converts:

```
CAMPAIGN: Baseline NMN — Scale (CBO)
├── Budget: Start at $100/day, scale 20% every 3 days if ROAS holds
│
├── AD SET: Champion Ad Set ⭐
│   ├── Targeting: Same broad targeting as winning ad set
│   ├── All winning ads from discovery phase
│   ├── New creative iterations of winning angle/hook
│   └── THIS is the ad set you push to exit learning phase
│       (needs 50 purchases/week → ~7 purchases/day)
│
├── AD SET: Testing (ongoing)
│   ├── Budget cap: 20% of total
│   └── New creatives testing new hooks for the WINNING avatar
│       (don't switch avatars — go deeper on what works)
│
└── RETARGETING AD SET
    ├── Audience: Website visitors (7-day), ATC (14-day), engaged (30-day)
    ├── Budget cap: 15% of total
    └── Creatives: Testimonial-style, proof-heavy (Batch 3 creative style)
```

### Exiting Learning Phase Math

To exit learning phase you need ~50 conversion events per week per ad set.

| Daily Budget | Avg CPA | Purchases/Day | Purchases/Week | Learning Phase? |
|-------------|---------|---------------|-----------------|-----------------|
| $100/day | $30 | 3.3 | 23 | Still learning |
| $200/day | $30 | 6.7 | 47 | Almost there |
| $250/day | $30 | 8.3 | 58 | Exited |
| $350/day | $30 | 11.7 | 82 | Comfortably exited |

**Your breakeven CPA** (based on your margins):
- Protocol SKU ($69, 84.1% margin): Breakeven CPA = **$58**
- Transformation SKU ($119, 81.5% margin): Breakeven CPA = **$97**
- Starter SKU ($49, 81.6% margin): Breakeven CPA = **$40**

You have enormous headroom. Even at a $40 CPA you're profitable on every SKU.

---

## PART 6: KPIs & TARGETS

### Primary KPIs (Check Daily)

| KPI | Target (Discovery Phase) | Target (Scale Phase) | Why |
|-----|-------------------------|---------------------|-----|
| **ROAS** | >1.5x (profitable) | >2.0x (healthy profit) | Breakeven is 1.19-1.27x — anything above that is gravy |
| **CPA (Cost Per Acquisition)** | <$50 CAD | <$40 CAD | Leaves $19-$79 margin depending on SKU |
| **CTR (Link Click-Through)** | >1.0% | >1.5% | Below 1% = creative isn't resonating |
| **CVR (Conversion Rate on PDP)** | >1.5% | >2.5% | Below 1.5% = PDP problem, not ad problem |
| **AOV (Average Order Value)** | >$65 | >$75 | Tells you if customers are choosing Protocol/Transformation |

### Secondary KPIs (Check Weekly)

| KPI | Target | Why |
|-----|--------|-----|
| **CPM (Cost Per 1000 Impressions)** | <$25 CAD | If CPMs are high, your audience is too narrow or competitive |
| **CPC (Cost Per Link Click)** | <$3 CAD | Efficiency metric — if CPC is low but CVR is low, it's a PDP problem |
| **Add to Cart Rate** | >5% of visitors | Measures purchase intent before checkout friction |
| **Cart Abandonment Rate** | <75% | Above 75% = checkout friction, shipping surprise, or trust issue |
| **Frequency** | <2.0 in first 14 days | Above 2.0 = audience is too small, you're showing ads too often |
| **Hook Rate (3-sec video views / impressions)** | >25% | For video ads — tells you if the opening frame stops the scroll |

### Financial KPIs (Check Weekly)

| KPI | Formula | Target |
|-----|---------|--------|
| **Blended ROAS** | Total Revenue / Total Ad Spend | >2.0x |
| **Contribution Margin** | (Revenue - COGS - Ad Spend) / Revenue | >40% |
| **Customer Acquisition Cost (CAC)** | Total Marketing Spend / New Customers | <$50 |
| **Profit Per Customer (Day 1)** | AOV - COGS - CAC | >$10 |
| **MER (Marketing Efficiency Ratio)** | Total Revenue / Total Marketing Spend | >2.5x |

### The "North Star" Dashboard (What You Actually Look At)

Every morning, check these 4 numbers:

1. **Yesterday's ROAS** — Are we profitable?
2. **Yesterday's CPA** — Is it getting better or worse?
3. **This week's purchases** — Are we on pace to exit learning phase?
4. **AOV** — Are people buying the Protocol tier or defaulting to Starter?

---

## PART 7: EMAIL & SMS FLOWS

### Pre-Launch Setup (Must Have Before Running Ads)

You need 4 flows live before your first ad dollar is spent. These are revenue recovery and customer experience essentials.

---

### Flow 1: Welcome / Email Capture — 10% Off First Order

**Trigger:** New email subscriber (popup on site)

**Popup Copy:**
> **Get 10% Off Your First Order**
> Plus a free copy of "The NAD+ Protocol" — our guide to cellular restoration.
> [Email field] [GET MY 10% OFF]
> *Join 500+ people restoring their cellular energy.*

**Why 10% (not 15% or $10 off):**
- 10% on the Protocol ($69) = $6.90 discount. Customer pays $62.10. Your margin is still $51.10 (82.3%). Almost no margin damage.
- 10% feels meaningful to the customer without training them to expect deep discounts.
- It's the industry standard — anything less feels stingy, anything more is unnecessary at these margins.

**Email Sequence:**

| Email | Timing | Subject Line | Content | Goal |
|-------|--------|-------------|---------|------|
| **E1: Welcome + Code** | Immediate | "Your 10% code is inside (+ a free guide)" | Deliver the discount code. Deliver the eBook PDF. One line about what Baseline is. CTA to shop. | Deliver value, get first click |
| **E2: The NAD+ Story** | 24 hours later | "Why you lost 50% of your cellular fuel (and didn't know it)" | Educate on NAD+ decline. The 50% by 50 stat. How NMN restores it. No hard sell — just the science. Link to PDP. | Build belief in the mechanism |
| **E3: Why Most NMN Doesn't Work** | 48 hours after E2 | "64% of NMN on Amazon failed lab testing" | The trust angle. Enzymatic vs chemical synthesis. QR-to-COA verification. Position Baseline as the answer to the trust problem. | Overcome skepticism, differentiate |
| **E4: Social Proof + Urgency** | 48 hours after E3 | "Here's what people notice first" | Customer language/testimonials. "More consistent energy," "the 3pm crash is gone," "I actually play with my kids after work." Remind them their 10% code expires in 48 hours. | Convert with proof + soft deadline |
| **E5: Last Chance** | 48 hours after E4 (code expiry) | "Your 10% code expires tonight" | Short. Direct. "Your code [CODE] expires at midnight. The Protocol (60-day supply) is just $62.10 with your code." Single CTA button. | Final conversion push |

**Code Expiry:** 7 days from signup. Creates natural urgency without fake scarcity.

---

### Flow 2: Abandoned Cart Recovery

**Trigger:** Added to cart but didn't purchase within 1 hour

| Email | Timing | Subject Line | Content | Goal |
|-------|--------|-------------|---------|------|
| **AC1: Reminder** | 1 hour after abandonment | "You left something behind" | Show the product they carted. Clean, simple. "Still thinking it over? Here's what you left in your cart." CTA to complete purchase. No discount. | Catch the distracted buyer |
| **AC2: Address Objections** | 24 hours after AC1 | "Questions before you commit?" | Address top 3 objections: (1) "Does NMN actually work?" → link to research, (2) "How do I know it's real?" → QR verification, (3) "How long until I feel something?" → 2-4 weeks for most people. | Remove friction |
| **AC3: Incentive** | 48 hours after AC2 | "We'll cover shipping" | Free shipping offer (if they weren't already at $59+ threshold). If they were above threshold, offer the free eBook as a reminder. Last push. | Convert fence-sitters |

**SMS (if you collect phone numbers):**

| SMS | Timing | Content |
|-----|--------|---------|
| **SMS1** | 30 min after abandonment | "Hey [Name], you left [Product] in your cart. Complete your order here: [link]" |
| **SMS2** | 24 hours later (only if no purchase) | "Still thinking about it? Your cells lose NAD+ every day — why wait? [link]" |

---

### Flow 3: Post-Purchase / Onboarding

**Trigger:** First purchase completed

This flow is CRITICAL. NMN takes 2-4 weeks to build NAD+ levels. If you don't set expectations, customers will think it "didn't work" and never reorder.

| Email | Timing | Subject Line | Content | Goal |
|-------|--------|-------------|---------|------|
| **PP1: Welcome + What to Expect** | Immediately after purchase | "Your Baseline order is confirmed — here's what happens next" | Thank them. Set the timeline: "Week 1-2: Your cells are rebuilding NAD+ stores. You may not feel anything yet. Week 2-4: Most people notice more consistent energy, better recovery, clearer focus. Week 4+: Your new baseline." Dosing instructions (2 caps/day, morning, with or without food). | Set expectations, prevent early disappointment |
| **PP2: The Science** | Day 7 | "What's happening inside your cells right now" | Brief explanation of NAD+ restoration process. "By now your cells have been receiving NMN for a week. Here's what the research shows is happening at the cellular level..." Educational, not salesy. | Keep them engaged during the "nothing's happening" phase |
| **PP3: Check-In** | Day 14 | "Notice anything different?" | Ask how they're feeling. Link to a simple survey or reply prompt. Share what other customers noticed at the 2-week mark. Build community feel. | Re-engage, collect testimonials |
| **PP4: Midpoint** | Day 21 (for 30-day) / Day 30 (for 60-day) | "You're halfway through — here's what comes next" | Reinforce that benefits compound over time. Introduce the subscription option: "Most people who feel a difference don't want to go back. Lock in your supply at 14% off." | Bridge to reorder/subscription |
| **PP5: Reorder Reminder** | Day 25 (30-day) / Day 50 (60-day) | "Running low? Your next bottle is ready" | Direct. "You've got about [5/10] days of Baseline left. Don't let your NAD+ levels drop back down. Reorder now — or save 14% with Subscribe & Save." | Drive reorder / subscription conversion |

---

### Flow 4: Browse Abandonment (Lower Priority — Build After Launch)

**Trigger:** Viewed PDP 2+ times without adding to cart

| Email | Timing | Subject Line | Content |
|-------|--------|-------------|---------|
| **BA1** | 24 hours | "Still researching NMN?" | Educational angle — link to a blog post or the eBook. Position Baseline as the "do your research" brand. Soft CTA. |
| **BA2** | 72 hours | "Here's what convinced most people" | Testimonials + the trust mechanism (QR, lab testing, enzymatic synthesis). |

---

### Email/SMS Platform Recommendation

**Klaviyo** — it's the Shopify-native standard. Handles all of the above flows, integrates directly with Shopify, and scales with you. Start on the free plan (up to 250 contacts, 500 emails/month), upgrade as your list grows.

---

## PART 8: BUDGET & TIMELINE SUMMARY

### Week-by-Week Launch Plan

| Week | Action | Daily Ad Spend | Cumulative Spend |
|------|--------|---------------|-----------------|
| **Week -2** | Build Shopify PDP, set up Klaviyo flows, install Meta pixel, create product images | $0 | $0 |
| **Week -1** | Final PDP review, test checkout flow, verify pixel fires, warm up email domain | $0 | $0 |
| **Week 1** | Launch all 5 batches in CBO. **DO NOT TOUCH.** | $150-200/day | $1,050-$1,400 |
| **Week 2** | Review data. Kill dead ads (not ad sets). Identify winning avatar + angle. | $150-200/day | $2,100-$2,800 |
| **Week 3** | Build Champion Ad Set with winning creative. Start scaling. Add retargeting. | $200-300/day | $3,500-$4,900 |
| **Week 4** | Scale Champion Ad Set 20% every 3 days if ROAS holds. Iterate new creatives. | $250-400/day | $5,250-$7,700 |

### Total Discovery Phase Budget: ~$2,800-$4,200 CAD (2 weeks)

This is the cost to find your winning avatar, angle, and creative. Think of it as market research — not wasted ad spend.

### When to Increase Budget

Scale the Champion Ad Set by 20% every 3 days IF:
- ROAS is above 1.5x (profitable)
- CPA is stable or decreasing
- Frequency is below 2.5

Stop scaling and hold IF:
- CPA increases by >25% after a budget increase
- ROAS drops below 1.3x
- Frequency exceeds 3.0

### When to Kill the Campaign

Pull the plug if after $3,000 in spend you have:
- Zero purchases
- CTR below 0.5% across all batches
- No ad set receiving meaningful CBO allocation

This would mean the product-market fit isn't there yet, NOT that the ads are bad. Revisit positioning, price, or offer before re-launching.

---

## PART 9: LAUNCH CHECKLIST

### Before You Turn On Ads

- [ ] Shopify store live with PDP fully built (Shrine Pro sections populated)
- [ ] 3-tier Bundle & Save functional (Starter $49 / Protocol $69 / Transformation $119)
- [ ] Compare-at prices set ($59 / $89 / $178)
- [ ] Free shipping threshold at $59+
- [ ] Subscription option live ($42/mo for 60ct, $59/60d for 120ct)
- [ ] Meta Pixel installed and firing on: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase
- [ ] Product images produced and uploaded
- [ ] Klaviyo connected to Shopify
- [ ] Welcome flow live (5 emails)
- [ ] Abandoned cart flow live (3 emails + optional SMS)
- [ ] Post-purchase flow live (5 emails)
- [ ] 10% popup live on site
- [ ] Payment processing tested (place a real test order)
- [ ] Mobile checkout tested on phone
- [ ] eBook PDF created and delivery automated
- [ ] All 30 ad variations uploaded to Meta (5 batches × 3 creatives × 2 body copies)
- [ ] CBO campaign structure built per Part 3
- [ ] UTM parameters on all ad links for tracking

---

## PART 10: COMMON MISTAKES TO AVOID

1. **Don't kill ads before day 7.** The algorithm needs time. Resist the urge.
2. **Don't duplicate the CBO campaign.** One campaign, one learning phase. Duplicating resets everything.
3. **Don't narrow targeting.** Broad + strong creative > narrow targeting + weak creative. Let the algorithm find your people.
4. **Don't change the PDP during the testing phase.** If you're changing both ads and PDP simultaneously, you can't attribute results to either.
5. **Don't run discounts in the first 30 days.** Your 10% welcome popup is enough. Establish full-price value first.
6. **Don't optimize for link clicks or landing page views.** Always optimize for purchases, even with low data. Meta will find buyers, not browsers.
7. **Don't panic if day 1-3 ROAS is 0.** The pixel is learning. Meta front-loads spend to gather data. Days 4-7 typically show the real picture.
8. **Don't add interests or lookalikes yet.** Broad targeting with CBO is the current Meta best practice. Interest stacking is a 2022 strategy.
