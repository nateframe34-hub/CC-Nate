# Hook research v1 (2026-11-13)

**Question (founder):** the Target ad had great CPMs and CPCs but no body. AD 7 has the body but a weak hook. What makes a hook cheap to deliver, and what should we test next?

**Sources:** (1) our own ad data, Nov 3–12 (`tracking/Ad_Performance_Tracker.csv`), which is the strongest evidence here; (2) web research, which was thin: mostly agency and tool blogs, read from search summaries only because this session's network blocks the sites themselves. (3) Still to come: converting ads from GetHookd (pull list in section 6).

---

## 1. What our own data says

### Finding 1: the opening footage sets the hook rate. The words barely move it.
Hook rate = 3-second plays ÷ impressions, lifetime per ad.

| Opening footage | Ad | Caption on it | Hook rate | Impressions |
|---|---|---|---|---|
| **Target store walk-in** | AD 8 (original) | "Gamers, RUN don't WALK to Target" | **45–50%** | ~2,100 |
| **Target store walk-in** | AD 11 (7A v1) | "Still looking for a Christmas gift?" | **55%** | 113 |
| **Target store walk-in** | AD 12 (7A v3) | "RUN don't WALK for this deal" | **44%** | 125 |
| AD 7's box on a table | AD 7 | none (voice only) | 25–33% | ~2,500 |
| AD 7's box on a table | AD 13 (7B) | "Still looking for a Christmas gift?" | 31% | 157 |
| Gift bag on a Christmas table | AD 15 (S2) | "my husband every year…" | 35% | 49 |
| Teal unit + comment bubble | AD 14 (S4) | "what do you even get a man…" | 23% | 43 |

- **Three different captions on the store walk-in all land at 44–55%.** Three different captions on product-on-a-table footage all land at 23–35%.
- Adding text to AD 7 (AD 13) moved the hook from ~25–33% to 31%. Nothing.
- **So a new hook means new opening footage, not new words.** The caption's job is to tell the right person "this is for you" once they've stopped.

### Finding 2: at the same volume, the Target ad's reach cost about half of AD 7's. Every other CPM we've looked at is noise.
| Ad | Impressions that day | CPM |
|---|---|---|
| AD 8 | 200 → 780 → 543 → 577 | $97 → $59 → $65 → **$44** |
| AD 7 | 654 / 648 | **$111 / $103** |
| AD 7 | 204–278 | $119–188 |
| Any ad | under ~150 | **$35 to $667** (random) |

- The fair comparison is AD 8 at 540–780 impressions/day (**$44–65**) against AD 7 at ~650/day (**$103–111**). That's a real ~2× gap, and it goes with the hook rate (45% vs 25%) and CTR (5% vs 2.5–3.5%).
- AD 8's own CPM was $97 on its first day (200 impressions). It only got cheap once it had volume.
- **The reskins and new ads have never had more than 116 impressions in a day.** Their CPMs ($104–259) can't be read. They also sit in an ad set with a forced $20 minimum, which makes Meta spend there whether or not the auction is cheap.

### Finding 3 (correction): "saying Christmas gift raises CPM" is not supported.
I said this on Nov 11. It doesn't hold. AD 11 (gift caption) and AD 12 (deal caption) share the same footage, and their CPMs overlap completely ($104–172 vs $81–214, on tiny samples). What we actually saw was low-volume noise.

