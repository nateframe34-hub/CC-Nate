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

# B1C2 — Relatable Hook · "NO MORE SWITCHING ROOMS BECAUSE OF THE HEAT."

**Format (swipe file):** **Relatable Hook**, a situational call-out plus a benefit stack (the "12-HOUR SHIFT SHOES" structure). One bold line in capitals names the situation. The real photo underneath proves it. Short outcome callouts sit on the photo, pointing at the things that changed.

**Rebuilt 2026-09-26.** Replaces the text-band design, which wasn't a swipe format and read as a designed ad. The first generation's photo also failed (stock living room, dog, air swirls, product as the hero), because the listing-style product reference pulled it into listing style.

**Product:** not in frame. C2 sells the outcome; C3 and the product page show the product.

## Why the photo is an edit of C1

The C1 image came out right. Editing it makes C1 and C2 the **same room**: C1 is the room she gave up on, C2 is that room back. That kind of consistency across the batch is something stock scenes can't give you.

## Step 1 — the photo: edit the approved B1C1 image

**Input:** attach the approved **B1C1 image** only. **Do NOT attach the product reference.**

```
Edit the attached photograph. Keep the room EXACTLY as it is: same camera position from
the open doorway, same lens, same framing, same white six-panel door and brass knob on
the left edge, same greige walls, same window with the white mini-blinds, the same tree
outside, same beige carpet with its vacuum tracks, same white desk against the right
wall, same black mesh office chair, same wall outlet, same textured ceiling. Keep the same
hard late-afternoon sunlight coming through the blinds and throwing slatted stripes
across the right wall, the desk and the carpet. It is still the hottest part of the day.

CHANGES — only these:

1. REMOVE BOTH FANS. The black box fan and the white tower fan are gone completely. The
   carpet where the box fan stood is plain carpet with a faint flattened square where it
   used to sit. The outlet on the wall below the window is empty, nothing plugged in.

2. ADD A PERSON WORKING AT THE DESK. A woman in her mid-40s sits in the black mesh chair,
   pulled in to the desk, seen from behind and slightly to her left (three-quarter back
   view) — her face is NOT visible. Shoulder-length brown hair loosely held up with a
   tortoiseshell claw clip. Heather-grey crew-neck t-shirt, navy cotton shorts, bare legs,
   one bare foot tucked up on the edge of the chair seat, the other flat on the carpet.
   She is typing on the laptop, which is now OPEN on the desk with its screen lit (screen
   content soft and not readable). Her posture is relaxed and settled: shoulders down,
   back loose, head tilted slightly toward the screen. The sun stripes fall across her
   back and shoulder. She looks completely comfortable. No sweat, no damp patches, no
   fanning, no hair stuck to the neck.

3. DESK CHANGES. The glass of water becomes a tall glass of iced water with visible ice
   cubes and light condensation. Keep the yellow legal pad, pen and mug of pens. Add her
   phone lying face-down beside the laptop.

Everything else in the image stays identical, including the full frame: keep the
ceiling and the plain wall above the window, because text will be placed there. Same
photographic quality as the original: real phone photo, mild grain, slight highlight
clipping in the sun stripes, natural warm white balance, no HDR, no cinematic grade.

DO NOT ADD: any fan, air conditioner, vent device or product; air swirls, wind lines,
leaves or any visual effect showing air; plants, pets, cushions or throws; any text,
logo or overlay; a remote control or a hand in the foreground.

Output 4:5, 1080 x 1350, same framing as the original.
```

## Step 2 — type, set in Canva / Figma on top of the photo (full bleed, 1080 × 1350)

### Layout

```
┌──────────────────────────────────────────┐ y=0
│ NO MORE SWITCHING ROOMS                  │ ← headline over ceiling / upper wall
│ BECAUSE OF THE HEAT.                     │   y 56–236, x 56–1024
│                                          │
│        [window]                          │
│                                  ┌──────┐│
│                                  │ ✓ Still at the desk at 4pm │ ← near her shoulder
│  ┌────────────────┐              └──────┘│
│  │ ✓ Both fans in the garage │  ← on the empty carpet where the box fan stood
│  └────────────────┘                      │
│┌──────────┐                              │
││✓ Door open again│ ← by the door edge, left
│└──────────┘                              │
└──────────────────────────────────────────┘ y=1350
```

