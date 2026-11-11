# Funnel walk simulation v1: 4 new scripts + PDP (2026-11-11)

**What this is:** a desk simulation. Personas built from our 6 real buyers walked the 4 new scripts (`ads/batch-1/VO_Scripts_Gift_Nostalgia_v1.md`) and the PDP as built in the repo (`store/theme/templates/product.pocketarcade.json` + `pocketarcade-pdp.liquid`). **Personas are simulated, not real customers, and this does not predict sales.**

**What was NOT done (founder skipped the tool connections):** no live browsing (this session's network blocks pocket-arcade.shop), no checkout sandbox, no analytics. The steps marked **blocked** need those.

## 1. Evidence and coverage
| Source | Count | Notes |
|---|---|---|
| Website purchases | 6 (each counted once) | **4 women 44–65+, 2 men 55–64** (founder, from Meta/Shopify) |
| Orders | 3 duos, 1 trio, 2 singles | 4/6 multi-unit |
| Ad that sold | AD 7 (all 6) | Gift voiceover |
| Recipient of each gift | **unknown** | Not collected yet |
| Sales calls, surveys, feedback | none | |

**Bias:** all 6 sales came from one ad (AD 7), so the buyers reflect who AD 7 reaches, not the whole market. 6 is a very small sample.

**Correction to earlier notes:** the split is 4 women / 2 men (not 5/1), and **buyers are older than assumed (44–65+)**.

## 2. Buyer types (fewer than 5 are supported)
| # | Type | Status | Goal | Situation | Likely objections | What makes them leave |
|---|---|---|---|---|---|---|
| P1 | **Wife buying for her husband** (she's 44–65, so he's ~45–65) | Observed: women 44–65 buy. Recipient = **guess** | He loves it on Christmas morning | Not a gamer; doesn't know what's "good" | Is it complicated? Will it arrive? Is it cheap junk? Are *his* games on it? | Tech jargon; nothing he'd recognize; no arrival date |
| P2 | **Mom/grandma buying for adult son and/or grandkids** (55–65+) | Observed: women 55–65+, multi-unit orders. Recipients = **guess** | One gift that works for her son *and* the grandkids | Buying 2–3 at once | Is it OK for kids? Easy for them? Different colors? | Not clear it suits kids; bundle math unclear |
| P3 | **Man 55–64 buying for himself or the grandkids** | Observed: 2 men 55–64. Why = **unknown** | Play the games he grew up on (arcade/Atari/NES era) or share them | Grew up ~1969–1984 | Does it have **Pac-Man, Galaga, Space Invaders**? Screen too small? | Only sees NES/PS1/N64 names; feels made for younger people |
| P4 | Adult child (25–40) buying for dad | **Provisional:** no buyer in our data matches | Dad loves it | — | — | — |
| P5 | Younger partner (25–35) buying for boyfriend | **Provisional:** no buyer in our data matches | — | — | — | — |

## 3. Walk results (per persona, per script)
Labels: **clear** / **friction** / **blocked**. No scores.

### Ad scripts
| Script | P1 wife 44–65 | P2 mom/grandma | P3 man 55–64 | Finding |
|---|---|---|---|---|
| **1 Sneaky question** (husband) | **friction:** the games named (Mario Kart, Pokémon, Zelda) and "his PC" fit a husband of ~35, not ~55. *Her* husband's childhood was Pac-Man, Space Invaders, the first Super Mario | n/a | n/a | Keep the idea; **change the game names to his era** |
| **2 Dad says "I don't need anything"** | **friction:** the speaker is an adult child; P1 is the *mom's* age | friction (same) | **clear for "that's me"**, but he's the recipient, not the buyer | Fits P4 (provisional). Lower priority |
| **3 Mom remembers (son, 30)** | n/a | **clear:** her exact situation; "You remembered" lands | n/a | **Best match to real buyers** |
| **4 Comment reply (boyfriend)** | **friction:** "boyfriend", "drive to his parents' house" reads 25–35 | friction | n/a | Fits P5 (provisional). Lowest priority |

### Landing page (PDP, from repo files)
| Step | P1 | P2 | P3 | Evidence |
|---|---|---|---|---|
| Hero line "Replay your childhood…" | **friction:** speaks to the player; she's the giver | friction | **clear** | `hero_sub` |
| Console list "NES, Super Nintendo, Game Boy, PS1, N64…" | friction: names mean little to her | friction | **friction:** no arcade names; his era is arcade/Atari | `hero_b3`; arcade only in FAQ 11 |
| Game search ("is his game on it?") | **clear:** perfect for "I wrote down his games" | clear | **clear:** Pac-Man (26 matches), Galaga (7), Space Invaders (7) are in the library | `assets/pocketarcade-games.json` |
| Bundles ("One for you, one for them", "For the whole family") | clear | **clear:** matches multi-unit buying | clear | `t2_sub`, `t3_sub` |
| Arrival / Christmas cutoff | clear (arrival estimate + FAQ "Order by Dec 11") | clear | clear | `pa-arrive`, `faq_q_1` |
| Easy / no setup | clear | **clear:** "OK for kids" FAQ helps | clear | `easy_*`, `faq_a_4` |
| Reviews | **blocked:** `show_reviews` is true in the repo template with no real reviews; can't see what the live page shows | blocked | blocked | template line 104 |
| Cart drawer → checkout | **blocked** (no sandbox). Real sales show ATC→purchase is high, so likely fine | blocked | blocked | Shopify data |

## 4. Problem list (one row per problem)
| # | Problem | Where | Personas | State |
|---|---|---|---|---|
| 1 | Script 1 game names / "PC" fit a younger husband than our buyers' | Script 1 | P1 | found |
| 2 | Scripts 2 and 4 speak as a 25–40 buyer; no real buyer is that age | Scripts 2, 4 | P1, P2 | found (business decision: test anyway or rewrite) |
| 3 | No arcade-era names above the fold (Pac-Man, Galaga, Space Invaders) | PDP `hero_b3` | P3, P1 | found |
| 4 | Hero speaks to the player only; nothing for the giver near the top | PDP `hero_sub` / bullets | P1, P2 | found |
| 5 | Reviews setting is on with no real reviews; live state unknown | PDP reviews | all | blocked (needs live view) |
| 6 | Checkout not walked | checkout | all | blocked (needs sandbox) |

**Totals (hand-checked):** 3 evidence-based personas walked + 2 provisional (not walked). 4 scripts × 3 personas = 12 script checks: 3 clear-for-buyer (Script 3 for P2; Script 1's *idea* for P1 once fixed counts as friction, not clear), 7 friction, 2 n/a-but-noted. 6 open problems: 4 found, 2 blocked.

## 5. Proposed fixes (not applied; offer and prices unchanged)
1. **Script 1:** swap the games for his era: *"Pac-Man, Space Invaders, the first Super Mario. I wrote it all down."* Drop "PC" → "He hasn't put it down since."
2. **Script 3:** test first. It matches the strongest real buyer.
3. **New script for P3 / P2 (grandparent):** *"I bought one for my grandson so I could show him the games I played at the arcade…"* (draft on request).
4. **PDP hero bullet 3:** "Arcade classics like Pac-Man and Galaga, plus NES, Super Nintendo, Game Boy, PlayStation and more".
5. **PDP giver line** near the top, e.g. "Ready to give. Charged, loaded and boxed." (copy only).
6. **Reviews:** confirm the live page shows no empty stars or placeholders; turn `show_reviews` off until real reviews exist.

## 6. Next
Founder picks which fixes to apply. Then re-walk the same personas on the changed scripts and PDP. After launch: compare with real numbers (Shopify ATC → checkout → purchase by ad), and add a post-purchase "Who is this for?" survey so recipients stop being a guess.

## 7. Likelihood of success (added 2026-11-11, founder request)
**Judgment, not a prediction.** Baseline = AD 7: hook ~25%, CTR ~2–3%, ~6 sales from ~70 clicks (~9%, small sample). "Success" = cost per sale under ~$55 over the first ~$100 of spend.

| Script | Est. hook rate | Est. CTR | Est. click→sale | Chance of success | Why |
|---|---|---|---|---|---|
| **3 Mom remembers** | 28–35% | 2–3% | 6–10% | **~45–55%** | Closest to real buyers; shared nostalgia; strong ending |
| **1 Sneaky question** | 30–40% | 2.5–3.5% | 4–8% | **~40–50%** | Curiosity hook, copyable trick; recipient a bit younger than buyers |
| 1b Sneaky question, older games | 30–40% | 2.5–3.5% | 5–9% | ~40–50% | Same, tested only as a variant |
| 4 Comment reply | 30–40% | 3–4% | 3–6% | ~30–35% | Most native (cheap reach) but speaks as a 25–35 buyer |
| 2 Dad | 25–35% | 2–3% | 3–6% | ~25–35% | Relatable, but buyers so far are the dads' age |

Founder decision: keep the original game names in Script 1; add 1b (Pac-Man / Space Invaders / first Super Mario) as a separate variant.
