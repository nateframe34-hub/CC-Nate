# Batch 1 — Nano Banana Pro 2 Image Prompts · FULL SPEC

**Rebuilt 2026-09-26 (founder: "literally as detailed as possible — fonts, colors, everything").**
For `B1_Ads.md` — SA1 The Fan Runner · hot framing. Canvas for every ad: **4:5, 1080 × 1350 px.**

---

## 0. How to use this file

### 0a. Product reference images — attach them every time the product appears

Nate is supplying real photos of our vent cover. **Any prompt that shows the product must be run with those photos attached**, labelled in this order:

| Ref | What it is |
|---|---|
| **REF-1** | The only supplied reference: the product on white with its remote. Everything else is carried by the written description in the lock |

Paste this **PRODUCT LOCK** block into any prompt that contains the product (it is already included below where needed):

```
PRODUCT LOCK — one reference image is attached (REF-1: the product on white, with its
remote). Use it ONLY for the product's appearance. Do not copy its white background,
its layout, or the remote unless this prompt asks for the remote.

The product, described precisely so it survives any angle:
- A flat rectangular floor register cover, about 2.4 times as wide as it is tall
  (roughly 12 x 5 inches overall for the 4x10 size), with a thin raised rim and softly
  rounded corners. One piece of moulded plastic.
- FINISH: [WHITE] matte bright white, like a white appliance, #F4F4F2.
  [BRONZE] dark oil-rubbed bronze, a deep brown-black with a faint warm metallic sheen,
  around #3B2F28. Not copper, not rose-gold, not pink, not shiny brass.
- LEFT ~70% OF THE FACE: a rectangular grille opening with rounded inner corners, filled
  by 18 thin, evenly spaced VERTICAL bars (they run top to bottom, not side to side),
  the same colour as the faceplate. Behind the bars, two identical round fans side by
  side, each with a dark charcoal-grey circular shroud and a black 5-blade impeller with
  broad curved blades and a small round hub.
- RIGHT ~25% OF THE FACE: a vertical black glossy display panel, taller than it is wide.
  Top of the panel: two small white icons with tiny labels. Middle: a large white
  seven-segment digital readout of the temperature followed by a small "°F". Bottom:
  four small white icons in a 2x2 grid (a flame, a snowflake, a fan, a crescent moon)
  with tiny labels under each.
- To the right of the display, two narrow vertical strips of small square black
  buttons with white symbols: an upper strip of 3 (power, and two mode buttons) and a
  lower strip of 3 (a mode button, "+", "−").
- Two round countersunk screw holes, one at each short end of the faceplate, centred
  vertically — left of the grille and right of the buttons.
- No logo, no brand name and no other text on the faceplate.
- REMOTE (only when asked for): a slim light-grey rounded-rectangle remote with a red
  power symbol top-left, a pill-shaped +/− temperature rocker in the middle, and small
  grey icon buttons (flame, leaf, snowflake, fan, moon) with tiny labels.

Match this exactly. Do not redesign, add fans, change the bar direction, move the
display, add a logo, or change the colour. The display must read exactly the number
given in this prompt (e.g. "72°F"), not "188".
```

### 0b. Brand tokens — the only colours and fonts used on any designed element

| Token | Value | Use |
|---|---|---|
| Terracotta (accent) | **`#B4553A`** · RGB 180/85/58 | Text bands, emphasis |
| Warm off-white (base) | **`#FAF7F2`** · RGB 250/247/242 | Text on terracotta, backgrounds |
| Warm near-black (text) | **`#1C1A17`** · RGB 28/26/23 | Text on light backgrounds |
| Slate (diagram only) | `#5B7185` | Never on ads |
| Headline font | **Archivo**, ExtraBold (800) | All headlines |
| Body font | **Inter**, Regular (400) / Medium (500) / SemiBold (600) | All supporting lines |
| Numbers font | **JetBrains Mono**, Medium (500), tabular figures | Every temperature and every price |

**Fonts in generators drift.** Nano Banana renders type well but cannot guarantee a named font. Every designed ad therefore has two routes:
- **Route A — one-pass composite.** Fast. Check the type against the spec; regenerate if it drifts.
- **Route B — plate + typeset. Preferred for launch.** Generate the photo with empty space, then set the exact type in Figma/Canva/Photoshop using the spec tables. Pixel-exact, on-brand, editable.

### 0c. Standing rules in every prompt

