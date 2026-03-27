# Listicle A Image Prompts — B4: The 3pm Wall Hitter

> **Listicle:** "5 Reasons the 3pm Crash Gets Worse After 40"
> **Batch:** 4 (Avatar Call Out — 3pm Wall Hitter)
> **Tool:** Nano Banana Pro (Google Gemini). Also compatible with GPT Image, Midjourney, DALL-E 3, Flux.
> **Critical rule:** These images must look editorial — like something you'd see in a health journalism article. Not commercial. Not branded. Not polished. The listicle lives on a Shopify blog post and should feel like an independent article, not a product page.

---

## Image 1: The 3pm Desk (Hero Image)

**Placement:** Top of article, below the headline and intro paragraph.

**Purpose:** Sets the scene. The reader should see this image and think "that's my desk at 3pm." Instant recognition before they read a single numbered point.

**Prompt:**

```
A photorealistic photograph of a cluttered desk in harsh afternoon office lighting. The focal point is three coffee cups in various states: one full and untouched (just poured), one half-drunk and cold with no steam, and one completely empty with a dried coffee ring at the bottom. A laptop is open in the background showing a blurred spreadsheet. Scattered around: a phone showing 2:47 PM on the lock screen, a few pens, a crumpled granola bar wrapper, reading glasses pushed to the side, a sticky note with illegible writing. The desk surface is standard office gray or beige laminate. Overhead fluorescent lighting — flat, institutional, no warmth. The entire mood is: the afternoon slump, captured in one image. No people visible. Everything looks slightly abandoned, like someone pushed back from the desk to take a break. Smartphone camera quality, shot from slightly above at a natural angle, muted washed-out color palette. 16:9 aspect ratio.
```

**Post-production notes:**
- The three coffee cups at different stages tell the whole story visually: she keeps pouring coffee and it keeps not working.
- If the AI makes it look too clean or too staged, regenerate. This should look like a real person's real desk — imperfect, slightly depressing.
- Do NOT add any branding, text overlay, or product. This is editorial content.

---

## Image 2: NAD+ Decline Graph

**Placement:** Inside Section 1 ("It's Not Caffeine Tolerance. It's a Fuel Problem."), after the mention of NAD+ decline research.

**Purpose:** Makes the science visual. The decline stat becomes undeniable when it's a graph, not just a sentence. Builds credibility — this is published research, not opinion.

**Prompt:**

```
Clean, minimal scientific infographic showing NAD+ decline with age. A simple line graph on a white background with subtle light gray grid lines. X-axis: age from 20 to 70 in decade intervals. Y-axis: "Relative NAD+ Levels" from 0% to 100%. A single smooth curve in deep teal (#0c3b3f) starts near 100% at age 20-30, holds relatively steady until ~35, then begins a clear downward slope, declining steeply through ages 40-60, ending near 50% at age 60. Subtle shaded area under the curve in very light teal (#e8f0f0). A small dotted vertical line at age 40 with a text annotation: "Decline accelerates." Clean sans-serif typography (similar to Plus Jakarta Sans). No 3D effects, no gradients, no clutter. The style of a research paper figure or a quality health journalism graphic. Flat design, vector-style, 16:9 aspect ratio.
```

