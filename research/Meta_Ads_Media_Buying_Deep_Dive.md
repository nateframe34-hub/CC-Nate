# Meta Ads Media Buying — Deep Dive Knowledge Base

> Compiled March 17, 2026. Cross-referenced across Meta official documentation, established media buyers (Jon Loomer, Depesh Mandalia, Barry Hott, Cody Plofker, Nick Shackelford, Dara Denney, Andrew Faris), and reputable marketing publications. Single-source claims are flagged. Fluff and "quick fix" advice has been filtered out.

---

## PART 1: HOW META'S AD SYSTEM ACTUALLY WORKS

Understanding the machine you're feeding money into is the foundation. Everything else — CPMs, CPAs, creative strategy, scaling — flows from this.

### The Auction

Every single time there's an opportunity to show an ad to a user, ALL ads targeting that user enter an auction. The winner is NOT the highest bidder. The winner is the ad with the highest **Total Value score**.

**Total Value = (Advertiser Bid x Estimated Action Rate) + User Value**

Three components:

**1. Advertiser Bid** — What you're willing to pay per desired outcome. With auto-bidding (Lowest Cost / Highest Volume), Meta sets this dynamically. You don't control individual bids.

**2. Estimated Action Rate (EAR)** — Meta's real-time prediction of whether THIS specific user will take your desired action (purchase, add to cart, click, etc.). Calculated per-user, per-impression. Based on:
- The user's historical behavior (what they've clicked, bought, engaged with)
- How similar users responded to similar ads
- Your ad's past performance data
- Device type, time of day, session context
- Your pixel/dataset event quality and volume

**3. User Value / Ad Quality** — A quality score reflecting user experience. Determined by:
- User feedback (hides, reports = bad)
- Low-quality signals (clickbait, sensationalized language, withheld information)
- Landing page experience (load time, bounce rate)
- Post-click experience
- Engagement signals (saves, shares, comments = good)

**Critical implication:** A lower bid can WIN against a higher bid if EAR and Quality are strong enough. This is why creative quality directly affects what you pay — it's not a "nice to have," it's a core input to the auction formula.

The auction uses a modified **Vickrey-Clarke-Groves (VCG)** mechanism — the winner pays just enough to beat the second-highest Total Value, not their full bid. This means truthful bidding is optimal. Gaming the system by overbidding doesn't help.

Sources: Meta Business Help Center, Cornell Networks Course, Marin Software, Ads Analysis, multiple academic publications.

---

### Meta's ML Delivery System: Exploration vs Exploitation

When an ad set goes live (or after a significant edit), Meta enters **exploration mode**. The algorithm experiments by showing your ad to diverse audience segments to discover who converts. Performance is volatile — CPA swings wildly because the system is casting a wide net.

Once enough data accumulates, the system shifts to **exploitation mode** — leaning into high-probability converters. Performance spikes and stabilizes. Then, once that pocket of demand is exhausted, it cycles back to exploration.

This cycle repeats continuously. It's not a one-time learning phase — it's the permanent operating rhythm of the algorithm.

**The key ML systems powering this (as of late 2025):**

**Andromeda (Retrieval Engine)** — Uses models 10,000x larger than the previous system. Maps users, contexts, and ads into a high-dimensional embedding space. Narrows billions of ads to a relevant shortlist in milliseconds. Result: +6% recall improvement, +8% ad quality improvement.

**Meta Lattice (Ranking Model)** — Multi-task learning architecture that predicts ad performance across different surfaces, objectives, and ad types simultaneously. Specifically designed to solve the cold start problem — can deliver relevant ads even with little data. Result: +12% ad quality improvement, +6% increase in conversions.

**GEM (Generative Ads Recommendation Model)** — Meta's largest foundation model for ad recommendations. Enables cross-surface learning (Instagram insights improve Facebook predictions). Result: +5% ad conversions on Reels at launch.

**What this means practically:** Andromeda doesn't start with your audience definition — it evaluates your ad creative, then predicts which users are most likely to engage. Your creative portfolio IS your targeting. The system matches ad creative to individual users based on thousands of behavioral signals.

Sources: Engineering at Meta (Andromeda blog post, GEM blog post), Meta AI Blog (Lattice), Social Nucleus, Northbeam, Madgicx.

---

### The Three Relevance Diagnostics

Meta replaced its single Relevance Score (1-10) in 2019 with three separate diagnostics, available once an ad has 500+ impressions:

**Quality Ranking:** Your ad's perceived quality vs competitors for the same audience. Based on hide/report rates and detection of low-quality attributes.

**Engagement Rate Ranking:** Expected engagement (clicks, reactions, comments, shares) vs competitors.

**Conversion Rate Ranking:** Expected conversion rate vs competitors with the same optimization goal. Reflects post-click experience — landing page, checkout friction, CTA clarity. This is NOT just about the ad itself.