- **Real prop branding stays.** Never write "unbranded", "no logos" or "no brand marks". Fans, laptops, bottles, markers show their normal manufacturer marks.
- **It must look like a real photo, not a render.** Imperfection is specified on purpose: grain, slight tilt, dust, scuffs, lived-in clutter.
- **No added promotional furniture**: no badges, stickers, starbursts, buttons, arrows-as-graphics, countdowns, star ratings. (A price line is allowed where the spec calls for one.)

---

# B1C1 — Native scene image *(no text, no product)*

**Job:** the image above ~1,400 words of Julie's first-person story. It shows the room she gave up on, exactly as she describes it: upstairs home office, west window, hot sun, a box fan on the carpet aimed at the desk, a tower fan by the window, a closed laptop. It must look like she stood in the doorway and took it without thinking.

**Product:** NOT in frame. No vent cover of any kind.

## Prompt

```
A candid, unposed smartphone photograph taken from the open doorway of a small upstairs
home office in an ordinary North American suburban house (1990s–2000s build), at about
3:45 pm on a very hot, cloudless day in late July.

ROOM: Roughly 10 by 11 feet. Walls painted a flat warm greige (close to #D9D2C5), slightly
scuffed at chair height. White painted baseboards (#F2F0EB) with a dust line along the
top edge. Beige low-pile wall-to-wall carpet (#C9B9A0) with visible vacuum tracks and a
slightly flattened path from the door to the desk. White six-panel door, opened inward,
its edge and the doorframe intruding into the left 8% of the frame, slightly out of focus.

WINDOW: One window centred on the far wall, west-facing, about 4 feet wide. White vinyl
horizontal mini-blinds lowered two-thirds of the way and tilted half-open. A thin cord
dangles. Through the gaps: overexposed white-blue sky and the blurred green top of a tree.

DESK: A plain white laminate desk (IKEA-style, simple rectangular top, metal legs) against
the right-hand wall, perpendicular to the window. On it: a closed silver laptop with its
manufacturer logo visible on the lid; a clear drinking glass two-thirds full of water with
heavy condensation, beads running down, and a wet ring spreading on the desk beneath it;
a yellow legal pad with a pen lying diagonally across it; a phone charging cable looping
off the back edge; a mug holding pens. A black mesh office chair pushed back from the
desk and turned slightly toward the door, as if someone just got up.

FAN 1: A black plastic 20-inch box fan standing directly on the carpet about 3 feet from
the desk, angled upward toward the chair. Running — the blades are a soft motion blur.
The manufacturer's name plate and its rotary speed dial are visible and legible on the
front corner, exactly like a real store-bought fan. Its grey power cord trails across the
carpet in a loose S-curve to a white duplex outlet on the baseboard of the right wall.

FAN 2: A white oscillating tower fan, about 40 inches tall, standing on the carpet to
the left of the window, also running, turned to face the desk. Its brand name and
control buttons are visible on the top panel. Its cord runs along the wall to the same
side.

LIGHT: Hard, low, late-afternoon sun (around 4500 K, warm golden-orange) coming through
the blinds, casting bright slatted stripes across the desk surface, the chair, and a wide
patch of carpet. High contrast: the sunlit stripes nearly blow out, the shadows are warm
brown, not black. Fine dust motes visible in the light shaft. No lamps on. The room feels
hot, still and airless.

CAMERA: As if shot on an iPhone 15, main wide lens (~24 mm equivalent), f/1.8, handheld at
chest height (about 4.5 feet) from the doorway, pointing slightly down. The horizon is
tilted about 2 degrees clockwise. Composition not centred: the window sits slightly left
of centre, the desk and chair occupy the right third, the box fan the lower centre. Deep
focus; everything reasonably sharp except the door edge.

RENDERING: Real phone-camera image quality — mild luminance noise in the shadows, a little
highlight clipping in the sunlit stripes, faint chromatic fringing along the window edge,
slight motion blur on both fans' blades, slightly warm auto white balance. No HDR look,
no cinematic colour grade, no vignette, no lens flare effects, no bokeh balls.

MOOD: A room someone has quietly given up on. Nothing styled, nothing arranged for a photo.

EXCLUDE: people, hands, pets; any text, caption, watermark, sticker or graphic overlay;
any air vent, floor register, wall register or vent-mounted device; air conditioner
units; studio lighting; magazine-interior styling; plants arranged decoratively.

Aspect ratio 4:5, 1080 x 1350.
```

