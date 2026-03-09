# CTA Product Reference — Baseline NMN

> This document is the single source of truth for linking CTAs to the Baseline NMN product.
> Any future CTA (homepage sections, landing pages, ads, email) should use these values.

---

## Store Info

| Field | Value |
|---|---|
| Store URL | `https://baseline-9962.myshopify.com` |
| Store CDN Path | `cdn.shopify.com/s/files/1/0978/0399/3409/` |
| Theme | Shrine Pro 1.3.0 |
| Product Template | `templates/product.json` (default) |

## Product Info

| Field | Value |
|---|---|
| Product Handle | `[GET FROM SHOPIFY ADMIN — see instructions below]` |
| Product URL | `https://baseline-9962.myshopify.com/products/[HANDLE]` |
| Product Price | $49.99 (one-time) / $42.95 (subscribe & save) |
| Product Name | Baseline NMN — Pure NMN Supplement, 500mg, 60 Capsules |

### How to Get the Product Handle & ID

1. Log into Shopify Admin: `https://baseline-9962.myshopify.com/admin`
2. Go to **Products** → click on the NMN product
3. **Product ID**: The number in the URL → `/admin/products/XXXXXXXXX` ← that number
4. **Product Handle**: Scroll down to **Search engine listing** → the URL slug is the handle
5. **UPDATE THIS FILE** with the handle once you have it

---

## CTA Locations That Need Product Linking

### 1. Shopify Theme — Homepage Sections (`templates/index.json`)

These `atc_product` fields are currently **EMPTY** and need the product handle:

| Section | Type | Field |
|---|---|---|
| Slideshow (slide 1) | `slideshow` | `atc_product` |
| Slideshow (slide 2) | `slideshow` | `atc_product` |
| Comparison Table | `comparison-table` | `atc_product` |
| Results | `results` | `atc_product` |

**To fix in Shopify Admin:**
1. Go to **Online Store** → **Customize**
2. Click on each section above
3. Set the **ATC Product** picker to the NMN product

### 2. Store Mockup (`current-brand/brand/store-mockup.html`)

| Line | CTA Text | Link Target |
|---|---|---|
| ~1193 | "Try Baseline NMN — 60-Day Supply" | `/products/[HANDLE]` |
| ~1368 | "See What's Actually in the Bottle — $49.95" | `/products/[HANDLE]` |
| ~1544 | "Start Your 60-Day Protocol — $49.95" | `/products/[HANDLE]` |

### 3. Product Page Sections (`templates/product.json`)

The product page's own CTA (Add to Cart) is handled automatically by Shopify via `{{ product }}` context — no manual linking needed.

---

## For Future CTAs

When creating ANY new CTA that links to the product, use:

**Shopify Liquid (theme sections):**
```liquid
<a href="{{ product.url }}">CTA Text</a>
```

**For sections with `atc_product` setting:**
Set to the product handle (e.g., `baseline-nmn-500mg` or whatever the handle is)

**Static HTML / Landing Pages / Ads:**
```
https://baseline-9962.myshopify.com/products/[HANDLE]
```

**Direct Add-to-Cart URL (skips product page):**
```
https://baseline-9962.myshopify.com/cart/add?id=[VARIANT_ID]&quantity=1
```
(Variant ID is also available in Shopify Admin → Products → Product → Variants)
