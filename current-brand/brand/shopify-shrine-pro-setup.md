# Baseline — Shopify Shrine Pro Theme Setup Guide

Reference for configuring the Shrine Pro theme with Baseline's brand identity (Modern Apothecary palette) and structuring the Product Detail Page for the soft launch 10-1 NMN product.

**Launch context:** This is a soft launch with one product — NMN 250mg capsules. No QR-to-COA batch verification system yet. The goal is to validate the product, learn from real customers, and build the foundation. The main selling point is NMN itself and the quality/purity behind it.

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

Ordered for the soft launch 10-1 NMN product. This is a single-product store — the PDP is essentially the entire buying experience. Every section earns the next scroll. The main selling point is NMN and its role in restoring NAD+ levels, backed by purity and transparent quality.

### Section Order

#### 1. Product Hero (Above the Fold)
- Product images (bottle front, bottle back with supplement facts, capsule close-up)
- Product title — clean, simple, led by the product name
- Short description (1-2 sentences hitting the core desire): "Restore the cellular energy your body has been losing since your 30s."
- Price with subscription toggle ($49/mo vs $55 one-time)
- Add to Cart / Subscribe button (Copper)
- Trust strip directly below button: "99%+ Pure | 3rd-Party Tested | 500mg Daily Dose"

**Why first:** This is the only shot at a first impression. The hero must communicate what this is, why it matters, and how to buy — all above the fold. Most visitors decide to stay or leave within 3 seconds.

#### 2. The Problem (NAD+ Decline)
- Simple visual showing NAD+ decline by age (chart or infographic)
- Headline addressing the core desire: "By 50, you've lost half the molecule that powers every cell in your body."
- 3-4 sentences at 6th-grade reading level explaining NAD+ decline
- Bridge to solution: "NMN is what your body uses to make more NAD+."
- Keep this short — educate, don't lecture

**Why second:** Before someone cares about your product, they need to feel the problem. This section creates the "oh no" moment — the realization that something important is declining and they didn't know. Without this, NMN is just another supplement. With it, NMN becomes the answer to a problem they now understand.

#### 3. How It Works (3-Step Mechanism)
- Step 1: You take 2 capsules daily (500mg)
- Step 2: Your body converts NMN into NAD+
- Step 3: Your cells get the fuel they need to repair, produce energy, and function like they used to
- Use icons or simple illustrations, not walls of text
- This section makes the product feel simple and accessible

**Why third:** Now that they feel the problem, they need to believe there's a simple solution. This section takes the science and makes it feel doable — three steps, no complexity. It answers "okay, but what do I actually DO?" and removes the intimidation factor.

#### 4. What Makes Baseline Different (Feature/Benefit Grid)
- 3 key differentiators in a clean grid or alternating layout:
  - **99%+ Purity, Enzymatic Synthesis** — real NMN your body can actually use, not rice flour in a capsule
  - **Every Batch Tested by Independent Labs** — purity, potency, heavy metals, microbial — all verified
  - **Clinically Relevant 500mg Daily Dose** — the dose used in human NMN research, not a token amount
- Each feature should pair with a short, benefit-driven sentence in customer language

**Why fourth:** At this point they understand the problem and the mechanism. Now the question becomes "why THIS NMN brand?" This section justifies why Baseline is worth choosing over cheaper alternatives. It's the "reason to believe" — purity, testing, and real dosing vs. the cheap underdosed products flooding the market.

#### 5. What's Inside (Ingredients Transparency)
- Clean supplement facts panel
- Call out: "No fillers. No proprietary blends. Every milligram accounted for."
- Full ingredient list, nothing hidden
- Optional: side-by-side comparison showing Baseline's clean label vs a typical NMN brand (proprietary blend, fillers, underdosed)

**Why fifth:** Trust is earned through proof. After the feature claims, this section backs them up visually — here's the actual label, here's exactly what's inside. For a supplement-skeptical audience, seeing a clean, transparent label does more than any paragraph of copy. It shows rather than tells.

#### 6. Social Proof / Reviews
- Customer reviews with star ratings
- Pull quotes that mirror the core avatar language: "I feel like I did 10 years ago," "My energy is back," "Finally a brand I actually trust"
- Filter by benefit (energy, clarity, recovery) if Shrine Pro supports it
- Include review count prominently
- **Soft launch note:** If reviews are limited at launch, use a "Be one of the first to try Baseline" framing or seed with testimonials from beta testers / friends & family batch

**Why sixth:** By now they believe the science and see the quality — but they want to know if it actually works for real people. Social proof converts belief into confidence. Even a small number of genuine reviews outperforms a wall of marketing copy.

#### 7. Subscription Value Block
- How subscription works: ships monthly, save $6/bottle, skip/pause/cancel anytime
- Address the objection: "No commitments. No hoops. One click to manage."
- Consistency messaging: "NMN works best when taken daily. We make that easy."
- Visual of subscription management (simple, clean UI)

**Why seventh:** The visitor is now educated and trusting — this section makes the buying decision easier by showing that subscribing saves money AND that they're never locked in. It reduces purchase anxiety and increases LTV at the same time.

#### 8. FAQ Accordion
- Target the top objections and questions:
  - "How long until I feel results?" (2-4 weeks for most people)
  - "Is NMN safe?" (well-studied, has a strong safety profile at clinical doses)
  - "How is this different from other NMN brands?" (enzymatic synthesis, third-party tested, clinically relevant dose)
  - "What if it doesn't work for me?" (money-back guarantee / return policy)
  - "Can I take it with other supplements?"
  - "Why is it $49-55 when some brands are $20?" (purity costs money — you get what you pay for)

**Why eighth:** This is the cleanup crew. Anyone still on the page at this point is interested but has one or two lingering doubts. The FAQ catches those objections before they become reasons to leave. It's not meant to sell — it's meant to remove the last barriers.

#### 9. Final CTA Block
- Repeat the core offer: product, price, subscription option
- Headline that re-anchors the desire: "Your cells are waiting."
- Add to Cart / Subscribe button
- Trust badges: independent lab tested, money-back guarantee
- This catches scrollers who read the full page and are now ready to buy

**Why last:** A significant percentage of buyers scroll the entire page before deciding. The final CTA gives them a clean, friction-free place to convert without scrolling back up. It re-anchors the emotional desire and makes the purchase feel like a natural next step, not a hard sell.

### Section Design Notes for Shrine Pro

- **Hero**: Use Shrine Pro's product page hero with sticky add-to-cart on scroll
- **Alternating sections**: Alternate between Cream (`#F5F0E8`) and White (`#FFFFFF`) backgrounds for visual rhythm
- **CTA blocks**: Use Teal Deep (`#0C3B3F`) as full-width background sections with Cream text — creates visual anchors
- **Feature grid**: Use Teal Tint (`#E8F2F1`) background to differentiate from standard sections
- **Copper accents**: Reserve for buttons, badges, and key callout text only — don't overuse
- **Typography**: Cormorant Garamond for section headlines, Plus Jakarta Sans for body and UI elements
