# Cart Email Capture + Follow-Up: In-House, No Paid ESP

**Date:** 2026-07-12
**Why this exists:** funnel data (`Ad_Performance_Tracker.csv` post-break analysis) showed the real leak isn't clicks or checkout completion, it's ATC -> Checkout, roughly 60-70% of people who add to cart never even start checkout. Shopify's native abandoned-checkout email already covers people who START checkout and leave (confirmed live). It does NOT cover people who add to cart and leave WITHOUT ever starting checkout, because Shopify never captures an email for that group. This flow closes that specific gap, entirely with tools already in the account (Shopify native customer form, Shopify Flow, Shopify Email), no Klaviyo, no paid app.

---

## Part 1: what's now live in the theme (done)

`tallow-cream/store/theme/sections/tallow-pdp.liquid`, inside the cart drawer footer (`.tlw-d-capture`):
- A native Shopify **Customer form** (`{% form 'customer' %}`), not a custom app, not a third-party embed.
- On submit, it creates (or updates) a Shopify customer record, tagged `cart-abandon-capture`, marked `accepts_marketing: true`.
- No password, no account activation email, no login required, this is the same mechanism Shopify uses for plain newsletter signup forms.
- Shows inline confirmation ("Saved. Check your email for 10% off.") on success via `form.posted_successfully?`, no page reload, no redirect needed since it's inside the drawer already.

This alone captures the email. It does NOT send anything yet, that's Part 2.

## Part 2: build in Shopify Flow (founder to build, steps below)

1. **New workflow, Trigger: Customer created OR Customer updated.** (Shopify Flow's customer triggers fire on both new signups and updates to existing customer records, use whichever is offered as a single combined trigger in your account, check the trigger picker, if both exist as separate triggers you'll need two workflows with identical logic below, or one workflow using both as alternate triggers if Flow supports OR-triggers in your version.)
2. **Add a Condition:** customer's tags **contains** `cart-abandon-capture`. This is the filter that makes sure this workflow only fires for people who used this specific form, not every customer event in the store.
3. **Add a Wait action:** 45-60 minutes. Long enough that it reads as a deliberate follow-up, not an instant bot reply, short enough to reach her while the cart (and the desire) is still fresh, this is a much shorter window than the 3-week gift-card flow because cart abandonment cools fast.
4. **Add action: Send marketing email** (Shopify Email, same native action already used in the review-request and gift-card flows in this account). Since this is a single-SKU store, you don't need per-item personalization, "you left the tallow balm in your cart" is already exactly correct for every recipient, this simplifies the email a lot compared to a multi-product store.
5. **Suggested email content** (keep it short, native tone, matches the account's existing voice):
   - Subject: something low-key, not shouty, e.g. "Still thinking it over?"
   - Body: one line acknowledging she looked, one line restating the guarantee + free shipping (the same trust signals now live in the drawer), the 10% code, one clear button back to the PDP or straight to checkout if you can pre-fill the cart via a `/cart/12345:1?discount=CODE` style link.
6. **Turn the workflow ON**, then test end to end: submit the drawer form yourself with a real inbox, confirm the customer record gets created/tagged in Shopify admin, confirm the Flow run appears in Activity history, confirm the email actually lands (check spam folder on first tests, cold sending domains sometimes land there initially).

## Part 3: the discount code

You'll need one 10% code to reference in the email (a single shared code is fine at this volume, doesn't need to be unique-per-customer given how few sends this will generate early on). Create it in Shopify admin -> Discounts, plain percentage code, no other conditions needed. If you'd rather not do 10% given the gift-card-on-every-order economics already in play, a flat $5 works too, just keep the email's copy matching whatever you actually create.

## What this does NOT do (be aware)
- It does not know what's specifically in her cart beyond "the tallow balm," fine for a single-SKU store, would need real work if a second SKU/bundle launches later.
- It only fires once per customer per tag application, if she submits the form again on a later visit, Flow's trigger will fire again since it's Customer updated, worth deciding later whether repeat submissions should re-enter the flow or be excluded (a second condition checking she hasn't received this specific email before, via a second tag added by Flow itself after the first send, e.g. `cart-recovery-sent`, would prevent repeat sends if that becomes a problem).

## Status
Theme code: **live**. Flow workflow: **not yet built**, founder to build per Part 2 steps above.
