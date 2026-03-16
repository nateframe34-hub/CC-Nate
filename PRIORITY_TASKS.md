# Priority Tasks — While Waiting for $100 Spend Threshold

> **Updated:** March 16, 2026
> **Context:** Engagement campaign running at ~$3.40 USD/day. Currently at $6.83 USD of $100. Estimated ~27 days at current pace (faster once traffic campaign launches). Use this time to build everything so you can flip the switch the moment the account is warm.
>
> **Time budget:** 6-8 hours total. Tasks ranked by impact — do them in order. Check off as you go (click the checkbox on GitHub).

---

## Tier 1 — Blocks Everything (Do First)

These are on the critical path. Purchase ads literally cannot launch without them.

- [ ] **Get the Shopify PDP live** (~2-3 hrs)
  - Build product page on Shrine Pro using copy from `current-brand/brand/pdp-copy.md`
  - FDA disclaimer on page (required for supplement ads)
  - 30-day money-back guarantee badge visible
  - Shipping info: "Ships within 1-2 business days. Delivers in 3-7 business days."
  - Product images uploaded (use Nano Banana Pro to generate from `Ad_Batch_Plans_B1-B3.md` prompts)
  - Test the page: loads fast, links work, mobile looks good

- [ ] **Install Meta Pixel + Conversions API (CAPI) on Shopify** (~30 min)
  - Use Meta's official Shopify integration
  - Verify pixel fires on: PageView, ViewContent, AddToCart, InitiateCheckout, Purchase
  - Test with Meta Pixel Helper Chrome extension
  - Once live, browse your own store a few times to seed ViewContent events

- [ ] **Launch the traffic campaign** (~30 min, do immediately after Pixel is live)
  - $5-10 CAD/day pointing to PDP
  - Objective: Landing page views
  - This doubles your spend rate toward the $100 threshold (~12-15 days instead of ~27)
  - Warms the pixel with real visitor data (ViewContent, AddToCart signals)

---

## Tier 2 — Blocks Ad Launch (Do Second)

These must be done before purchase ads go live but don't block each other.

- [ ] **Create the Ad Partner Page on Facebook** (~30 min)
  - Generic health/wellness page name (not Baseline-branded)
  - Add it to Meta Business Manager
  - All B1-B3 purchase ads will run through this page

- [ ] **Generate the 9 ad creatives** (~1-2 hrs)
  - Use Nano Banana Pro with the prompts in `Ad_Batch_Plans_B1-B3.md`
  - 3 per batch × 3 batches = 9 total
  - Edit in Canva: add text overlays, brand elements per the briefs
  - Save finals in a folder you can grab when it's upload time

- [ ] **Generate Sarah's profile photo** (~15 min)
  - Needed for Partner Page content to look legit
  - Use Nano Banana Pro — natural, approachable, Austin wellness practitioner vibe

- [ ] **Compliance check all 9 ads + 9 body copies** (~30 min)
  - Run every creative and body copy against `research/Meta_Health_Ad_Restrictions_Guide.md`
  - No direct health claims, no before/after implications, no "cures" language
  - Fix anything that doesn't pass before upload

---

## Tier 3 — Builds the Foundation (Do Third)

Not technically blockers, but empty pages kill trust when people check.

- [ ] **Seed Brand Page content (@baselinenmn)** (~1 hr)
  - Profile photo, cover, bio set up
  - Post at least 5-7 posts from Week 1-2 of `current-brand/organic-brand-post/Organic_Post_Plan_Brand_Page.md`
  - Page should look established, not freshly created
  - Continue posting daily after initial seed

- [ ] **Seed Sarah's Partner Page (@sarahlawson.wellness)** (~1 hr)
  - Profile photo (generated above), bio, first posts
  - Post at least 5-7 posts from `current-brand/partner-page/Partner_Page_Identity_and_Post_Plan.md`
  - Include FTC disclosure (`#BaselinePartner`) on any Baseline-mentioning posts
  - Mix Baseline and non-Baseline content so it feels real

- [ ] **Seed Ad Partner Page content** (~30 min)
  - 3-4 generic health/wellness posts from `current-brand/ads/Ad_Partner_Page_Content_Plan.md`
  - Doesn't need to be heavy — just can't be an empty shell

---

## Tier 4 — Retention Infrastructure (Do When You Can)

Not a launch blocker, but you'll regret not having it when sales start.

- [ ] **Set up Klaviyo email flows** (~1 hr)
  - Welcome flow (triggered by 10% popup signup)
  - Abandoned cart sequence
  - Post-purchase thank you + education sequence
  - Connect to Shopify

- [ ] **Add 10% welcome popup to store** (~15 min)
  - Triggers on first visit
  - Captures email for Klaviyo welcome flow
  - "Get 10% off your first order" or similar

---

## Quick Time Estimate

| Tier | Tasks | Est. Time |
|------|-------|-----------|
| Tier 1 | PDP + Pixel + Traffic campaign | 3-4 hrs |
| Tier 2 | Ad Partner Page + Creatives + Sarah photo + Compliance | 2-3 hrs |
| Tier 3 | Content seeding (3 pages) | 2-3 hrs |
| Tier 4 | Klaviyo + Popup | 1-1.5 hrs |
| **Total** | | **8-11 hrs** |

> **If you only have 6 hours:** Tier 1 + Tier 2 is the move. Content seeding and Klaviyo can happen in a second session. Getting the PDP live and traffic campaign running is the single highest-leverage use of your time — it cuts your wait time nearly in half.

---

*Reference: `current-brand/tracking/Master_Launch_Timeline.md` for the full launch sequence.*
