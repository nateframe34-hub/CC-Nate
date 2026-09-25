# Batch 1 — Nano Banana Pro 2 Image Prompts

**Created 2026-09-26.** For `B1_Ads.md` — SA1 The Fan Runner · Angle 1 · hot framing.

## Rules baked into every prompt below

| Rule | Source |
|---|---|
| **Never generate our product.** No prompt renders the vent thermostat | `Offer_Structure.md` §4b |
| **Never write "unbranded" / "no logos" / "no brand marks."** Tested: prop branding has zero measurable CPM impact, and a de-labelled object reads as staged. Natural branding stays | Tallow Creative Principles §0 |
| **No offer terms rendered in the image** — no guarantee badge, shipping strip, discount flash, countdown or CTA button. A plain inline price line is allowed | Brand_Mastery 1e / TOF rule |
| **Degrees in mono tabular figures.** Terracotta `#B4553A` · base `#FAF7F2` · text `#1C1A17` | Brand system A3-A4 |
| **It must not look generated.** Interrupt traffic rewards authenticity — imperfection is specified deliberately | Static_Ad_Framework |

---

# B1C1 — Native scene image *(no text, no product)*

**Job:** an authorless photograph that looks like someone stood in a doorway and took it without thinking. It runs above ~1,000 words of first-person copy, so it must not compete — it must corroborate.

### PROMPT — primary

```
A candid, unposed smartphone photograph taken from the open doorway of an ordinary
upstairs bedroom in a North American suburban house, late afternoon in summer.

SUBJECT AND STAGING: A black plastic box fan sits directly on the beige carpet in the
middle-left of the frame, angled up toward an unmade double bed, running. Its power
cord trails across the carpet to a white baseboard outlet on the right wall. The fan is
an ordinary hardware-store model with its manufacturer's label and control dial visible
and legible — keep all product markings and branding intact and natural, exactly as a
real fan in a real room would look. On the nightstand: a half-full glass of water with
condensation running down it, a paperback book lying face-down and open, a phone
charging cable. The duvet is pushed down to the foot of the bed and crumpled.

LIGHT: Strong, low, late-afternoon sun entering through a west-facing window on the far
wall, venetian blinds drawn about two-thirds down. Hard, bright slabs of sunlight fall
across the duvet and part of the carpet, with visible slatted shadow bands. The light is
warm and slightly orange, high contrast, the kind that makes a room feel hot. A faint
haze of dust is visible in the light shaft. No artificial lights are on.

CAMERA: Shot as if on an iPhone, main wide lens, roughly 24mm equivalent, f/1.8,
handheld at chest height from the doorway. Natural, slightly imperfect framing — the
horizon is very slightly tilted, the composition is not centred, the doorframe intrudes
into the left edge. Deep focus; everything reasonably sharp.

RENDERING AND GRADE: Realistic consumer-phone image quality. Mild luminance noise in the
shadows, slight highlight clipping in the brightest part of the sunlit duvet, subtle
chromatic aberration at the window edge, very slight motion blur on the fan blades from
the shutter speed. Natural white balance, a touch warm. No HDR look, no cinematic
grading, no vignette, no bokeh effect, no colour pop.

MOOD: Hot, still, lived-in, slightly airless. An ordinary room on an uncomfortable
afternoon. Nothing is styled.

STRICTLY EXCLUDE: any people, hands or pets; any text, caption, watermark, logo overlay
or graphic element added on top of the photograph; any air vent, register or vent-mounted
device anywhere in frame; any studio or professional lighting; any staged or
interior-design-magazine quality.

Aspect ratio 4:5, 1080 x 1350.
```

### PROMPT — variant B *(two fans, escalation)*

As above, but: **two** fans in the room — the box fan on the carpet and a white oscillating tower fan standing near the window, both running. This visualises the escalation beat in the copy (*"then I bought a second one"*) and is worth testing as the stronger recognition image.

---

# B1C2 — The reframe static

**Two production routes. Use route A for speed, route B for brand precision.**

## Route A — full composite generated in one pass

Nano Banana Pro 2 renders typography reliably. This gets a finished ad in one generation.

