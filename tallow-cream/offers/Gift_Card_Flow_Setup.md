# $10 Gift Card: Shopify Flow Setup

**Date:** 2026-07-07
**What this is:** step-by-step for building the automation that actually fulfills the promise now live on the PDP ("Get a $10 gift card with your first purchase," `tallow-cream/store/theme/sections/tallow-pdp.liquid`). Confirmed: Shopify Flow is available on your plan.

The goal: when someone places their first order, Shopify automatically creates a real $10 gift card and emails it to them a few days later (not instantly, so it reads as a reward, not a checkout glitch).

---

## Step 1: Build the Flow workflow

1. In Shopify admin, go to **Apps → Shopify Flow** (if it's not pinned, search "Flow" in the admin search bar).
2. Click **Create workflow**.
3. **Trigger:** search for and select **Order created**.
4. **Add a condition** (this is the step that keeps it to first-time buyers only, don't skip it): 
   - Condition: `Order > Customer > Orders count` **is equal to** `1`
   - This checks the customer's total lifetime order count at the moment this order was placed. If it's their first order, it equals 1. This is the detail that stops repeat buyers from getting a card every time they order.
5. **Add action: Create gift card**
   - Amount: `10.00`
   - Note/internal reference: something like "First-purchase reward, order {{order.name}}" so support can trace it later if a customer asks.
   - Recipient: assign it to the customer's email from the order (`{{order.customer.email}}`).
6. **Add a Delay step** (Flow has a "Wait" action) before the email send, 2-3 days is a good default. This is what makes it feel like a deliberate reward instead of an automated afterthought.
7. **Add action: Send email** (Flow can send a basic email itself, or you can trigger a Klaviyo flow instead if you want nicer design, see Step 3 below).
8. **Turn the workflow ON.**

## Step 2: Test it before trusting it

Before this touches real customers:
1. Place a real test order yourself (smallest amount, use a discount code to zero it out if needed, or just eat the cost of one jar as a test).
2. Confirm in Flow's **Activity** / run history that the workflow fired, the condition passed, and a gift card was actually created (check **Shopify admin → Products → Gift cards** for a new card).
3. Confirm the delay step worked and the email actually arrived after the wait period, not instantly.
4. Place a SECOND test order from the same test customer account and confirm the condition correctly blocks it (order count would be 2, so the workflow should NOT create a second card). This is the check that matters most, it's the one thing that would be expensive to get wrong at volume.

## Step 3: Email delivery, two options

**Option A: Flow's native email action.** Simplest, works immediately, basic formatting. Good enough to launch with.

**Option B: Route it through Klaviyo instead** (better design/branding control, and it's probably where other lifecycle emails already live). Instead of Flow's "Send email" action, use a "Send to Klaviyo" / webhook-style action (or have Flow tag the customer/order with something like `first-purchase-gift-card-issued`, and build a Klaviyo flow triggered off that tag or off a custom event). This is the nicer version but takes longer to wire up. Start with Option A, migrate to Option B later if you want the email to look better.

## Step 4: Decide and confirm two things before going live

1. **Expiration on the gift card.** Shopify gift cards can be set to expire or never expire when created. Recommend 90 days, creates gentle urgency without feeling stingy. Set this in the "Create gift card" action's options.
2. **What the email actually says.** Keep it simple and on-voice: something like "Here's your $10, thanks for trying [product]. Use it on your next order, no strings." Avoid anything that reads like a coupon-spam subject line.

## What this does NOT need
- No new app or paid tool, Flow + native Shopify gift cards covers the whole mechanic.
- No changes to the PDP or checkout, the gift card is issued after the sale, not applied to it.
- No manual work once it's built and tested, this fully replaces the "export weekly and hand-create cards" bridge process from the earlier planning doc.

## If something breaks
- If gift cards are being created for repeat customers too, the order-count condition (Step 1.4) is misconfigured or evaluating at the wrong point, double check it's reading the count AT the time of this order, not their current lifetime total (which would already include the order that just triggered the workflow and always be ≥1, so make sure you're testing this against a truly fresh test customer).
- If no card is created at all, check the Flow **Activity log** for the specific run, it will show exactly which step failed and why.
