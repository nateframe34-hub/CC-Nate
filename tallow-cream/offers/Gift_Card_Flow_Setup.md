# $10 Gift Card: Shopify Flow Setup

**2026-07-19 UPDATE: switched from every-order to a scarcity "next 100 customers" mechanic.** Founder's call: every-order was a real 20% reorder cost with no urgency lever, "the next 100 customers get a $10 gift card, X remaining" gives real urgency AND caps the cost. Mechanism (same inventory-token pattern proven out for the free lip balm, avoids the unreliable `customerJourneySummary` field this doc already learned not to trust):

1. **Create a $0.00 "Gift Card Eligibility Token" product** in Shopify admin (hidden from all sales channels/search, not linked in any nav). Set its inventory to exactly **100**, track quantity, do NOT allow overselling.
2. **`tallow-pdp.liquid` already auto-adds this token to the cart silently** alongside the main balm, via the same JS that adds the free lip balm (see `addGiftsSilently()` in the section file), IF the section's `gift_token_variant_id` setting is filled in. Paste the token product's variant ID there once created.
3. **The PDP's live "X remaining" counter is already wired**, it reads the token product's real inventory via its handle (`gift_token_product_handle` setting), no manual updating needed, it decrements automatically as real orders consume the token's inventory and the callout hides itself entirely once inventory hits 0.
4. **Update the live Flow's trigger step:** add a **Condition** checking that the order's line items include the Gift Card Eligibility Token product (this is the reliable per-order signal the original build was missing, a real line item, not an unreliable customer-journey field). Only orders containing the token proceed to the `giftCardCreate` mutation below. Since Shopify decrements the token product's own inventory automatically as orders are placed, the condition combined with the inventory cap does the "first 100" gating without any manual tracking.
5. **Everything below this point (the Admin API mutation, the notification) stays the same,** this only changes what gates entry into the existing, already-working workflow.

**Original build, still fully valid below, dated 2026-07-07:**

