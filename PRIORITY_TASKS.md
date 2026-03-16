# 7-Day Work Plan — Building While the Account Warms

> **Updated:** March 16, 2026
> **Situation:** Engagement campaign running at ~$3.40 USD/day ($6.83 of $100 threshold). PDP is live. Ad Partner Page is live. All 3 pages have content. 9 creatives generated. Body copies written + compliance-checked. Sarah's page created.
>
> **What's left before purchase ads can launch:** Pixel + CAPI, traffic campaign, creative compliance check, Klaviyo flows, welcome popup, legal pages, campaign structure in Ads Manager.
>
> **Format:** 6-8 hours/day for 7 days. Check boxes on GitHub as you go.

---

## Day 1 — Pixel, Traffic Campaign & Legal Pages

*Get the two biggest blockers out of the way. Then handle legal pages so Meta doesn't flag your store during ad review.*

- [ ] **Install Meta Pixel + Conversions API (CAPI) on Shopify** (30-45 min)
  - Use Meta's official Shopify sales channel integration
  - Verify pixel fires on: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase
  - Test with Meta Pixel Helper Chrome extension
  - Browse your own store 5-10 times to seed initial ViewContent events

- [ ] **Launch the traffic campaign** (30 min)
  - $5-10 CAD/day → PDP (landing page views objective)
  - Broad targeting, 40+ US
  - This nearly doubles your spend rate toward $100 threshold (~12-15 days instead of ~27)
  - Pixel starts collecting real visitor data immediately

- [ ] **Build legal pages in Shopify** (1-1.5 hrs)
  - Privacy Policy (Settings → Policies → Create from template, customize per `Media_Buying_Plan.md`)
  - Terms of Service (same — use the copy from the media buying plan)
  - Refund Policy (30-day money-back guarantee, no bottle return required)
  - Link all three in footer navigation
  - Meta reviewers check for these — missing them can get ads rejected

- [ ] **PDP quality check** (1 hr)
  - Mobile test (80%+ of Meta traffic is mobile) — does everything render clean?
  - Page load speed — target under 3 seconds
  - FDA disclaimer visible on page
  - 30-day guarantee badge visible
  - Shipping info present
  - All links/buttons work
  - Subscription option visible but not forced
  - Price displays correctly ($49.99 / $42.95 subscribe)

- [ ] **Browse your own store from different devices** (15 min)
  - Use phone, tablet, different browsers
  - Generate ViewContent and AddToCart events for the pixel
  - Note any UX issues to fix

**Day 1 total: ~4-5 hrs of work + ongoing pixel data collection**

---

## Day 2 — Klaviyo & Email Infrastructure

*Set up the retention machine before a single sale comes in. You don't want to be scrambling to build email flows when purchases start.*

- [ ] **Connect Klaviyo to Shopify** (15 min)
  - Install Klaviyo app
  - Sync customer data, products, and order events

- [ ] **Build the welcome flow** (1.5 hrs)
  - Triggered by: email signup via popup
  - Email 1 (immediate): Welcome + 10% discount code + brand story intro
  - Email 2 (Day 2): "What actually happens inside your cells after 40" — education, no sell
  - Email 3 (Day 4): "Why we built a 10-in-1" — ingredient story, soft CTA
  - Email 4 (Day 6): "Your 10% code expires soon" — urgency + link to PDP

- [ ] **Build the abandoned cart flow** (1.5 hrs)
  - AC1 (1 hour after abandon): "Still thinking it over?" — product image, cart link, mention 30-day guarantee
  - AC2 (24 hours): "Most people hesitate because..." — address objections (purity, dosing, price per day)
  - AC3 (48 hours): Final nudge — "Your cart expires soon" + maybe 5% extra off or free shipping emphasis

- [ ] **Build the post-purchase flow** (1.5 hrs)
  - PP1 (immediately): Order confirmation + "What to expect" timeline (week 1-2 probably nothing, week 3-4 subtle shifts, week 5-8 consistent)
  - PP2 (Day 3): Shipping confirmation + "How to take it" (morning, with food)
  - PP3 (Day 14): Check-in — "How's it going?" + reminder that NMN builds over time
  - PP4 (Day 45): "You're halfway through" — subscription pitch + reorder link
  - PP5 (Day 55): "5 days left in your supply" — reorder or subscribe CTA

