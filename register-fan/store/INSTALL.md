# Installing the Evenroom PDP

**File:** `theme/sections/evenroom-pdp-sa1.liquid` → upload to `sections/` in the theme.

**No snippets.** The section is self-contained, CSS, JS, SVG diagram, fonts and schema all live in that one file. Nothing to coordinate across files, nothing to add to `theme.liquid`.

---

## What it DOES depend on

| # | Dependency | Why | Status |
|---|---|---|---|
| 1 | **The product exists with two variants**, `4×10` and `6×10` | The size step iterates `product.variants`. With one variant it renders a single button and still works | ⬜ |
| 2 | **Compare-at price set on the product** | The struck-through price and the 2-pack saving both derive from `product.compare_at_price`. Without it the page just shows one price and doesn't break | ⬜ |
| 3 | 🚨 **An automatic order discount in Shopify admin** | The 2-pack adds **quantity 2 of the same variant**. Shopify charges 2 × price unless a discount exists | ⬜ |
| 4 | **Upload both theme files, then assign the template** | Code editor: add `sections/evenroom-pdp-sa1.liquid` **and** `templates/product.evenroom.json` (Add a new template → product → JSON → name it `evenroom`, paste the file). Then **Products → the vent → Theme template → `evenroom`** | ⬜ |
| 5 | Theme's own cart / drawer | The three `{% form 'product' %}` blocks post to `/cart/add` like any theme form | - |

### Mixed 2-packs (added 2026-09-28)
When "Two vents" is picked with two **different** vents (e.g. one white, one bronze), the form adds two line items (`items[0]`, `items[1]`) instead of one item with quantity 2. Two checks:
- **The discount must count any variant.** Set the automatic discount to "Minimum quantity of items: 2" on **the product** (all variants), not on a single variant, or a mixed pair won't get $19.99 off.
- The section now has **its own cart drawer** (setting "Use this section's cart drawer", on by default). It adds via `/cart/add.js` directly, so mixed pairs always land. Turn it off to fall back to the theme's cart.

### 3 in detail: do not skip this

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
- [ ] The "Pick your vent" dropdown changes the variant that lands in the cart
- [ ] Two vents, same choice → 1 line × qty 2 · two vents, different choices → 2 lines × qty 1, both discounted
- [ ] **Our cart drawer opens** after adding: lines, bundle discount (−$19.99 on 2), subtotal, Check out goes to checkout
- [ ] The theme's header cart count updates (if not, it updates on the next page load; tell me the theme name and I'll hook it)
- [ ] Sticky bar price updates when the tier changes
- [ ] `grep -r "\[PH\]" ` over the theme returns **nothing**, placeholder reviews must not ship
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