**Post-production notes:**
- AI models struggle with precise graph rendering. Best approach: use this prompt to generate the overall aesthetic, then recreate in Canva or Figma with exact data points.
- Use brand teal (#0c3b3f) for the curve instead of purple — matches the listicle tone (direct, factual).
- Add small source text at bottom: "Based on published NAD+ research. Illustration simplified for clarity."
- No branding. No logo. Editorial only.

---

## Image 3: The Supplement Graveyard (Optional)

**Placement:** Inside Section 3 ("Most Supplements You've Tried Don't Address This"), to visualize the failed supplement stack.

**Purpose:** Shows the reader their own experience — the pile of things they've already tried. Creates the "that's exactly me" moment visually before the copy explains WHY none of it worked.

**Prompt:**

```
A photorealistic overhead photograph of a bathroom shelf or kitchen counter with 5-6 supplement bottles and wellness products scattered in a disorganized cluster. Visible items: a magnesium bottle with a blue label, a bottle of B-complex vitamins, a greens powder tub with a green label half-used, a small amber bottle of vitamin D drops, an ashwagandha bottle with earthy branding, and a generic multivitamin. Some bottles have dust on the caps. One bottle is nearly empty with the cap off. A few loose capsules have spilled onto the surface. The arrangement is not styled — it looks like someone opened their cabinet and saw the mess. Natural overhead lighting, slightly cool bathroom tone. The image communicates: this is what "trying everything" looks like. Smartphone camera quality, shot from directly above, natural color temperature. 4:5 aspect ratio.
```

**Post-production notes:**
- This image mirrors B5C2's creative (supplement graveyard) but is shot overhead and editorial rather than designed-ad style.
- None of these bottles should look like Baseline. They're the competition's failures.
- If any AI-generated labels are too legible or reference real brands, blur them slightly in post.
- Optional image — the listicle works without it. Only include if it looks genuinely messy and real.

---

## Image 4: The 10-in-1 Formula Visual (Product Section)

**Placement:** At the bottom, inside "The Formula That Covers All of It" section, above the CTA.

**Purpose:** This is the ONE place where the product appears. It's the payoff — after 5 sections of education, the reader finally sees what the answer looks like. Must feel editorial (ingredient breakdown), not commercial (product hero shot).

**Build method:** Canva — not AI generated.

**Canva specs:**
- **Size:** 1080×1080 (1:1) or 1080×1350 (4:5)
- **Background:** Clean white or very light cream (#FAFAF7)
- **Layout:** Center the Baseline bottle (use actual product photo, cut out on white). Around the bottle, arrange 10 small text labels in a circular or semi-circular layout, each connected to the bottle with a thin teal (#0c3b3f) line:
  - NMN — 500mg
  - Resveratrol
  - CoQ10
  - Glutathione
  - TMG
  - Quercetin
  - Astaxanthin
  - Apigenin
  - Grape Seed Extract
  - Vitamin C
- **Typography:** Plus Jakarta Sans, 14-16pt, near-black. Clean, minimal.
- **Bottom text:** "$49.99 · 60-day supply · 30-day guarantee" in JetBrains Mono, 12pt, teal.
- **Mood:** Informational diagram, like an ingredient breakdown in a health magazine. NOT a marketing graphic.

---

## Image Priority

1. **3pm Desk** — highest impact, instant recognition, sets the tone for the entire listicle
2. **NAD+ Decline Graph** — makes the science tangible. Build in Canva if AI generation is imprecise.
3. **10-in-1 Formula Visual** — product section payoff. Canva build, use actual bottle photo.
4. **Supplement Graveyard** — optional. Include only if it looks genuinely messy and real.

---

## Usage in Shopify HTML

Upload images to Shopify (Settings → Files → Upload files) and insert at the specified placement points:

```html
<!-- Image 1: 3pm Desk — below intro -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Cluttered desk at 3pm with multiple coffee cups" style="max-width: 100%; border-radius: 8px;">
</div>

<!-- Image 2: NAD+ graph — inside Section 1 -->
<div style="margin: 20px 0;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Graph showing NAD+ decline with age" style="max-width: 100%; border-radius: 4px;">
  <p style="font-size: 12px; color: #999; margin-top: 6px;">Based on published NAD+ research. Illustration simplified for clarity.</p>
</div>

<!-- Image 3: Supplement graveyard — inside Section 3 (optional) -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Cabinet full of supplements that didn't work" style="max-width: 100%; border-radius: 8px;">
</div>

<!-- Image 4: 10-in-1 formula breakdown — above CTA -->
<div style="margin: 30px 0; text-align: center;">
  <img src="YOUR_SHOPIFY_FILE_URL_HERE" alt="Baseline NMN 10-in-1 ingredient breakdown" style="max-width: 100%; border-radius: 8px;">
</div>
```

Replace `YOUR_SHOPIFY_FILE_URL_HERE` with the actual file URL from Shopify's file manager after uploading.
