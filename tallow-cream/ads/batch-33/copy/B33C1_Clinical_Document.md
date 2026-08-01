# B33C1 — The Ingredient Panel Document

**Batch:** 33, Cell 1 of 5
**Sub-Avatar:** SA2 The Product Graveyard (runs as one audience with SA5)
**Angle:** Angle 1 — one jar replaces the shelf that failed, delivered as *why* the shelf failed
**Format:** Clinical / technical evidence document
**Awareness:** Solution-Aware entry → Most-Aware close
**Sophistication response:** New Information
**Status:** Image prompt written. **Hook SELECTED.** Skeleton and copy not yet written.

---

## Where this concept came from

**Origins native swipe, Camouflage Ad #4** (`origins-training/swipe-file/origins-native-swipe/45.png`): a genuine X-ray of both legs with blue measurement lines overlaid, an orange annotation arrow pointing to the problem site, and "171°" labelled beside a circled joint. It is not a photograph of a person or of objects. It is a **document about the problem**, and it stops the scroll because you cannot resolve what you are looking at without reading.

Annotation grammar (measurement lines, dimension arrows, callouts on 90-degree elbow joints, scale bar, revision block) borrowed from the technical-blueprint pattern in the Nano Banana Pro library, `infographic-edu-visual.json`.

**Why this replaces the original C1.** The first C1 was a first-person photo of a drawer full of dead product. Founder killed it: B21's H1A (trash can) and H1B (cluttered counter) already ran that concept, and pre-B16 batches ran it repeatedly without converting. Correct call — and the swipe supports it. **Every Origins native image is evidence of the problem or a document about it. Not one is objects on a surface.** This account has spent its whole history photographing inventory. This cell photographs proof.

## Why it should earn cheap delivery

Meta prices CPM on predicted engagement, and its classifier is tuned to recognise advertising. A scanned document with annotation linework has essentially no ad signature: no centred subject, no product hero, no negative space, no beauty lighting. It reads as a screenshot of something informational — which is what it is.

Legibility at thumbnail is the scarcest property in this batch. Black text on white paper with two saturated annotation colours survives a 200px feed render better than any photograph we have run.

## What it uniquely tests

**Does a non-photographic, document-class image change delivery cost?** No cell in the account's history has tested this. Distinct from B33C3 (hand-drawn whiteboard, folksy, personal register) — this is the opposite pole: printed, clinical, impersonal, authoritative.

## Truthfulness constraint — read before generating

The image shows **real ingredient panels with water listed first.** That is a true, publicly verifiable fact about the category and it is the actual mechanism behind our angle.

- ✅ Show ingredient text as it genuinely appears (`AQUA/WATER` or `WATER (AQUA)` in position one)
- ❌ **Do NOT fabricate laboratory results, test percentages, assay values, or study data.** Invented "68% water" style figures are manufactured scientific evidence. The ingredient panels are real; numbers we made up are not.
- ❌ Do not name or make legible any competitor brand name. The panels are examined as *category convention*, not as accusations against a named company. This also keeps us clear of comparative-claim exposure.
- ❌ No skin, no faces, no bodies anywhere in frame.

---

## IMAGE PROMPT (Nano Banana Pro)

