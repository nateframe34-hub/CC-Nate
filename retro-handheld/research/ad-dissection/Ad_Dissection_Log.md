# Ad dissection log (started 2026-11-13)

**Goal (founder):** take apart winning ads that are running now, hooks first and then the whole ad, to learn why native-looking ads deliver cheaply and ours don't. CPM is not the target; ROAS and cost per sale are. But a 20% lower CPM on AD 7 buys 25% more impressions for the same money, which on its lifetime numbers ($342.78, 7 sales) would move ROAS from about 2.7 to 3.4 and profit from about $148 to $270, if click and buy rates hold.

**Method:** `dissect.py` makes one sheet per ad (top row = the first 3 seconds, rows below = the rest) plus the countable numbers. The sheet is then read by eye and filled into the template below. Competitor videos are not committed to the repo; the sheets, numbers and write-ups are.

Run: `python3.13 retro-handheld/research/ad-dissection/dissect.py <out-folder> <videos…>`

---

## Template (one per ad)
**Ad:** name · category · days running · length
**Hook, 0–3 s**
- First frame: a place, a person, a moment, the product, or text?
- What moves in the first second?
- On-screen text (exact words) and its style (app-native caption or designed graphic)
- First spoken line, and when speech starts
- Sound: voice, trending audio, music, silence
- The open question it plants
**Native signals:** shot on a phone? real location or a set? face on camera? app elements (comment reply, native captions)? how polished is the voice?
**Body:** the beats in order · who is speaking, to whom · the problem named · proof or demo
**Ending:** outcome, offer or call to action
**Pace:** cuts in the first 3 s · cuts per 10 s · words per second
**What we can use**

---

## Baseline: our own ads (2026-11-13)
Sheets and numbers in `ours/`.

| | **AD 8 · Target find** | **AD 7 · gift voiceover** | **S2 · "I don't need anything"** |
|---|---|---|---|
| Result | 45–50% hook, $44–65 CPM, 0 sales on $147 | 25–33% hook, $103–188 CPM, 7 sales | 35% hook (49 impressions), 2 ATC |
| Length | 11.8 s | 24.4 s | 26.6 s |
| **First frame** | **A place:** Target store front at night, cars in the lot | **The product:** boxes laid out on a white rug with glitter gift boxes | A Christmas gift bag on a table |
| Product first appears | **3.0 s** (box on a store shelf) | **0.0 s** | ~1 s |
| What moves in second 1 | The camera walks to the doors; the scene changes twice in 3 s | A hand picks up a box, same spot | Hands at a gift bag |
| On-screen text | App-style white caption bubble, on from frame 1 | **None** | App-style bubble for 3.5 s |
| Sound | Song with lyrics, no voice | Polished voiceover from 0.0 s ("Imagine giving a single present…") | AI voiceover from 0.0 s + soft music |
| Words in first 3 s | 0 spoken (caption only) | 13 | 10 |
| Setting | Real store, then a cluttered real desk | A staged flat-lay set, shot top-down | Staged Christmas tables |
| Face on camera | No | No | No |
| Cuts per 10 s | 3.4 | 2.0 | 6.4 |
| Open question | "What's at Target?" | None. You see what it is at once | "What did she get him?" |
| Ending | Gameplay, no offer | Soft spoken CTA ("I've left the link below…"), no offer | Him "playing", no offer |

**What the baseline already shows**
1. **AD 8 hides the product for 3 seconds and opens on a real place.** AD 7 shows the product in a staged set in frame 1. A viewer knows AD 7 is an ad before she has heard a word.
2. **AD 8's scene changes twice in 3 seconds** (lot → doors → shelf). AD 7 stays in one spot for 24 seconds.
3. **AD 8 has text on screen from the first frame; AD 7 has none.** Most people watch muted, so AD 7's hook does not exist for them.
4. **AD 7's voice sells, but it sounds like an ad read.** That is the body we keep, not the opening.
5. **None of our ads has a face, or a person reacting.**

## Competitor ads
| Batch | Ads | Write-up |
|---|---|---|
| 1 (2026-11-13) | C01 Click & Grow garden · C02 essie polish (DE, brand ad) · C03 Mad Lady trousers (FI, sale ad) · C04 Socialize app · C05 ForeverSongs (ES, gift reaction) · C06 travel toiletry bag · C07 TerraShell founder ad | `Batch1_C01-C07_Dissection.md` |

## Cross-ad patterns
*(filled once 15+ ads are in: how often each first-frame type appears, typical time before the product shows, time before speech starts, cuts in the first 3 s, share with a face on camera, share with app-style captions, how they end)*