### Headline

| Property | Value |
|---|---|
| Text (exact) | **NO MORE SWITCHING ROOMS / BECAUSE OF THE HEAT.** (break exactly there) |
| Font | **Archivo ExtraBold 800**, ALL CAPS |
| Size | 64 px, line height 1.05 (67 px), tracking −0.5% |
| Colour | `#1C1A17` warm near-black, straight on the photo, no box |
| Position | Left-aligned, x = 56 px, top of cap height at y = 60 px, max width 968 px |
| Legibility | If the ceiling/wall behind is too busy or dark, add a soft `#FAF7F2` glow behind the letters (outer glow, 0 offset, 18 px blur, 55% opacity). No drop shadow, no outline, no solid band |

### Benefit callouts (3), as small label chips placed on the photo

| # | Text (exact) | Placed |
|---|---|---|
| 1 | Still at the desk at 4pm | Beside her shoulder / the laptop, right side, around y ≈ 560 |
| 2 | Both fans in the garage | On the empty carpet where the box fan stood, left-centre, around y ≈ 900 |
| 3 | Door open again | Near the door edge, bottom left, around y ≈ 1180 |

| Property | Value |
|---|---|
| Chip | Rounded rectangle, corner radius 14 px, fill `#FAF7F2` at 94% opacity, padding 14 px vertical / 20 px horizontal, soft shadow 0 4 px 12 px `rgba(28,26,23,0.18)` |
| Check | A filled terracotta `#B4553A` circle, 30 px, with a white `✓` inside (Inter Bold 18 px), 12 px left of the text |
| Text | **Inter SemiBold 600**, 30 px, `#1C1A17`, sentence case, single line |
| Pointer | None. The chip sits right next to the thing it describes |

### Not in the image
No price, no logo, no wordmark, no CTA button, no badge, no product. The price lives in the primary text. (A small `$89` in JetBrains Mono 28 px bottom-right is an easy add if you want a value nudge; it's off by default.)

## Route A — one pass (only if not using Canva)

Attach the approved C1 image, paste the Step 1 edit prompt, then add:

```
Then add text to the image:
- At the top, over the ceiling and the plain wall above the window, left-aligned with
  a 56-pixel margin, in a heavy, tight geometric grotesque sans serif (Archivo
  ExtraBold style), ALL CAPITALS, warm near-black #1C1A17, about 64 px, broken exactly as:
      "NO MORE SWITCHING ROOMS
       BECAUSE OF THE HEAT."
- Three small rounded off-white (#FAF7F2) label chips placed on the photo, each with a
  small solid terracotta (#B4553A) circle holding a white checkmark, then text in a
  clean semibold sans serif (Inter style), about 30 px, #1C1A17:
      next to the woman's shoulder: "Still at the desk at 4pm"
      on the empty carpet where a fan used to be: "Both fans in the garage"
      near the door edge at bottom left: "Door open again"
All text correctly spelled, crisp, legible on a phone. No other text, no logo, no price,
no badges, no buttons, no arrows.
```

## QA before using
- [ ] Headline in caps, breaks as *NO MORE SWITCHING ROOMS / BECAUSE OF THE HEAT.*, legible at thumbnail size
- [ ] **Same room as B1C1**: door, window, desk, chair, carpet all match
- [ ] **No fans, no air effects, no product, no remote, no pets, no plants**
- [ ] Hard sun still clearly coming in; she's clearly comfortable; face not visible
- [ ] Each chip sits next to the thing it names

## Cold version (hold for the pivot)
Headline → *NO MORE SWITCHING ROOMS BECAUSE OF THE COLD.* · edit: flat grey 4pm winter light, bare tree, remove the space heater instead of the fans, her in an oatmeal knit sweater and wool socks, steaming mug of tea · chips → *Still at the desk at 4pm* / *Space heater in the garage* / *Door open again*.

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
