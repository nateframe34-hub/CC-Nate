# B30 Feedback Loop - Cheap CPM, Weak CTR, Zero Conversions

**Date:** 2026-07-23
**Founder's read, confirmed correct by the data below:** B30 reached a cheaper audience than the proven native ads, but failed to convert that audience into clicks. Most likely both creative and copy, diagnosed below with a specific mechanism for each, not just a general impression.

---

## The numbers, aggregated across all reads to date

| Cell | Lifetime spend | Impressions | Clicks | Blended CTR | CPM range seen |
|---|---|---|---|---|---|
| B30C1 | $12.90 | ~243 | 2 | **0.82%** | $10.91-$57.55 |
| B30C2 | $25.02 | ~247 | 7 | **2.83%** | $64.63-$173.78 |
| B30C3 | $9.23 | ~418 | **0** | **0%** | $4.91-$25.10 |
| **B30 total** | **$47.15** | **~908** | **9** | **~0.99%** | consistently well under $200 |

For comparison, B17C1 and B28C1 (the account's proven converters) run **8-16% CTR** on most days, with CPMs typically **$200-530**. B30's CPM is genuinely, consistently 3-10x cheaper. Its CTR is 3-16x weaker. Both numbers are real at this point, B30C3 alone has cleared the 50-impression noise threshold by 8x with a flat 0% CTR, that's not noise, that's a real result.

**The mechanical link between the two findings, stated plainly:** these aren't two independent things to explain, they're causally connected. When engagement is this weak, Meta's delivery algorithm can't find enough people who want to interact with the ad inside a narrow, high-intent pool, so it broadens delivery into cheaper, less-qualified inventory to keep spending the floor budget. Cheap CPM here isn't a lucky break, it's the algorithm's response to weak signal. The two readings are one finding, not two.

---

## Per-cell diagnosis

### B30C3 - the clearest, most confident diagnosis in the batch

Opening line: **"Not younger. Just like myself again."** - a bare identity claim, stated before any scene, before any concrete detail.

This is a direct hit against a rule this account already proved with real spend, months ago: `Killed_Batch_Failure_Analysis.md`, **Pattern C, "Hooks That Don't Open Loops."** B1C3's thesis opener, B5C3's counter-intuitive claim opener, both went to 0% CTR on real volume and are named in that doc as a *hard-learned* failure mode. B30C3 opens the exact same way, a claim first, sentence 2 finally arrives at a scene (cleaning a drawer, finding a badge). The account's own rule, already paid for once, says the scene has to come first or the loop the hook is supposed to open never opens. 0% CTR on 418 impressions is that rule reasserting itself, not bad luck.

**This is fixable without touching the angle, avatar, or mechanism at all** - just reorder the hook so the scene leads and the identity line lands as a payoff, not an opener. Cheapest fix in the whole batch, highest confidence.

### B30C1 - likely a creative (image concept) problem more than a copy problem

Opening line: **"My cousin Emily posted the photos from her birthday dinner the next morning, and I scrolled straight past mine twice before I went back and looked. Mid-laugh. Candlelight. A glass halfway to my mouth. I looked exhausted."** This is a real scene-first hook, doesn't violate Pattern C, comparable in construction to B28C1's proven hook.

The image is where this cell likely breaks. B28C1's comparative analysis (logged earlier this batch) credited its strength to a specific, replicable visual trope: a single ambiguous OBJECT in an almost-empty domestic scene, the viewer has to parse what they're looking at and why it matters. B30C1's image concept is a woman looking at a blurred, soft-focus FaceTime call on her phone in her kitchen. That's a different kind of ambiguity, a blurred face doesn't read as "mysterious," it reads as "low-quality photo" at small mobile-feed thumbnail size, especially since the prompt deliberately softens/blurs the faces for privacy reasons. There's no single strange object anchoring the frame the way the empty counter did for B28C1. The mechanism that made object-discovery work (a viewer has to look twice to understand a striking, specific visual) doesn't transfer cleanly to "person looking at a phone," because that's an extremely common, non-strange thing to see in a feed.

**Likely fix:** keep the hook, change the image concept to something with a single unusual physical anchor (an object, not a blurred face), or accept that self-recognition as a door needs a genuinely different visual language than object-discovery and hasn't found it yet.

### B30C2 - the closest to working, weak but non-zero, points at the same image problem with a stronger hook partially compensating

Opening line: **"Three people asked if I was tired this month. I wasn't. I counted."** This is the tightest, most confident hook of the 3, no Pattern C violation, arguably as strong as anything in B9C3/B28C1. It's also the only cell with a real, non-zero, above-B30C3 CTR (2.83% blended).

That gap (a strong hook, a still-weak CTR relative to the account's 8-16% norm) is itself diagnostic: if the hook were the main problem, this cell should be dead like C3. It isn't dead, it's just weak. That points at the same image-concept issue as C1, a candid social scene (coffee counter, cookout) without a single striking visual anchor, partially rescued by a stronger hook, not fully.

---

## Synthesis: what actually went wrong

1. **The angle (SA1, self-recognition/external-comment/identity as doors into "surface dryness reads as tired") is not confirmed broken by this data.** Nothing here tests the angle in isolation, every cell also changed the image language away from the account's only proven high-CTR visual formula (a single ambiguous object in a quiet scene) at the same time. Angle and image concept were never isolated from each other in this batch, that's a real design gap worth naming for next time: B30 controlled for hook/copy structure across cells but did NOT control for image concept against the account's proven object-discovery visual language.

2. **Copy is mostly fine, with one confirmed real bug (B30C3's opener).** 2 of 3 hooks pass the account's own hard-learned rules cleanly. Only C3's violates a named, previously-paid-for failure pattern, and its result (flat 0% on real volume) matches that pattern's signature exactly.

3. **Creative (image concept) is the more likely dominant cause across all 3 cells.** None of the 3 images use the specific "one strange object, ambiguous quiet scene" formula that's the account's only validated cheap-CTR-driving visual trope (B9C3, B28C1). Self-recognition, social-candid, and mirror-comparison are all softer, more "slice of life" concepts that don't force the same half-second parse the object-discovery shots do.

4. **The cheap CPM is not a separate win to bank.** It's the direct downstream consequence of weak engagement, the algorithm reaching for cheaper inventory because it can't find enough qualified engagement in the pool it's already tried. Cheap CPM with this CTR profile is a symptom, not a discovery.

---

## Recommendations for the next iteration

1. **Fix B30C3's hook now, independent of anything else** - reorder so the scene leads, the identity line becomes the payoff not the opener. Highest-confidence, cheapest fix available.
2. **Before testing SA1 further, run ONE cell that keeps SA1's angle/door structure but reverts to the proven object-discovery visual language** (a single strange object in a quiet scene, not a face/social moment), to isolate whether the angle itself is weak or the image concept is what's been holding it back. Right now those two variables are confounded across the whole batch.
3. **Don't conclude SA1 is a weak angle from this data.** The account's own research still rates it "⭐ STRONGEST" with verbatim-validated hooks, this batch tested it through an unproven image language, not through the angle itself failing on a fair test.
4. **File this as the actual reason to be cautious about future creative-format departures from proven visual tropes**, not just for SA1: any time a new batch moves away from the object-discovery formula, treat it as its own variable, isolate it, don't bundle it with a new angle/door test at the same time.
