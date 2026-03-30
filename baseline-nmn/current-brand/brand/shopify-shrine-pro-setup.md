# Baseline — Shopify Shrine Pro Theme Setup Guide

Reference for configuring the Shrine Pro theme with Baseline's brand identity (Modern Apothecary palette) and structuring the Product Detail Page for the soft launch 10-in-1 NMN product.

**Launch context:** This is a soft launch with one product — NMN 10-in-1 Ultimate (500mg NMN + 8 synergistic longevity ingredients, available in 60/90/120ct). No QR-to-COA batch verification system. The goal is to validate the product, learn from real customers, and build the foundation. The main selling point is the comprehensive formula — 500mg clinical NMN dose plus resveratrol, CoQ10, glutathione, TMG, quercetin, astaxanthin, apigenin, and vitamin C.

---

## Part 1: Fonts

| Role | Font | Shrine Pro Setting |
|------|------|--------------------|
| **Headings** | Cormorant Garamond (400, 500, 600, 700) | Heading font |
| **Body** | Plus Jakarta Sans (300–700) | Body font |
| **Accent / Data** | JetBrains Mono (400, 500) | Custom CSS if needed — use for dosage callouts, data points |

Both Cormorant Garamond and Plus Jakarta Sans are available in Shopify's built-in font picker.

---

## Part 2: Color Mapping

### Primary Theme Colors

| Shrine Pro Setting | Color Name | Hex | Usage |
|--------------------|-----------|-----|-------|
| **Primary / Accent 1** | Deep Teal | `#0C3B3F` | Nav, headers, primary buttons, footer |
| **Accent 2** | Copper | `#C07840` | CTAs, sale badges, add-to-cart, highlights |
| **Background 1** | Cream | `#F5F0E8` | Main page background |
| **Background 2** | White | `#FFFFFF` | Cards, modals, product image backgrounds |
| **Text** | Near Black | `#1A1A1A` | Body copy, product descriptions |
| **Secondary text** | Warm Gray | `#5A5550` | Subtitles, meta text, secondary descriptions |
| **Outline / Border** | Sand | `#DDD6CC` | Dividers, input borders, card borders |

### Button Colors

| Element | Background | Text |
|---------|-----------|------|
| **Primary button** (Buy Now, Subscribe) | Deep Teal `#0C3B3F` | Cream `#F5F0E8` |
| **Primary button hover** | Teal Hover `#0A2F32` | Cream `#F5F0E8` |
| **Secondary button** (Add to Cart, Learn More) | Copper `#C07840` | White `#FFFFFF` |
| **Secondary button hover** | Copper Light `#D4944E` | White `#FFFFFF` |

### Extended Palette (Custom CSS / Section Settings)

| Purpose | Hex | When to Use |
|---------|-----|-------------|
| Teal Mid | `#165C5A` | Section backgrounds, gradient endpoints |
| Teal Light | `#1E7A77` | Links, hover states, inline text accents |
| Teal Tint | `#E8F2F1` | Light section alternates, feature blocks |
| Copper Glow | `rgba(192, 120, 64, 0.15)` | Subtle highlight backgrounds behind badges |
| Cream Dark | `#EBE4D8` | Alternate card backgrounds, divider sections |
| Success | `#3B8A6E` | In-stock indicators, trust checkmarks |
| Warning | `#C49A2A` | Low stock alerts, urgency messaging |

### Color Ratio

Use the **70/20/10 rule**:
- **70% Teal** — brand dominance, trust, authority
- **20% Cream/White** — breathing room, readability
- **10% Copper** — action, energy, draws the eye to CTAs

---

## Part 3: Product Detail Page (PDP) Sections

Ordered for the soft launch NMN 10-in-1 product. This is a single-product store — the PDP is essentially the entire buying experience. Every section earns the next scroll. The main selling point is the comprehensive formula: 500mg clinical NMN dose plus 8 synergistic longevity ingredients that support the full cellular ecosystem.

### Section Order

#### 1. Product Hero (Above the Fold)
- Product images (bottle front, bottle back with supplement facts, capsule close-up)
- Product title — clean, led by the product name: "Baseline NMN 10-in-1 — Complete Cellular Support"
- Short description (1-2 sentences hitting the core desire): "You didn't lose your energy. Your cells lost their fuel."
- Price with subscription toggle ($49.99 one-time vs $42.99/60 days subscribed)
- Packaging options: 60ct / 90ct / 120ct
- Add to Cart / Subscribe button (Copper)
- Trust strip directly below button: "500mg NMN Clinical Dose | 10 Longevity Ingredients | 98% Trans-Resveratrol | 30-Day Money Back"

**Why first:** This is the only shot at a first impression. The hero must communicate what this is, why it matters, and how to buy — all above the fold. Most visitors decide to stay or leave within 3 seconds.

#### 2. Is This You? (Message Match)
- 5 cards matching each ad batch avatar
- Each card mirrors the emotional state of a specific visitor segment
- No imagery needed — copy does the work
- Bridges from ad → PDP emotional thread

**Why second:** No matter which ad brought the visitor here, one of these cards mirrors their emotional state. This creates an immediate "this brand gets me" moment before we explain the product.

