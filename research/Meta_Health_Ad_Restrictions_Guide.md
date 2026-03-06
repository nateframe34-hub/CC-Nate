# Meta Health & Wellness Ad Restrictions — Baseline NMN Action Guide

> **What this is:** A comprehensive breakdown of how Meta's 2025-2026 health and wellness advertising restrictions affect your NMN supplement launch, with specific actions to take before spending $1 on ads.
>
> **Why this matters:** Your Media Buying Plan is built around purchase-optimized campaigns. Meta may block that optimization entirely for health/wellness brands. If you launch without checking, you'll waste budget on a campaign that can't learn.
>
> **Bottom line:** This is manageable — but you need to check your classification and potentially adjust your campaign structure BEFORE launch.

---

## PART 1: HOW META CLASSIFIES YOUR BRAND

### The Classification System

Meta uses a **three-tier restriction system** for health and wellness advertisers. Your tier determines what you can and can't do.

| Tier | What's Restricted | Who Gets This |
|------|-------------------|---------------|
| **Tier 1 (Core Setup)** | Custom parameters and URL parts blocked from being shared with Meta. Custom audiences may shrink. UTM parameters beyond domain stripped. | General wellness brands, fitness equipment, non-condition-specific supplements |
| **Tier 2 (Mid-Restricted)** | Purchase and Add to Cart events blocked for optimization. Must use Landing Page Views or Engagement instead. Custom/lookalike audiences restricted. | Supplements making condition-adjacent claims, vitamins targeting specific health issues |
| **Tier 3 (Full Restriction)** | ALL events restricted. Essentially blind advertising. | Patient portals, telehealth, prescription-adjacent, condition-specific treatment brands |

### How Meta Decides Your Tier

Meta uses **multiple automated signals** — not just one:

1. **Website & Landing Page Scanning:** Meta's systems crawl your Shopify store and PDP. If they find health-condition language (disease names, symptom-specific claims, medical terminology), you get classified higher.

2. **Pixel & CAPI Event Payloads:** When your pixel fires with product names like "NMN Anti-Aging Supplement" or "NAD+ Cellular Repair," Meta reads those product names. Condition-implying product names trigger classification.

3. **URL Parameters:** If your URLs contain health-related terms (e.g., `/products/nmn-anti-aging-supplement` or `?utm_campaign=cellular-repair`), Meta reads those too.

4. **Ad Copy & Creative:** Health claims in your ads feed the classification algorithm. More clinical language = higher classification risk.

5. **Product Category in Shopify:** Your Shopify product type and Google product category (if set) influence Meta's classification.

### What Tier Will Baseline NMN Get?

**Most likely: Tier 1 (Core Setup) or Tier 2 (Mid-Restricted).**

Here's why:

**Arguments for Tier 1 (best case):**
- NMN is a general dietary supplement, not a prescription or condition-specific treatment
- NMN was confirmed as a lawful dietary supplement in September 2025 — it's a food supplement, not a drug
- Your brand positioning is "cellular energy support" not "disease treatment"
- Your PDP language uses "supports" not "treats" or "cures"
- A Meta rep was quoted saying "most health supplement brands will not be affected, unless it is a prescription or for a specific disease"

**Arguments for Tier 2 (probable case):**
- Your product name contains "NMN" which Meta's scanner may associate with anti-aging/longevity (health condition adjacent)
- Your PDP discusses NAD+ decline, cellular aging, energy restoration — language that Meta's automated scanner may flag
- The competitive analysis shows ProHealth Longevity and Cymbiotika ARE actively running purchase-optimized NMN campaigns (400+ days for Cymbiotika), which suggests NMN brands CAN get Tier 1 classification — but this isn't guaranteed

**Arguments against Tier 3 (almost certainly not):**
- You're not a patient portal, telehealth provider, or prescription product
- You don't collect medical data
- NMN is an OTC dietary supplement

---

## PART 2: WHAT EACH TIER MEANS FOR YOUR CAMPAIGN

### If You're Tier 1 (Core Setup) — Best Case

