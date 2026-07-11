# OpenAI Ads Pixel: Setup Log + Shopify Install Guide

**Date:** 2026-07-11
**Why:** OpenAI ads conversion events just rolled out. Early-platform conversion optimization = cheap delivery while the auction is underpopulated, the same early-mover economics Meta had years ago. Worth wiring up now even before OpenAI ad spend starts, so the pixel accumulates conversion history.

## Logged data (from setup dialog)

| Field | Value |
|---|---|
| Pixel ID | `AUa2aGQPEx21gg49VpjMNz` |
| Script global | `oaiq` (loader pattern: `!function(w,d,s,u){if(w.oaiq)return;var q=functio...` truncated in screenshot, full code in the OpenAI dashboard "Copy" button) |
| Example event shown | `oaiq("measure", "registration_completed", { type: "customer_action", amount: 0, currency: "USD" })` |
| Setup rules per dialog | Setup script goes in HTML head, once per page, near the top. Event calls go ONLY where the action happens, never alongside the sitewide setup code. |
| Next step in their flow | "Next: create conversion event" |

## Install plan for Shopify (two pieces, both required)

Shopify doesn't let you inject scripts into checkout pages from theme.liquid anymore, so this is a two-part install: the sitewide pixel goes in the theme, the purchase event goes in a Customer Events custom pixel (Shopify's sandboxed pixel system, which IS allowed to see checkout).

### Piece 1: Sitewide setup script (theme.liquid)
1. Shopify admin → Online Store → Themes → current theme → Edit code → `layout/theme.liquid`
2. Find the `<head>` tag near the top.
3. Paste the FULL setup code (copied via the dialog's Copy button) on a new line directly after `<head>`.
4. Save. This makes `oaiq` available on every storefront page (page views, landing pages, PDP). Do not add any event calls here.

### Piece 2: Purchase conversion event (Customer Events custom pixel)
1. First, in the OpenAI dashboard, click "Next: create conversion event" and create the purchase event. **Name it `purchase`** (or note whatever name you choose, the code below must use the exact same string).
2. Shopify admin → Settings → Customer events → Add custom pixel → name it "OpenAI Pixel".
3. Paste the following, with two substitutions: the `[PASTE ...]` block gets the full setup code JS (everything INSIDE the `<script>...</script>` tags, without the script tags themselves), and the event name string must match step 1:

```js
// OpenAI pixel loader (paste the setup code contents here, WITHOUT the <script> tags)
[PASTE SETUP CODE JS HERE]

// Fire the purchase conversion when checkout completes
analytics.subscribe('checkout_completed', (event) => {
  const checkout = event.data.checkout;
  oaiq("measure", "purchase", {
    type: "customer_action",
    amount: Number(checkout.totalPrice.amount),
    currency: checkout.totalPrice.currencyCode
  });
});
```

4. Save, then click **Connect** (a saved-but-disconnected pixel does nothing, this is the step everyone misses).

Why the loader is pasted twice (theme + custom pixel): Shopify's custom pixels run inside a sandboxed context that cannot see scripts loaded by the theme, so the pixel needs its own copy of the loader to have `oaiq` available when checkout_completed fires. The `if(w.oaiq)return` guard in the loader makes double-loading harmless on regular pages.

### Verify it works
1. Place a test order (or a 100% discount-code order).
2. In the OpenAI dashboard, check the pixel/data-source page for received events (most platforms show a "last received" timestamp or event debugger).
3. Storefront sanity check: open the site, browser console, type `oaiq` and press enter, it should return a function, not undefined.

## Notes / open items
- If the OpenAI dashboard offers additional standard ecommerce event names (add_to_cart, begin_checkout etc.) when creating conversion events, purchase is the only one that matters for optimization now; add-to-cart can be added later in the same custom pixel with `analytics.subscribe('product_added_to_cart', ...)`.
- The truncated setup code was NOT captured in this log, only the dashboard has the full version. If the theme install ever needs to be redone, re-copy from OpenAI's dashboard, don't reconstruct it.
- Currency: account bills USD, store sells USD, so `currencyCode` will pass through as USD with no conversion concerns.
