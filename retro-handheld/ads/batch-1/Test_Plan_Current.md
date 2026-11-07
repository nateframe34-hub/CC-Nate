# PocketArcade: Current Test Plan (2026-11-08)
**This file replaces every earlier iteration list** (Round 1 call-outs, 8A–8F, 6A–6E, 7A–7D, 8V). Those stay in `B1_Testing_CBO_Copy.md` as a backlog only.

## What we know (the only things the data has shown)
1. **AD 8 (Target):** a hook that stops people (45–50% 3s rate, $44–62 CPM) but **no body or CTA**, so 0 sales on $147. Killed. (`feedback-loops/Test_AD8_Target_RunDontWalk.md`)
2. **AD 7 (T06, Christmas gift VO):** a **body that sells** (the only full funnel, 1 duo sale on ~$51) but a weak hook (33%) and expensive reach ($140–196 CPM).
3. **The other 8 ads have never been tested** (<$5 each). AD 8 ate the budget.
**The one question to answer next:** can we give AD 7's selling body a hook as strong as AD 8's, so it gets cheap reach *and* converts?

## Budget reality
At ~$50–90/day, an ad needs ~$15–20 for a hook read and ~$50 for a purchase read. **We can properly test 2 new ads at a time.** More than that and nothing gets enough spend to judge.

## What runs now
### Campaign 1: Testing CBO (existing, $50/day). No new ads.
| Ad | Why it stays |
|---|---|
| **AD 7 (T06)**, control | Our only converter. Needs more spend to show whether the sale repeats. Don't edit it. |
| The 8 untested old ads | With AD 8 gone, they finally get budget. That is a free, honest first test. Apply the kill rule ($49 with zero intent). |

### Campaign 2: Iteration test (new ad set, ABO, $20/day each, 3–4 days). **3 ads (founder, 2026-11-08)**
**Renders:** `renders/7A_Target-intro_T06-body.mp4` (v1), `renders/7A_v3_Target-hook_DEAL-caption_T06-body.mp4` (v3), `renders/7B_T06_onscreen-hook.mp4`.
- **7A v1:** Target intro with the caption replaced by "Still looking for a Christmas gift?" → T06 body (hard cut at 2.5 s, VO from 0).
- **7A v3:** Target intro (through grabbing the box) with the caption replaced by **"Gamers, RUN don't WALK for this deal!"** (drops "to Target" to cut "this isn't Target" bounces) → 0.2 s fade, box-to-box → full T06 body with its VO.
- **7B:** T06 + on-screen "Still looking for a Christmas gift?"
(v2, which keeps the original Target caption, is not running: the founder chose to remove "to Target".)
| Ad | Build | Why this one | What it tells us |
|---|---|---|---|
| **7A** ⭐ | AD 8's Target store intro (first ~2.5 s) with **AD 7's voiceover starting over it**, then AD 7's unboxing body | Combines the **only proven hook** with the **only proven body**. Highest upside. | Whether a hook transplant fixes AD 7's reach cost while keeping its conversion |
| **7B** | AD 7 unchanged + big on-screen text for the first 3 s: **"Still looking for a Christmas gift? 🎁"** | Cheapest single change. Most people watch muted, so AD 7's hook currently exists only in the audio. | Whether AD 7's weak hook is just a sound-off problem. If 7B ≈ 7A, we don't need the store intro. |

**Judge:** hook rate ≥45% and CPM within ~$20 each; purchases after ~$50 each. Kill at $49 with zero intent.

## Cut, with reasons
| Planned | Decision | Reason |
|---|---|---|
| Target ad versions (banner, offer-in-hook, Walmart, call-out swaps, 8A–8E) | **Cut** | They change the hook, and AD 8's problem was the body. More hooks on a body that doesn't sell won't fix it. |
| 8V (AD 8 footage + a selling VO) | **Cut** | 7A answers the same question more directly, with a body we know sells. |
| 8C (unboxing + "RUN don't WALK") | **Cut** | Same idea as 7A without the proven body. |
| 6B | **Merged into 7B** | Same test. |
| 7C ("RUN don't WALK" text on AD 7) | **Backup** | Run only if 7B's hook rate comes in under 45%. |
| 7D (open on the brightest game screen) | **Backup** | Same role as 7C: a second hook option if 7B underperforms. |
| 6A banner, 6C duo end card | **Next round** | CTA/offer tests. Only worth running once we have a hook + body that works; then stack the CTA on the winner. |
| 6D (AD 7's VO over other footage) | **Later** | Useful (voice vs visuals) but not urgent. |
| 6E "Order by Dec 11" end card | **Scheduled Dec 1** | A deadline only matters once it is close. |
| Pink "pov" iterations | **Cut** | Built on a wrong ad mapping. |

## Decision tree after 3–4 days
- **7A or 7B converts with a ≥45% hook** → move it to a scaling CBO by post ID, then test the CTA (6C duo end card) on it.
- **Good hook, no sales** → the hook transplant broke the body. Go back to AD 7's original opening and test 7C/7D.
- **AD 7 (control) keeps selling as it takes more budget** → it is real. Scale it by post ID even before the iterations finish.
- **An old ad shows intent in Campaign 1** → it gets its own read; no new ads until one of these resolves.
