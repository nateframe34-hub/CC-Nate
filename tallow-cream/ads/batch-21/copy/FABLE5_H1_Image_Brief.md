# Brief for Fable 5: B21 H1 "Bold Native" Image Set (3 images)

You're picking up an image-generation task mid-project. Here's everything you need.

## The brand
Whipped Tallow & Honey Balm. A 4-ingredient skincare balm (grass-fed tallow, manuka honey, olive oil, calendula). $49.99. Sold via native long-form Facebook/Instagram ads that read as a real woman's personal story, not a produced ad: the entire strategy depends on the ad NOT looking like an ad.

## The ad this image belongs to
This is the account's best-performing ad ever: **7 lifetime purchases**, far more than anything else tested. The copy is a first-person story: a 54-year-old woman named the narrator is at her friend Elaine's house for book club, goes upstairs to use the guest bathroom, and notices the counter: which used to have seven products on it: now has just one amber glass jar. That image (one jar on an otherwise near-empty bathroom counter, seen from her POV while washing her hands) is the hook image currently in use. Full body copy is in `B9C3_The_Counter_With_One_Thing.md` in this repo if you want the whole story for tonal reference; you don't need to read all of it to do this task, the scene below is what matters.

## The problem we're solving
This ad converts extremely well but runs at a very high CPM ($150-550, often the highest CPM segment on the account). A cheaper competing format (whiteboard-diagram ads) delivers at $20-80 CPM but converts far worse. **Leading hypothesis: the native image is too visually plain to "stop the scroll" in Meta's auction**: even though the story it leads into converts great once someone clicks. The current image (see prompt below) is deliberately shot to look like an unremarkable, boring iPhone snapshot: that authenticity is the whole POINT of the format (it's camouflage: it must NOT look like an ad, or the entire trust mechanic collapses), but we may have gone too far in the "boring" direction and it's costing us in the auction.

## The task
Generate **3 distinct images**, all depicting the SAME underlying scene (one amber glass jar, alone, on an otherwise near-empty bathroom counter, POV shot), but each pushed to be **visually bolder and more scroll-stopping** than the current baseline: while staying inside a hard constraint: **it must still read as a real candid photo taken by a real person, NOT a professional product shot, NOT a "produced" or "designed" image.** If it looks staged, branded, or polished, it breaks the format and the whole ad stops working. Bold ≠ polished. Bold = more visually striking WHILE staying photographically authentic (real light, real imperfection, real phone-camera quality).

Think of the boldness lever as: dramatic natural light, richer color, more striking composition, a closer/more intimate crop: the kind of thing that happens in a genuinely well-timed real photo, not the kind of thing an art director stages.

## The 3 variants (each tests a different "boldness lever," isolated)

**Variant A: Dramatic light.** Same near-empty stone bathroom counter, same single amber glass jar near the back edge. Push the lighting: strong late-afternoon or golden-hour light coming through a nearby window, catching the amber glass and throwing a warm glow/long shadow across the counter. Still candid iPhone quality, still POV (looking down at the counter, her wet hands visible at the bottom of frame), still no styling: but the light itself is the dramatic, scroll-stopping element instead of flat bathroom overhead lighting.

**Variant B: Bold close crop.** Same scene, but crop dramatically closer and lower: almost macro-close on the amber jar itself, catching a bathroom light reflection on the glass, with the vast negative space of the empty stone counter defocused behind it. Still shot like someone quickly snapped a photo on their phone inches from the jar, not a lit product shot. The boldness lever here is composition/intimacy, not light or color.

**Variant C: Rich color/contrast.** Same scene, same framing as the original (POV looking down at the counter, hands visible), but with richer, more saturated real-world color: warm stone tones, deep amber glass, a contrast-y overhead bathroom light rather than the flat cool light in the original. The boldness lever here is color depth and contrast, keeping composition and light angle closer to the original baseline so this variant isolates color specifically.

## Hard constraints (apply to ALL 3)
- 4:5 aspect ratio, 1080×1350
- First-person POV, looking down/slightly to the side at the counter: this is HER discovering the scene, not a third-person shot
- Her hands may be visible at the bottom edge of frame (wet, resting on the counter edge): no face, no body, no other people
- One amber glass jar, simple/unreadable label, NOT a branded product shot: no logo text legible
- Real bathroom details in soft background blur are fine (edge of a mirror, corner of a linen cupboard, a small towel): keep it domestic and lived-in
- NO text overlays, NO captions, NO graphic elements, NO borders
- Must NOT look like a professional product photograph, a stock photo, or a styled flat-lay: it needs to pass as something a real woman would actually take and text to a friend
- Slight grain/imperfection is good: this is a phone photo, not a camera photo

## Reference: the current (baseline) image prompt, for tone calibration only
```
Candid iPhone photograph taken from a woman's POV standing at the pedestal sink in someone else's guest bathroom, looking down and slightly to the left. The counter (a narrow stone surround around the pedestal sink) is almost entirely empty: conspicuously so, like someone recently cleaned it off. One amber glass jar with a simple label sits alone near the back edge of the counter, close to where a tiled wall meets the stone. The jar catches the overhead bathroom light. Around it: nothing. Just a faint ring-mark where another bottle used to sit. A folded small hand towel at the other end of the counter. The sink basin itself shows a thin film of water and a small puddle near the drain: someone is mid-wash. Her hands are just visible at the bottom of the frame, wet, holding the edge of the counter. The soap is a simple unmarked glass pump dispenser, out of focus. In the background, slightly blurred: the edge of an unframed mirror, the corner of a linen cupboard, a small framed botanical print. Normal bathroom overhead light, slightly cool, not dramatic. Real iPhone quality, slight grain, the kind of photo you'd take with your wet hand just to show someone something weird. Domestic, lived-in, a real guest bathroom in a friend's house: NOT a magazine bathroom, NOT a styled set, NOT a product shot, NO brand logos on the jar label readable, NO text overlays, NO captions. Just a counter that used to have seven things on it and now has one.
```

Each of your 3 variants should read as a clear escalation of boldness from this baseline along ONE dimension (light / crop / color), not a totally different scene.

## What to deliver
3 finished images (or 3 fully-specified image-generation prompts if you're not generating directly), clearly labeled Variant A / B / C, each ready to drop into a Meta ad next to the SAME unchanged proven ad copy. The copy does not change across variants: only the image does. This is a controlled test: if none of the 3 lowers CPM, that's a real signal the image-boldness hypothesis is wrong, not that one execution failed.