```
A flat overhead scan of a plain white A4 sheet of paper, photographed straight-on so the paper fills 95% of the frame, edge to edge, with only a sliver of matte grey desk surface visible at the extreme corners. The paper is real: very slightly warm off-white (#FAF8F4), with a faint soft shadow along the left edge where it lifts a millimetre off the desk, one barely visible horizontal crease across the lower third, and a small dog-eared corner at the bottom right. This is a working document someone printed and handled, not a pristine digital render.

DOCUMENT HEADER, top of page, left aligned:
- A thin horizontal black rule running the full width, 1pt.
- Above the rule, in small black uppercase sans-serif (Helvetica Neue Light, generously letterspaced, approximately 11pt): "INGREDIENT PANEL COMPARISON — FIRST-LISTED CONSTITUENT"
- Below the rule, smaller, in grey: "SAMPLES 01-06 · FACIAL PREPARATIONS · RETAIL PURCHASE" and on the right of the same line "SHEET 1 OF 1"

MAIN BODY — six specimen blocks arranged in a strict 2-column x 3-row grid, evenly spaced, each block identical in construction:
- Each block contains a small rectangular greyscale photographic crop, roughly 45mm wide by 22mm tall, showing a genuine close-up of the back-of-pack ingredient text on a cosmetic container. The crop is deliberately tight so that ONLY the dense small-print ingredient paragraph is visible — no brand name, no logo, no product name, no cap, no bottle silhouette. Each crop has slightly different paper stock, print weight and curvature so the six read as six genuinely different products: one on glossy white, one on matte cream, one on a curved tube casting a soft gradient, one slightly out of focus at its right edge, one with a fold running through it, one printed in dark grey rather than black.
- In every one of the six crops, the ingredient paragraph begins with the word "AQUA/WATER" (in two of the six, the variant "WATER (AQUA)"), and that opening word is CIRCLED by hand in a saturated red-orange marker (#E8542A), an imperfect elliptical loop drawn slightly too fast, overshooting and crossing itself at the top left. The circles vary in size and angle across the six blocks because they were drawn one at a time by a human.
- To the left of each block, a specimen number in bold black: "01." through "06."
- Beneath each block, one line of small black monospace text stating the position only, e.g. "POSITION 1 OF 24", "POSITION 1 OF 31", "POSITION 1 OF 19", "POSITION 1 OF 27", "POSITION 1 OF 22", "POSITION 1 OF 35". No percentages, no measured values, no test results.

ANNOTATION LAYER, drawn over the printed document in the same red-orange marker (#E8542A):
- From the right edge of specimen 02, a hand-drawn arrow with a single sharp 90-degree elbow joint travels right then up, terminating in an arrowhead. At its end, handwritten in the same marker, in real cursive-leaning handwriting with uneven baseline: "every single one"
- A straight ruled underline in the same marker beneath the header phrase "FIRST-LISTED CONSTITUENT".
- In the bottom right quadrant, in the largest handwriting on the page, underlined twice: "water evaporates"

FOOTER, bottom of page, in small grey printed sans-serif:
- Left: "ORDER OF LISTING IS BY DESCENDING QUANTITY. FIRST-LISTED = LARGEST SINGLE CONSTITUENT BY WEIGHT."
- Right: a simple black scale bar 20mm long with tick marks and the label "20mm"

LIGHTING AND CAPTURE:
Flat, even, ordinary indoor light from a window to the upper left. Slight warm cast. Very faint paper grain and a barely perceptible moiré where the printed photographic crops are reproduced. Shot handheld from directly above on a phone: the paper is rotated approximately 1.5 degrees off true, and there is the faintest motion softness at the extreme bottom edge. Real, imperfect, taken quickly.

ASPECT RATIO: 4:5, 1080 x 1350 pixels.

CRITICAL NEGATIVE CONSTRAINTS:
NOT a clean digital infographic. NOT a vector graphic. NOT a branded template. NO company logos, NO brand names legible anywhere. NO product bottles, jars, tubes or containers shown in silhouette — only the tight ingredient-text crops. NO skin, NO faces, NO hands, NO people. NO percentages, NO laboratory values, NO test results, NO study citations, NO fabricated data of any kind. NO stock-photo styling. NO drop shadows or glossy digital effects. NO decorative icons, badges, starbursts or design furniture. The only colours present are black, greys, warm off-white paper, and the single red-orange marker.
```

**Aspect ratio:** 4:5 (1080 × 1350)
**Delivery target:** Meta, US only
**Product in frame:** NO — deliberately. This cell is the problem document; the product does not appear.

---

## QC gate — reject and regenerate if any of these are true

- [ ] Any competitor brand name or logo is legible
- [ ] Any percentage, assay value, or test result appears anywhere
- [ ] It looks like a designed infographic rather than a printed-and-handled sheet
- [ ] The six ingredient crops look like six copies of the same crop
- [ ] The marker circles are neat, uniform, or evenly sized
- [ ] Any skin, face, hand or person is visible
- [ ] "AQUA/WATER" is not clearly legible in first position on every specimen
- [ ] The page is perfectly square to frame (it must be ~1.5° off)

---

## HOOK — SELECTED (founder, 2026-07-31)

> **"My sister-in-law circled one word on six different labels and laid them on the table in front of me like evidence."**

**Why this one (founder):** *"explains the creative way better than any of the others."* Correct — it is the only candidate that tells you what the document in the image IS, which the others leave the reader to work out. "Like evidence" carries the whole tone: someone else built the case, the narrator is the one being shown. Peer-relay credibility chain intact (4 of 4 converters). Loop planted: which word?

---

## All candidates considered

Hooks must open on a scene or an action, never a bare claim (Pattern C failure mode). All avoid clock-time language, which the 7/29 problem-side research established is our invention and not customer language.

1. *"My niece printed the ingredient lists off six of them and circled the first word on each one."*
2. *"I never once turned the bottle over. In eleven years I never turned a single one of them over."*
3. *"She asked me what the first ingredient was in the one I liked best. I had no idea. So we looked."*
4. *"Fourteen products, and the same word was at the top of every label."*

> #1 and #3 preserve the peer-relay credibility chain that appears in 4 of 4 converters — someone else does the explaining. #2 is the strongest damaging admission but has no second character in it.

---

## Still to do

1. ~~Founder picks hook~~ ✅ done
2. Build story skeleton (step 4)
3. Write body copy with the `learnings-on-native-ads` skill (step 5)