## QA before using
- [ ] Two fans, both clearly running (blade blur), box fan on the floor aimed at the desk
- [ ] Laptop **closed**, glass sweating, chair pushed back — she's just left
- [ ] Sunlight is hard and slatted; the room reads hot at thumbnail size
- [ ] No vent visible anywhere
- [ ] Passes the caption test: *"two fans and it's still 84 in here"*

---

# B1C2 — Relatable Hook · copied from the swipe file

**Format:** **Relatable Hook**, copied as closely as possible from the swipe file's ComfortWear "12-HOUR SHIFT SHOES" ad (`origins-training/swipe-file/relatable-hook.jpg`). Founder call 2026-09-26: when using a swipe, copy it closely.

**What the swipe ad does, and our version of each part:**

| Swipe ad | Ours |
|---|---|
| Plain white background, nothing else | Plain white `#FFFFFF` background |
| Huge bold black headline at top that names the situation and the thing | **NO MORE SWITCHING ROOMS / BECAUSE OF THE HEAT.** |
| Five bullet lines, each starting with an orange-red **+**, features written for that situation | Five **+** bullets in terracotta, features written for the hot-room situation |
| Large product photo in the lower half, three-quarter angle, soft reflection, clean product shot | The vent cover, three-quarter angle, soft reflection, display reading 72°F |
| No price, no logo, no button | Same |

