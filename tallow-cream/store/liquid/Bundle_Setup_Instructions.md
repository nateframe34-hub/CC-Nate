# 2-Pack Bundle — Setup Instructions

**Created:** 2026-08-02
**Files:** `store/theme/snippets/tallow-bundle-selector.liquid`
**Applies to:** `store/theme/sections/tallow-pdp-v2-reformulated.liquid` (Shrine Pro compatible)

---

## Why this exists

At the new COGS ($10.81 for balm + lip mask, $8.47 for the balm alone):

| Offer | Price | COGS | Contribution | Supports a CPC of |
|---|---|---|---|---|
| 1 jar (no gift) | $49.99 | $8.47 | **$41.52** | ~$1.42 |
| 2 jars + lip mask | $79.99 | $19.28 | **$60.71** | ~$2.08 |

*(at the account's real 3.42% click→purchase)*

**Actual account CPC is $3.17.** The 2-pack roughly halves the gap, and it does it without needing anything from Meta.

It also hedges retention. There are **0 repeat purchases**, but only **3-4 customers are past a 6-8 week reorder window** as of 2026-08-02, so that is absence of data rather than proof of a problem. The 2-pack captures the second unit at peak intent instead of betting on a return visit — which matters more than usual here, because **the product is ~$20 cheaper on Amazon**, so a satisfied customer reordering may not reorder from us.

**No subscription.** Founder call, 2026-08-02: subscribe-and-save depresses CVR and isn't worth it while the messaging is still unproven. Revisit once a winning ad exists.

---

## Step 1 — Shopify admin: create the variant

The PDP hardcodes *displayed* price via section settings, but the **cart charges the real variant price**, so the variant must be created properly.

On the Tallow Honey Balm product, add an option (e.g. `Size` or `Pack`) with two values:

| Variant | Price | SKU suggestion | Inventory |
|---|---|---|---|
| 1 Jar | **$49.99** | TLW-60G-1 | tracked |
| 2 Jars + Lip Mask | **$79.99** | TLW-60G-2GIFT | tracked |

Notes:
- Set **compare-at $99.98** on the 2-pack so Shopify's own discount display is consistent with the struck-through price in the selector.
- The 2-pack is **one variant that ships two jars plus a lip mask**. Do not model it as quantity 2, or the per-unit price maths and the gift logic both break.
- Make sure the **2-pack variant is not excluded** from any existing automatic discounts. Check for leftovers — the PDP file notes a past incident where two automatic discounts stacked and produced an unintended price.

Copy both **variant IDs** (Products → variant → the `variant=` number in the URL).

---

## Step 2 — Render the snippet

In `tallow-pdp-v2-reformulated.liquid`, immediately **after** the price block (around line 340, after the closing `</div>` of `.price`) and **before** `{%- form 'product', product, id: 'tlw-form-hero' -%}`:

```liquid
{%- render 'tallow-bundle-selector' -%}
```

That's the only markup change required. The snippet finds the forms by ID and injects/controls their `id` and `quantity` inputs itself.

**Optional but recommended:** wrap the text inside each Add to Cart button in `<span class="tlw-cta-label">…</span>`. The snippet updates that span if present, and falls back to replacing the button's whole text content if not — the span just protects any icons inside the button.

---

## Step 3 — Add the section settings

Append to the `schema` block's `settings` array in `tallow-pdp-v2-reformulated.liquid`:

```json
{ "type": "header", "content": "Bundle selector" },
{ "type": "select", "id": "default_tier", "label": "Pre-selected tier",
  "options": [ { "value": "1", "label": "Single" }, { "value": "2", "label": "2-Pack" } ],
  "default": "2" },
{ "type": "text", "id": "form_ids", "label": "Product form IDs (comma separated)",
  "default": "tlw-form-hero,tlw-form-final,tlw-form-sticky" },

{ "type": "text", "id": "t1_variant", "label": "Tier 1 variant ID" },
{ "type": "text", "id": "t1_label",   "label": "Tier 1 name",  "default": "One jar" },
{ "type": "text", "id": "t1_sub",     "label": "Tier 1 subtitle", "default": "60g · about 6 weeks" },
{ "type": "text", "id": "t1_price",   "label": "Tier 1 price",  "default": "$49.99" },
{ "type": "text", "id": "t1_each",    "label": "Tier 1 per-unit", "default": "$49.99 per jar" },
{ "type": "text", "id": "t1_cta",     "label": "Tier 1 button price", "default": "$49.99" },

{ "type": "text", "id": "t2_variant",   "label": "Tier 2 variant ID" },
{ "type": "text", "id": "t2_label",     "label": "Tier 2 name", "default": "Two jars" },
{ "type": "text", "id": "t2_sub",       "label": "Tier 2 subtitle", "default": "120g · about 3 months" },
{ "type": "text", "id": "t2_gift_line", "label": "Tier 2 gift line", "default": "Includes the lip mask free" },
{ "type": "text", "id": "t2_badge",     "label": "Tier 2 badge", "default": "Most popular" },
{ "type": "text", "id": "t2_price",     "label": "Tier 2 price", "default": "$79.99" },
{ "type": "text", "id": "t2_was",       "label": "Tier 2 struck price", "default": "$99.98" },
{ "type": "text", "id": "t2_each",      "label": "Tier 2 per-unit", "default": "$40.00 per jar" },
{ "type": "text", "id": "t2_cta",       "label": "Tier 2 button price", "default": "$79.99" },

{ "type": "text", "id": "reassure", "label": "Line under selector",
  "default": "Free shipping either way. 60 days to send it back." }
```

Then set the two variant IDs in the theme customizer.

---

## Step 4 — Move the free gift onto the 2-pack only

**This is the part that changes existing behaviour, so read it.**

Today the lip mask auto-adds to every order via the script around line 709 of the PDP file. Founder decision 2026-08-02: it moves to the 2-pack, both to remove the *"I'm paying $50 for a lip mask I don't want"* read and to take $2.34 out of every single-jar order.

Find the gift auto-add block and gate it on the selected tier:

```js
document.addEventListener('tlw:bundle-change', function(e){
  window.TLW_GIFT_ELIGIBLE = e.detail.gift;   // true only on the 2-pack
});
```

then wrap the existing auto-add call in:

```js
if (window.TLW_GIFT_ELIGIBLE) { /* existing add-gift-to-cart logic */ }
```

If the 2-pack variant physically ships with the lip mask included (recommended — simpler, one SKU, no cart trickery), **skip the auto-add entirely for that tier** and just say so in `t2_gift_line`. Fewer moving parts, and the cart can't get into a state where the gift is present without the bundle.

⚠️ **Watch ATC→purchase after this change.** The 7/22 note says the universal gift *appeared* to lift CVR but was never confirmed on volume. You are removing something unproven, not something known-good, but it's the metric where a regression would surface.

---

## Step 5 — Update the ads before they run

**All five B33 cells state `$49.99` in their closes**, and several imply a single jar. Once the bundle is live the copy isn't wrong, but it undersells. Options in order of preference:

1. **Leave the ads alone for now.** $49.99 is still the entry price and the selector does the upsell on the page. No copy edits, no delay to launch.
2. Later, once a winning ad exists, add a bundle line to that ad's close only.

Do **not** rewrite all five closes before launch. The batch's job is finding a scroll-stopper; changing the offer copy mid-test adds a variable.

---

## What to measure

| Metric | Why |
|---|---|
| **Bundle take rate** | The whole point. Blended contribution at 25% take is ~$46, at 50% ~$51. |
| **LPV→ATC** | Confirms the second option isn't causing choice paralysis. |
| **ATC→purchase** | Where removing the universal gift would show up if it was helping. |
| **Blended AOV** | The number that moves the CPC you can afford. |

**Breakeven CPA moves from $30.16 to $39-41 on the single and $60.71 on the bundle.** Every kill decision made before 2026-08-02 was judged against a bar that was ~30% too strict.