**How to read them together:**
- Low Quality + Low Conversion = your ad doesn't represent the actual product well
- Low Engagement + Low Conversion = both ad and landing page need work
- Low Engagement + High Conversion = the ad works for those who see it but doesn't attract attention (scale problem)

Moving from Below Average to Average has far more impact than Average to Above Average. These are diagnostics, not goals — don't over-optimize them.

Sources: Meta Business Help Center (multiple pages), J7 Media.

---

## PART 2: NEW AD ACCOUNT MECHANICS

### Spending Limits — How They Actually Work

Meta imposes THREE distinct types of spending limits (conflating them is a common mistake):

**A. Daily Spending Limit (set by Meta, often invisible to you)**
- New accounts start with a low ceiling — sources report $25 to $250/day depending on the account.
- This limit is invisible. You may set a $100/day budget but Meta will only spend $50.
- It increases automatically based on: successful payment history, consistent spend patterns, policy compliance, and time.
- The billing threshold also starts very low (as low as $2) and ratchets up through $4, $10, $20, $25, etc. after each successful charge.
- After roughly $600-$1,000 in cumulative successful spend, most accounts see meaningful limit increases.
- Business verification and 2FA can accelerate the process.
- There is no reliable way to manually request an increase.

**B. Account Spending Limit (set by you, optional)**
- A lifetime cap you can set on your total ad account spend. All campaigns pause when hit.

**C. Campaign Spending Limit (set by you)**
- A lifetime cap on a single campaign.

Sources: Meta Business Help Center, Jon Loomer, Graphed, AgencyGDT, Eight Digit Media.

---

### Account Trust and Quality Signals

Meta uses multiple overlapping scoring systems:

**HiVA Score (Hidden)** — An internal, invisible score Meta assigns to your Business Manager. Based on historical performance, policy adherence, user experience signals. Determines leniency on bans and limitations. You cannot see this score. Confirmed by multiple industry sources but Meta does not publicly document it.

**Business Account Feedback Score (Visible)** — 0-5 score based on post-purchase customer feedback.
- Below 2: Meta may restrict ad delivery
- Below 1: May lose ability to advertise entirely
- October 2025 update: Customer feedback will play a significantly stronger role in the ad auction going forward

**Account Quality Dashboard (Visible)** — facebook.com/accountquality/. Traffic-light system (green/yellow/red). Tracks rejected ads, violation severity, negative user feedback patterns. High rejection rates = throttled reach, higher CPMs, potential account disablement.

**Every ad rejection on a new account carries disproportionate weight.** On a new account in the health/supplement space, a pattern of rejections early on could hamper the account's trust score for months.

Sources: Uproas, Meta Business Help Center (multiple pages), The Digital Exchange, Birch, Madgicx, Graphed.

---

### Warming Up a New Ad Account — What's Real vs Myth

**REAL (consistent across multiple sources):**

- **Gradual budget scaling is real and important.** Every credible source agrees: jumping from $0 to hundreds/day on a brand-new account is a red flag to Meta's fraud detection. Start small ($5-$10/day), scale by 20% increments every 2-4 days.
- **Payment history matters.** Successful charges build trust. Confirmed by Meta's own documentation.
- **Policy compliance from day one matters.** Ad rejections on a new account are disproportionately damaging vs. an established account.
- **Business verification helps.** Sends a trust signal that can accelerate limit increases and reduce restriction risk.
- **Organic page activity helps.** Real posts and engagement before running ads looks more legitimate.

**MYTH or OVERSTATED:**

- **"You must wait 30 days before running any ads."** Overly cautious. Legitimate advertisers with clean creative and gradual budgets can start within days.
- **"Warming up guarantees you won't get banned."** False. Reduces risk but doesn't eliminate it.
- **"You need to simulate human browsing behavior."** Only relevant for purchased/farmed accounts (TOS violation). Irrelevant for legitimate advertisers.

Sources: Uproas, Graphed, AdMove, multiple practitioner forums.

---

### Does Running Cheaper Campaigns First Help Purchase Campaigns Later?

**The verdict: This is largely a myth, with two legitimate exceptions.**

**Why it's a myth:** Meta's algorithm optimizes for the objective you select. If you optimize for engagement, Meta finds engagers. If you optimize for traffic, Meta finds clickers. These are fundamentally different audiences than purchasers. Multiple sources use the same analogy: "Training for a marathon in a swimming pool."

Test data from Lebesgue: Sales-optimized campaigns showed 89.5% higher conversion rates and 76% higher ROAS compared to traffic campaigns targeting the same product.

**The two legitimate exceptions:**

1. **Social proof accumulation:** Running an ad as an engagement campaign for a few days to build likes/comments before using that same post as a purchase ad. The social proof makes the purchase ad more effective. This is about the creative, not the account.

2. **Account warm-up (payment/trust signals):** Running cheap campaigns builds payment history and trust signals. This is about account health, NOT about training the algorithm for purchases.