```
A vertical 4:5 advertising graphic, split vertically into two panels.

LEFT PANEL (occupying the left two-thirds of the frame): a realistic, candid smartphone
photograph of an ordinary white metal wall register — an air vent with horizontal louvred
slats and two visible screws — mounted low on a plain painted interior wall just above a
white baseboard. Beige low-pile carpet runs along the bottom. Soft, flat, indirect daylight
from the left. The paint has faint scuffs and the vent has a little dust on the lower
slats. Realistic phone-camera quality, mild grain, natural white balance, no styling. The
vent is a plain builder-grade cover; it is NOT a fan and has no electronics, no display and
no cable.

RIGHT PANEL (occupying the right third, full height): a flat solid panel of warm terracotta,
hex #B4553A, with no texture or gradient. Text is set in this panel in a clean, confident
geometric sans-serif, left-aligned, in off-white #FAF7F2, with generous margins and clear
size hierarchy:

  Large and bold, at the top:
  "You already tried a fan in there."

  Smaller, regular weight, in the middle, with comfortable line spacing:
  "A fan cools you, not the room. Step three feet away and it's as hot as it was.
  This isn't a fan for the room — it's a fan for the vent. It pulls in the cold air
  your AC already made."
  The word "vent" is set in bold for emphasis.

  Small, near the bottom:
  "The room gets cooler. Not just the spot in front of the fan."

  Smallest, at the very bottom, plain and unemphasised:
  "$89"

Typography must be crisp, correctly spelled, evenly kerned and fully legible at small
sizes. The layout is calm and editorial, with a lot of breathing room — not crowded.

STRICTLY EXCLUDE: any badge, sticker, starburst, ribbon, button, arrow, countdown timer,
"money-back guarantee" mark, shipping icon, rating stars, or any promotional graphic
furniture of any kind; any person; any vent fan, motor, grille-mounted device or product
photograph; any drop shadow, bevel, glow or 3D effect on the text.

Aspect ratio 4:5, 1080 x 1350.
```

## Route B — photograph only, type set in design software

Generate the plate, then set Archivo / Inter to exact brand spec. Preferred if the composite's typography drifts off-brand.

```
A realistic, candid smartphone photograph of an ordinary white metal wall register — an
air vent with horizontal louvred slats and two visible screws — mounted low on a plain
painted interior wall just above a white baseboard, shot straight on from about knee
height. Beige low-pile carpet along the bottom of the frame. Soft, flat, indirect
daylight from the left, no hard shadows. Faint scuffs on the paint, a little dust
settled on the lower louvres, one screw very slightly proud. Utterly ordinary and
unremarkable. Realistic phone-camera quality with mild grain and natural white balance.
Composition leaves clear empty wall space above the vent for text to be placed later.

The vent is a plain builder-grade cover. It is NOT a fan: no electronics, no display,
no dial, no cable, no vent-mounted device.

STRICTLY EXCLUDE: people, hands, pets, text, captions, watermarks, graphic overlays,
studio lighting, styled interiors.

Aspect ratio 4:5, 1080 x 1350.
```

---

# B1C3 — The two-thermometer demonstration

> ## ⚠️ DO NOT GENERATE THIS ONE. SHOOT IT.
>
> **Three reasons, and the first is the one that matters:**
>
> 1. **The entire persuasive power of this ad is that it looks like someone documenting their own house.** A generated "photograph" of a measurement is a fabricated measurement dressed as evidence. Everything else in this batch is a scene; this one is a *claim about a reading*.
> 2. **Generated displays render badly.** Seven-segment digits come out garbled, inconsistent or nonsensical at small sizes — and the numbers are the whole ad.
> 3. **It costs $20 and an afternoon.** Two identical cheap digital thermometers, a hallway, a hot bedroom, a box fan, one afternoon. Cheaper than iterating a prompt.
>
> **Shoot spec:** same thermometer model twice, same camera, same distance, same height, same white balance, within ten minutes of each other. Hallway on a console table; bedroom on a nightstand with the box fan visible and out of focus behind it. Let the readings be whatever they genuinely are — **the real numbers are better than chosen ones**, and if the gap is small that is worth knowing before we build a campaign on it.

### If a placeholder is needed for layout only

Clearly marked as a mockup, never published:

```
MOCKUP FOR LAYOUT ONLY — NOT FOR PUBLICATION.

A vertical 4:5 image split into two equal square panels side by side with a thin warm
off-white gutter between them.

LEFT PANEL: a candid smartphone photograph of a small white digital thermometer with a
simple LCD display, sitting on a wooden hallway console table beside a set of keys. Plain
painted wall behind. Soft, even, indirect daylight.

RIGHT PANEL: the same model of thermometer, photographed from the same distance, height
and angle, in the same light, sitting on a bedside table in a bedroom. A black box fan is
visible behind it, out of focus, clearly running. Late afternoon sun through blinds falls
across the wall behind.

Both thermometer displays show clear, crisp, unambiguous seven-segment digits.
Realistic phone-camera quality in both panels, mild grain, natural white balance, no
styling, no HDR.

STRICTLY EXCLUDE: people, hands, text overlays, captions, badges, graphic furniture, any
vent-mounted device or product.

Aspect ratio 4:5, 1080 x 1350.
```

**Leave the readings to be composited from the real shoot. Do not let a generative model invent the numbers.**

---

# Cold-weather re-shoot notes

When the season turns, the concept is unchanged — only the props and light:

| | Hot version | Cold version |
|---|---|---|
| **B1C1** | Box fan on carpet, hard low sun, blinds half drawn | Small oil-filled radiator against the wall, flat grey overcast light through bare window, a folded blanket on the bed |
| **B1C2** | Same vent plate, unchanged | Same vent plate, unchanged |
| **B1C3** | Fan out of focus behind the bedroom thermometer | Space heater out of focus behind it |

**The vent photograph in B1C2 is season-agnostic and never needs re-shooting.**