- [ ] **Set up the 10% welcome popup** (30 min)
  - Triggers on first visit (delay 5-10 seconds)
  - Captures email for Klaviyo welcome flow
  - "Get 10% off your first order"
  - Include small privacy policy link line

**Day 2 total: ~5-6 hrs**

---

## Day 3 — Creative Compliance & Ad Upload Prep

*Body copies are checked. Now run every creative image through compliance + the origins-writing lens. Then get everything organized for upload.*

- [ ] **Compliance check all 9 ad creatives** (2-3 hrs)
  - Check each image against `research/Meta_Health_Ad_Restrictions_Guide.md`
  - No before/after implications in the visuals
  - No health claims in any text overlays
  - No "miracle cure" visual language
  - Run through origins-writing skill for quality/angle alignment
  - Flag and fix any that don't pass

- [ ] **Organize ad assets for upload** (1 hr)
  - Create a folder structure: Batch 1 / Batch 2 / Batch 3
  - Each folder: creative image + paired body copy + headline + CTA
  - Label everything clearly so upload day is copy-paste, not a scavenger hunt

- [ ] **Draft campaign structure in a doc** (1 hr)
  - 1 CBO campaign → 3 ad sets → 3 ads each
  - Budget: $50 CAD/day CBO
  - Targeting per ad set (broad, 40+ US, gender splits per batch)
  - Optimization: Purchases
  - Placements: Advantage+ or manual (feeds + stories)
  - This way when spend hits ~$80 you just execute the doc, no decisions to make

- [ ] **Daily organic posting** (1 hr)
  - Post on all 3 pages per content plans
  - Engage with comments/DMs (15 min per page)

**Day 3 total: ~5-6 hrs**

---

## Day 4 — Content Batching (Brand Page)

*You have content plans but you'll burn out creating posts one at a time. Batch a full week's worth for the Brand Page today.*

- [ ] **Write next week's Brand Page captions** (2 hrs)
  - Pull from `current-brand/organic-brand-post/Organic_Post_Plan_Brand_Page.md`
  - Write 5-6 captions (Instagram length + Facebook extended versions)
  - Include hashtags for each post
  - Cross-reference against Sarah's page — no duplicate angles in the same week

- [ ] **Create next week's Brand Page graphics** (2-3 hrs)
  - Carousel slides, stat graphics, text cards — whatever the post format calls for
  - Use Canva with brand colors (Teal Deep, Copper, Cream) and fonts (Cormorant Garamond headers, Plus Jakarta Sans body)
  - Size for Instagram (1080x1080 feed, 1080x1350 portrait) + resize for Facebook
  - Save all to a "Week X" folder, ready to schedule

- [ ] **Schedule posts** (30 min)
  - Use Meta Business Suite or a scheduler
  - 7-9am EST posting time
  - Queue the full week so you're not scrambling daily

- [ ] **Daily organic posting + engagement** (1 hr)
  - Today's posts on all 3 pages
  - Reply to comments/DMs

**Day 4 total: ~6-7 hrs**

---

## Day 5 — Content Batching (Sarah's Page + Ad Partner Page)

*Same thing as Day 4, but for the other two pages.*

