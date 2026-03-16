# Baseline NMN — Master Launch Timeline

> **Updated March 16, 2026.** Timeline restructured around a **spend-gated launch trigger** instead of fixed calendar dates. Purchase ads go live when the ad account hits $100 USD in cumulative clean spend across warm-up campaigns — not on a predetermined day.

> **NOTE:** We are currently running **only the Baseline NMN 10-in-1** supplement. QR-to-COA verification is a **future feature** — not available on the current product.

> **Three pages in play:**
> 1. **Brand Page** (@baselinenmn) — official Baseline Instagram/Facebook
> 2. **Partner Page** (Sarah Lawson, @sarahlawson.wellness) — organic social proof engine
> 3. **Ad Partner Page** (generic health/wellness page) — camouflage ad delivery vehicle
>
> **Reference docs:** `Media_Buying_Plan.md`, `Ad_Batch_Plans_B1-B3.md`, `Organic_Post_Plan_Brand_Page.md`, `Partner_Page_Identity_and_Post_Plan.md`, `Ad_Partner_Page_Content_Plan.md`

---

## Launch Trigger (NOT a Calendar Date)

**Purchase ads go live when ALL of the following are true:**

1. **$100 USD cumulative clean spend across warm-up campaigns** — no policy violations, no rejected ads
2. **Infrastructure complete** — PDP live, pixel firing, email flows working
3. **9 ad creatives finalized** and compliance-checked
4. **All 3 pages have content** — not empty shells

That's it. No arbitrary waiting period. The $100 threshold is the gate.

### Dual Warm-Up Campaign Strategy

Run **two campaigns simultaneously** to warm the account. Both count toward the $100 threshold.

| Campaign | Objective | Budget | What It Does |
|----------|-----------|--------|--------------|
| **Engagement** (already running) | Page followers + post engagement | $5 CAD/day | Grows page, builds account trust |
| **Traffic** (launch when PDP is live) | Landing page views → PDP | $5-10 CAD/day | Warms the pixel with real visitor data (ViewContent, AddToCart events), tests audience response to PDP |

**Combined budget: $10-15 CAD/day** → hits $100 USD threshold in ~12-15 days.

**Why two campaigns instead of just engagement:**
- The engagement campaign warms the account but teaches the pixel nothing about your buyers
- The traffic campaign sends real people to your PDP — the pixel starts collecting ViewContent, AddToCart, and time-on-site signals
- When purchase ads launch, the pixel already has upstream data about who engages with your product page — it's not starting completely cold
- Each campaign optimizes for its own objective independently. The traffic campaign's "clicker" data does NOT contaminate the purchase campaign's optimization. Meta treats them as separate learners.

### Current Status

| Metric | Value | Updated |
|--------|-------|---------|
| Engagement spend to date | $6.83 USD | March 16, 2026 |
| Traffic campaign spend to date | $0 (not yet launched — needs PDP) | |
| **Total account spend** | **$6.83 USD** | |
| Spend remaining to threshold | ~$93 USD | |
| Policy violations | 0 | |
| Estimated days to threshold (engagement only, ~$3.40/day) | ~27 days | |
| Estimated days to threshold (both campaigns, ~$10 CAD/day) | ~12-15 days | |

> **Traffic campaign launches when PDP is live.** Until then, engagement runs alone. Once both are running, the threshold approaches roughly twice as fast.

---

## Phase 1: Infrastructure (Do Now — Parallel to Engagement Campaign)

Don't wait for the spend threshold. Build infrastructure while the engagement campaign runs.

| Task | Status | Notes |
|------|--------|-------|
| **Shopify PDP live** — built on Shrine Pro with all sections from `pdp-copy.md` | [ ] | |
| **FDA disclaimer on PDP** | [ ] | Required for supplement ads |
| **30-day money-back guarantee** — badge visible on PDP | [ ] | |
| **Shipping info on PDP** | [ ] | "Ships within 1-2 business days. Delivers in 3-7 business days." |
| **Meta Pixel + Conversions API (CAPI)** installed on Shopify | [ ] | |
| **Browse your own store** — generate ViewContent events | [ ] | |
| **Klaviyo/email platform** — welcome flow, abandoned cart, post-purchase | [ ] | |
| **10% welcome popup** live on store | [ ] | |
| **Product images finalized** — Nano Banana Pro prompts from `Ad_Batch_Plans_B1-B3.md` | [ ] | |
| **Brand Page** created (@baselinenmn) on Instagram + Facebook | [ ] | |
| **Sarah's Partner Page** created (@sarahlawson.wellness) | [ ] | |
| **Ad Partner Page** created on Facebook | [ ] | |
| **Ad Partner Page** added to Meta Business Manager | [ ] | |
| **9 ad creatives generated** — Nano Banana Pro + Canva edits | [ ] | |
| **Sarah's profile photo generated** | [ ] | |
| **Compliance check** — all 9 creatives + 9 body copies pass Meta health ad policy | [ ] | |

---

## Phase 2: Content Seeding (Start When Pages Are Created)

Post daily per existing content plans. The engagement campaign runs in parallel — these are independent tracks.

**The point of content seeding:** Pages should look established, not freshly created. Most people won't click the page from a native ad — but the few who do shouldn't see an empty shell.

