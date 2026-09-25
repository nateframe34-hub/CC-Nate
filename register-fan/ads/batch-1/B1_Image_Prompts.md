# Batch 1 — Nano Banana Pro 2 Image Prompts

**Created 2026-09-26.** For `B1_Ads.md` — SA1 The Fan Runner · Angle 1 · hot framing.

## Rules baked into every prompt below

| Rule | Source |
|---|---|
| **Generate whatever the ad calls for, including the product.** Founder call 2026-09-26 | — |
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

**Job:** show the reader their own house. The research found they describe this problem in **degrees, not metaphors** — four searches for icebox / sauna / meat locker returned nothing in their own words. The single most important element is that **a box fan is visibly running in the hot room**, because that is what turns a picture of the problem into a picture indicting the solution they already bought.

## Route A — full composite, generated in one pass

```
A vertical 4:5 advertising graphic. The top 62% of the frame is a side-by-side
photographic diptych; the bottom 38% is a clean typographic panel.

── THE DIPTYCH ──
Two square photographs sit side by side, separated by a thin 8-pixel vertical gutter of
warm off-white (#FAF7F2). Both are candid smartphone photographs taken on the same
afternoon, with matched camera height, matched distance, matched focal length and matched
white balance, so they read as a deliberate before/after pair shot by the same person.

LEFT PHOTOGRAPH — THE HALLWAY:
A small white digital room thermometer stands on a wooden hallway console table. It is a
plain rectangular household unit about the size of a pack of cards, with a large
high-contrast monochrome LCD screen angled slightly toward the camera. The display shows,
in crisp black seven-segment digits filling most of the screen:

    72°F

Beside the thermometer on the console: a set of keys on a small ceramic dish, and the
corner of an unopened envelope. Behind it, a plain painted hallway wall in a warm
off-white, with a framed picture edge just intruding at the top corner. Lighting is soft,
even, indirect afternoon daylight — flat, shadowless, unremarkable.

RIGHT PHOTOGRAPH — THE BEDROOM:
The same model of thermometer, photographed from the same distance and height, standing on
a wooden bedside table. The display shows, in the same crisp black seven-segment digits:

    81°F

Directly behind the thermometer, roughly a metre back and clearly out of focus, a black
plastic box fan sits on the carpet, running, its blades slightly motion-blurred, its grille
and its manufacturer's label visible — keep all product markings and branding on the fan
intact and natural, as a real fan in a real bedroom would look. Its white power cord runs
out of frame to the right. Behind that, a wall with hard, bright slabs of late-afternoon
sun falling across it through half-drawn venetian blinds, with visible slatted shadow
bands. The light in this panel is noticeably warmer, harder and higher-contrast than the
hallway panel — the two photographs should feel like different temperatures before the
viewer reads a single digit.

BOTH PHOTOGRAPHS: realistic consumer-phone image quality. Mild luminance grain, natural
white balance, slight handheld imperfection in framing, no HDR, no cinematic grade, no
vignette, no colour pop. The thermometers are the sharpest things in each frame and their
digits are perfectly legible, correctly formed and unambiguous.

── THE TYPOGRAPHIC PANEL ──
Below the diptych, a flat warm off-white (#FAF7F2) panel, no texture or gradient. Text is
set in a clean, confident geometric sans-serif, left-aligned, generous margins, clear size
hierarchy, in near-black (#1C1A17):

  Immediately under the photographs, small, uppercase, letter-spaced, in a muted grey,
  sitting under its own panel:
      "HALLWAY"        (left, under the left photograph)
      "BACK BEDROOM"   (right, under the right photograph)

  Large and bold:
      "Same house. Same afternoon. One fan running."

  Smaller, regular weight, comfortable line spacing:
      "The fan has been on all day. It moves the hot air around; it doesn't bring cold
      air in. That room is last on the duct run — it gets whatever's left after every
      other room takes its share."

  Smaller still, in warm terracotta (#B4553A), with the price plain and unemphasised at
  the end of the line:
      "Put the fan in the vent instead of the room. $89."

Typography must be crisp, correctly spelled, evenly kerned and fully legible at small
sizes. The layout is calm and editorial with real breathing room, not crowded.

STRICTLY EXCLUDE: any badge, sticker, starburst, ribbon, button, arrow, countdown timer,
guarantee mark, shipping icon, rating stars or promotional graphic furniture; any person,
hand or pet; any drop shadow, bevel, glow or 3D effect on the text; any watermark.

Aspect ratio 4:5, 1080 x 1350.
```

## Route B — diptych only, type set afterwards

Identical to Route A but **stop at the diptych** — generate only the two photographs and the gutter, filling the full 4:5 frame, and set the type yourself in Archivo/Inter to exact brand spec. Use this if the composite's typography drifts off-brand.

## Route C — single-frame variant worth testing

A tighter, more arresting version: **one photograph, both thermometers in it.**

```
A candid smartphone photograph, taken at eye level in a hot upstairs bedroom on a summer
afternoon. Two identical small white digital room thermometers stand side by side on a
wooden bedside table, about ten centimetres apart, both angled toward the camera. Their
large high-contrast monochrome LCD screens are the sharpest elements in the frame and
both are perfectly legible in crisp black seven-segment digits:

    the left unit reads   72°F
    the right unit reads  81°F

A small strip of masking tape is stuck to the table beneath each, with short handwritten
biro labels in ordinary untidy handwriting: "hallway" under the left, "in here" under the
right.

Behind them, roughly a metre back and clearly out of focus, a black plastic box fan sits
on the carpet, running, blades slightly motion-blurred, its grille and manufacturer's
label visible — keep all product markings and branding intact and natural. Beyond it, a
wall with hard bright slabs of late-afternoon sun through half-drawn venetian blinds,
with visible slatted shadow bands. Warm, high-contrast, airless light.

Shot as if on an iPhone, main wide lens, roughly 24mm equivalent, f/1.8, handheld, very
slightly tilted. Shallow depth of field on the fan, thermometers tack sharp. Realistic
phone-camera quality: mild grain, natural slightly warm white balance, no HDR, no
cinematic grade, no vignette.

STRICTLY EXCLUDE: people, hands, pets, text overlays, captions, badges, graphic furniture,
watermarks.

Aspect ratio 4:5, 1080 x 1350.
```

**Why Route C may beat the diptych:** one frame, two numbers, a fan running behind them, and handwritten labels — it reads as something a frustrated person actually did, rather than as a designed comparison. The handwriting is doing the authorship work.

## Notes on getting the digits right

- Seven-segment digits are the failure point. **Specify the reading twice** — once in the scene description and once as an isolated line — and regenerate rather than accept a garbled display.
- **Whole numbers with °F render more reliably** than decimals.
- The gap between the two readings is a creative choice. **Worth testing a smaller, more modest gap** (say `74°` / `80°`) against the wider one — a more believable number may outperform a more dramatic one with a sceptical reader.

# Cold-weather re-shoot notes

When the season turns, the concept is unchanged — only the props and light:

| | Hot version | Cold version |
|---|---|---|
| **B1C1** | Box fan on carpet, hard low sun, blinds half drawn | Small oil-filled radiator against the wall, flat grey overcast light through bare window, a folded blanket on the bed |
| **B1C2** | Same vent plate, unchanged | Same vent plate, unchanged |
| **B1C3** | Fan out of focus behind the bedroom thermometer | Space heater out of focus behind it |

**The vent photograph in B1C2 is season-agnostic and never needs re-shooting.**
