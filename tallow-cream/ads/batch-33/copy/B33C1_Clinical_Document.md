# B33C1 — The Ingredient Panel Document

**Batch:** 33, Cell 1 of 5
**Sub-Avatar:** SA2 The Product Graveyard (runs as one audience with SA5)
**Angle:** Angle 1 — one jar replaces the shelf that failed, delivered as *why* the shelf failed
**Format:** Clinical / technical evidence document
**Awareness:** Solution-Aware entry → Most-Aware close
**Sophistication response:** New Information
**Status:** ✅ COMPLETE — image prompt, hook, skeleton and body copy all written. Awaiting launch.

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

---

---

## STORY SKELETON — REBUILT VIA `learnings-on-native-ads` (step 4, 2026-08-01)

> Supersedes the first-pass skeleton below, which used the internal 10-beat template without the skill's architecture. Beat table retained at the end as the word-count budget.

**1. Awareness level — Solution-Aware.** Entry is a table of products she already owns. The reader must already know solutions exist and have bought several for the hook to land. Per the skill, the job at this stage is to explain *why everything else failed* and position ours as the only thing addressing the real cause. That is exactly what a circled word on six labels does.

**2. Narrator type — first-person personal story.** Strongest for solution-aware readers who must trust the person before the product. The narrator is not the expert; she is the one being shown.

**3. Sophistication — Stage 3-4. Response: New Information.** Not a bigger claim, not a better mechanism. A fact she can verify herself in ninety seconds on her own bathroom shelf. Verifiability is what beats accumulated skepticism at this stage.

**4. Angle — belief SHIFTING.** Old belief: *my skin is difficult and I have not yet found the product strong enough for it.* New belief: *the products were never the wrong strength, they were the wrong category, and the label says so.* The shift must feel self-reached — the narrator has to go and check her own bottles on the page.

**5. Concept / the door — "The Relative Who Investigated."** Someone else builds the case against your cabinet while you are downstairs. Pulls the segment who suspect they have been wasting money but have never had it demonstrated. **Farthest-door check:** distinct from the other four cells — she is not confessing (C2), not arguing (C3), not deprived by circumstance (C4), not challenged on her own account (C5). Here she is simply *shown*, and her passivity is the point.

**6. Hook mechanics.** *"My sister-in-law circled one word on six different labels and laid them on the table in front of me like evidence."* Self-selection: only someone with six-plus bottles reads on. No product, benefit, or category is hinted. Emotional trigger is not curiosity but **exposure** — someone has gone through her things and found a pattern she missed. "Like evidence" is the load-bearing phrase; it frames her as the subject of an investigation. Loop planted: *which word?* — resolves at the mechanism, roughly halfway.

**7. World-building.** Before-state: a person who does not chase things, who treated this as weather. Gradual decline told through *purchases* rather than symptoms, because for this avatar the purchases are the record. False belief pre-installed: price was the variable she had not yet tried. That belief is what makes the mechanism land, because it explains why spending more kept failing.

**8. Villain — earned, structural, and defensible.** The category convention that water leads the panel. It has a legitimate position (water is not a scandal, it is a formulation choice) which per the skill is what stops it being cartoonish. Its crime is not the ingredient, it is that the ordering rule is printed on every package and nobody reads it. Secondary human villain: the counter assistant with *"some skin is just difficult."*

**Permission shift — placed immediately after the mechanism.** She has not been foolish and she has not failed. She read the front of every package and never the back, which is what the packages are designed for.