**Bottom line:** When you launch purchase campaigns, the algorithm starts learning about purchasers from scratch. Engagement campaign data does NOT transfer to help find buyers. Optimize for purchases (or Add to Cart) from day one of your purchase campaigns.

Sources: ZillaClick, Transcend Digital, Lebesgue, LinearDesign, Heath Media.

---

## PART 3: CPM MECHANICS — WHY COSTS ARE WHAT THEY ARE

### Why CPMs Are High for New Accounts

Multiple compounding factors:

**Cold Pixel / No Conversion Data:** Meta's EAR predictions are essentially guesses without purchase history. Lower EAR = lower Total Value = you pay MORE to win auctions.

**Learning Phase Volatility:** Meta is exploring — testing different segments, placements, creative combinations. This exploration is deliberately broad and inefficient. CPM and CPA swing wildly. This is expected behavior, not failure.

**Account Trust Score:** New accounts have lower trust. High-tier whitelisted accounts (agency accounts with spend history) consistently get lower CPMs.

**iOS Privacy / Signal Loss:** 20-30%+ of actual conversions may never reach Meta due to iOS privacy changes and browser blocking. For new accounts without CAPI, this is worse, further degrading EAR accuracy.

Sources: Feedforce, Lebesgue, Two Owls, The Brand Amp, GlobeNewsWire.

---

### What Drives CPM Variation

**By Audience:**
- Retargeting CPMs are 100%+ higher than prospecting (smaller audience = fewer auction opportunities = higher price)
- Narrow interest segments: $10-15 CPM
- Narrow custom/remarketing: $15-25 CPM
- Broad prospecting: generally lowest CPMs
- Frequency above 3x per user = CPA increases 10-25% due to fatigue

**By Placement:**
- Restricting placements pushes CPM toward $15-20+
- Reels are 10-30% cheaper than Feed video (expanding inventory, lower competition)
- Advantage+ placements (letting Meta choose) = lowest blended CPM

**By Time of Year:**
- Q1 is cheapest. Q4 is most expensive.
- Black Friday/Cyber Monday/Christmas spike CPMs 20-40%
- January sees a reset to lower CPMs
- You're in March (Q1) right now — best time to be building data.

**By Objective:**
- Campaign objective has the STRONGEST influence on CPM
- Purchase objectives carry higher CPMs than engagement/traffic/video views
- Makes sense: purchase-optimized auctions compete against other advertisers also bidding for buyers

Sources: Affect Group, 303 London, Madgicx, Databox.

---

### What Actually Lowers CPMs vs What's Myth

**CONFIRMED (multi-source agreement):**

| Lever | Why It Works |
|-------|-------------|
| Broad targeting | Reduces auction competition; more room for Meta to find cheap conversions |
| Creative quality/freshness | High engagement improves EAR and User Value, directly boosting Total Value. Strongest single lever. |
| Video-first / Reels format | 10-30% lower CPMs, expanding inventory |
| Advantage+ placements | Meta optimizes placement, reduces blended CPM |
| Higher-funnel optimization events | More signals faster, exits Learning Phase sooner |
| CAPI | Recovers lost signal data, improving EAR accuracy and Total Value |

**MYTHS:**

| Claim | Reality |
|-------|---------|
| "Low CPM = good performance" | WRONG. Cheap impressions that don't convert are wasted budget. A $25 CPM that converts profitably beats a $10 CPM that doesn't. |
| "Narrow targeting = lower CPM" | Opposite is generally true. Narrow audiences increase auction pressure. |
| "Just increase budget to fix CPM" | Budget needs to be sufficient for learning, but more money on bad creative doesn't help. |
| "Engagement bait lowers CPM" | Meta penalizes engagement bait in quality scoring. Tanks ad quality and risks account penalties. |

Sources: Madgicx, Databox, NestScale, ShortVids, WASK.

---

### The Metric Chain — Which Numbers Actually Matter

```
CPC = CPM / (CTR x 1,000)
CPA = CPC / Conversion Rate
ROAS = Revenue per Conversion / CPA
```

**Hierarchy of importance:**

1. **ROAS / CPA** — The only metrics that directly measure business outcome. North Star for DTC.
2. **CTR** — Primary diagnostic for creative performance. Below ~0.9%, Meta effectively penalizes you with higher CPMs.
3. **CPM** — Cost-efficiency indicator, but it's an OUTPUT of the auction, not something you directly control. Don't optimize for low CPM alone.
4. **CPC** — Derived metric. Useful as diagnostic, not a primary target.

**The key insight:** Creative affects CTR, which affects CPC, which affects CPA, which affects ROAS. AND creative quality feeds back into the auction via EAR and User Value, affecting CPM. Creative is the one input that cascades through EVERY metric.

Sources: Triple Whale, WordStream, WUpscale, BestEver.

---