#### 3. How It Works (3-Step Mechanism)
- Step 1: You take 2 capsules daily (500mg NMN + 8 synergistic ingredients)
- Step 2: NMN converts to NAD+, resveratrol activates sirtuins, CoQ10 fuels mitochondria, TMG supports methylation, glutathione defends against oxidative stress
- Step 3: Your cells get complete support — energy, defense, and maintenance
- Use icons or simple illustrations, not walls of text
- This section makes a 10-ingredient formula feel simple and accessible

**Why third:** Now that they feel the problem, they need to believe there's a simple solution. This section takes 10 ingredients and makes them feel like one cohesive system — not a random grab bag. It answers "okay, but what do I actually DO?" and removes the intimidation factor.

#### 4. What's Actually Inside (Ingredient Breakdown)
- Full ingredient-by-ingredient breakdown with role explanation
- NMN foundation (500mg, fully disclosed dose)
- Each blend ingredient explained: what it does, why it's in the formula
- Highlight premium forms (98% trans-resveratrol, reduced glutathione, natural astaxanthin)
- "Why These 10 Together" — stack replacement value proposition

**Why fourth:** At this point they understand the problem and the mechanism. Now they want to know exactly what they're taking and why. This section builds trust through education — showing that every ingredient has a specific, researched role. For the 10-in-1, this is the most important trust-building section.

#### 5. The Science Behind NAD+ (Education)
- Simple visual showing NAD+ decline by age (chart or infographic)
- Synergy visual showing how the ingredients work together
- Lifestyle / energy imagery
- Bullet points reinforcing the formula's comprehensive approach

**Why fifth:** Deepens the science education with visuals. The ingredient breakdown told them WHAT's inside — this section shows them WHY it matters at the cellular level.

#### 6. Why Baseline? (Differentiators)
- 4 key differentiators:
  - **500mg NMN** — the full clinical dose, fully disclosed
  - **10 Synergistic Ingredients** — each chosen for a specific cellular role
  - **Stack Replacement** — replaces $150-300/month in separate supplements
  - **Premium Ingredient Forms** — 98% trans-resveratrol, reduced glutathione, natural astaxanthin
- Each differentiator pairs with benefit-driven copy

**Why sixth:** At this point they know what's inside. Now they need to understand why this formula is better than buying separate supplements or choosing a competitor. The "stack replacement" angle is the strongest differentiator — it saves money AND simplifies their routine.

#### 7. What Customers Are Saying (Social Proof)
- Customer reviews with star ratings
- Pull quotes emphasizing: stack simplification, energy consistency, value vs. separate bottles
- Include one 4-star honest review (Pratfall Effect)
- **Soft launch note:** Placeholder reviews written to match avatar language. Replace with real reviews as they come in.

**Why seventh:** By now they believe the science and see the quality — but they want to know if it actually works for real people. Reviews emphasize the stack simplification angle and real-world energy improvements.

#### 8. Guarantee + Subscription CTA
- 30-day money-back guarantee
- Subscribe & save details ($42.99/60 days)
- Launch pricing block (real urgency — price will increase)
- Free shipping on every order
- Final CTA with value reframe

**Why eighth:** The visitor is educated and trusting — this section makes the buying decision easy and addresses the last objections (risk, price, commitment).

#### 9. FAQ Accordion
- Target the top objections and questions:
  - "How long until I feel results?" (2-4 weeks for most people)
  - "Is this supplement safe?" (all ingredients well-studied)
  - "What makes this different from NMN alone?" (full cellular ecosystem support)
  - "Why is there a proprietary blend?" (honest answer about blend + disclosed NMN dose)
  - "I tried NMN before and it didn't work" (dose + supporting ingredients matter)
  - "Can I take this with other supplements?" (check for overlap)
  - "Why $49.99 when some NMN is $15-20?" (10 ingredients vs. one)
  - Plus sizing, subscription, timing, vegan/allergen, perimenopause, and more

**Why ninth:** The cleanup crew. Catches lingering doubts. The proprietary blend FAQ is critical — it addresses the elephant in the room honestly.

#### 10. Email Subscribe (Footer)
- Headline: "The Science of Feeling Like Yourself Again"
- Email capture for NAD+ research and longevity science updates
- Simple, non-pushy

**Why last:** Catches visitors who aren't ready to buy but are interested enough to stay connected. Builds the email list for future remarketing.

### Section Design Notes for Shrine Pro

- **Hero**: Use Shrine Pro's product page hero with sticky add-to-cart on scroll
- **Alternating sections**: Alternate between Cream (`#F5F0E8`) and White (`#FFFFFF`) backgrounds for visual rhythm
- **CTA blocks**: Use Teal Deep (`#0C3B3F`) as full-width background sections with Cream text — creates visual anchors
- **Feature grid**: Use Teal Tint (`#E8F2F1`) background to differentiate from standard sections
- **Copper accents**: Reserve for buttons, badges, and key callout text only — don't overuse
- **Typography**: Cormorant Garamond for section headlines, Plus Jakarta Sans for body and UI elements
