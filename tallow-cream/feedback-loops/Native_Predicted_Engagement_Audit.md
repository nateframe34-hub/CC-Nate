# Native Predicted-Engagement Audit

**Date:** 2026-07-03
**Trigger:** founder relayed outside ecom advice: "the ads just aren't good enough, Meta doesn't like to show ads it doesn't think will get engagement." This is a real, documented mechanic (predicted engagement rate is a direct input to Meta's ad rank/CPM formula) and it overlaps with items 2 and 3 in `B17C1_CPM_Diagnosis.md`. This doc checks the actual native creative against it concretely instead of agreeing in the abstract.

## Finding 1: the truncated preview text is weak (concrete, fixable today)

Meta shows roughly the first 125 characters of primary text before "...See more." That snippet, not the full 1,500 words, is what most scrollers ever see, and it is what most directly drives whether someone stops, reacts, or comments before ever clicking through.

B17C1/B9C3's actual first 125 characters, verbatim:

> "I was at Elaine's house for book club last month and I went upstairs to use the guest bathroom.\n\nThere was one thing on the c"

It cuts off mid-word, before the actual hook (the jar, the stare) ever arrives. Everyone who doesn't tap "See more" sees only "went upstairs to use the guest bathroom" and nothing else. That is scene-setting, not a hook. The intrigue payoff ("One jar. Amber glass. Simple label. I stood there... and stared at it for too long.") is real, tested, working copy, it is just sitting outside the window that determines whether most viewers ever see it.

**Fix, cheap and zero risk to the proven story:** move the object-mystery line to open the post, scene-setting second. Something like:

> There was one thing on Elaine's bathroom counter. One jar. Amber glass. Simple label.
>
> I was at her house for book club last month, upstairs using the guest bathroom, and I stood there with my hands wet staring at it for too long.

Same words, same order of information delivered to a reader who clicks through, but now the first 125 characters end on the actual hook instead of "guest bathroom." This does not touch the copy that has proven itself against the 10-element density audit, it is a resequencing of the first two paragraphs only.

## Finding 2: zero human faces in any native image, ever

Every native image in this account, baseline through B21, is deliberately object/hand-only: a jar, a counter, a trash can, wet hands. This was a deliberate compliance and camouflage choice (no identifiable face protects Julie's likeness and avoids implying a specific real testimonial), and it is defensible. But it also means every single native image is fighting the single best-documented lever for organic engagement and predicted-engagement scoring: photos with a visible human face reliably outperform object/product photos on likes, comments, and dwell time, independent of how authentic the object photo looks.

This is a real, not-yet-tested variable, separate from "candid vs staged" (which B21 already tested) and separate from "problem vs outcome" (also already tested). It has never been isolated.

**Fix, worth one real test cell:** a native image that includes a partial or candid face, not a posed portrait, something like a genuine half-laugh caught candidly, a side profile mid-conversation, or the moment from B17C1's own copy where the husband's hand touches her cheek (which already implies a face in-frame without being a hero close-up). This does not have to break camouflage, most real candid photos people take of a moment DO include some face; hands-only has been a stricter constraint than authenticity actually requires.

## Finding 3: no comment-thread activity, ever

Already flagged in the Gap Analysis (Julie never replies to comments), worth restating in this specific frame: predicted engagement is not a one-time snapshot at launch, it updates as real engagement accumulates. A dead comment section is itself a negative signal over the life of the ad, on top of losing whatever organic reach a live conversation would generate. This connects directly to the post-ID seasoning work already in motion, seasoning is necessary but not sufficient if the resulting comments never get replied to.

## Finding 4: the copy never invites a response

House style correctly bans second-person preaching ("you should," "imagine if you") to protect the first-person authenticity. But that also means there is no natural comment-bait anywhere in the copy, no line that makes a reader want to type something back. This is a real tension: engagement-bait phrasing ("comment YES if...") would break camouflage instantly and is explicitly against house voice. But a single, in-voice, first-person closing line that a real woman might actually add when sharing something personal ("Anyone else have a drawer of these travel packets they don't remember buying?") is different from engagement-bait phrasing and worth testing as a controlled addition, not a wholesale rewrite.

## What this does NOT explain

Frequency is fine (1.0-1.2), CTR is excellent (7-9%), and the ad has never been rejected. This audit is specifically about predicted engagement (comments/likes/shares/saves) as a CPM input, which is a different signal than click-through performance, and it is plausible for an ad to have great CTR among the small % who read the preview and still get penalized on predicted engagement because the vast majority who scroll past never see anything worth reacting to.

## Recommended order

1. **Today, free, zero risk:** resequence B17C1's opening two paragraphs so the hook lands inside the 125-character preview window. Apply the same check to B21's cells and any future native copy before launch, this is now a standing pre-launch check, not a one-time fix.
2. **Standing, already in motion:** Julie replies to comments on all live native ads.
3. **Next native test cell:** one variant with a partial/candid face in frame (the B17C1 husband-hand-on-cheek moment is the most natural candidate since the moment is already IN the copy) tested against the current hands-only version, isolating "face vs no face" as its own variable.
4. **Lower priority test:** one in-voice, non-preachy closing question line, tested as a controlled addition on a single cell, not rolled out account-wide until read.
