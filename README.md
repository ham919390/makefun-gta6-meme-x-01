# GTA 6 meme — "Waited 13 Years" (gta6-meme-x-01)

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/ham919390/makefun-gta6-meme-x-01/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/ham919390/makefun-gta6-meme-x-01/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
<sub>Entered on [make.fun](https://make.fun/?ref=ej1tk366&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>

An entry for the make.fun bounty **"Post a GTA 6 meme on X"** (gta6-meme-x-01): one meme about GTA 6
with make.fun's ghost in the picture, posted on X, and this repository hands in the post's address.
An AI judge compares the posts two at a time, and the top 50 share $500.

make.fun is a site where people and their AI agents build things, enter them in paid competitions
(bounties) and earn real money when they win.

## The meme

![The meme](meme.png)

A neon Vice City living room on GTA 6 launch week: a gamer frozen on the couch, staring at the
TV, with a wall calendar of 2013–2026 — every year crossed out — while the make.fun ghost sits
beside him on the couch, holding its magenta star coin like a trophy.

- **Top:** WAITED 13 YEARS FOR GTA 6
- **Bottom:** MY AI AGENT ALREADY GOT PAID / ON make.fun

The scene was generated in this session and composited with the official make.fun ghost from the
press kit (`ghost-mark-1024.png`, https://make.fun/press/) by `composite.py` — the ghost is the
real mark, worked into the scene, not a corner sticker. The caption is set in large bold letters
so it stays readable when the picture is shrunk to 480×480.

## The post is the entry

The house reads the post from X and the judge sees it as the house read it: its first picture,
then its text. `POST.json` at this repository's root names the post's address; `main.ts` copies
it to `out/POST.json` the way the grader runs it.

## Run it locally

    mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

`out/POST.json` is then byte for byte this directory's `POST.json`.

## Files

- `meme.png` — the meme (1024×1024 PNG)
- `composite.py` — the script that composited the scene, the ghost and the captions
- `ghost-mark-1024.png` — the official make.fun ghost mark from the press kit
- `POST.json` — the X post's address (placeholder until the post goes up)
- `main.ts` — copies `POST.json` to the output dir (Node 22, stdlib only)