**Date:** 2026-07-07, corrected same day against founder's real Flow action list (screenshot, `New Workflow` action picker)
**2026-07-12 UPDATE: no longer first-purchase-only.** The `order.customerJourneySummary.customerOrderIndex` condition built into the live workflow returned null on a real order (confirmed via a live run, order #1019, Brenda), so the "equal to 1" check failed even on what looked like a genuine order. Root cause: that field depends on marketing/session attribution data, not a simple count of the customer's orders, and Shopify doesn't reliably populate it. No usable order-count field was available in the Condition step's picker off the Order paid trigger either. **Founder's decision: delete the condition entirely, every paid order gets a $10 gift card.** This also reframes the mechanic from an acquisition incentive to a reorder incentive, which is arguably a better fit for the funnel anyway. PDP copy updated to match (`tallow-cream/store/theme/sections/tallow-pdp.liquid`, "with your first purchase" -> "with your purchase").
**Margin note, flagged not blocked:** $10 on every $49.99 order is a 20% reorder cost indefinitely, stacking on every repeat purchase, not just once. Worth revisiting if reorder volume grows and margin needs a closer look, no action taken on this yet, just logged so it's not a surprise later.

**What this is:** step-by-step for building the automation that fulfills the promise now live on the PDP ("Get a $10 gift card with your purchase," `tallow-cream/store/theme/sections/tallow-pdp.liquid`).

**Correction from the first draft of this doc:** I had guessed at Flow's trigger/action names instead of working from what's actually in the account, and got both wrong. Confirmed from the real action list: the trigger is **Order paid** (not "Order created"), and there is NO native "Create gift card" action, and NO generic "Send email" action either. This version is built from what's actually there.

---

## What's actually available (from the real action list)

Relevant ones for this task:
- **Trigger: Order paid** (confirmed, already in the screenshot as the default trigger)
- **Get customer data**: pulls customer fields, needed to check order count
- **Get gift card data**: READ only, can look up/query existing gift cards, cannot create one
- **Send Admin API request**: this is the one that matters. It lets Flow call Shopify's Admin GraphQL API directly, which is how gift cards actually get created (there's a `giftCardCreate` mutation in Shopify's Admin API even though Flow has no dedicated one-click action for it)
- Various tag actions (**Add customer tags**, **Add order tags**, **Update customer metafield**): useful for handing off to Klaviyo, since Flow can't send a general customer-facing email itself
- No generic "Send email" action exists in this list. The only email-shaped actions are transactional ones tied to specific Shopify objects (order invoice, payment reminder, B2B access), none of which fit "here's your reward."

**Conclusion:** Flow creates the gift card via a raw Admin API call, then hands off delivery to Klaviyo (since that's where customer emails should live anyway) by tagging the customer or order. Flow doesn't send the reveal email itself.

---

## Step 1: Build the Flow workflow

1. **Trigger:** Order paid (already set in your draft workflow).
2. **No condition step.** Every paid order proceeds straight to the gift card mutation, per the 2026-07-12 decision above. (Historical note, kept for reference: the original plan here was a first-purchase-only gate via `Get customer data` + a Condition checking order count equals 1. Abandoned because no reliable order-count field was available in the Condition step's field picker off the Order paid trigger, and the `customerJourneySummary.customerOrderIndex` field that was tried instead returned null on a real live order.)
3. **Add action: Send Admin API request.** This calls Shopify's Admin GraphQL API using a mutation like:
   ```graphql
   mutation giftCardCreate($input: GiftCardCreateInput!) {
     giftCardCreate(input: $input) {
       giftCard { id maskedCode }
       userErrors { field message }
     }
   }
   ```
   with variables built from the order/customer data available in the workflow (customer ID, an initial value of $10 USD, an expiry date, and a note referencing the order for traceability). **The exact input field names should be checked against Shopify's current Admin API docs at build time** (Settings → search "Admin API" or shopify.dev's GraphQL Admin API reference for `GiftCardCreateInput`), API mutation shapes shift between API versions and I don't have live access to confirm the exact current schema against your API version.
4. **Add a tag action** right after the API call succeeds: e.g. **Add customer tags** with `first-purchase-gift-card-issued`, or **Update customer metafield** storing the gift card code/id. This is the handoff point to Klaviyo.
5. **In Klaviyo:** build a flow triggered off that tag (Klaviyo syncs Shopify customer tags) or off a custom event, with a 2-3 day delay before sending, so it reads as a deliberate reward rather than an instant afterthought. The actual gift card code needs to reach Klaviyo somehow, either by writing it to a customer metafield that syncs into a Klaviyo custom property, or by having the Admin API call's response captured and passed along in the same Flow run via another action. This hand-off mechanic is the part most worth testing carefully, see Step 2.
6. **Turn the workflow ON** only after Step 2 passes.

## Step 2: Test it before trusting it

1. Place a real test order (smallest possible amount).
2. Check the Flow **Activity/run history** to confirm every step fired, especially the Admin API call, look at its response for `userErrors` (an empty array means it worked).
3. Confirm a real gift card now exists: **Shopify admin → Products → Gift cards**.
4. Confirm the customer tag/metafield got set, and that it correctly reached Klaviyo and triggered the reveal flow after the delay.
5. Place a SECOND order from that same test customer and confirm a SECOND gift card is issued (expected behavior now, no dedupe condition exists, every paid order gets one). If margin ever needs the dedupe back, the fix path is a self-enforced tag check (see the 2026-07-12 note above), not the journey-summary field.

## Step 3: Decide before going live

1. **Expiration on the card** (a field in the mutation input), recommend 90 days.
2. **What the Klaviyo email says**, keep it simple: "here's your $10, thanks for trying [product], good toward your next order."
3. **Confirm the Admin API scope** the workflow needs (`write_gift_cards` or equivalent) is actually granted to Flow's Admin API access in your store, if the mutation fails with a permissions error, this is where to check.

## Open items I can't resolve without your Shopify instance in front of me
- The exact current field names/shape of `GiftCardCreateInput` for your API version, pull this from shopify.dev when you're actually building the "Send Admin API request" step, don't trust the field names I wrote above as gospel.
- How best to pass the newly-created gift card's code from the Admin API response into the customer record Klaviyo reads (metafield vs. Klaviyo custom event payload), this depends on exactly how your Klaviyo-Shopify sync is configured, worth a quick check together once you're at that step.