**Earlier versions retired:** the text-band design (not a swipe format) and the edited C1 room with chips (didn't match the swipe: no product, no features).

## Why the swipe uses those bullets, and ours line for line

The shoe ad's bullets aren't a feature list. They follow a strict sequence, and every line is built the same way: **[feature or claim] for [a specific problem this person already names]**.

| # | Swipe bullet | Job it does | Our bullet | Why it maps |
|---|---|---|---|---|
| 1 | Made affordable for healthcare essential workers | **Who it's for + the price objection.** Tells the nurse "this is for you" and answers "can I afford it" first, before any feature | **A fraction of what a contractor quotes for ductwork** | Our price objection is measured against the fix they already priced or assume ($3–4k duct rebalancing, sourced). It settles "is this affordable" in their own reference point |
| 2 | Comfortable for back-to-back 12-hour shifts | **Restates the headline situation as the core outcome.** Repeats the pain from the headline, now promised away | **Comfortable through long afternoons in the hot room** | Same move: the headline's situation (switching rooms because of heat) comes back as the outcome |
| 3 | Arch support for plantar fasciitis foot pain | **Feature → a named pain they have.** Uses their own term for the problem | **Twin fans for vents that barely blow any air** | "Barely any air" is their words for the problem, from the research and the hand test. The fans are the feature that answers it |
| 4 | Slip-resistant grip for fluids and slippery floor | **Feature → their specific environment.** Proves it was made for their world, not generic | **Its own thermostat, separate from the hallway one** | Their environment is one room hotter than the rest. The thermostat is the feature built for exactly that |
| 5 | Wide toe-box for bunions/hallux valgus | **Feature → a sub-group's objection or condition.** Pulls in people who assume "won't work for me" | **Two-screw drop-in install. No contractor needed** | Our "won't work for me" is "this is a project / I'm not handy / I rent." The install answers it |

**Swipe bullet 6 ("#1 rated for comfort & cushion", proof to close) is left out on purpose.** We have no rating yet, and a guarantee isn't the same job (founder call). Add a real rating line as bullet 6 once reviews exist.

**Rules the swipe follows, and so do ours:** one line each · starts with the feature or claim · ends on their problem in their words · no adjectives doing the work ("amazing", "premium") · the sequence runs who/price → outcome → three feature-for-pain lines.

## ⭐ THE PROMPT — one pass, final image (founder: no edits, no Canva)

**Attach:** REF-1 (the product photo with the remote) and nothing else. Paste everything inside the box.

```
Create ONE finished, ready-to-post social media advertisement image, exactly 1080 pixels
wide by 1350 pixels tall (4:5 portrait). It is a simple, clean direct-response product
ad in the style of a classic "headline + plus-sign bullet list + product photo on white"
e-commerce ad. Everything below must appear in the single image. Nothing else.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. CANVAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Background: one flat, pure, solid white (#FFFFFF) across the entire image, edge to
  edge. No gradient, no texture, no vignette, no border, no frame, no drop shadow around
  the edges, no floor line, no horizon, no room, no scene.
- Margins: 64 px of empty white on the left and right of all text. 70 px empty white at
  the top. At least 60 px empty white at the bottom below the product.
- Three zones stacked top to bottom: HEADLINE (top), BULLET LIST (middle), PRODUCT PHOTO
  (bottom half).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
2. HEADLINE — top zone, from y = 70 px to about y = 235 px
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Text, exactly, on exactly two lines, ALL CAPITAL LETTERS:
      Line 1:  NO MORE SWITCHING ROOMS
      Line 2:  BECAUSE OF THE HEAT.
  (the full stop after HEAT is included)
- Typeface: a heavy, bold, tightly spaced geometric grotesque sans-serif — Archivo
  ExtraBold (weight 800) or the closest match (e.g. Poppins ExtraBold / Montserrat
  ExtraBold). Flat, solid letterforms. NOT condensed, NOT italic, NOT outlined, NOT a
  serif, NOT a script, NOT rounded.
- Size: cap height about 52 px (font size about 72 px). Line 1 spans roughly 900 px of
  the 952 px text width. Line 2 is shorter.
- Letter spacing slightly tight (about −1%). Line spacing tight: the two lines sit close,
  about 76 px baseline to baseline.
- Colour: solid near-black #111111. No shadow, no glow, no outline, no gradient.
- Alignment: flush LEFT at x = 64 px. Not centred.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
3. BULLET LIST — middle zone, first bullet about 60 px below the headline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- Exactly FIVE bullets, each on ONE single line (no line may wrap), in this exact order
  and wording:
      +  A fraction of what a contractor quotes for ductwork
      +  Comfortable through long afternoons in the hot room
      +  Twin fans for vents that barely blow any air
      +  Its own thermostat, separate from the hallway one
      +  Two-screw drop-in install. No contractor needed
- The "+" marker: a bold plus sign in solid terracotta #B4553A (a warm burnt
  orange-red), about 34 px tall, vertically centred on the text line, left edge at
  x = 64 px. The same plus sign for all five. Not a bullet dot, not a checkmark, not an
  emoji.
- Bullet text: starts at x = 110 px. Typeface a clean, neutral, regular-weight sans-serif
  — Inter Regular (400) or the closest match (e.g. Poppins Regular / Helvetica). Font size
  about 33 px. Colour solid dark charcoal #222222. Sentence case exactly as written
  (capital first letter only, plus "No" after the full stop in bullet 5).
- Even spacing: about 60 px baseline to baseline, identical between every bullet. All
  five left edges perfectly aligned.
- Punctuation exactly as written: a comma after "thermostat" in bullet 4; a full stop
  after "install" in bullet 5; no full stops at the end of any bullet. "Two-screw" and
  "drop-in" are hyphenated.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4. PRODUCT PHOTO — bottom zone, from about y = 690 px to about y = 1270 px
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Use the attached reference image ONLY to get the product's exact appearance. Do NOT
include the remote control from the reference. Do not copy the reference's layout.

THE PRODUCT (match the reference exactly):
- A flat rectangular WHITE floor vent cover (register) with two built-in fans. About 2.4
  times as wide as it is tall. One piece of matte bright-white moulded plastic (#F4F4F2),
  a thin raised rim around the edge, softly rounded outer corners.
- LEFT about 70% of the face: a rectangular grille opening with rounded inner corners,
  crossed by 18 thin, evenly spaced VERTICAL white bars running top to bottom (not
  horizontal louvres). Behind the bars, two identical round fans side by side, each with
  a dark charcoal-grey circular shroud and a black five-blade impeller with broad,
  curved blades and a small round centre hub.
- RIGHT about 25% of the face: a vertical, glossy black display panel, taller than it is
  wide. At its top, two small white icons with tiny labels. In its middle, a large white
  seven-segment digital readout showing exactly "72" followed by a small "°F". At its
  bottom, four small white icons in a 2 x 2 grid (a flame, a snowflake, a fan, a
  crescent moon) with tiny labels under each.
- To the right of the display: two narrow vertical strips of small square black buttons
  with white symbols — an upper strip of three (power symbol at top) and a lower strip
  of three (a mode button, then "+", then "−").
- One round countersunk screw hole at each short end of the faceplate, centred
  vertically: one left of the grille, one right of the buttons.
- No logo, no brand name, no other text anywhere on the product. Exactly two fans.
- THE DISPLAY MUST READ "72°F". It must NOT read "188" or any other number.

HOW IT IS SHOT:
- A clean, professional e-commerce product photograph on the same pure white background
  as the rest of the ad — it sits directly on the ad's white with no box, panel, border
  or visible edge around it, seamlessly part of the canvas.
- Angle: seen from the front and slightly above, the product turned about 15 degrees to
  the left (so the display end is nearer the camera) and tilted back about 20 degrees,
  like a product lying on a white surface photographed from a low front angle. The whole
  faceplate is clearly visible: every vertical bar, both fans, and the full display with
  "72°F" crisp and legible. A thin sliver of the housing's depth shows along the bottom
  edge.
- Size and position: horizontally centred, about 860 px wide (from roughly x = 110 to
  x = 970), vertically centred in the bottom zone.
- Lighting: bright, soft, even studio light from above and front-left, like a big
  softbox. The white plastic looks clean and crisp with gentle grey shading on the rim
  and inside the grille; the fans read dark behind the white bars; the black display is
  glossy with one soft, subtle highlight that does not cover the digits.
- A soft, faint mirror reflection of the product on the white surface directly beneath
  it, about 20% opacity, fading to nothing within about 60 px. A very soft grey contact
  shadow where it meets the surface.
- Tack sharp everywhere. Realistic plastic, not a cartoon, not a 3D-render look, not
  plastic-toy shiny.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
5. ABSOLUTELY DO NOT INCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- The remote control. Any hand, person, pet, plant or furniture. Any room, floor, wood,
  carpet or background scene.
- Air-flow swirls, wind lines, leaves, snowflakes, sparkles, glow effects or any visual
  effect showing air or temperature.
- Any logo, brand name, wordmark, price, "$", "Shop now" button, badge, sticker, seal,
  star rating, ribbon, arrow, banner, border or frame.
- Any text other than the headline and the five bullets. No extra words on the product.
- Copper, rose-gold, pink, bronze, grey or cream product colour — the product is WHITE.
- Horizontal grille slats, more or fewer than two fans, the display on the left side.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
6. FINAL CHECK BEFORE OUTPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Every word is spelled exactly as given. The headline is exactly two lines. There are
exactly five bullets, each one line, each with a terracotta "+". The product is white,
has vertical bars, two fans, and a display on the right reading "72°F". The background
is pure white everywhere. The image is 1080 x 1350.
```

## If a generation misses (re-run, don't edit)

| Miss | Add to the end of the prompt and re-run |
|---|---|
| A bullet wraps to two lines | *"Reduce the bullet font size slightly so every bullet fits on one line."* |
| Display shows 188 or garbled digits | *"The display digits are the most important detail: exactly 72 then °F, large and legible."* |
| Remote appears | Crop the reference to remove the remote before attaching, then re-run |
| Horizontal slats / wrong fan count | *"Copy the grille from the reference exactly: vertical bars, two fans."* |
| Headline centred or thin | *"The headline is left-aligned and extra-bold, matching the heaviest weight available."* |
| Product looks rendered or toy-like | *"Photograph it like a real Amazon main image: realistic matte plastic, natural soft shadows."* |

## QA before using
- [ ] Looks like the swipe ad at a glance: white, big black headline, + bullets, product below
- [ ] Headline breaks exactly as specified; all five bullets spelled right, one line each
- [ ] Product matches the reference: vertical bars, 2 fans, display on the right reading **72°F** (not 188)
- [ ] White finish, not copper, pink or grey
- [ ] No remote, no air swirls, no room

## Cold version (hold for the pivot)
Headline → *NO MORE SWITCHING ROOMS / BECAUSE OF THE COLD.* · bullet 2 → *+ Comfortable through long evenings in the cold room* · bullet 4 unchanged · display → **70°F**.

---

# B1C3 — Whiteboard · "Normal vent" vs "Evenroom vent"

**Job:** a real whiteboard photographed at home, with the same room drawn twice. On the left, a normal vent with the person miserable. On the right, our vent with the person comfortable. The faces carry the ad and the arrows explain why. Our vent is drawn as a **hand sketch that clearly resembles the reference product**, not a photo of it.

## Board layout (as drawn)

```
┌───────────────────────────┬───────────────────────────┐
│      NORMAL VENT          │      EVENROOM VENT        │  ← black, underlined
│  ┌─────────────────────┐  │  ┌─────────────────────┐  │
│  │ [window ☀ red]  81° │  │  │ [window ☀ red]  74° │  │  ← thermometer: red / blue
│  │                     │  │  │                     │  │
│  │ ▭ vent (small, high)│  │  │   🙂 relaxed figure │  │
│  │   at desk, laptop   │  │  │   at desk, iced drink│  │
│  │  ▭ vent  ↑↑ (tiny)  │  │  │ ▭◉◉▣ ⇗⇗⇗ (long,   │  │
│  │                     │  │  │   curling to desk)  │  │
│  └─────────────────────┘  │  └─────────────────────┘  │
│ "barely any air           │ "cold air actually        │
│  coming out" →            │  reaching the room" →     │
├───────────────────────────┴───────────────────────────┤
│   "Same room. Same afternoon. You just stay."         │  ← black, across the bottom
└───────────────────────────────────────────────────────┘
```

## Marker colours (dry-erase, real ink tones, not pure RGB)

| Marker | Approx. ink colour | Used for |
|---|---|---|
| Black | `#1E1E1E`, slightly streaky | Headings, room outlines, figures, desk, labels, bottom line |
| Red | `#C8312B` | Sun, 81° thermometer, sweat drops |
| Blue | `#1F5FAE` | All air arrows, 74° thermometer, ice cubes |

## Prompt

```
[Attach REF-1 (the product photo) so the drawn vent resembles the real product.
Use it ONLY for the vent's shape. Do not copy its white background, its layout, its
remote, or render it as a photo — on the board it is a marker sketch.]

NOTE — this prompt now matches the APPROVED C3 generation (2026-09-26): both vents are
drawn high on the room's back wall, with arrows coming DOWN toward the desk.

A candid smartphone photograph of a real white dry-erase whiteboard hanging on the wall
of an ordinary home office, with a hand-drawn marker drawing on it.

THE BOARD: A standard 36 x 24 inch magnetic whiteboard with a thin brushed-aluminium
frame and rounded plastic corner caps, hung slightly crooked (about 1 degree) on a warm
greige painted wall (#D9D2C5). Its surface is glossy white (#F7F7F5) with faint grey
ghosting from older wiped-off writing in the upper right, a few smudges where a hand
brushed the ink, and one small fingerprint smear. An aluminium marker tray runs along
the bottom holding three dry-erase markers with their caps off beside them — black, red
and blue — plus a used grey felt eraser. The markers' manufacturer brand name and
colour band are printed on the barrels and visible, exactly as real markers look.

THE DRAWING — done by an adult, quickly and confidently, in chisel-tip dry-erase marker.
Lines are slightly wobbly and uneven in thickness (about 3–5 mm strokes), with visible
streaking where the marker ran a little dry, overlapping line ends at corners, and
occasional tiny gaps. The style is expressive simple cartoon, like someone explaining
something to their family. Nothing is ruled or perfect. Black ink is #1E1E1E, red ink is
#C8312B, blue ink is #1F5FAE, each with the slightly translucent, streaky look of real
dry-erase ink.

A single vertical black line, drawn freehand down the middle, divides the board into two
equal halves. A horizontal black line about 85% of the way down separates a bottom strip.

LEFT HALF:
- Heading at the top centre in black capital letters, handwritten, about 1.2 inches tall,
  underlined with one quick stroke: "NORMAL VENT"
- Below, a simple room drawn as a square outline with a floor line.
- In the upper left of the room, a small window (rectangle with a cross) with a big red
  sun drawn in it — a circle with eight short red rays blazing out.
- On the right wall of the room, a small drawn thermometer (tube and bulb) with "81°"
  written beside it in red, clearly readable.
- In the middle, a stick-figure-plus person (round head, simple body, arms) sitting on a
  chair at a small desk with an open laptop drawn as an L-shape. The person is clearly
  MISERABLE: eyebrows slanted down and inward, mouth a flat wavy line, three red sweat
  drops flying off the head, two short wavy "heat" lines rising from the shoulders, and
  one hand holding a sheet of paper up and fanning the face (two little motion arcs
  beside the paper).
- High on the back wall, near the top right of the room, a plain rectangle representing
  an ordinary vent with four short horizontal slat lines inside it. Coming out of it,
  pointing down: just THREE short, limp blue arrows that droop sideways and stop after about 2 inches — obviously weak.
- Below the room, a handwritten black label with a short arrow pointing at the vent:
  "barely any air coming out"

RIGHT HALF:
- Heading at the top centre in black capital letters, same size, underlined:
  "EVENROOM VENT"
- The SAME room drawn the same way: same window, same big red blazing sun.
- On the right wall, the same drawn thermometer with "74°" beside it in BLUE, clearly
  readable.
- The SAME person at the SAME desk, now clearly COMFORTABLE: sitting upright, a small
  smile, eyebrows relaxed, both hands on the laptop keyboard (typing), no sweat drops, a
  tall glass on the desk with two little blue ice cubes drawn in it.
- High on the back wall, drawn LARGER than the left vent, a marker sketch of OUR vent
  cover based on the
  attached reference photos: a longer rectangle with the same general proportions as the
  reference, vertical bar lines across its left part, two circles with fan blades drawn behind
  the bars, and a small filled dark rectangle at the right-hand end for the display panel
  with a few dots for the buttons, and a small blue "74" written inside the display (matching
  the display's position on the reference). It is a quick sketch, not a detailed drawing,
  but anyone who has seen the product would recognise it.
- Coming out of it: FOUR long, strong, bold blue arrows sweeping down and out across the
  room in a fan shape, two of them ending right at the person at the desk.
  These arrows are at least three times longer and bolder than the left side's arrows.
- Below the room, a handwritten black label with a short arrow pointing at the blue
  arrows: "cold air actually reaching the room"

BOTTOM STRIP (spanning both halves, centred, black, slightly larger handwriting):
  "Same room. Same afternoon. You just stay."

ALL HANDWRITING: genuinely handwritten in marker by a real adult, mixed-case except the
two headings, letters slightly uneven in size and baseline, naturally imperfect but
fully legible and spelled exactly as given. NOT a font, NOT a handwriting typeface.
"81°" and "74°" must be clearly readable, each with a proper degree symbol.

PHOTOGRAPH: Taken on a phone from about 5 feet back, nearly straight on but a few
degrees off-axis from the left, so the board is very slightly trapezoidal. The whole
board fills about 85% of the frame, with a strip of greige wall visible around it and,
at the right edge, part of a white bookshelf with a few books (real spines and titles
visible). Ordinary indoor daylight from a window off to the left (about 5000 K), giving
a soft diagonal glare band across the top-left corner of the board that slightly washes
out the ink there but does not cover any words. Mild phone-camera grain, natural white
balance, very slight barrel distortion at the edges, focus sharp across the board.

EXCLUDE: people or hands in frame; any typeset or printed text on the board; any digital
arrows, stickers, badges, price, logo overlays or CTA added over the photo; vector-perfect
or ruled lines; colour fills or shading beyond marker strokes; emoji.

Aspect ratio 4:5, 1080 x 1350.
```

## QA before using
- [ ] Headings read exactly **NORMAL VENT** / **EVENROOM VENT**, and nothing says "before" or "after"
- [ ] At thumbnail size: left figure obviously miserable, right figure obviously comfortable
- [ ] Left arrows tiny and limp, right arrows long, bold and reaching the desk
- [ ] `81°` in red, `74°` in blue, both legible
- [ ] Drawn vent on the right resembles the real product (display at the correct end)
- [ ] Bottom line spelled exactly; handwriting looks human, not a font
- [ ] Marker branding on the tray visible and natural

**If it drifts:** handwriting too neat → add *"messy, rushed handwriting, letters uneven in size and slightly slanted."* Arrows too similar → add *"the left arrows are tiny and faint; the right arrows are three times longer and twice as bold."* Faces unclear → add *"exaggerated cartoon expressions readable from across a room."*

## Cold version (hold for the pivot)
Window: red sun → blue snowflakes and a bare tree · left figure: wrapped in a blanket, shivering lines, teeth-chatter zigzag, `58°` in blue · right figure: t-shirt, relaxed, hot mug with red steam lines, `68°` in red · arrows: **red** warm-air arrows (weak left, strong right) · labels: *"barely any warm air coming out"* / *"warm air actually reaching the room"* · bottom line unchanged.

---

# Cold-weather summary

| | Hot (now) | Cold |
|---|---|---|
| **B1C1** | Two running fans, hard west sun | Small oil-filled radiator glowing next to the desk, grey overcast light, blanket over the chair, laptop closed, mug gone cold |
| **B1C2** | See B1C2 cold version | — |
| **B1C3** | See B1C3 cold version | — |