### Finding 4: cheap clicks only matter if the body qualifies the buyer.
| | Landing page views | Sales |
|---|---|---|
| AD 8 (gamer call-out, music only, no voice) | ~127 | **0** |
| AD 7 (woman's gift voiceover) | ~80 | **7** |

### Finding 5: the founder's exact thesis has barely been tested.
"Target hook + AD 7's selling body" **is AD 11**. It has spent ~$19. So far: 55% hook, 7 clicks at $2.67 (one day at $0.89), 5 landing page views, 0 ATC. At AD 7's rate (~9% of page views buy) you'd expect less than half a sale from 5 views, so this is neither a pass nor a fail. **I suggested turning AD 11 off on Nov 13. That was wrong.** It should run to the $49 line.

### Finding 6: no placement is causing the high CPM. But Reels is where AD 7 sells.
AD 7 lifetime by placement (founder's breakdown, Nov 13): $342.78, 2,791 impressions, 7 purchases.

| Placement | Spend | CPM | Hook rate | Landing page views | Purchases | Cost per purchase |
|---|---|---|---|---|---|---|
| Facebook Feed | $141.81 | $145 | 31% | 36 | **1** | $141.81 |
| **Facebook Reels** | $113.55 | $120 | 25% | 31 | **4** | **$28.39** |
| Instagram Reels | $38.58 | $138 | 20% | 12 | 1 | $38.58 |
| Instagram Feed | $25.00 | $152 | 35% | 7 | 1 | $25.00 |
| Facebook Feed (desktop) | $9.75 | $98 | 27% | 1 | 0 | n/a |
| Instagram Stories | $7.17 | $184 | 21% | 1 | 0 | n/a |
| Everything else | ~$7 | low | n/a | ~8 | 0 | n/a |

- **CPM is $120–150 in every placement that gets real spend.** There is no expensive placement to switch off. The cost is in the ad, not in where it runs.
- **Instagram costs about the same as Facebook** ($138–152 vs $120–145). So the missing Instagram account is not what's making reach expensive.
- **Facebook Feed took the most money (41%) and made 1 of 7 sales.** Facebook Reels made 4 of 7 at $28 each. On 7 sales this could still be chance (1 of 36 page views vs 4 of 31), so it's a watch item, not a reason to cut Feed yet. Cutting placements also shrinks delivery, which usually raises CPM.
- **5 of 7 sales came from Facebook,** which fits buyers aged 44–65+.
- **What it means for hooks:** our buyers are converting in Reels, so story-led vertical videos (the S scripts) are the right format.

---

## 2. What outside research adds (low confidence)
All of this comes from agency/tool blogs and talks, via search summaries. Treat it as hints that match or don't match our data.

| Claim | Source type | Fits our data? |
|---|---|---|
| Meta only treats an ad as a new variation when the **visual in the first 3–5 s** is different. Text-only changes don't count | Creator talk (Motion summit, 2026) | **Yes.** AD 13 |
| Hook rate: ~25% average, 30–40% good, 40%+ elite | Vendor benchmarks, not Meta | AD 7 is average. The store walk-in is elite |
| A direct call-out stops fewer people, but the ones it stops have higher intent | Vendor blog | Yes. AD 7 vs AD 8 |
| "Husband review" (he reacts to or reviews the gift) is performing well in recent BFCM testing | One presenter's observation | Untested by us |
| Gift-givers respond to a **real customer's genuine reaction**; humor and self-deprecation ease the pressure of gifting | Ad-library audience profile | S2's "sweater" line; 2 ATC on day 1 |
| A skeptical comment on screen, answered in the body | Creator talk | Our comment-reply ads delivered cheaply |
| A brand with a mostly 50+ gift audience won by using **customers' own review words** as hooks | Agency case study (their own numbers) | Untested by us |
| Ad set spend limits can cause delivery problems; avoid them except in extreme cases | Independent Meta specialist (Jon Loomer) | Matches the reskin ad set |
| Small budgets pay a CPM premium | Single blog | Plausible, unverified |
| Creator gift guides beat brand-made gift catalogs; gift content surges in November | Holiday playbooks | General |

**Not found:** any measured data on gift-for-husband hooks, on retro handheld ad hooks, or on why store-find videos deliver cheaply. Those answers have to come from our tests and from GetHookd.

---

## 3. Why the Target ad was cheap (ranked by how sure we are)
1. **The footage.** A place and a walk, not a product. Movement in the first second. It looks like a video someone would post anyway. *(Strong: three ads, three captions, same result.)*
2. **An open question.** "What did they find?" keeps people watching past 3 seconds.
3. **Volume.** It took 55–80% of the budget, so Meta had room to find the cheap impressions.
4. **A broad call-out.** "Gamers" is a big group, so many people click. This is also why the clicks didn't buy.
5. **Comments.** People replied to correct the Target claim, and engagement likely helped delivery. *(Guess.)*

## 4. The hook brief (what every new hook must do)
1. **Open on a person doing something: a place, a moment, or the product being used, tested or reacted to. Never the product lying still.** *(Updated 2026-11-13 after batch 1: five of seven winning ads show the product in the first frame, but always in someone's hands and in motion.)*
2. **Something moves in the first second** (walking, wrapping, a hand reaching, a reaction).
3. **Leave a question open** (what did she find, what's in the box, how did he react).
4. **The caption names the giver's situation within 3 seconds**, so gift shoppers stay and browsers leave *after* they've counted as a view.
5. **Then AD 7's kind of body:** a woman's voice, the nostalgia through *his* memory, easy to use, ends on him loving it.
6. **Every new test changes the opening footage.** Caption-only variants are not tests.

## 5. Hook concepts to test, ranked

| # | Concept | First 3 seconds | Evidence | Footage |
|---|---|---|---|---|
| **A** ⭐ | **"I went to the store and found nothing"** | Store front → walking in. Caption: "3 stores looking for my husband's gift. nothing." | The proven store walk-in, with a giver caption. Honest: the store is where she *didn't* find it, so no "this isn't at Target" bounce | **We have it** (first ~2.5 s of AD 8, before the shelf) |
| **B** | **Keep AD 11 running** (store walk-in + gift caption + AD 7 body) | Already live | Best hook rate and cheapest clicks of any ad with a selling body. ~$19 spent | Live |
| **C** | **Husband review / reaction** | He opens the box on camera. Caption: "gave my husband his gift early 🫣" | Outside research + our "outcome" endings | Film or generate |
| **D** | **Wrap with me** | Hands wrapping the box on the floor, paper and tape. Caption: "wrapping the one gift I know he'll love" | "Wrap with me" is a native December genre; movement from frame 1 | Easy to film at home |
| **E** | **The 1996 photo** (S3) | An old Christmas photo of a kid with a Game Boy | Pattern break; the strongest script for our real buyers | Generate |
| **F** | **Skeptic comment** | Comment on screen: "10,000 games for $75? yeah right." Then she proves it | Comment-reply ads delivered cheaply; answers the 55–64 men's doubt | We have it |
| **G** | **Notes app** (S1) | Her phone, a note titled "his games 🤫" | Curiosity; a trick she can copy | Generate or film |

**First test (free, no new voice needed):** put concept A's store walk-in on the front of **S2**. S2's first line is "Every year my husband says he doesn't need anything. And every year I end up buying him a sweater," which fits a store run exactly. Same voiceover, new opening footage, so it's a clean test of the footage.

## 6. What to pull from GetHookd
**Filters:** Meta, video, US, active **30+ days** (longer is better: nobody pays for a losing ad for a month), sorted by longest-running or highest reach.

**Categories (5–10 ads each is plenty):**
1. **Retro handhelds / R36S-type consoles**, and anything else in "nostalgia tech" (retro radios, film scanners, record players, Tamagotchi-type toys).
2. **Gifts for men bought by women**, any product: "gifts for him / husband / dad", massage guns, wallets, pocket tools, whiskey sets, personalized items. This is our buyer, so their hooks transfer best.
3. **Q4 gift products with an older audience (45+)**: puzzles, photo gifts, comfort gadgets.
4. **Store-find or "I found this" videos** that send people to an online store.
5. **Reaction / "husband review" ads.**

**For each ad, send (a screenshot of the first frame plus these is enough):**
- The **first 3 seconds**: what's on screen, what moves, the on-screen text, the first spoken line.
- How long it has been running, and any spend or reach estimate.
- Who is on screen or speaking (age, gender) and who they're talking to.
- How it ends (offer, outcome, CTA).
- The landing page link.

I'll break each one down the same way (hook footage, hook words, body, ending) and look for the opening shots that repeat across long-running ads.

## 7. Sources (web)
- Jon Loomer Digital, "Why won't Meta spend my advertising budget": https://www.jonloomer.com/why-wont-meta-spend-my-advertising-budget/
- Motion, "15+ Proven UGC Ad Hooks That Are Working Right Now" (Savannah Sanchez, 2026): https://motionapp.com/library/talk/15-proven-ugc-ad-hooks-that-are-working-right-now-savannah-sanchez/
- Motion, "33 Black Friday Ad Formats": https://motionapp.com/library/talk/33-black-friday-ad-formats-you-need-to-try-now-for-2025/
- Motion, gift-givers audience profile: https://motionapp.com/library/audiences/gift-givers
- Jetfuel, creative performance benchmarks 2026: https://jetfuel.agency/creative-performance-metrics-for-dtc-video-ads-hold-rate-thumbstop-and-thruplay-benchmarks-2026/
- Billo, H1 2026 video ad benchmarks: https://billo.app/blog/h1-2026-video-ad-benchmarks/
- Hustler Marketing, 50+ gifting brand case study: https://www.hustlermarketing.com/?p=17038
- New Engen, holiday creative playbook: https://newengen.com/insights/the-holiday-creative-playbook-what-actually-works-in-2025/
- Segwise, Meta Andromeda 2.0: https://segwise.ai/blog/meta-andromeda-2-0.md