### CPM Benchmarks for Health/Supplement DTC (2024-2026)

| Source | Category | CPM | Period |
|--------|----------|-----|--------|
| Triple Whale | Health & Wellness (all) | $20.70 median | Full year 2025 |
| Triple Whale | H&W YoY change | +38.03% | 2024 to 2025 |
| Mesha | Healthcare | $15.77 avg | 2025 |
| Lebesgue | Beauty & Health | $12.46 | 2026 |
| Affect Group | US average (all industries) | $22.20 | 2025 |

Health & Wellness experienced the HIGHEST CPM inflation of any industry in 2025 at +38%. But also had the highest absolute CTR at 2.70%, suggesting the category has leaned heavily into video/Reels.

Sources: Triple Whale, Mesha, Lebesgue, Affect Group, Varos.

---

## PART 4: CAMPAIGN STRUCTURE & CPA OPTIMIZATION

### CBO vs ABO — When to Use Each

**ABO (Ad Set Budget Optimization):** Budget set at the ad set level. You control spend per ad set. Use for:
- Early-stage creative or audience tests where each variation needs equal spend
- Small budgets where you need to guarantee each test gets enough spend
- New accounts with limited pixel data
- Isolating variables — prevents Meta from prematurely picking a "winner"

**CBO (Campaign Budget Optimization / Advantage Campaign Budget):** Budget at campaign level. Meta distributes. Use for:
- Scaling proven winners
- When pixel records 50+ conversion events per week
- Budget is $500+/day (Depesh Mandalia's threshold)

**Consensus: Use both, sequentially.** ABO for testing → Migrate winners to CBO for scaling.

**Depesh Mandalia's GT Framework:**
- GT Phase 1: ABO to identify best audiences
- GT Phase 2: ABO to test new creatives against winning audiences
- GT Phase 3: Proven combos moved to CBO, optimized 2-3 days, then scaled

**CBO Pro Tip:** Set daily minimums at the ad set level within CBO to force initial equal distribution. Remove after ~1 week once Meta has enough data.

Sources: AdAmigo, AdsUploader, Depesh Mandalia, RebootIQ, Motion.

---

### Optimal Structure by Budget Level

| Budget Level | Recommended Ads per Ad Set | Ad Sets per Campaign |
|---|---|---|
| Small ($20-50/day per ad set) | 3-4 ads | 1-2 |
| Moderate ($50-150/day per ad set) | 4-6 ads | 2-5 |
| Large ($150+/day per ad set) | Can experiment with more | 3-5 |
| Testing-focused (any budget) | 1 ad per ad set for cleanest data | As many as budget supports |

Meta's official guidance: 6 or fewer creatives per ad set. Beyond 6, "little marginal benefit."

At $50/day total: 1 campaign, 2 ad sets ($25/day each), 3 ads per ad set.

Sources: Meta Business Help Center, Jon Loomer, Digital Position.

---

### The Learning Phase

**What it is:** Meta's data-gathering period for newly created or significantly edited ad sets. Performance is unstable and more expensive. The algorithm is exploring, not exploiting.

**The threshold:**
- Standard: 50 optimization events per ad set within 7 days
- NEW (2025, rolling out): 10 optimization events for Purchase-optimized campaigns (not all accounts yet)

**What resets learning:**
- Budget changes >20%
- Changing optimization event
- Swapping core creative
- Modifying audience targeting
- Changing bid strategy
- Pausing for 7+ days

**What does NOT reset learning:**
- Small text edits to copy
- Modest budget adjustments (under 20%)
- Adding new ads to an ad set (existing ads keep their learning)

**"Learning Limited" status:** Appears when Meta can't get enough events. Common causes: budget too low relative to CPA, audience too narrow, too many ad sets fragmenting data. Solution: consolidate, broaden targeting, increase budget, or optimize for a higher-funnel event.

**For a $50/day budget with ~$40 CPA:** You'd get ~8 purchases/week. That's well short of 50 under the old threshold, but close under the new 10-event threshold. The new threshold is a significant tailwind for your budget level.

Sources: Meta Business Help Center, Madgicx, Digicom, Lebesgue, Jon Loomer, Birch.

---

### Signal Density — The Most Important Concept for New Advertisers

Meta's algorithm needs a critical mass of conversion data concentrated in a single optimization target to learn effectively.

**The math:** Five ad sets getting 2 conversions each will NOT exit learning. One ad set getting 10 conversions WILL. Consolidation concentrates signals.

**The CPA x 50 Rule:**
- Minimum weekly budget per ad set = Target CPA x 50
- Minimum daily budget = (Target CPA x 50) / 7
- With the new 10-event threshold: (Target CPA x 10) / 7 = minimum daily budget

**Choosing optimization event by volume:**
- If purchase volume is too low, optimize for Add to Cart temporarily
- Add to Cart events happen far more frequently
- Switch to Purchase optimization once you have data/budget

**Data fidelity multiplies signal density:**
- Pixel + CAPI hybrid maximizes signal redundancy
- EMQ score improvement from ~8.6 to ~9.3 can reduce CPA by ~18%
- Server-side tracking helps hit the event threshold faster

Sources: Silverback Strategies, ROASPIG, Code3, AdStellar.

---

### Kill vs Scale Decision Framework

**Kill Threshold:**

| Spend Level | CPA Result | Action |
|---|---|---|
| Less than 1x target CPA | No conversion | Too early. Wait. |
| 1x-2x target CPA | No conversion | Concerning. Monitor closely. |
| 2x-3x target CPA | No conversion | Prepare to kill. 24 more hours max. |
| 3x+ target CPA | No conversion | **Kill immediately.** |
| Any spend | CPA below target | Winner. Prepare to scale. |
| Any spend | CPA 1-1.5x target | Potential. Continue testing. |
| Any spend | CPA 1.5-2x target | Marginal. Test iterations. |
| Any spend | CPA 2x+ target | Kill or significantly iterate. |

**Stability requirement before scaling:** Minimum 5 consecutive days of stable performance (within 10% of target CPA). Do NOT scale a 1-2 day winner.

**Minimum data before any decision:** At least 1,000+ impressions, 20+ link clicks, ideally 3+ conversions before declaring a winner.

Sources: AdStellar, Crunchy Digital, Cropink, Cody Plofker.

---

### Scaling — Vertical vs Horizontal

**Vertical (going deeper):**
- Increase budget by no more than 15-20% every 3-4 days
- Wait 3 full days minimum between increases
- Only scale ad sets stable for 7+ days
- Never scale during learning phase
- Use CBO for vertical scaling

**Why performance drops when you scale too fast:** Budget increases >20% can reset learning. The algorithm explores broader (lower-quality) segments. CPA spikes 25-40%.

**Horizontal (going wider):**
- Duplicate winning ad sets with modified targeting (new lookalike %, broader interests, new geos)
- New creative angles for the same product
- New campaign types (add ASC alongside manual)

**When to switch from vertical to horizontal:** Rising CPA despite stable creative, frequency above 2.5, declining CTR.

**Combined approach:**
1. Validate: Find 1-2 profitable ad sets via ABO testing
2. Vertical scale: 15-20% increases every 3-4 days
3. Horizontal scale when vertical hits ceiling
4. Repeat: Winners from horizontal get vertically scaled

Sources: AdBid, Jon Loomer, Lebesgue, Admetrics, TheOptimizer, Silver Spoon Agency.

---

## PART 5: TARGETING IN THE ANDROMEDA ERA

### The Landscape Has Shifted

The old playbook of stacking 5-10 interests per ad set is effectively dead:
- iOS 14.5+ destroyed behavioral data interest targeting relied on
- Meta's June 2025 update removed many specific interests
- Detailed targeting exclusions sunset for new campaigns
- Advantage+ Audience now treats interests as suggestions, not constraints

**Broad targeting paired with strong creative and first-party data signals is outperforming interest targeting for most advertisers.**

Meta's own data: Advantage+ audiences cut CPA by up to 32% compared to traditional interest targeting. 65% of US advertisers now use Advantage+ as their primary growth engine.

### When Interest Targeting Still Makes Sense

1. Brand new accounts with zero conversion history (algorithm has no signals)
2. Very small budgets where broad might waste spend
3. Niche markets with clearly identifiable interest categories
4. As "suggestions" within Advantage+ Audience — starting signals, not constraints

### Practical Strategy for New Accounts

**Week 1-2:** Advantage+ Audience with 2-3 relevant interest suggestions (health supplements, anti-aging, wellness). Age 40+, US.

**Week 3+:** Test fully broad (age + location only) against interest-suggested ad sets. Let data decide.

**Month 2+:** Likely migrate to primarily broad, as pixel/CAPI data become the dominant targeting signals.

Sources: Turba Media, Lebesgue, FanIQ, Cropink, WordStream.

---

## PART 6: CREATIVE — THE SINGLE BIGGEST LEVER

### "Creative Is the New Targeting" — The Numbers

- 70-80% of Meta ad performance now stems from creative quality, not budget or targeting (AppsFlyer 2025)
- 56% of all action outcomes are attributable to creative factors alone (Meta's own data, citing Nielsen)
- The remaining ~20-30% comes from campaign settings, audience configuration, and bid strategy

Each ad concept acts as its own audience selector. A video about afternoon energy crashes will find the 3pm Wall Hitter. A testimonial about perimenopause fatigue will find The Invisible Woman. You don't need to micro-target — you need creative that speaks to them.

Nick Shackelford ($200M+ managed spend): "Audience marketing is nearly dead and creative is almost all that matters." Brands that looked genuinely different saw a 32% performance jump and reached 9% more people.

Sources: Social Media Examiner, Nest Commerce, Engineering at Meta, Foxwell Digital, Kynship.

---

### How Engagement Affects Delivery Cost

The relationship is direct and mechanical:
- High engagement → higher EAR → higher Total Value → win impressions at lower prices → lower CPM compounds across entire campaign
- Low engagement → lower EAR → lower Total Value → pay MORE to win same impressions

**CTR below ~0.9%** = the algorithm effectively "taxes" you with higher CPMs.

**The 3-second threshold:** If your ad doesn't capture attention in 3 seconds, Meta deprioritizes it almost immediately. This is the earliest signal the algorithm uses to decide scale or kill.

**Diagnostic framework:**
- High CPC + Low CTR = creative isn't resonating
- CTR drop + frequency above 3-4 = ad fatigue
- Strong CTR + low conversions = landing page problem, not ad problem

Sources: WordStream, Affect Group, Growth-Onomics.

---

### Static vs Video vs Carousel

**Video (especially Reels):**
- 52% more engagement than static
- 42% higher ROAS than image ads
- Reels with curiosity-driven hooks + burned-in subtitles: 44% higher CTR

**Carousel:**
- Outperforming single-image by 27% in 2025
- Dynamic catalog carousels far outperform static carousels
- Excellent for mid-funnel education (ingredients, benefits, transformation)

**Static images:**
- Still drive 60-70% of conversions on Meta — do not abandon
- Best at bottom of funnel ("final call," price/offer focused)
- 4:5 vertical outperforms 1:1 square by up to 15% in Feed

**The real answer: mixed format wins.** Over-indexing on any single format = faster fatigue and rising CPMs.

- Top of funnel: Reels/video (awareness, storytelling)
- Mid-funnel: Carousels (education, ingredient breakdowns, social proof)
- Bottom of funnel: Static images (offers, urgency, direct response)

Sources: DeepSolv, Lion Media, Billo, Dataslayer.

---

### Native/UGC vs Polished — The Data Is Overwhelming

- UGC-based ads deliver 4x higher CTR and 50% lower CPC than branded/polished ads
- 92% of consumers trust UGC more than traditional advertising
- UGC ads are 31% more memorable
- DTC brands saw 38% higher ROAS with UGC overlaid with benefit-first text vs plain talking-head UGC

**Barry Hott ($600M+ in social ad spend for AT&T, Toyota, AG1, Harry's):** "Go watch what your audience is watching and make s*** that looks like that. That's it. Game over." His "ugly ads" approach consistently outperforms polished production. Client reports: 72% ROAS increase and 90% revenue increase after shifting to UGC-style.

**2025 evolution:** Not all UGC performs equally anymore. The old scripted "OMG I just tried this product" formula has become predictable. What works now:
- Value-first, feed-native formats (skits, expert commentary, pattern-interrupt)
- Content that provides upfront value — viewers learn something from the ad
- Selfie videos, off-the-cuff voiceovers, natural lighting
- Education-based approach that looks wildly different from the formula

**Dara Denney's key insight:** The biggest shift is brands finding success with content-first, education-based creative. The differentiator: customers gain upfront value from the ad itself.

Sources: Showcase, Zeely, Taggbox, Billo, Foxwell Digital, Building Ads with Barry.

---

### Hook Rate — The Single Most Important Early Creative Metric

**Formula:** Hook Rate = (3-second video views / total impressions) x 100

**Why it matters for delivery:**
- It's the earliest signal Meta uses to evaluate creative quality
- Ads with high hook rates get tested more aggressively by the algorithm
- Ads with low hook rates get deprioritized even if they would convert when forced
- CPMs drop 30-40% when hook rates improve

**Benchmarks:**
- Above 35%: Strong
- 25-35%: Decent but room for improvement
- Below 25%: Rework your opening immediately
- Reels benchmarks are 5-10 points lower

**Paired metric — Hold Rate:** Hook rate = stopped the scroll. Hold rate (ThruPlays / 3-second views) = kept them watching. You need both.

Sources: Five Nine Strategy, Great Marketing AI, Vaizle, Motion, Affect Group.

---

### Creative Fatigue — How to Identify and Manage It

**Meta's own data:** CTR drops 41% after an ad has been shown to the same user more than 4 times. Conversion rate drops 60%.

**Five signals (monitor simultaneously):**

| Signal | Threshold |
|--------|-----------|
| CTR decline | 20% drop from baseline |
| CPM increase | 30% week-over-week |
| Frequency | Above 2.5-3.0 for prospecting |
| CPA increase | 15-25% above target |
| Quality/Engagement Diagnostics | Hits "Below Average" |

**True fatigue = multiple signals declining simultaneously.** A single metric dipping is often noise.

**The 70% Rule:** When performance drops to 70% of peak, start testing new creative. Don't wait for complete failure.

**Refresh cadence:**
- Cold prospecting: every 2-3 weeks
- Retargeting: every 4-6 weeks
- High-budget: rotate weekly or run multiple simultaneously
- Build creative "angles" (different motivations/objections) rather than cosmetic refreshes. New value propositions outperform cosmetic refreshes by 2x+ (HubSpot 2025).

Sources: Analytics at Meta, Meta Business Help Center, DeepSolv, Revel Interactive, inBeat, Madgicx.

---

### Creative Diversity — The Andromeda Tax

Meta's system literally penalizes lack of creative diversity with higher CPMs — a "monotony tax."

- Meta's visual recognition detects when ads with slightly different text overlays are essentially the same image
- After 4 exposures to the same ad, conversion probability drops ~45%
- Accounts feeding 10-15 unique creative types per campaign see CPM compression and steadier delivery

**Volume vs true diversity (critical distinction):**
- Creative iteration (changing the hook on the same concept) is NOT the same as creative variation (changing the entire concept)
- Minor tweaks don't count as diversity to the algorithm
- You need concept-level diversity — genuinely different visual approaches, messaging angles, formats, styles

**Recommended mix:** Static + short-form video + Reels + carousels. UGC + founder content + product-focused + lifestyle + testimonial. Different pain points, different visual styles.

Different persona-targeted creatives in the same campaign let Andromeda find different audiences through each ad, effectively broadening reach without broadening targeting.

Sources: Reshift Media, Foxwell Digital, Jon Loomer, SuperAds, Motion, Admetrics.

---

### The 80/20 of Creative — What Actually Moves the Needle

**Hierarchy of impact:**
1. **Creative concept/angle** — ~70-80% of results
2. **Offer/pricing** — significant but secondary
3. **Audience/targeting** — largely handled by algorithm now
4. **Copy/headline** — matters but less than visual
5. **Campaign settings/structure** — ~20-30% of results

**The single highest-leverage element: The hook (first 3 seconds).** If you can only improve one thing, improve your opening.

**What does NOT move the needle much:**
- Micro-targeting audience segments
- Minor copy variations on the same visual
- Overly polished production value (often hurts more than helps)
- Complex campaign structures with many ad sets

**Budget allocation:** 80% of spend on proven winning creative, 20% on testing new creative.

Sources: Billo, AskNeedle, Kynship, Anchour.

---

## PART 7: TRACKING INFRASTRUCTURE

### CAPI — Why It's Non-Negotiable

Browser-based tracking (Meta Pixel alone) is now missing 40-60% of conversions due to iOS privacy changes, Safari ITP, ad blockers, and cookie restrictions.

CAPI sends conversion data directly from your server to Meta, bypassing all browser-side restrictions.

**Impact:** Pixel + CAPI together track ~95% of conversions vs 60-70% with Pixel alone. Some report up to 30% ROAS improvement after implementing CAPI.

**How CAPI improves CPA:**
1. Better optimization signals — can't optimize for purchases it can't see
2. Improved audience building
3. Accurate learning phase — 50-conversion threshold counts faster
4. Better Event Match Quality

**Setup for Shopify (do this first):**
1. Install "Facebook and Instagram" app from Shopify App Store
2. Connect Business Manager, pixel, and page
3. Enable Automatic Advanced Matching
4. Set data sharing to "Maximum" — this activates CAPI
5. Remove manually installed pixel code to avoid duplication

Setup time: 15-30 minutes. Free. Good enough for stores under $5K/month on Meta.

**Event Match Quality (EMQ):** Check in Events Manager. Below 6.0 = significant signal loss. Above 8.0 = excellent.

Sources: Meta for Developers, Meta Business Help Center, Triple Whale, wetracked.io, Ingest Labs, Elevar.

---

### Attribution Windows

**Use 7-day click + 1-day view** for your purchase campaigns. This is Meta's default and the right choice for a $50 health supplement targeting adults 40+ who research before buying.

Set up custom columns showing both 1-day and 7-day attribution side by side. If 7-day shows 100 conversions and 1-day shows 60, that means 40% of conversions happen between day 2 and day 7. Optimizing on 1-day alone would miss nearly half your impact.

Sources: Foreplay, Jon Loomer, Madgicx, Foxwell Digital, Dataslayer.

---

## PART 8: MYTHS vs REALITY — QUICK REFERENCE

| Claim | Verdict | Why |
|-------|---------|-----|
| "Run engagement/traffic first to train the algorithm for purchases" | MYTH | Algorithm optimizes for selected objective. Engagement finds engagers, not buyers. |
| "You must wait 30 days before running ads on a new account" | MYTH | Overly cautious. Clean creative + gradual budget = fine within days. |
| "Low CPM = good performance" | MYTH | Cheap impressions that don't convert = wasted money. |
| "Narrow targeting = lower CPM" | MYTH | Opposite is true. Narrow = more auction pressure. |
| "Engagement bait lowers CPM" | MYTH | Meta penalizes it. Tanks quality score. |
| "Account trust score exists" | PARTIALLY TRUE | The effect is real (established accounts get better delivery), but Meta hasn't confirmed a specific scoring system. |
| "CTR below 0.9% triggers a CPM penalty" | DIRECTIONALLY TRUE | Specific threshold may be approximate, but low CTR = higher effective CPM is consistent with auction mechanics. |
| "Creative is 70-80% of performance" | TRUE | Confirmed by AppsFlyer, Meta/Nielsen, and every credible media buyer. |
| "Gradual budget scaling matters" | TRUE | Every credible source agrees. 20% increments every 2-4 days. |
| "CAPI is essential" | TRUE | Missing 40-60% of conversions without it. |
| "Broad targeting beats interest targeting" | MOSTLY TRUE | In 2025-2026 with Andromeda, yes for most advertisers. Exception: brand new accounts may benefit from interest suggestions initially. |
| "The 1,000 exits from learning phase benchmark" | NOT CONFIRMED | Not in any Meta documentation. May be a rule-of-thumb for overall pixel maturity, but not an official threshold. |

---

## PART 9: FLAGGED — SINGLE-SOURCE OR UNVERIFIED CLAIMS

These appeared in research but could only be confirmed by one source:

1. **"User Value is scored 1-10"** — Referenced by Marin Software and a few media buyers, but not confirmed in Meta's official docs.
2. **"Account trust score"** — Widely referenced by agency account resellers but never publicly confirmed by Meta.
3. **"CTR below 0.9% triggers a CPM penalty"** — Multiple media buyers reference this but not Meta's official docs. The directional claim is consistent with mechanics.
4. **"20-30% of conversions are lost to iOS/browser blocking"** — Directionally supported post-iOS 14.5, but exact percentage varies by source and vertical.
5. **"HiVA Score"** — Confirmed by multiple industry sources to exist, but Meta does not publicly document it or its formula.

---

## APPLIED: WHAT THIS ALL MEANS FOR BASELINE NMN

### Your Situation
- New ad account, ~$42.98/day spending limit, ~$13 in total spend
- DTC supplement, $49.99 USD price point
- Target: 40+ US adults
- Running through Sarah Lawson's partner page
- Shopify store
- Engagement campaigns running since March 14

### What's Working For You Already
1. **Engagement campaigns are building real account warm-up** — payment history, billing threshold increases, clean ad record, account quality signals. This is not wasted money from an account health perspective.
2. **Q1 timing** — You're launching in the cheapest quarter for CPMs. This is the best time to be building data.
3. **Native/camouflage style through Sarah's page** — This is exactly the creative format delivering 4x CTR and 50% lower CPC vs polished brand ads. You're aligned with the winning strategy.

### What to Do When You Launch Purchase Campaigns

**Infrastructure (do before launching):**
- Set up CAPI via Shopify's native integration (Maximum data sharing, Advanced Matching ON). 15-30 minutes. Free. Non-negotiable.
- Check your EMQ score in Events Manager. If below 6, investigate.

**Campaign structure:**
- 1 ABO campaign (not CBO — at $50/day, CBO has nothing meaningful to distribute)
- 2 ad sets, 3 ads each (your best 6 from B1-B3)
- Advantage+ Audience with age 40+ US, 2-3 interest suggestions (health supplements, wellness, anti-aging)
- 7-day click + 1-day view attribution

**Optimization event:**
- Consider starting with Add to Cart optimization instead of Purchase. At $50/day with a ~$40 CPA, you'll get ~8 purchases/week — short of the 50-event threshold (though the new 10-event threshold helps). Add to Cart happens more frequently, giving the algorithm more signals faster.
- Switch to Purchase optimization once data builds.

**Launch protocol:**
- Set it and DO NOT TOUCH IT for 5-7 days. No budget changes, no creative swaps, no targeting tweaks.
- Accept that week 1 CPMs and CPAs will be high. This is the learning phase tax. It is expected.
- Focus on relative performance between the 9 ads, not absolute costs. The high CPMs affect all ads equally, so they don't distort your avatar/angle test.

**Decision framework:**
- Kill at 3x target CPA with zero conversions
- Scale after 5+ days of stable CPA
- Budget increases: 15-20% every 3-4 days only
- Frequency above 2.5 = start preparing new creative

**The biggest lever at your budget level is creative quality, not campaign structure.** Every credible source converges on this. A great ad at $50/day will outperform a mediocre ad at $500/day. Your camouflage-style ads are directionally correct.

### The Patience Factor
Your engagement campaigns building payment history → spending limit increases → launch purchase campaigns when limit hits $50+ → accept learning phase tax → let data accumulate → make decisions at day 7, not day 1 → scale gradually.

The advertisers who fail at this stage are the ones who panic-edit their campaigns every 24 hours. The algorithm needs time and data. Give it both.
