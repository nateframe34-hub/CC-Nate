# Installing the Evenroom PDP

**File:** `theme/sections/evenroom-pdp-sa1.liquid` → upload to `sections/` in the theme.

**No snippets.** The section is self-contained — CSS, JS, SVG diagram, fonts and schema all live in that one file. Nothing to coordinate across files, nothing to add to `theme.liquid`.

---

## What it DOES depend on

| # | Dependency | Why | Status |
|---|---|---|---|
| 1 | **The product exists with two variants** — `4×10` and `6×10` | The size step iterates `product.variants`. With one variant it renders a single button and still works | ⬜ |
| 2 | **Compare-at price set on the product** | The struck-through price and the 2-pack saving both derive from `product.compare_at_price`. Without it the page just shows one price and doesn't break | ⬜ |
| 3 | 🚨 **An automatic order discount in Shopify admin** | The 2-pack adds **quantity 2 of the same variant**. Shopify charges 2 × price unless a discount exists | ⬜ |
| 4 | **The section added to the product template** | Theme editor → product template → Add section → "Evenroom PDP (SA1)" | ⬜ |
| 5 | Theme's own cart / drawer | The three `{% form 'product' %}` blocks post to `/cart/add` like any theme form | — |

### 3 in detail — do not skip this

```
Shopify admin → Discounts → Create discount → Amount off order
  Method:            Automatic
  Value:             $19.99   (must equal bundle_discount_cents ÷ 100)
  Minimum quantity of items: 2
  Combinations:      tick "combines with product discounts"
```

**Then verify:** select the 2-pack on the page, add to cart, and confirm the cart total reads **$159.99**, not $179.98. If it reads $179.98 the discount isn't firing and every 2-pack order overcharges.

⚠️ **Check for stale automatic discounts first.** The tallow build hit an incident where two automatic discounts stacked and produced a price nobody intended.

---

## Before sending traffic

- [ ] Cart total on the 2-pack reads $159.99
- [ ] Both size buttons change the variant that lands in the cart
- [ ] **Cart drawer still opens** after adding — the selector script is isolated to prevent this, but test it
- [ ] Sticky bar price updates when the tier changes
- [ ] `grep -r "\[PH\]" ` over the theme returns **nothing** — placeholder reviews must not ship
- [ ] `show_reviews` is off unless real reviews exist
- [ ] Mobile: hero ATC, sticky bar, and the size/bundle steps all reachable one-handed

---

## Settings worth knowing

| Setting | Note |
|---|---|
| `bundle_discount_cents` | Default `1999`. **Must match the Shopify discount exactly** |
| `load_fonts` | On by default. Loads Archivo / Inter / JetBrains Mono. Turn off only if the theme already serves them |
| `show_reviews` | **Off by default.** Placeholder markup lives in `PLACEHOLDER_reviews_block.html` |
| `fit_image` | The measure-your-vent photo. Prompt in `PDP_Image_Prompts.md` §2 |

## Prices are NOT hardcoded

Unlike the tallow PDP, every price on this page derives from the Shopify product. Change the price or compare-at in admin and the hero, the selector, the sticky bar and the value stack all follow. **The only thing to change alongside it is the automatic discount**, if the bundle saving should move too.
