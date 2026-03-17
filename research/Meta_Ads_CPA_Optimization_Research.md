# Meta Ads CPA Optimization Research

> Deep research on optimizing cost per acquisition for new Meta ad accounts running DTC ecommerce. Cross-referenced from Meta official documentation, established media buyers, and reputable marketing publications.
>
> **Compiled:** March 17, 2026

---

## Table of Contents

1. [Campaign Structure: CBO vs ABO](#1-campaign-structure-cbo-vs-abo)
2. [Ads Per Ad Set / Ad Sets Per Campaign](#2-ads-per-ad-set--ad-sets-per-campaign)
3. [Budget Allocation for New Accounts ($40-50/day)](#3-budget-allocation-for-new-accounts-40-50day)
4. [The Learning Phase](#4-the-learning-phase)
5. [Kill vs Scale Decision Framework](#5-kill-vs-scale-decision-framework)
6. [Broad vs Interest Targeting (2024-2026)](#6-broad-vs-interest-targeting-2024-2026)
7. [Advantage+ Shopping vs Manual Campaigns](#7-advantage-shopping-campaigns-vs-manual-campaigns)
8. [Conversion API (CAPI) Setup](#8-conversion-api-capi-setup)
9. [Attribution Windows](#9-attribution-windows)
10. [Scaling Strategies: Vertical vs Horizontal](#10-scaling-strategies-vertical-vs-horizontal)

---

## 1. Campaign Structure: CBO vs ABO

### What They Are

- **ABO (Ad Set Budget Optimization):** Budget is set at the ad set level. You control exactly how much each ad set spends. More manual, more control.
- **CBO (Campaign Budget Optimization / "Advantage Campaign Budget"):** Budget is set at the campaign level. Meta distributes spend across ad sets based on predicted performance. More automated, less control.

### When to Use ABO

ABO is the testing workhorse. Use it when:

- **Running early-stage creative or audience tests** where each variation needs equal spend to generate clean data
- **Budget is small** and you need to guarantee each test gets enough spend to reach statistical significance
- **The account is new** and the pixel has limited purchase event data
- **You need to isolate variables** -- ABO ensures Meta doesn't prematurely pick a "winner" before other variations have been properly tested

**Depesh Mandalia's take:** "ABOs work well because you can control them far better... If your ABO is performing well, it means you've put the right inputs in -- good product, good targeting, good funnel." He specifically notes ABO is more stable with budgets **below $250/day**, while CBO works better at **$500+/day**.

### When to Use CBO

CBO is the scaling engine. Use it when:

- You already know your top 3 audiences or creatives and want to scale them
- The pixel records **at least 50 conversion events per week** -- this gives the algorithm enough data to allocate budget wisely
- You want to increase budget without resetting learning phase (CBO handles budget redistribution without triggering resets the way ABO budget changes do)

**Key data point:** Meta's internal data from April 2025 shows switching to CBO resulted in a **17% increase in ROAS** within six weeks for advertisers with sufficient conversion volume.

### The Consensus: Hybrid Approach

Every credible source converges on the same answer: **use both, sequentially.**

1. **ABO for testing** -- controlled creative/audience testing with equal budget distribution
2. **Migrate winners to CBO for scaling** -- use post ID duplication to preserve social proof
3. Consider **Advantage+ Shopping** once pixel data is strong

**Depesh Mandalia's GT (Graduate Testing) Framework:**
- **GT Phase 1:** ABO campaigns to identify best audiences (testing existing ads against new audiences)
- **GT Phase 2:** ABO campaigns to test new creatives against winning audiences
- **GT Phase 3:** Proven ad set/ad combos moved to CBO, optimized for stability over 2-3 days, then scaled

### CBO Pro Tips

- **Minimum Spend Hack:** Set daily minimums at the ad set level within CBO to force initial equal distribution (similar to ABO). Remove the minimums after ~1 week once Meta has enough data to make informed allocation decisions.
- **Budget Formula:** Campaign daily budget = (Target CPA x 50 conversions) / 7 days. This gives the algorithm enough budget to potentially exit learning within a week.
- Stick to **2-5 ad sets per CBO campaign** to avoid spreading data too thin.

**Sources:**
- [AdAmigo: CBO Best Practices for Meta Ads 2025](https://www.adamigo.ai/blog/cbo-best-practices-meta-ads)
- [AdsUploader: ABO vs CBO 2026](https://adsuploader.com/blog/abo-vs-cbo)
- [Depesh Mandalia: The Unexpected Journey -- CBO](https://depeshmandalia.com/the-unexpected-journey-cbo/)
- [Depesh Mandalia: 7 Facebook Ads Growth Strategies](https://depeshmandalia.com/7-facebook-ads-growth-strategies-for-scaling-ecommerce/)
- [RebootIQ: ABO vs CBO Finally Solved](https://rebootiq.com/abo-vs-cbo-meta-ads/)
- [Motion: Ultimate Guide to Creative Testing 2025](https://motionapp.com/blog/ultimate-guide-creative-testing-2025)

---

## 2. Ads Per Ad Set / Ad Sets Per Campaign

### Meta's Official Guidance

Meta's Help Center ("About Managing Ad Volume") recommends: **Use 6 or fewer creatives per ad set.** The delivery system favors ads with more delivery because conversion predictions are more accurate. Once you've added more than 6 ads, there is "little marginal benefit."

**Update (mid-2025):** Meta has softened this guidance. The 6-ad maximum was always a guideline, not a hard limit. Meta saw that *on average* more than 6 ads provided no benefit, but advertisers with larger budgets may see value in testing more.

### The Budget-Dependent Answer

| Budget Level | Recommended Ads per Ad Set |
|---|---|
| Small ($20-50/day per ad set) | 3-4 ads |
| Moderate ($50-150/day per ad set) | 4-6 ads |
| Large ($150+/day per ad set) | Can experiment with more |
| Testing-focused (any budget) | 1 ad per ad set for cleanest data |

**Why budget matters:** Facebook's algorithm needs **50 conversions per ad set per week** to optimize effectively. If you're running too many ads within an ad set on a small budget, the algorithm can't gather enough data on any single ad to make informed decisions.

### Ad Sets Per Campaign

- **2-5 ad sets per campaign** is the consensus sweet spot
- Having more than 5 ad sets spreads budget too thin, especially with smaller budgets
- Each ad set should represent a meaningfully different audience segment or creative angle

### The 1-Ad-Per-Ad-Set Testing Approach

Some experienced media buyers (including those aligned with Barry Hott's methodology) advocate for **1 ad per ad set during testing**. Rationale: while Facebook's algorithm tries to optimize multiple ads within an ad set, results are often skewed toward a single ad, making testing less accurate. Separating each creative into its own ad set gives cleaner performance data.

### Practical Rule for $50/Day

At $50/day total budget, you're looking at:
- 1 campaign
- 2-3 ad sets ($15-25/day each)
- 3-4 ads per ad set (or 1 ad per ad set if testing)

**Sources:**
- [Meta Business Help Center: Simplify Your Ad Set Structure](https://www.facebook.com/business/ads/ad-set-structure)
- [Meta Business Help Center: About Managing Ad Volume](https://www.facebook.com/business/help/2720085414702598)
- [Jon Loomer: No More Six Ad Limit Per Ad Set](https://www.jonloomer.com/qvt/no-more-six-ad-limit-per-ad-set/)
- [Jon Loomer: Number of Ads Per Ad Set](https://www.jonloomer.com/qvt/number-of-ads-per-ad-set/)
- [Digital Position: The Meta Ads Structure Every Business Should Be Using](https://www.digitalposition.com/resources/blog/ppc/the-meta-ads-structure-every-business-should-be-using/)

---

## 3. Budget Allocation for New Accounts ($40-50/day)

### Meta's Daily Spending Limits on New Accounts

New Meta ad accounts are subject to **daily spending limits imposed by Meta** (separate from your own budget settings). A $50 daily spending limit is commonly reported. This is not a bug -- it's Meta protecting against fraud on unverified accounts.

**How to increase the limit:**
1. **Complete business verification** -- Meta says this may help increase limits more quickly
2. **Build spending history** -- limits increase naturally as you spend consistently and stay in good standing
3. **Set budgets at your goal level** even if the spending limit is lower -- Meta recommends this so the limit can ramp up organically

### The Core Problem: $50/Day vs. the 50-Conversion Rule

Meta's algorithm needs ~50 optimization events per ad set per week to exit learning. If your target CPA is $40+ (realistic for a $50 supplement), the math doesn't work at $50/day:

- $50/day x 7 days = $350/week
- $350 / $40 CPA = ~8.75 purchases/week
- That's well short of 50

**Solutions for low-budget accounts:**

1. **Optimize for a higher-funnel event temporarily.** Instead of optimizing for Purchase, optimize for Add to Cart or Initiate Checkout. These happen more frequently, so you can hit 50 events faster and give the algorithm real signals to work with. Then switch to Purchase optimization once you have more data/budget.

2. **Consolidate ruthlessly.** Run ONE campaign with 1-2 ad sets maximum. Every dollar of data fragmentation at this budget level hurts.

3. **Use ABO, not CBO.** At $50/day, CBO doesn't have enough budget to meaningfully distribute. ABO gives you control over exactly where every dollar goes.

4. **Start with engagement/traffic campaigns** to build pixel data and audience pools before running conversion campaigns. (This is what you're already doing with the engagement campaigns.)

5. **Focus on creative, not structure.** At this budget, the #1 lever is your ad creative. A great ad at $50/day will outperform a mediocre ad at $500/day.

### Budget Benchmarks

- Average Facebook CPM: ~$14.69
- Average CPC: ~$0.72
- Average ecommerce ROAS: 2.05x
- At $50/day, you can expect roughly 3,400 impressions or ~70 clicks per day at average rates

### Allocation Strategy at $50/Day

**Phase 1 (Week 1-2): Creative Testing**
- 1 ABO campaign
- 2 ad sets (broad targeting, age 40+ US)
- 3 ads per ad set (your best 6 creatives)
- $25/day per ad set
- Optimize for Add to Cart or View Content (higher volume event)

**Phase 2 (Week 3-4): Winner Scaling**
- Kill losers, consolidate budget behind 2-3 winning creatives
- Switch optimization to Purchase if Add to Cart data is strong
- Single ad set if needed to concentrate data

**Phase 3 (Month 2+): Gradual Expansion**
- As spending limit increases, add new ad sets for horizontal testing
- Graduate to CBO when budget supports $100+/day

**Sources:**
- [Meta Business Help Center: About Daily Spending Limits](https://www.facebook.com/business/help/563129151097553)
- [Jon Loomer: Daily Spending Limits Stop Your Ads](https://www.jonloomer.com/qvt/daily-spending-limits-stop-your-ads/)
- [Jon Loomer: Campaign, Account, and Daily Spending Limits](https://www.jonloomer.com/campaign-spending-limits-account-spending-limits-daily-spending-limits/)
- [Cropink: Facebook Ad Budget Benchmarks](https://cropink.com/facebook-ad-budget)

---

## 4. The Learning Phase

### What It Is

The learning phase is Meta's data-gathering period for newly created or significantly edited ad sets. During this time, the algorithm is experimenting -- testing different audience segments, placements, and delivery patterns to find the optimal combination.

**Performance during learning is unstable and typically more expensive.** This is normal. The algorithm is exploring, not exploiting.

### How to Exit It

**The threshold:** ~50 optimization events per ad set within a 7-day period.

**The formula for budget needed:** (50 x Target CPA) / 7 = Required daily budget per ad set.

Example: If your target CPA is $40, you need ($50 x 40) / 7 = ~$286/day per ad set. At $50/day total budget, this is impossible for Purchase optimization -- which is why optimizing for a higher-funnel event matters for new/low-budget accounts.

### What Resets the Learning Phase

**Major resets (avoid during learning):**
- Budget changes greater than ~20%
- Changing the optimization event (e.g., Add to Cart to Purchase)
- Swapping core creative (images/videos)
- Modifying audience targeting (broadening or narrowing)
- Changing bid strategy
- Pausing for 7+ days and restarting

**Minor changes that typically do NOT reset:**
- Small text edits to copy
- Modest budget adjustments (under 20%)
- Adding new ads to an ad set (existing ads keep their learning)

### How to Exit Faster

1. **Set realistic budget** using the 50-conversion formula
2. **Simplify account structure** -- 2-3 ad sets max, not 10
3. **Use CBO** when budget allows (algorithm distributes to best performers)
4. **Scale budget gradually** -- no more than 20% at a time
5. **Choose the right optimization event** -- if you can't hit 50 purchases, use Add to Cart
6. **Don't edit during learning** -- resist the urge to "fix" things for 7 days
7. **Broaden targeting** -- Advantage+ placements and broad audiences give the algorithm more room to find conversions faster

### "Learning Limited" Status

This appears when Meta doesn't receive enough optimization events to make reliable predictions. Common causes:
- Budget too low relative to CPA
- Audience too narrow
- Too many ad sets fragmenting data
- Optimization event fires too infrequently

**What to do:** Consolidate ad sets, broaden targeting, increase budget, or switch to a higher-funnel optimization event.

**Sources:**
- [Meta Business Help Center: About the Learning Phase](https://www.facebook.com/business/help/112167992830700)
- [Brimar Online Marketing: Exit the Learning Phase Faster (2025)](https://brimaronlinemarketing.com/blog/what-is-the-facebook-ads-learning-phase-and-how-can-you-exit-it-faster/)
- [Social Media Examiner: How to Exit the Learning Phase Quicker](https://www.socialmediaexaminer.com/how-to-exit-the-facebook-ads-learning-phase-quicker/)
- [Lebesgue: Facebook Ads Learning Phase (2025 Update)](https://lebesgue.io/facebook-ads/facebook-ads-learning-phase-what-you-need-to-know-2024-update)

---

## 5. Kill vs Scale Decision Framework

### The 3x CPA Rule (Kill Threshold)

**Cross-referenced across multiple sources:** When an ad set has spent **3x your target CPA** without generating a single conversion, kill it. It's not "still learning" -- it's not working.

Example: If your target CPA is $40, kill any ad set that has spent $120+ with zero conversions.

### The Graduated Decision Framework

| Spend Level | CPA Result | Action |
|---|---|---|
| Less than 1x target CPA | No conversion yet | Too early to decide. Wait. |
| 1x-2x target CPA | No conversion | Concerning. Monitor closely. |
| 2x-3x target CPA | No conversion | Prepare to kill. Give it 24 more hours max. |
| 3x+ target CPA | No conversion | **Kill immediately.** |
| Any spend | CPA below target | Winner. Prepare to scale. |
| Any spend | CPA 1-1.5x target | Potential. Continue testing with more budget. |
| Any spend | CPA 1.5-2x target | Marginal. Test iterations of the creative. |
| Any spend | CPA 2x+ target | Kill or significantly iterate. |

### The Stability Requirement for Scaling

**Do not scale an ad that is performing well for only 1-2 days.** The consensus threshold:

- **Minimum 5 consecutive days** of stable performance (within 10% of target CPA) before scaling
- Some sources say 5-7 days
- Must show stable delivery volume, not just good CPA on tiny spend

### The Scaling Protocol

Once an ad qualifies:

1. Increase budget by **15-20% every 2-3 days** (not 50%, not 100%)
2. Wait 48-72 hours between adjustments -- the delivery system needs time to stabilize
3. If CPA holds after the increase, repeat
4. If CPA spikes, **reduce budget by 20%** and wait 2-3 days
5. If CPA exceeds target by 50% for 3 consecutive days, **pause the ad set**

### Key Metrics to Watch

- **CPA trend over 7-day and 14-day windows** (not just today's number)
- **Frequency** -- when it crosses 2.5 in prospecting campaigns, performance typically declines (CTR drops first, then CPM rises, then conversion rate drops)
- **CTR** -- declining CTR is the earliest warning sign of creative fatigue
- **CPM trends** -- rising CPMs with flat CTR means you're paying more for the same audience
- **ROAS stability** -- if daily ROAS bounces between 2x and 6x, the algorithm hasn't stabilized. Wait until numbers tighten before scaling.

### Minimum Data Before Any Decision

A creative that gets 10 clicks might show a $20 CPA, but that's not statistically meaningful. You need:
- At least 1,000+ impressions
- At least 20+ link clicks
- Ideally 3+ conversions before declaring a winner

### CPA Context

Your CPA only matters relative to your unit economics. If your CPA is $45 and your customer LTV is $200, you have room to scale aggressively. If your CPA is $45 and your LTV is $50, you're barely breaking even. **Always evaluate CPA against LTV, not in isolation.**

**Cody Plofker's insight from Jones Road Beauty:** "The hard truth for most DTC businesses is that CPAs only go one direction over time: up. The only defense is increasing the value of each customer" -- through AOV optimization, subscriptions, retention, and LTV plays.

**Sources:**
- [AdStellar: How to Scale Facebook Ad Campaigns (2026)](https://www.adstellar.ai/blog/how-to-scale-facebook-ad-campaigns)
- [Crunchy Digital: Scale Facebook Ads Without Losing Performance (2026)](https://crunchydigital.com.au/blog/scaling-facebook-ad-campaigns-without-killing-performance-in-2026/)
- [Cropink: How to Scale Facebook Ads (2025)](https://cropink.com/how-to-scale-facebook-ads)
- [Cody Plofker's Newsletter](https://codys-newsletter.beehiiv.com/)

---

## 6. Broad vs Interest Targeting (2024-2026)

### The Landscape Has Shifted Dramatically

The old playbook of stacking 5-10 interests per ad set is effectively dead. Multiple converging forces killed it:

- **iOS 14.5+ (2021)** destroyed much of the behavioral data that interest targeting relied on
- **Meta's June 2025 update** removed many specific interests and merged others into broader categories
- **Detailed targeting exclusions sunset** as of June 2025 for new campaigns
- **Advantage+ Audience** now treats interests as *suggestions*, not hard constraints

### What's Working Now

**Broad targeting (age + gender + location only) paired with strong creative and first-party data signals is outperforming interest targeting for most advertisers.**

Meta's own data: Advantage+ audiences cut CPA by up to **32%** compared to traditional interest targeting in ecommerce and lead gen verticals. 65% of US advertisers now use Advantage+ as their primary growth engine (Insider Intelligence).

Meta also reported a **22.6% lower median cost per conversion** when advertisers removed detailed targeting exclusions.

### When Interest Targeting Still Makes Sense

Interest targeting is not dead -- it's just repositioned:

1. **Brand new ad accounts** with zero conversion history (the algorithm has no signals to work with)
2. **Very small budgets** where broad targeting might waste spend on irrelevant audiences
3. **Niche markets** with clearly identifiable interest categories
4. **As "suggestions" within Advantage+ Audience** -- not hard constraints, but starting signals

### Advantage+ Audience: The New Default

Advantage+ Audience sits between manual interest targeting and fully open broad. You provide interests as *suggestions*, and Meta treats them as starting points but delivers outside them if the algorithm predicts conversions.

**How it works in practice:**
- Your interest suggestions influence early delivery (first few days)
- As conversion data accumulates, the suggestions fade in importance
- The algorithm increasingly relies on pixel/CAPI data and behavioral signals over your manual inputs

### The Practical Strategy for New Accounts

**Week 1-2:** Use Advantage+ Audience with 2-3 relevant interest suggestions (e.g., "health supplements," "anti-aging," "wellness") to give the algorithm a starting direction. Age 40+, US.

**Week 3+:** As pixel data builds, test fully broad (age + gender + location only) against your interest-suggested ad sets. Let the data tell you which performs better.

**Month 2+:** Likely migrate to primarily broad targeting, as your pixel and CAPI data become the dominant targeting signals.

**Nick Shackelford's position:** "Creative is the new targeting." With broad audiences, your ad creative does the segmentation work -- the right hook and visual naturally attracts the right person. The algorithm then learns from who engages and converts.

**Sources:**
- [Turba Media: Broad vs Interest Targeting -- 2025 Guide](https://www.turbamedia.io/post/broad-targeting-vs-interest-targeting---the-definitive-2025-guide)
- [Lebesgue: Broad Targeting Beats Lookalikes](https://lebesgue.io/facebook-ads/broad-targeting-beats-lookalikes-the-future-of-facebook-audience-targeting)
- [FanIQ: Meta Detailed Targeting Update 2025](https://www.faniq.live/blog/meta-targeting-update)
- [Cropink: Meta Ads Targeting Options 2026](https://cropink.com/meta-ads-targeting-options)
- [WordStream: Facebook Ad Targeting 2026](https://www.wordstream.com/blog/facebook-ad-targeting)

---

## 7. Advantage+ Shopping Campaigns vs Manual Campaigns

### What ASC Is (2025-2026)

Meta renamed Advantage+ Shopping Campaigns to **Advantage+ Sales Campaigns (ASC)** in early 2025. ASC now supports ecommerce sales, lead gen, and app installs -- not just shopping.

ASC is Meta's most automated campaign type: it handles targeting, placements, creative mix, and budget distribution via AI. You provide creatives and a budget; Meta handles the rest.

### ASC Pros

- **Time savings** -- dramatically less manual management
- **Dynamic budget allocation** -- shifts spend to what's working in real-time
- **Massive creative testing** -- can test up to 150 creative assets in a single campaign
- **AI audience discovery** -- finds converters you wouldn't have targeted manually
- **Strong for top-of-funnel prospecting** at scale

### ASC Cons

- **"Black Box" problem** -- you can't see detailed audience breakdowns or placement-level performance. Hard to extract learnings.
- **Limited targeting controls** -- historically country-level only (though 2026 updates added basic age/gender preferences and custom audience exclusions)
- **Severe learning phase** -- more instability than standard campaigns when changes are made. Make fewer changes and wait longer for results.
- **Creative burnout risk** -- the algorithm finds winners and runs them into the ground. Requires constant creative refresh.
- **Lead quality concerns** -- some advertisers report lower quality conversions vs. manual campaigns

### Manual Campaign Pros

- Full control over audience, creative, budget splits, placements
- Better transparency into what's working and why
- Ideal for retargeting and mid/bottom funnel
- Superior for structured A/B testing
- Better for niche/segmented audiences

### The Critical Question for New Accounts

**ASC requires conversion data to perform well.** It uses your pixel history, customer lists, and past conversion patterns to optimize. A brand new account with zero purchase data is giving ASC nothing to work with.

**The consensus for new accounts:**

1. **Start with manual campaigns** to build learnings, test creative, and accumulate pixel data
2. **Layer in ASC** once you have consistent conversion volume (ideally 50+ purchases/week)
3. **Run both in parallel** -- ASC for broad prospecting, manual for retargeting, testing, and niche segments

**Cody Plofker's team at Jones Road Beauty** runs both: ASC handles scaled prospecting while manual campaigns handle specific segments and creative testing.

### ASC Budget Tip

If you do test ASC early, use the "existing customer" cap. ASC lets you set a maximum percentage of budget that goes to existing customers. Set this to 0-10% to ensure most spend goes to new customer acquisition.

**Sources:**
- [Birch: Understanding Meta's Advantage+ Sales Campaigns (2025)](https://bir.ch/blog/advantage-plus-sales-campaigns-guide)
- [Drive Creative Agency: Meta Advantage+ vs Manual](https://drivecreativeagency.com/meta-advantage-plus-vs-manual/)
- [Marpipe: Meta Advantage+ Pros, Cons 2025](https://www.marpipe.com/blog/meta-advantage-plus-pros-cons)
- [AskNeedle: Founder's Guide to ASC](https://www.askneedle.com/blog/meta-advantage-plus)
- [WordStream: Meta Advantage+ vs Manual Setup](https://www.wordstream.com/blog/meta-advantage-vs-manual-settings)

---

## 8. Conversion API (CAPI) Setup

### Why CAPI Is Non-Negotiable

**Browser-based tracking (Meta Pixel alone) is now missing 40-60% of conversions.** iOS privacy changes, Safari ITP, ad blockers, and browser cookie restrictions have systematically degraded pixel reliability since 2021.

CAPI sends conversion data directly from your server to Meta, bypassing all browser-side restrictions.

**The data:** Advertisers running Pixel + CAPI together report tracking **~95% of conversions** vs. 60-70% with Pixel alone. Some report up to **30% improvement in ROAS** after implementing CAPI, because the algorithm is finally getting accurate data to optimize against.

### How CAPI Improves CPA

This isn't just about reporting accuracy -- it directly affects CPA:

1. **Better optimization signals** -- the algorithm can't optimize for purchases it can't see. Missing 40% of conversion signals means 40% of your optimization data is invisible.
2. **Improved audience building** -- custom audiences and lookalikes are built from conversion data. Missing data = worse audiences.
3. **Accurate learning phase** -- the 50-conversion threshold counts faster when CAPI captures events the pixel misses.
4. **Better Event Match Quality (EMQ)** -- higher EMQ means Meta can match more events to user profiles, improving targeting precision.

### Setup for Shopify

**Option 1: Native Shopify Integration (Recommended to Start)**
1. Install the "Facebook and Instagram" app from Shopify App Store
2. Connect your Facebook Business Manager, pixel, and page
3. Enable **Automatic Advanced Matching** (passes customer data for better matching)
4. Set data sharing to **"Maximum"** -- this activates the Conversions API
5. Remove any manually installed pixel code to avoid duplication

Setup time: 15-30 minutes. Free. Good enough for stores spending under $5K/month on Meta.

**Limitations of native integration:**
- Still partially browser-dependent
- No subscription event tracking
- Limited product ID management
- Event Match Quality may be lower than server-side solutions

**Option 2: Server-Side GTM (More Control)**
- More accurate, fully server-side
- Requires technical setup
- Better for higher spend levels

**Option 3: Third-Party Apps (Elevar, Littledata, etc.)**
- Bridge between native simplicity and server-side accuracy
- Good middle ground as spend scales

### Event Match Quality (EMQ)

EMQ measures how well Meta can match your events to user profiles. Score ranges 1-10.
- **Below 6.0:** Significant signal loss. Investigate and fix.
- **6.0-7.0:** Acceptable. Room for improvement.
- **7.0-8.0:** Good. Algorithm has strong matching data.
- **Above 8.0:** Excellent. Maximum matching accuracy.

Check your EMQ in Events Manager. If it's below 6, the native Shopify integration may not be passing enough identifiers.

### Deduplication

CAPI + Pixel will fire the same events from both browser and server. Meta deduplicates using a shared `event_id` -- make sure this is configured correctly or you'll double-count conversions and skew optimization.

**Sources:**
- [Meta for Developers: Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/)
- [Meta Business Help Center: About Conversions API](https://www.facebook.com/business/help/AboutConversionsAPI)
- [Triple Whale: Facebook CAPI in 2026](https://www.triplewhale.com/blog/facebook-capi)
- [wetracked.io: Meta Ads CAPI Explained (2026)](https://www.wetracked.io/post/what-is-capi-meta-facebook-conversion-api)
- [Ingest Labs: Shopify CAPI Setup Guide](https://ingestlabs.com/shopify-capi-setup-guide/)
- [Elevar: Meta CAPI for Shopify](https://getelevar.com/facebook/meta-capi-for-shopify-stores-why-and-how-to-implement/)

---

## 9. Attribution Windows

### Available Windows (Post-iOS 14)

Meta removed 28-day click, 28-day view, and 7-day view windows for privacy compliance. Current options:

| Window | What It Measures |
|---|---|
| **1-day click** | Conversions within 24 hours of clicking the ad |
| **7-day click** | Conversions within 7 days of clicking the ad |
| **1-day view** | Conversions within 24 hours of viewing (not clicking) the ad |
| **1-day engaged view** | Conversions within 24 hours after watching 10+ seconds of a skippable video ad |

### The Default: 7-Day Click + 1-Day View

This is Meta's default and the recommendation for most advertisers. It provides Meta with the **largest addressable audience** to target, which generally means lower costs.

### Which to Use by Scenario

| Scenario | Recommended Window | Why |
|---|---|---|
| **Most DTC ecommerce** | 7-day click + 1-day view | Captures the typical 2-7 day consideration period for $40-50 products |
| **Impulse buys / flash sales** | 1-day click | Most conversions happen immediately; shorter window gives more conservative data |
| **B2B / lead gen** | 7-day click | Longer consideration cycle |
| **Higher-ticket items** | 7-day click + 1-day view | Need the full window to capture deliberate buyers |
| **NMN supplement ($50 product, 40+ audience)** | **7-day click + 1-day view** | This audience researches before buying. A 40+ health-conscious consumer is not an impulse buyer. |

### The Comparison Technique

**Always set up multiple attribution views in your reporting columns.** Create custom columns showing both 1-day and 7-day click attribution side by side. This reveals your consideration window:

- If 7-day shows 100 conversions and 1-day shows 60, that means **40% of conversions happen between day 2 and day 7.** Optimizing on 1-day data alone would miss nearly half your impact.
- If 7-day and 1-day are nearly identical, most buyers convert fast and a shorter window may be more accurate.

### 2026 Attribution Changes

Meta removed longer view-through attribution windows from the Ads Insights API in January 2026. Some advertisers saw **30-40% drops in attributed conversions** because the 8-28 day view-through window no longer counts. This affects reporting, not actual performance -- but it means your reported numbers may look worse even if real performance hasn't changed.

**Meta's Incremental Attribution (2025+):** A new tool that isolates conversions that would NOT have happened without the ad. Helps separate correlation from causation. Worth monitoring as it matures.

### Practical Advice

Stick with **7-day click + 1-day view** for your purchase campaigns. It gives the algorithm the broadest optimization scope and matches the consideration timeline for a $50 health supplement targeting adults 40+. Use 1-day click as a secondary reporting column to understand your immediate conversion rate.

**Sources:**
- [Foreplay: Ultimate Guide to Facebook Attribution Settings (2025)](https://www.foreplay.co/post/where-and-how-to-use-facebook-attribution-settings-ultimate-guide)
- [Jon Loomer: Meta Ads Attribution Setting -- Complete Guide](https://www.jonloomer.com/meta-ads-attribution-setting-a-complete-guide/)
- [Madgicx: Complete Guide to Facebook Ads Attribution 2025](https://madgicx.com/blog/facebook-ads-attribution)
- [Foxwell Digital: Meta Ads Attribution Settings Guide](https://www.foxwelldigital.com/blog/meta-ads-attribution-settings-a-guide-to-choosing-the-right-one-for-your-account)
- [Dataslayer: Meta Ads Attribution Window Changes 2026](https://www.dataslayer.ai/blog/meta-ads-attribution-window-removed-january-2026)
- [Cometly: Facebook Ads Attribution Window Guide 2026](https://www.cometly.com/post/facebook-ads-attribution-window)

---

## 10. Scaling Strategies: Vertical vs Horizontal

### Vertical Scaling (Going Deeper)

Vertical scaling = increasing budget on what's already working.

**The Rules:**
- Increase budget by **no more than 15-20% every 3-4 days**
- Wait **3 full days minimum** between increases to let delivery stabilize
- Only scale ad sets that have been **stable for 7+ days**
- **Never scale during learning phase**
- Use CBO for vertical scaling (algorithm distributes increased budget across ad sets without triggering individual resets)

**Why performance drops when you scale too fast:**
- Budget increases >20% can reset the learning phase
- The algorithm suddenly has more budget than it knows what to do with
- It explores broader (often lower-quality) audience segments
- CPA spikes 25-40% before (hopefully) stabilizing

**Vertical scaling ceiling:** Eventually, you'll hit a point where adding more budget yields diminishing returns. Signs include rising CPAs despite stable creative, frequency climbing above 2.5, and CTR declining. This is when you switch to horizontal scaling.

### Horizontal Scaling (Going Wider)

Horizontal scaling = duplicating what works and finding new pools of potential customers.

**The Tactics:**
1. **Duplicate winning ad sets** with modified targeting:
   - New lookalike percentages (1% -> 3% -> 5%)
   - Broader interest clusters
   - Open/broad targeting with strong creatives
   - New geographic regions
2. **New creative angles** for the same product (different hooks, formats, styles)
3. **New campaign types** (e.g., adding ASC alongside manual campaigns)

**When to Use Horizontal Scaling:**
- Your vertically-scaled campaign shows signs of fatigue (rising CPA, declining CTR, frequency above 2.5-3)
- You've maxed out budget increases on current ad sets
- You want to test new audiences without disrupting proven performers

**Critical Rule:** Test ONE variable per duplication. If you duplicate an ad set and change both the audience AND the creative, you can't learn anything from the results.

### The Combined Approach

**Phase 1: Validate**
- Find 1-2 profitable ad sets via ABO testing

**Phase 2: Vertical Scale**
- Increase budget 15-20% every 3-4 days on winners
- Monitor CPA stability

**Phase 3: Horizontal Scale (when vertical hits ceiling)**
- Duplicate winners into new audiences
- Test new creative angles
- Launch ASC campaign alongside manual

**Phase 4: Repeat**
- Each new horizontal test produces new data
- Winners from horizontal testing get vertically scaled
- Cycle continues

**Important:** Do NOT mix vertical and horizontal scaling simultaneously on the same ad set. If you duplicate an ad set into a new audience AND increase budget, you can't tell which change caused any performance shift.

### Creative as a Scaling Lever

**Nick Shackelford (managed $200M+ in Meta spend):** Most winning creatives emerge from the top 10% of tests. Launch 20-30 variations weekly across different hooks, tones, and formats.

**Barry Hott (managed $600M+ in social ad spend):** His "ugly ads" methodology -- ads that look native/organic rather than polished -- consistently outperforms in testing. He emphasizes working WITH the Meta algorithm, not against it. His framework involves broad audience targeting combined with high creative volume and systematic testing.

**The creative fatigue cycle:** At scale, creative fatigue becomes the #1 performance killer. A creative that works at $50/day may fatigue within 2-3 weeks at $500/day. You need a pipeline of new creatives ready to replace fatigued ones. This is why Nick Shackelford recommends testing 20-30 new creative variations weekly at scale.

**Sources:**
- [AdBid: Facebook Ads Scaling -- Vertical vs Horizontal 2026](https://adbid.me/blog/facebook-ads-scaling-strategies-2026)
- [Jon Loomer: Two Strategies to Scale Facebook Ads](https://www.jonloomer.com/facebook-ad-scaling/)
- [Lebesgue: 5 Strategies to Scale Facebook Ads 2025](https://lebesgue.io/facebook-ads/how-to-scale-facebook-ads)
- [Admetrics: How to Scale Facebook Ads for Maximum ROI 2026](https://www.admetrics.io/en/post/how-to-scale-facebook-ads-in-2025)
- [TheOptimizer: Scale Meta Ads Without Killing Performance](https://theoptimizer.io/blog/how-to-scale-meta-ads-without-killing-performance)
- [Silver Spoon Agency: Scale Facebook Ads Without Wasting Budget](https://silverspoonagency.com/how-to-scale-facebook-ads/)

---

## Summary: Key Takeaways for Baseline NMN Launch

### Your Specific Situation
- New ad account with $40-50/day spending limit
- DTC supplement, $49.99 price point
- Target audience: 40+ US adults
- Running through Sarah Lawson's partner page
- Shopify store with CAPI needed

### The Priority Actions

1. **Set up CAPI immediately** via Shopify's native integration (Maximum data sharing, Advanced Matching ON). This is the single highest-ROI infrastructure task. Without it, you're flying blind on 40-60% of conversions.

2. **Use ABO for testing, not CBO.** At $50/day, CBO doesn't have enough budget to distribute meaningfully. Control where every dollar goes.

3. **Start with Add to Cart optimization** instead of Purchase. You won't hit 50 purchases/week at $50/day, but you can hit 50 Add to Carts, giving the algorithm real learning data.

4. **Run 1 campaign, 2 ad sets, 3 ads each.** Maximum consolidation at this budget. Each ad set gets ~$25/day. Use Advantage+ Audience with age 40+ and 2-3 health/wellness interest suggestions.

5. **Attribution: 7-day click + 1-day view.** Your audience researches before buying a $50 supplement. They're not impulse buyers.

6. **Kill threshold: 3x target CPA with zero conversions.** Scale threshold: 5+ days of stable CPA within target.

7. **Creative is your biggest lever.** At this budget, one great ad beats ten mediocre ones. Focus creative energy on the native/camouflage style ads running through Sarah's page -- they should look organic, not like ads. This aligns with Barry Hott's "ugly ads" methodology and the broader industry trend toward native-feeling creative.

8. **Scale gradually.** 15-20% budget increases every 3-4 days. Graduate to CBO when budget supports $100+/day. Add ASC when you have 50+ purchases/week.

9. **Remember the currency gap.** Meta bills in CAD, revenue is USD. Your actual ROAS is ~35% better than what Meta reports if you're comparing CAD spend to USD revenue. Track this manually.

10. **Patience is a strategy.** The learning phase, the spending limit ramp-up, the data accumulation -- all of it takes time. The advertisers who fail at this stage are the ones who panic-edit their campaigns every 24 hours. Set up properly, launch, and wait 7 days before making any decisions.
