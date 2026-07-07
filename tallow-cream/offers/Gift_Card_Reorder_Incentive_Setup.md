# $10 Next-Order Gift Card: Implementation Plan

**Date:** 2026-07-07
**Confirmed with founder:** this is a REORDER incentive, a $10 credit issued after her first purchase, usable on her next order. It is not a discount on the order she's placing now. That distinction matters for both margin (the June offer council explicitly rejected a first-order discount, this doesn't touch first-order contribution at all) and for how it has to be built in Shopify (it can't just be a coupon code typed at checkout, it has to be generated and delivered AFTER the sale).

Store is Shrine Pro 1.3.0 on Shopify. This assumes Shopify's native gift card system plus Shopify Flow (available on most current plans) for the automation. No app purchase should be required for the basic version.

---

## The mechanic, in plain terms

1. Customer buys her first jar.
2. Order triggers a rule.
3. Shopify auto-generates a $10 gift card code tied to her.
4. She gets an email with that code, timed to land when she's likely to be thinking about reordering, not instantly (instant makes it feel like a coupon glitch, not a thank-you).
5. She redeems it at checkout on order #2. Standard Shopify gift card field, no custom code needed there, that part already works out of the box.

---

## Three ways to build the automation, ranked

### Option A (recommended to start): Shopify Flow + native gift cards
Shopify Flow is Shopify's built-in automation tool (free on most plans, check your plan tier). It can watch for an "Order Created" or "Order Paid" event, filter for first-time customers, and trigger a "Create Gift Card" action, then a follow-up "Send Email" step or a queued Klaviyo/Shopify Email flow.

- **Setup effort:** low, a few hours, no developer needed if Flow is available on your plan.
- **Limitation:** Flow's native gift-card action creates the card but the "first-time customer" filter needs to be built carefully (checking customer order count = 1 at the time of the trigger, not just "has an email"), otherwise repeat buyers could get a card every order. This is the one detail worth double-checking in testing before it goes live.
- **Delivery timing:** you can add a "Wait" step in Flow (e.g., wait 3 days) before sending the email, so it lands as a "here's your reward" moment rather than an instant afterthought.

### Option B: Klaviyo automation (if Klaviyo is already the email tool)
If order data already flows into Klaviyo (likely, since it's the standard Shopify email tool), build a flow: trigger = "Placed Order" + filter "order count = 1," action = call Shopify's Admin API to create a gift card (via a webhook or a lightweight integration like Zapier/Make bridging Klaviyo → Shopify), then Klaviyo sends the reveal email with the code.

- **Setup effort:** medium, needs an API call step, which usually means a Zapier/Make connector unless someone can write ~20 lines against Shopify's Admin API.
- **Upside:** better email design/timing control than Flow's native email, and it's probably where the day-30 reorder email (from the offer doc) already lives or should live, this can piggyback on that same flow.

### Option C: Manual/CSV batch (bridge solution, ships today, no automation build)
Before any automation is wired up, this can launch immediately as a manual process: export first-time-buyer emails weekly (Shopify admin → Customers → filter by 1 order), bulk-create gift cards in Shopify admin (supports CSV-ish bulk creation, or one-by-one for early low volume), and send the codes via a simple templated email (even manually through Shopify Email or Klaviyo's one-off send).

- **Setup effort:** near zero, works today.
- **Cost:** founder time, doesn't scale past maybe a few dozen orders/week before it's a real chore.
- **Use case:** exactly right for right now, since B24/B25 volume is still small. Automate (Option A) once order volume makes the manual version annoying, don't over-build before there's enough volume to justify it.

---

## Recommended sequence

1. **Now:** launch manually (Option C). PDP copy is already live/ready with the "$10 gift card on your next order" language; you fulfill it by hand for the first batch of orders while volume is low.
2. **Once volume picks up (a natural trigger: when the manual process starts taking more than ~15 min/week):** build Option A (Shopify Flow), it's the lowest-effort automation and doesn't require touching Klaviyo.
3. **Optional later upgrade:** fold it into Klaviyo (Option B) once/if there's a reason to control email design and timing more precisely, e.g. bundling it with the day-30 reorder email already planned in the offer doc.

---

## Things to decide/confirm before this goes live for real customers

1. **Expiration:** does the $10 card expire? Recommend 90 days, creates urgency without feeling stingy.
2. **Stacking:** can it combine with the 2-jar/3-jar bundle discounts already on the PDP? Recommend yes, simplest and most generous, avoids a confusing "gift card doesn't work on sale items" support headache.
3. **First-time-customer filter:** needs to be airtight so this doesn't accidentally fire on every order for repeat buyers, this is the one technical detail that actually needs testing before going live.
4. **Where the code lives:** confirm it's a real Shopify gift card object (trackable, real balance) and not something represented only in an email, so support can look it up if a customer says they never got it.

## What I need from you to move this forward
Tell me which option to build now (my read: start with C today since PDP copy already promises it, then move to A), and confirm your Shopify plan includes Flow (Shopify Basic and up all have some Flow access; if you're on the entry Starter plan, Flow may be limited, worth a 2-minute check in Settings → Apps → Shopify Flow).