| Page | Content Plan | Posting Cadence |
|------|-------------|-----------------|
| **Brand Page** | `Organic_Post_Plan_Brand_Page.md` | 5-6 posts/week |
| **Sarah's Partner Page** | `Partner_Page_Identity_and_Post_Plan.md` | 4-5 posts/week |
| **Ad Partner Page** | `Ad_Partner_Page_Content_Plan.md` | 3-4 posts/week |

Continue posting through and after ad launch. Don't stop organic content when purchase ads go live.

---

## Phase 3: Launch Prep (When Spend Approaches $100 USD)

When engagement spend hits ~$80 USD, start launch prep. You want everything uploaded and ready so you can flip the switch at $100.

| Task | Timing |
|------|--------|
| Upload all 9 ad variations to Meta Ads Manager | ~$80 spend |
| Set all ads to run through Ad Partner Page | ~$80 spend |
| Campaign structure: 1 CBO → 3 ad sets → 3 ads each | ~$80 spend |
| Budget: $50/day CBO across all 3 ad sets | ~$80 spend |
| Targeting: Broad — age + gender + US only | ~$80 spend |
| Optimization: Purchases | ~$80 spend |
| **Final PDP check** — load speed, links, FDA disclaimer, guarantee, pixel | ~$90 spend |
| **Final compliance check** — all 9 ads pass policy | ~$90 spend |
| **Email flows test** — test purchase, verify all sequences trigger | ~$90 spend |
| Set ads to **scheduled** | ~$95 spend |
| **GO LIVE** | $100 spend hit |

---

## Phase 4: Discovery (Day 0 to Day 28 After Launch)

### Week 1 (Day 0-7) — Hands Off

- B1-B3 purchase campaigns go live. $50/day CBO.
- **Do not touch anything for 7 days.** Resist the urge.
- Check Meta dashboard 1x/day max
- Continue organic posts across all 3 pages
- Reply to all comments/DMs daily

### Week 2 (Day 8-14) — First Read

| Action | Detail |
|--------|--------|
| **Read the data** | Which ad set is getting spend? Which ads have purchases? CTR vs. conversions? |
| Kill obvious losers | Ad with $0 purchases after $50+ spend and bad CTR — pause the ad (not the ad set) |
| Continue organic posting | Normal cadence across all 3 pages |

### Week 3-4 (Day 15-28) — Pattern Recognition

| Action | Detail |
|--------|--------|
| **Identify winning ad set** | One ad set should be getting majority of CBO spend + purchases |
| **Identify winning angle** | Within winning ad set, which angle converts best? |
| Continue organic content | Both pages ongoing |
| **Post-purchase survey** after 20+ sales | "How did you hear about us?" |
| Prepare Champion Ad Set brief | Winning sub-avatar + winning angle → 3 new format variations |

---

## Phase 5: Validation & Scale (Day 29+)

| Week | Action | Budget |
|------|--------|--------|
| Week 5 | Build Champion Ad Set — winning avatar + angle, new creatives in 3 formats | $75/day |
| Week 6 | Monitor Champion. If CPA holds, increase. | $75-100/day |
| Week 7-8 | Scale if data supports. Commission UGC video for winning angle. | $100-125/day |
| Week 9-10 | UGC video enters Champion Ad Set. Push toward learning phase exit. | $150-200/day |
| Week 10+ | Evaluate: Bundle & Save, price increase to $59.99, expand to new avatars. | Scale based on data |

---

## Critical Dependencies

These block purchase ad launch. If any are incomplete when spend hits $100, the launch waits.

| Dependency | Blocks | Status |
|-----------|--------|--------|
| PDP live on Shopify | All ad traffic | [ ] |
| Meta Pixel + CAPI installed | Purchase tracking | [ ] |
| 9 ad creatives finalized | Ad upload | [ ] |
| Ad Partner Page created + populated | All B1-B3 ads | [ ] |
| Partner page added in Business Manager | All B1-B3 ads | [ ] |
| Email flows connected | Post-purchase retention | [ ] |
| Sarah's profile photo generated | Partner page content | [ ] |
| Brand page profile/cover/bio set | Brand organic content | [ ] |
| **$100 USD clean account spend** (engagement + traffic) | **Account trust** | **$6.83 / $100** |

---

## Quick Reference

```
NOW ──────── Engagement campaign running ($6.83 USD spent)
             Build infrastructure in parallel
             Post organic content daily across all 3 pages

PDP LIVE ─── Launch traffic campaign → PDP ($5-10 CAD/day)
             Both campaigns now warming account + pixel

~$80 USD ─── Upload purchase ads to Meta, final prep
~$100 USD ── B1-B3 PURCHASE ADS GO LIVE ($50/day CBO)
             Pause traffic campaign (purchase campaign takes over)

Day 7 ────── First data read (no changes before this)
Day 14 ───── Kill losers, identify trends
Day 28 ───── Winner identified → Champion Ad Set
Day 35 ───── Champion live, begin scaling
Day 56 ───── UGC video enters rotation
Day 70 ───── Target: learning phase exit
```

---

*Launch gated by $100 USD total account spend (engagement + traffic), not calendar dates. Everything runs in parallel. The moment the account is warm and infrastructure is ready, purchase ads go live.*