**What changes:**
- Custom parameters and URL parts are stripped from data sent to Meta
- Your UTM parameters won't be visible to Meta's optimization algorithm
- Custom audiences may be slightly smaller

**What stays the same:**
- You CAN optimize for Purchases ✅
- You CAN use Add to Cart as an optimization event ✅
- You CAN build lookalike audiences (with some data reduction) ✅
- You CAN use CAPI ✅
- You CAN use Advantage+ Shopping ✅
- You CAN retarget website visitors ✅

**Impact on your Media Buying Plan: Minimal.** The purchase-optimized CBO campaign structure works as designed. You just can't rely on UTM-based attribution as heavily. Use Meta's built-in attribution window (7-day click, 1-day view) instead.

### If You're Tier 2 (Mid-Restricted) — Probable Case

**What changes — THIS IS THE BIG ONE:**

| Capability | Status | Impact |
|-----------|--------|--------|
| Optimize for Purchase | ❌ BLOCKED | Can't tell Meta to find buyers. Must use upper-funnel events. |
| Optimize for Add to Cart | ❌ BLOCKED | Same — Meta can't see or optimize for cart events. |
| Optimize for Landing Page Views | ✅ ALLOWED | Your best alternative optimization event. |
| Optimize for Engagement | ✅ ALLOWED | Good for content-style ads (camouflage format). |
| Optimize for Link Clicks | ✅ ALLOWED | Weaker signal than LPV but available. |
| Optimize for Lead (Lead Gen forms) | ✅ ALLOWED | Useful if you add an email capture quiz funnel. |
| Custom Audiences (email lists) | ⚠️ RESTRICTED | May work but with reduced match rates. |
| Custom Audiences (website visitors) | ⚠️ RESTRICTED | Retargeting capability reduced. Audiences may be smaller. |
| Lookalike Audiences | ⚠️ RESTRICTED | Can't build lookalikes from purchase data. Can build from engagement data. |
| CAPI (Conversions API) | ⚠️ LIMITED | Server-side data restricted. Can still send some events but Meta may not use them for optimization. |
| Advantage+ Shopping | ❌ LIKELY BLOCKED | A+ Shopping relies on purchase optimization. Without it, A+ can't function as designed. |
| Broad Targeting | ✅ ALLOWED | Age, gender, geo targeting still works. |
| Interest Targeting | ⚠️ REDUCED | Health-related interests removed. General interests still available. |

**Impact on your Media Buying Plan: Significant but workable.** You need to restructure the campaign.

### If You're Tier 3 (Full Restriction) — Unlikely

All events blocked. You'd essentially be running blind — optimizing for impressions only. This would require a fundamentally different strategy (brand awareness only, driving to email capture outside of Meta's tracking). **This is unlikely for an NMN supplement brand but check to be sure.**

---

## PART 3: HOW TO CHECK YOUR CLASSIFICATION (Do This Before Spending $1)

### Step-by-Step Classification Check

**Before you launch any paid campaign, do this:**

1. **Set up your Meta Pixel + CAPI on Shopify** (you need these installed to check)

2. **Go to Events Manager** in Meta Business Suite
   - Click on your pixel/data source
   - Go to **Settings** tab
   - Look for **"Data Source Category"** or **"Business Category"**
   - If it says "Health and Wellness" → you've been classified
   - If it shows nothing → you may not be classified yet (but this can change after your first ad submission)

3. **Check for restriction notifications:**
   - Meta sends emails and in-platform notifications when they classify you
   - Check your Meta Business Suite notification center
   - Check the email associated with your Business Manager account