- [ ] **Write next week's Sarah captions** (1.5 hrs)
  - Pull from `current-brand/partner-page/Partner_Page_Identity_and_Post_Plan.md`
  - Mix Baseline and non-Baseline content (her page shouldn't feel like an ad feed)
  - FTC disclosure (`#BaselinePartner`) on every Baseline-mentioning post
  - Voice: personal, warm, practitioner POV — NOT brand voice

- [ ] **Create Sarah's graphics** (2 hrs)
  - More lifestyle/personal feel than the brand page
  - Her content should feel like a real wellness practitioner's feed
  - Supplement cabinet photos, morning routine, "what I tell my clients" cards

- [ ] **Write + create Ad Partner Page content** (1.5 hrs)
  - Pull from `current-brand/ads/Ad_Partner_Page_Content_Plan.md`
  - Generic health/wellness — this page just needs to not look empty
  - 3-4 posts queued

- [ ] **Schedule all posts across both pages** (30 min)

- [ ] **Daily engagement** (30 min)
  - Reply to comments/DMs across all pages

**Day 5 total: ~6-7 hrs**

---

## Day 6 — Store Optimization & Test Orders

*Everything is built. Now stress-test it like a customer would.*

- [ ] **Place a test order** (30 min)
  - Go through the full purchase flow on mobile
  - Verify: Pixel fires Purchase event, Shopify order comes through, confirmation email sends
  - Test abandoned cart: add to cart, leave — does the Klaviyo AC1 fire after 1 hour?
  - Test welcome flow: sign up via popup — does welcome email arrive immediately?

- [ ] **SEO check on PDP** (1 hr)
  - Page title tag under 60 chars: "Baseline NMN 10-in-1 | NMN + Resveratrol + CoQ10 Supplement"
  - Meta description under 160 chars (from `pdp-copy.md`)
  - H1 is the product title
  - Alt text on all product images
  - FAQ section on PDP (can win featured snippets if you add FAQPage schema)

- [ ] **PDP conversion audit** (1-2 hrs)
  - Above the fold: Is the value prop immediately clear on mobile?
  - Social proof: Are reviews/testimonials visible without scrolling far?
  - Trust signals: Guarantee badge, ingredient transparency, "independently tested"
  - CTA clarity: Is "Add to Cart" obvious and frictionless?
  - Compare at price showing ($69.99 crossed out, $49.99 displayed)?
  - Subscription option clear but not pushy?

- [ ] **Check Pixel data in Events Manager** (30 min)
  - Are events firing correctly from the traffic campaign visitors?
  - ViewContent, AddToCart showing up?
  - Any errors in CAPI connection?

- [ ] **Review ad spend progress** (15 min)
  - Check total account spend
  - Update `current-brand/tracking/Ad_Performance_Tracker.csv`
  - How many days until ~$80 USD (launch prep trigger)?

- [ ] **Daily organic posting + engagement** (1 hr)

**Day 6 total: ~5-6 hrs**

---

## Day 7 — Campaign Pre-Build & Content Buffer

*Get ahead. Build the campaign structure in Ads Manager (paused) and stack up a content buffer so you're not scrambling during launch week.*

- [ ] **Pre-build the purchase campaign in Meta Ads Manager (PAUSED)** (1.5 hrs)
  - Create campaign: CBO, $50 CAD/day, purchase optimization
  - Create 3 ad sets (one per batch): broad targeting, 40+ US
  - Upload all 9 creatives + body copies into their respective ad sets
  - Set everything to PAUSED — do NOT publish
  - This way when you hit $100, you just unpause

- [ ] **Build a 2-week content buffer** (2-3 hrs)
  - Batch another week of content for all 3 pages (on top of the week you batched on Days 4-5)
  - You'll be focused on ad performance once purchase campaigns go live — you won't want to be writing captions
  - Queue everything in scheduler

- [ ] **Create a launch-day checklist** (30 min)
  - Final PDP check (speed, links, disclaimer, guarantee, pixel)
  - Final compliance check on all 9 ads
  - Email flows test (trigger each one manually)
  - Unpause purchase campaign
  - Pause traffic campaign (purchase campaign takes over)
  - Set daily check-in time (1x/day, resist over-monitoring)

- [ ] **Update repo tracking files** (30 min)
  - Update `Ad_Performance_Tracker.csv` with latest numbers
  - Update `Master_Launch_Timeline.md` status fields
  - Update `SESSION_STATE.md` with current state

- [ ] **Daily organic posting + engagement** (1 hr)

**Day 7 total: ~6-7 hrs**

---

## Weekly Summary

| Day | Focus | Key Outcome |
|-----|-------|-------------|
| **1** | Pixel + Traffic + Legal | Account warming 2x faster, store is Meta-compliant |
| **2** | Klaviyo + Email flows | Full retention machine ready before first sale |
| **3** | Creative compliance + Upload prep | All 9 ads cleared and organized for one-click upload |
| **4** | Brand Page content batch | Full week of branded content queued |
| **5** | Sarah + Ad Partner content batch | All 3 pages have a week+ of content queued |
| **6** | Store testing + Optimization | Purchase flow verified end-to-end, PDP polished |
| **7** | Campaign pre-build + Buffer | Campaign ready to unpause, 2-week content buffer built |

> **After this week:** You're in maintenance mode — daily posts (already scheduled), daily engagement (15-30 min), and checking spend progress. When spend hits ~$80 USD, pull up your launch-day checklist and start final prep. At $100, unpause and go.

---

*All reference docs live in this repo. See `CLAUDE.md` for the full file index.*