**9. Mechanism — root cause and cascade, delivered in dialogue.** Root cause: the first-listed ingredient is the largest constituent by weight. Cascade: water leads → water leaves → what remains is a small residue and a bill → buying a more expensive version buys a more expensive water. **Required analogy** (writer's choice, one only): the ordering rule as a receipt she never turned over. Every alternative closes here without one being named.

**10. Discovery vehicle — credibility architecture.** Dana, 52, twenty years in food packaging, reads ingredient panels the way some people proofread menus. **Motive: none.** She was not looking to help; she was being nosy. Habit-based authority, never credential-based, never medical. Pre-emptive inoculation: the reader leaves knowing how to evaluate anything in the category, and everything in her cabinet fails the test.

**11. Results timeline — skepticism rhythm mandatory.** Day 1 qualified and unremarkable. Day 4, 9, 14, 21. Doubt precedes every improvement. **Third-party observation** required at least once — someone notices unprompted, which is worth more than any self-report.

**12. Villain reversal — understated.** She returns to the same counter for something unrelated and does not need to ask the assistant anything. Played as a non-event.

**13. Transition to the reader — Completion of Thought.** Not "are you struggling with." Instead: *you have never turned one over either, and you could tell me right now which drawer they are in.* Contrast amplification immediately after the resolution.

**14. Product section — ~78%.** Confirmation, not persuasion. Every differentiator ties back to the cascade: four ingredients, fat-first, nothing that evaporates. **Watch for failure mode 4 — no tonal break at the reveal.**

**15. Close.** Mirrors the hook: six bottles, one circled word. Loss framing over gain framing. Risk reversal (60-day) placed after the mechanism, functioning as risk removal rather than defensive pre-handling.

**Six failure modes check:** engine correct for solution-aware (Relatability, not Twist the Knife) ✅ · twisting the knife not merely describing pain, via the "never turned one over" admission ✅ · permission shift present and placed ✅ · no character break at reveal — enforce in the draft ✅ · results modest and qualified ✅ · angle confirms a suspicion she already holds rather than fighting her ✅

---

## First-pass skeleton (superseded, retained as the word-count budget)

**Narrator:** first-person personal story. Unnamed narrator, 47, secondary characters named. Standard for this account: the narrator is the reader, the named people are the credibility chain.
**Discovery vehicle:** Dana, 52, married to the narrator's brother. Spent twenty-odd years in food packaging and reads ingredient panels reflexively, the way some people proofread menus. **Peer-adjacent, never medical.** Her authority is a habit, not a credential.
**Villain:** the category convention itself — water as the largest constituent by weight — plus the counter assistant who kept telling her she had "difficult skin."
**Permission shift:** it was never her skin failing. She was buying the same thing six times and being told the fault was hers.
**Mechanism depth:** ~50%, standard native placement. The image is the *evidence* of the mechanism, not the mechanism itself, so the copy does not need to front-load it.

| # | Beat | Words | Content |
|---|---|---|---|
| 1 | **Hook scene** | 60-90 | Sunday, the kitchen table, after lunch. Dana has been upstairs "washing her hands" for far too long. She comes down with six of the narrator's own bottles and a printed sheet, and lays them out. One word circled on each. She does not explain immediately. |
| 2 | **Narrator context** | 150-200 | 47. Office manager. Two kids, one at college. Not a person who chases things. The skin thing started years ago and she treated it as weather: something that happens to you. Names the specific feeling in customer language, not clock language — it never feels like anything went in. |
| 3 | **The failed products** | 150-200 | The count. Six on the table, more in the drawer. The escalation pattern: each one bought after the last stopped doing anything, each one more expensive than the last on the theory that price was the variable. The counter assistant's line: "some skin is just difficult." **Damaging admission: she never once turned a bottle over.** |
| 4 | **Discovery scene** | 200-250 | Dana explains what she was doing upstairs. The ordering rule on an ingredient panel — descending by quantity, so whatever is first is the largest single thing in the jar. She had checked all six. Same word, first position, every time. The sheet is what she printed to show it, because saying it out loud sounded like a conspiracy. |
| 5 | **Mechanism** | 150-200 | Delivered as Dana's dialogue, not exposition. Water is the biggest thing in the jar. Water leaves. What is left behind is a small amount of everything else and a bill. Skin makes its own oil and makes less of it than it used to, so the thing being replaced is a fat, and what she has been buying is mostly not fat. **Each competitor closes here, without a single one being named.** |
| 6 | **The skeptic beat** | 80-120 | She argues. If it were that simple somebody would have said so. Dana's answer is the strongest line available: nobody is hiding it, it is printed on the back of every single one, and nobody reads the back. |
| 7 | **First use + day markers** | 250-300 | Day 1 skeptical and specific, "it did not disappear, which was new." Day 4. Day 9. Day 14. Day 21. Skepticism precedes every improvement — Damaging Admission applied to the timeline. |
| 8 | **Habit-cessation** | 100-150 | She notices the drawer is still shut. Weeks of not opening it. She had not decided to stop, she just had no reason to open it. |
| 9 | **Social expansion + villain reversal** | 100-150 | Her daughter takes it to college. The reversal is played quiet: she goes back to the same counter for something else and does not need to ask the assistant anything. |
| 10 | **Transition to reader** | 80-120 | Completion of Thought. Not "are you struggling with" — instead: *you have never turned one over either. You know exactly where they are right now.* |
| 11 | **Close** | 200-250 | Mirrors the hook: six bottles and a circled word. Identity payoff. Product named at ~78%. $49.99, four ingredients, 60-day guarantee, free shipping. Loss framing, not gain framing. |

**Compliance notes for the writer:** no menopause or hormonal language; no anti-aging, wrinkles, or fine lines; no heal/repair/treat/cure — use works, absorbs, feels different; call it a jar or balm, never a moisturizer, serum, routine or regimen; no em-dashes in body copy; no clock-time idioms ("by noon," "by 2pm") since the 7/29 research established those are ours, not the customer's.

---

## Still to do

1. ~~Founder picks hook~~ ✅ done
2. ~~Build story skeleton (step 4)~~ ✅ done
3. ~~Write body copy with the `learnings-on-native-ads` skill (step 5)~~ ✅ done

---

# BODY COPY (step 5, written 2026-08-01 via `learnings-on-native-ads`)

**Word count:** ~1,480 · **Product named at:** ~77% · **Mechanism at:** ~48%

---

My sister-in-law circled one word on six different labels and laid them on the table in front of me like evidence.

She had been upstairs for twenty minutes. I assumed she was on the phone.

She was not on the phone.

========

I am forty seven. I run the office for a company that installs commercial flooring, which means I am the person who knows where every single thing is and who has never once been thanked for it.

Dana is married to my brother. She is fifty two. She spent twenty years in food packaging and the most irritating thing about her is that she reads the back of everything. Menus. Cereal boxes. Paint tins. My brother says she has never bought anything in her life without turning it over first.

My skin stopped behaving somewhere around forty two and I never really treated it as a thing to fix. It was more like weather. Something that happened to me.

I would put something on in the morning and it would sit there. That was the part I could never explain to anyone. It never went in. It rested on top of my face like a film, and underneath it my skin felt exactly as tight as it had before I put anything on at all.

========

There were six of them on the shelf and four more in the drawer under the sink.

I want to be honest about how that happens, because nobody sets out to buy ten of anything.

You buy one. It does nothing. So you assume you bought the cheap one, and the next one costs more. That one does nothing either, so you decide you must need something targeted, and now you own three. Then a woman at a counter tells you that some skin is just difficult, and you believe her, because she works there and you do not.

I kept every single one. They were expensive. Throwing them out felt like admitting the money was already gone.

Here is the part I am embarrassed about.

In eleven years I never once turned a single one of them over.

Not one.

========

Dana put the six bottles down in a row and put a printed sheet next to them.

She had photographed the backs of all six upstairs. On the sheet she had circled the first word on every list.

It was the same word every time.

"Do you know how those are ordered," she said. It was not really a question.

I said alphabetically. I genuinely thought it was alphabetically.

She said no. They are ordered by quantity, most to least. So whatever is sitting in first position is the single largest thing in the jar. More of it than everything else in there put together, most of the time.

Then she said, "So what is the biggest thing in all six of the ones you bought?"

I looked at the sheet.

Water.

========

I said that could not be right, because I had paid a hundred and ten dollars for one of them.

She said that was correct, and that I had paid a hundred and ten dollars for water with a small amount of other things in it.

She was not being cruel about it. She was almost apologetic. She said this is not a scandal and nobody is hiding it. Water is cheap, it spreads well, it feels nice going on. It is a perfectly reasonable thing to build something out of.

The problem is what water does next.

It leaves. That is the entire thing water does. It sits on your skin and then it goes into the air and what stays behind is whatever small percentage was not water.

And your skin, she said, does not make water. It makes an oil. It makes less of it than it used to, which is why this started for me when it did. So the thing that had gone missing was a fat, and every single thing I had bought to replace it was mostly not fat.

I had spent eleven years buying more and more expensive versions of the same wrong category.

========

I want to say I argued for a long time. I did not. I argued for about a minute.

I said if it were that simple somebody would have told me.

Dana said nobody is hiding it. It is printed on the back of every one of them. It is just that nobody reads the back, and nothing on the front is ever going to say it.

That was the sentence that landed. Not the science. That one.

I had read the front of every package I ever bought. Beautiful fronts. Every one of them.

========

She told me what she used. Her son had brought it back from a farm shop two Christmases ago as a joke present, because she is the sort of person who complains about ingredient lists at the table, and it had four things in it.

Tallow. Honey. Olive oil. Calendula.

I said that sounded like something you would cook with.

She said yes. That is rather the point.

========

Day one I did not think anything. I put a small amount on and waited to feel it disappear the way everything else disappeared.

It did not disappear. That was the only thing I noticed. Not that it worked. Just that it was still there.

Day four I noticed I had not thought about my face. Which sounds like nothing. It is not nothing when you have thought about it every single day for eleven years.

Day nine my skin did not feel like it had a film on it. I kept touching my cheek to check and then feeling ridiculous.

Day fourteen a woman I have worked with for six years asked me if I had been away somewhere. I said no. She said I looked rested. I have not been rested since 2014.

Day twenty one it stopped being a thing I was monitoring and started being a thing that was just true.

========

The part I did not see coming was the drawer.

There is a drawer under my sink with four things in it. I used to open that drawer most days, digging around for whichever one I had decided to try again.

About six weeks in I realised I had not opened it. Not once. I had not decided to stop. There was simply no reason to open it, so I did not, and I did not notice not doing it.

That is what got me. Not the skin. The not looking.

========

My daughter took a jar back to college in September. She is twenty and has skin like a peach and does not need it, and she took it anyway.

And I went back to that same counter in October, for a birthday present for someone else, and the same woman was working, and I did not need to ask her anything.

I did not say anything to her either. There was nothing to say. I just did not need her.

========

So here is what I actually want to tell you.

You have not turned one over either.

You could tell me right now where they are. The shelf, or the drawer, or the bag at the back of the cupboard you have not opened since you moved. You know how many there are, roughly. You know which one was the expensive one.

Go and turn that one over. Read the first word.

I am not asking you to buy anything to do that. You already own it. It will take you about ten seconds and you will not be able to unsee it.

========

The one Dana had is the Tallow Honey Balm. Four ingredients, which is the whole label, and you can read all of them.

It is a fat, which is the thing my skin had stopped making enough of, which is why it goes in instead of sitting there.

It is $49.99, which is less than the second cheapest thing on my shelf. Shipping is free. If it does nothing for you, you have sixty days to send it back and they refund you, which is more than any of the other ten ever offered me.

I am not going to tell you it will work for you. I spent eleven years being told that.

I will tell you that the six bottles Dana put on my table are still on my table, because I have not worked out what to do with them, and that I know exactly what the first word on each one is now, and that I cannot go back to not knowing it.

---

## Meta headline
Turn the bottle over and read the first word.

## Meta description
Four ingredients. $49.99. Free shipping, 60-day money-back guarantee.
