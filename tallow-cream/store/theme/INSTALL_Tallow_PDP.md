# Install the Tallow PDP product template (Shrine Pro / OS 2.0)

This turns the A2 mockup into a REAL Shopify product template — the Add to Cart
buttons actually add to cart (they're native `{% form 'product' %}` forms), and the
title/price/images/variant are pulled live from the product.

## Files
- `sections/tallow-pdp.liquid` → the section (design + real product forms + schema)
- `templates/product.tallow.json` → the template that loads the section

---

## Step-by-step (Shopify admin, ~5 minutes)

1. **Back up first.** Online Store → Themes → (your live theme) → ⋯ → **Duplicate**. Work on the duplicate, or download a copy. Never edit live without a backup.

2. **Add the section file.**
   - Online Store → Themes → ⋯ → **Edit code**.
   - In the left panel under **Sections**, click **Add a new section**.
   - Name it exactly `tallow-pdp` (Shopify will create `sections/tallow-pdp.liquid`).
   - Delete the default contents, paste the entire contents of `sections/tallow-pdp.liquid`, **Save**.

3. **Add the template file.**
   - Under **Templates**, click **Add a new template**.
   - Choose: For **Product**, type **JSON**, name it `tallow`. Shopify creates `templates/product.tallow.json`.
   - Replace its contents with the contents of `templates/product.tallow.json`, **Save**.
   - (If the editor won't let you paste JSON, instead create the template named `tallow` and it will scaffold; then open it and ensure the single section is `tallow-pdp`.)

4. **Assign the template to the product.**
   - Products → open **Whipped Tallow & Honey Balm**.
   - Right sidebar → **Theme template** dropdown (the one in your screenshot) → select **tallow**.
   - **Save**.

5. **Set the price + anchor so the strikethrough shows.**
   - On the product/variant: set **Price = $49.99** and **Compare at price = $59.99** (or $69.99).
   - The template shows the strikethrough + "Save $X" automatically whenever Compare-at > Price. (Right now the variant is $69.99 with no compare-at, so no strikethrough would show — fix this or the anchor won't render.)

6. **Preview & test.**
   - Use **Preview** (eye icon) or the theme preview link. View on a phone (98% of traffic).
   - Click **Add to Cart** → confirm the item lands in the cart and checkout works.
   - Test the sticky mobile bar button and the bottom button too — all three are real forms.

7. **Edit copy without code (optional).**
   - In the theme **Customizer** (Customize → navigate to the product using this template), the "Tallow PDP" section exposes editable fields: announcement, badge, rating text, subtitle, shipping line, upsell note, the 3 proof stats, and the featured review (image/quote/author).

---

## Notes & guardrails

- **Images:** the gallery uses the product's own images (featured image = hero, next 3 = thumbnails). Upload real product/texture/lifestyle photos to the product. Hero image loads with high priority; thumbnails lazy-load. Use compressed webp where possible for speed.
- **Speed:** CSS is inline and scoped to `#tallow-pdp` (won't collide with Shrine). Below-fold sections use `content-visibility:auto`. The only external request is the Fraunces font (with display:swap). For maximum speed you can self-host Fraunces or swap to a system serif — ask and I'll wire it.
- **Single variant (120g):** the forms use `selected_or_first_available_variant`, so it works as-is. If you add variants later, we'll add a variant picker.
- **Reviews:** the featured review is one editable block. To show your full review widget (e.g. a reviews app), add its app block / snippet inside the `#tlw-reviews` section — tell me which app and I'll wire it.
- **This does NOT change your default product template.** Only the products you assign to `tallow` use it. Everything else is untouched.

---

## Rollback
If anything looks wrong: Products → the product → Theme template → set back to **Default product** → Save. The page reverts instantly. The section/template files can stay; they only apply when assigned.