4. **Run a test before your real campaign:**
   - Create a test campaign (don't publish it yet)
   - Set the optimization event to "Purchase"
   - If Meta lets you select it without warnings → you're likely Tier 1
   - If you get an error or warning saying this optimization isn't available → you're Tier 2+

### If You're Classified as Health & Wellness

**Option A: Appeal the classification**
- File an appeal through Events Manager → Settings → Business Category → Request Review
- Argument: "We sell a general dietary supplement (NMN) that supports overall wellness. We are not a healthcare provider, do not collect medical data, and our product is not a prescription or condition-specific treatment."
- Timeline: 3-7 days for initial review, up to 30 days for complex cases
- Success rate: Mixed — Meta has final discretion. Worth trying but don't count on it.

**Option B: Reduce your classification risk** (do this BEFORE the appeal or BEFORE your first ad submission)
- Review your Shopify product name — change "NMN Anti-Aging Supplement" to "NMN Cellular Support" or just "Baseline NMN"
- Review your PDP for medical terminology — replace "aging," "decline," "restoration" with softer wellness language where possible
- Check your URL slugs — avoid `/products/anti-aging-nmn` → use `/products/baseline-nmn`
- Review your Google product category in Shopify — set it to "Health & Beauty > Vitamins & Supplements" (general), not anything condition-specific
- Strip health-condition keywords from your meta descriptions and alt tags

**Option C: Adapt your campaign structure** (if classification sticks — see Part 4)

**Option D: Server-side data cleansing** (technical but powerful)
Use a middleware layer between Shopify and Meta to control exactly what data reaches Meta:
- Tools: Server-Side Google Tag Manager (free), CustomerLabs, Able CDP, or PixelFlow
- How it works: Intercepts your pixel/CAPI data, strips health-related product names, condition-specific URLs, and PHI-like parameters, then forwards only "safe" data to Meta
- Instead of sending `product_name: "NMN Anti-Aging Supplement"`, send `product_name: "Daily Wellness Capsule"` or just a SKU number
- **Critical Shopify note:** Shopify's default pixel integration automatically sends product names and categories in event payloads. If your product name contains health terms, Shopify is handing Meta the evidence to restrict you. A server-side intermediary fixes this regardless of what your product is named on the frontend.

---

## PART 3.5: WORKAROUND CAMPAIGN STRUCTURES (If Tier 2)

Before the full adjusted campaign structure, here are three proven workarounds that successful supplement brands use under Tier 2 restrictions:

### Workaround 1: Video Retargeting Funnel

This is the most reliable bypass for website retargeting restrictions:

```
STEP 1: Video Awareness Campaign
├── Objective: Engagement or Awareness
├── Optimization: ThruPlay (15+ second views)
├── Creative: Educational/storytelling video (not product pitch)
├── Targeting: Broad (40+, US)
├── Budget: 30-40% of total spend
└── Purpose: Build a retargetable audience that Meta CAN track
    (on-platform engagement is NOT restricted)

STEP 2: Traffic Retargeting Campaign
├── Objective: Traffic
├── Optimization: Landing Page Views
├── Audience: Custom audience of 50%+ video viewers from Step 1
├── Creative: Camouflage static ads (B1, B2v2, B3) with PDP link
├── Budget: 40-50% of total spend
└── Purpose: Drive warm, interested traffic to your store

STEP 3: Email Capture (Optional but Valuable)
├── Objective: Lead Generation
├── Format: Meta Instant Forms (on-platform — NOT affected by restrictions)
├── Offer: "Find your cellular age" quiz or "Free NMN guide"
├── Budget: 10-20% of total spend
└── Purpose: Build first-party email list for Klaviyo conversion
```

**Why this works:** Website visitor retargeting is restricted, but on-platform engagement audiences (video viewers, page engagers) are NOT restricted. By running a video first, you build a retargetable warm audience entirely within Meta's platform — then drive them to your store with a traffic campaign.

### Workaround 2: Lead Form → Email Nurture

Meta's on-platform Instant Forms are completely unaffected by health/wellness restrictions:
- Run a Lead Generation campaign with an Instant Form
- Offer something valuable: "Free guide: The NAD+ Science Explained" or "Take the Cellular Energy Quiz"
- Capture name + email directly on Facebook/Instagram
- Import leads into Klaviyo automatically (Meta → Zapier → Klaviyo)
- Nurture with your email welcome sequence → convert off-platform

This bypasses ALL pixel/tracking restrictions because the lead capture happens on Meta's own platform, not your website.

### Workaround 3: First-Party Data Loop

Build a self-reinforcing cycle that doesn't depend on Meta's pixel:
1. Run traffic/engagement ads (allowed under all tiers)
2. Capture emails via popup on your PDP (use Klaviyo or Privy)
3. Upload email list back to Meta as a custom audience (still allowed)
4. Build lookalike audiences from your email list (still allowed)
5. Run traffic ads to the lookalike audience
6. Repeat — each cycle makes your custom audience and lookalike more refined

---

## PART 3.6: ENFORCEMENT TIMELINE

Understanding when each restriction hit helps predict what's coming:

| Date | What Happened |
|------|---------------|
| **Nov 2024** | Meta sent initial notifications to impacted advertisers about upcoming categorization |
| **Dec 2024** | Specific classification notices sent. Appeal window opened. |
| **Jan 6, 2025** | "Request more time" button appeared in Events Manager (30-day extension, available for 7 days) |
| **Jan 13-20, 2025** | **Wave 1 enforcement:** Lower-funnel event restrictions (Purchase, Add to Cart) went live for flagged brands |
| **Feb 14, 2025** | Full enforcement for brands that didn't request extensions |
| **Mar 2025** | Detailed targeting exclusions removed for ALL advertisers (not just health) |
| **Throughout 2025** | Enforcement expanded to custom audiences and lookalikes built from restricted data. Interest targeting options consolidated and retired. |
| **Sep 2, 2025** | Meta began **proactively scanning and disabling** custom audiences and conversion events referencing protected health attributes — even previously approved ones |
| **Jan 15, 2026** | Consolidated interest targeting fully enforced |
| **Early 2026 (expected)** | **Wave 2:** Expected to restrict Lead, Schedule, and CompleteRegistration events. May expand "sensitive data" classification to appointment booking pages. |

**Trajectory:** Restrictions are getting **actively stricter**, not stabilizing. Industry sources report a **30-40% drop in ad efficiency** for affected health brands since Wave 1. Meta's motivation is FTC settlements (BetterHelp, GoodRx in 2023) and lawsuits over health data sharing via Meta Pixel. This regulatory pressure is not going away.

**What this means for your timing:** Launch sooner rather than later. Wave 2 (early 2026) may restrict Lead events, which would break Workaround 2 (Lead Form → Email Nurture). Getting your account established, your pixel warmed, and your first-party list built NOW gives you a foundation before the next restriction wave hits.

---

## PART 4: ADJUSTED CAMPAIGN STRUCTURE (If Tier 2)

If you're classified Tier 2, here's how to restructure your Media Buying Plan:

### Original Plan (Purchase Optimized)
```
CAMPAIGN: Baseline NMN — Avatar Discovery (CBO)
├── Budget: $50 CAD/day
├── Optimization: Purchases ← BLOCKED IF TIER 2
├── Attribution: 7-day click, 1-day view
```

### Adjusted Plan (Landing Page View Optimized)
```
CAMPAIGN: Baseline NMN — Avatar Discovery (CBO)
├── Budget: $50 CAD/day
├── Optimization: Landing Page Views ← REPLACEMENT
├── Attribution: 7-day click, 1-day view
│
├── AD SET 1: Batch 1 — The Reluctant Decliner
│   ├── Targeting: Broad (40+, US)
│   ├── Creative 1: B1C1
│   ├── Creative 2: B1C2
│   └── Creative 3: B1C3
│
├── AD SET 2: Batch 2 — The 3pm Wall Hitter (REBUILT)
│   ├── Targeting: Broad (35+, US)
│   ├── Creative 1: B2C1 (new)
│   ├── Creative 2: B2C2 (new)
│   └── Creative 3: B2C3 (new)
│
└── AD SET 3: Batch 3 — The Burned Supplement Buyer
    ├── Targeting: Broad (35+, US)
    ├── Creative 1: B3C1
    ├── Creative 2: B3C2
    └── Creative 3: B3C3
```

### Why Landing Page Views > Link Clicks > Engagement

| Event | Signal Quality | Why |
|-------|---------------|-----|
| **Landing Page Views** | Best available | Only counts when the page actually loads (not just clicks). Filters out bounces. Closest proxy to purchase intent. |
| **Link Clicks** | Medium | Counts all clicks, including accidental. Higher volume but lower quality signal. |
| **Engagement** | Lower for sales | Counts likes, comments, shares. Great for content virality but doesn't necessarily mean purchase intent. |

**Use Landing Page Views as your primary optimization event.** This is what most successful supplement brands under Tier 2 restrictions are doing.

### What Changes in Your Decision-Making

With purchase optimization, you track ROAS and CPA directly. Without it, you need proxy metrics:

| Metric | What It Tells You | Tier 2 Decision Rule |
|--------|-------------------|---------------------|
| **CTR (Click-Through Rate)** | Which creative stops the scroll and drives clicks | >1.5% = good creative. <0.8% = kill it. |
| **CPC (Cost Per Click)** | How efficiently you're driving traffic | <$1.50 CAD = healthy. >$3.00 = creative fatigue or wrong audience. |
| **Landing Page View Rate** | What % of clickers actually see your PDP | >70% of clicks = good page speed. <50% = page load issue. |
| **On-Site Conversion Rate** | Track in Shopify analytics, not Meta | >2% = PDP is working. <1% = PDP or offer problem. |
| **Add to Cart Rate** | Track in Shopify analytics, not Meta | >5% of visitors = strong intent. Use this as your internal "purchase proxy." |
| **Purchases** | Track in Shopify, attribute manually | Use UTM parameters + Shopify analytics for attribution since Meta can't track it. |

**Critical:** With Tier 2, your Shopify analytics become your primary source of truth for conversion data, not Meta Ads Manager. Meta will show you clicks and landing page views. Shopify will show you actual sales.

### Attribution Workaround

Since Meta can't see your purchases, you need to attribute manually:

1. **UTM every ad:** Use unique UTM parameters for each ad set/creative
   - `?utm_source=meta&utm_medium=paid&utm_campaign=avatar-discovery&utm_content=B1C1`
2. **Track in Shopify:** Shopify Analytics → Marketing → shows which UTM sources drove sales
3. **Daily reconciliation:** Compare Meta spend per ad set vs Shopify revenue from that UTM source
4. **Calculate manual ROAS:** Shopify revenue from UTM ÷ Meta spend on that ad set = true ROAS

This is more work than pixel-based attribution, but it gives you accurate data.

---

## PART 5: WHY THIS ACTUALLY HELPS YOUR CREATIVE STRATEGY

Here's the counterintuitive truth: **Tier 2 restrictions make your camouflage ads MORE valuable, not less.**

### The Logic

When everyone optimizes for purchases, Meta's algorithm rewards ads that drive quick transactions — direct-response clinical claims, discount offers, product shots with "Buy Now." These ads win the purchase-optimization auction.

But when nobody in the health space can optimize for purchases, the algorithm optimizes for the next best signal: **Landing Page Views.** What drives landing page views? **Ads that people actually want to engage with.** Ads they stop scrolling for. Ads that feel like content, not commerce.

Your camouflage ads (B1, B3, B4) are built for exactly this. A clinical infographic from ProHealth gets scrolled past. A first-person story about a dad who was too tired to play catch gets read, clicked, and shared. Under purchase optimization, both approaches can work because Meta finds buyers regardless. Under landing page view optimization, only the engaging ad wins — and that's you.

### What This Means for Each Batch

| Batch | Purchase-Optimized Performance | LPV-Optimized Performance | Net Effect |
|-------|-------------------------------|--------------------------|------------|
| **B1** (Reluctant Decliner) | Good | **Excellent** — camouflage format drives curiosity clicks | ↑ Better under restrictions |
| **B2** (3pm Wall Hitter — rebuilt) | Good | **Excellent** — relatable formats drive engagement | ↑ Better under restrictions |
| **B3** (Burned Buyer) | Good | **Excellent** — trust angle drives investigation clicks | ↑ Better under restrictions |
| **B4** (Exhausted Parent) | Excellent | **Excellent** — emotional resonance drives clicks and shares | → Same either way |
| **B5** (Invisible Woman) | Medium (compliance risk) | Medium | → Same either way |

### Competitor Impact

**ProHealth Longevity's clinical infographic ads?** These perform well when Meta can optimize for buyers who respond to clinical claims. Under LPV optimization, they get fewer clicks because nobody stops scrolling for an infographic.

**Cymbiotika's 400+ day campaigns?** These likely work because Cymbiotika uses hybrid UGC + polished creative — engagement-friendly formats that work under any optimization. They probably adapted early.

**Your camouflage-format ads?** Purpose-built for engagement. Your structural advantage gets larger, not smaller, under these restrictions.

---

## PART 6: CREATIVE COMPLIANCE (What Gets Your Ads Rejected)

This supplements Part 3.5 of your Media Buying Plan. Here's the specific language and format guidance under current Meta policy:

### Claims That Get Rejected

| Category | Will Get Rejected | Safe Alternative |
|----------|-------------------|------------------|
| **Personal health assertions** | "Your cells are dying" / "Your body is broken" | "NAD+ levels naturally decline with age" |
| **Disease/condition claims** | "Reverses aging" / "Prevents Alzheimer's" | "Supports cellular health" |
| **Guaranteed outcomes** | "You WILL feel different" / "Guaranteed energy" | "Many people notice more consistent energy" |
| **Before/after implications** | "Look 10 years younger" / transformation imagery | Show the lifestyle outcome, not the physical transformation |
| **Negative self-perception** | "Are you tired all the time?" / "Feeling old?" | "What if feeling depleted isn't inevitable?" (reframe as possibility, not diagnosis) |
| **Second-person health status** | "Your energy is declining" / "You're aging faster" | "Energy levels can decline as we age" (third-person/general) |

### Special Rules for Your Creatives

**Testimonials:** Allowed, but they can't promise specific health outcomes. "I noticed more consistent energy by week three" = okay. "NMN cured my fatigue" = rejected.

**Before/after imagery:** Strictly prohibited for weight loss and anti-aging. Your B4 creative (parent playing with kids) is fine because it shows a lifestyle outcome, not a physical transformation. Don't show "tired vs energized" side-by-side of the same person.

**The "second person" trap:** Meta's Personal Attributes Policy flags ads that assert knowledge of a user's health status. "Your NAD+ is depleted" = flagged. "NAD+ naturally declines with age" = safe. Use "we" or third-person framing.

### Batch-by-Batch Compliance Notes (Updated)

| Batch | Risk | Specific Flags to Fix |
|-------|------|-----------------------|
| **B1** | Medium | B1 Body Copy 1: "your cells slowly running out of fuel" — change to "cells that may be running low on fuel." B1C1: "50% of your cellular fuel. Gone by 50." — change "your" to "our" or use third-person. |
| **B2** | Low | Energy/caffeine comparison is the safest angle. Avoid "your cells can't produce energy" — use "cells may produce less energy over time." |
| **B3** | Very Low | Trust/verification angle barely touches health claims. Safest batch. |
| **B4** | Medium | "You're not a bad parent. You're a depleted one." — the "you're depleted" is a personal health assertion. Reframe to "What if the exhaustion isn't about willpower — but cellular energy?" |
| **B5** | High | Any menopause/hormonal language will be flagged. "Perimenopause energy crashes" = immediate rejection. Must frame entirely around general wellness. |

---

## PART 6.5: NMN-SPECIFIC RISK FACTORS

NMN supplement brands face **elevated classification risk** compared to general supplements for several reasons:

### FDA Regulatory History

The FDA determined in late 2022 that NMN was **excluded from dietary supplement classification** due to prior investigation as a pharmaceutical drug (by Metro International Biotech/Sinclair). This created regulatory uncertainty that made NMN brands more visible to enforcement.

**However:** In September 2025, NMN was confirmed as a lawful dietary supplement, resolving this uncertainty. This is good news for your brand's legal standing — but Meta's classification systems may not have caught up. Meta's automated scanner likely still has "NMN" flagged from the 2022-2025 period when it was in regulatory limbo.

### Anti-Aging Positioning Risk

NMN is almost universally marketed around longevity, anti-aging, NAD+ replenishment, and cellular health. These are exactly the terms that push a brand from "general wellness" into "health/medical" classification:

| High-Risk NMN Language | Lower-Risk Alternative |
|------------------------|----------------------|
| "Anti-aging supplement" | "Daily wellness capsule" |
| "Reverses biological age" | "Supports cellular vitality" |
| "NAD+ restoration / cellular repair" | "Supports energy at the cellular level" |
| "NMN longevity supplement" | "Baseline NMN" (just the brand name) |
| "Fights aging at the molecular level" | "Supports your body's natural processes" |

### Science-Heavy Marketing Risk

NMN brands typically reference studies, biological mechanisms (NAD+, sirtuins, mitochondrial function), and aging-related outcomes. This language reads as medical to Meta's automated systems — even if it's technically structure/function claims.

**Recommendation:** Save the science for your email marketing, blog, and PDP education sections. On your Meta ad landing pages and in ad copy, lead with lifestyle benefits (daily vitality, consistent energy, feeling your best) rather than biological mechanisms. The science converts people who are already interested — but it can get your ads restricted before they reach those people.

### Practical Positioning Guidance

For Meta's classification system, you want to be seen as:

| Classification | Risk Level | Your Goal |
|---------------|-----------|-----------|
| General ecommerce | No restrictions | Ideal but hard to achieve for supplements |
| Beauty/cosmetic | Least restricted health category | Possible if you position around "cellular vitality" |
| **Wellness** | **Partially restricted** | **Most likely landing spot — plan for this** |
| Health/medical | Most restricted | Avoid — keep medical language off your domain |

---

## PART 7: LAUNCH CHECKLIST (Updated for Restrictions)

### Before Your First Ad Dollar

- [ ] **Check classification:** Events Manager → Settings → Data Source Category. Is it "Health and Wellness"?
- [ ] **If classified:** File appeal immediately. Don't wait for the result to continue setup.
- [ ] **Test purchase optimization:** Create a draft campaign with Purchase optimization. Does Meta allow it or throw an error?
- [ ] **Review Shopify product name:** Remove any condition-specific language. "Baseline NMN" is ideal.
- [ ] **Review PDP language:** Ensure "supports" not "treats/cures/fixes." Add FDA disclaimer.
- [ ] **Review URL slugs:** Remove anti-aging, cellular-repair, or condition-specific terms from URLs.
- [ ] **Set up UTM tracking:** Create unique UTMs for every ad set and creative variant.
- [ ] **Verify Shopify Analytics:** Confirm you can see traffic by UTM source in Shopify → Analytics → Marketing.

### Campaign Setup (Adapting for Classification Outcome)

**If NOT classified (Tier 0) or Tier 1:**
- Proceed with original Media Buying Plan — purchase-optimized CBO at $50/day
- Everything works as designed

**If Tier 2:**
- Switch optimization to Landing Page Views
- Set up manual attribution via UTM + Shopify Analytics
- Lean harder into camouflage creative (engagement-first ads)
- Monitor Shopify conversion rate as your primary success metric
- Add an email capture popup on your PDP (Klaviyo or Privy) — this becomes your retargeting channel since Meta website retargeting is restricted
- Consider the Video Retargeting Funnel (Part 3.5, Workaround 1) — run a video campaign first to build on-platform audiences, then retarget with traffic ads
- Consider Lead Form campaigns (Part 3.5, Workaround 2) — on-platform Instant Forms are NOT affected by restrictions. Capture emails directly on Meta, then convert via Klaviyo
- Set up server-side data cleansing (Part 3, Option D) — strip health-related product names from CAPI payloads before they reach Meta

**If Tier 3 (unlikely):**
- Pause Meta ads
- Build email list through organic content + lead magnet (quiz funnel, free guide)
- Use Google Ads (Shopping + Search) as primary paid channel — Google doesn't have these restrictions
- Return to Meta once you have a first-party audience to target

### Ongoing Monitoring

- [ ] **Weekly:** Check Events Manager for any new classification changes
- [ ] **Weekly:** Reconcile Meta spend vs Shopify revenue by UTM source
- [ ] **Bi-weekly:** Check for Meta notification emails about policy changes
- [ ] **Monthly:** Review if any new restriction tiers have been applied

---

## PART 8: ALTERNATIVE CHANNELS IF META RESTRICTS TOO HEAVILY

If Meta Tier 2 restrictions make CPA unsustainable, these channels don't have the same health/wellness restrictions:

| Channel | Restrictions | Best For | Estimated CPA vs Meta |
|---------|-------------|----------|----------------------|
| **Google Shopping** | Product listing standards only. No health-category optimization blocks. | High-intent buyers searching for NMN | Similar or lower CPA for branded/category search |
| **Google Search** | Can't claim disease treatment. Otherwise flexible. | "Best NMN supplement" searchers | Higher intent, comparable CPA |
| **TikTok Ads** | Less restrictive than Meta for supplements currently. UGC format native. | Younger 35-50 demo, viral potential | Higher volume, slightly higher CPA |
| **YouTube Ads** | Standard ad policies, no health-category blocks on optimization. | Educational/long-form content for warm audiences | Higher CPM but higher engagement |
| **Pinterest** | Wellness-friendly platform. Supplement ads allowed with general claims. | Women 40-55 (your biggest demo gap) | Lower CPM, longer conversion window |
| **Email (Klaviyo)** | No restrictions. You own the channel. | Retargeting, abandoned cart, education sequences | Best ROI once list is built |

**Priority if Meta is restricted:** Google Shopping + Search (captures high-intent buyers) → TikTok (captures broad awareness) → Email (captures and converts warm leads).

---

## Sources

Research compiled from:
- [Foxwell Digital — Sensitive Ad Categories: Meta's 2025 Rule Changes](https://www.foxwelldigital.com/blog/sensitive-ad-categories-changes-coming-to-meta-in-2025)
- [Triple Whale — Meta's Health and Wellness Restrictions: Policy Changes & Fixes](https://www.triplewhale.com/blog/meta-health-and-wellness-brands)
- [Digital Position — Meta's Restrictions on Health and Wellness Ads](https://www.digitalposition.com/resources/blog/ppc/metas-new-restrictions-on-health-and-wellness-ads-what-you-need-to-know/)
- [Shop2App — Meta Restrictions 2025: How New Healthcare Ad Policies Impact Brands](https://www.shop2app.com/blog/meta-restrictions-2025-how-new-healthcare-ad-policies-impact-brands)
- [Marketing Brew — Meta plans crackdown on health-related user data](https://www.marketingbrew.com/stories/2024/12/09/meta-plans-crackdown-on-health-related-user-data)
- [Polar Analytics — 2025 Meta's Tracking Restrictions For Health & Wellness](https://www.polaranalytics.com/post/2025-metas-tracking-restrictions-for-health-wellness-are-here----heres-how-to-fix-it)
- [Accelerated Digital Media — Guide to Social Media Health Ad Restrictions](https://www.accelerateddigitalmedia.com/insights/guide-to-social-media-health-ad-restrictions-2026/)
- [CustomerLabs — Meta's Health & Wellness Restrictions: The Guide](https://www.customerlabs.com/blog/meta-ads-restriction-health-wellness-workaround-solution/)
- [Tracklution — Navigating Meta Sensitive Ad Categories 2025](https://www.tracklution.com/learn/navigating-meta-sensitive-ad-categories-2025/)
- [GoInflow — How to Run Health Supplement Ads on Facebook](https://www.goinflow.com/blog/facebook-ads-health-supplements/)
- [Meta Transparency Center — Health and Wellness Ad Standards](https://transparency.meta.com/policies/ad-standards/restricted-goods-services/health-wellness/)
- [AdAmigo — Meta Ads Policy: Unapproved Health Claims Explained](https://www.adamigo.ai/blog/meta-ads-policy-unapproved-health-claims-explained)

---

*Guide prepared March 2026. Meta policies are subject to change — verify current status in Events Manager before launch.*
