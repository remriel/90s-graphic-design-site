# NOIZ — ten-second earbuds concept ad

An original vertical motion campaign translating this repository's visual direction into a product ad: pink `#ff2ba6`, aqua `#00e7dc`, yellow `#fff200`, purple `#6236ff`, paper `#fffdf1`, black `#080808`, heavy outlined type, offset shadows, a retro browser window, moving ticker, and printed halftone cues.

NOIZ is fictional. The earbuds are an AI-generated concept, not an advertised real product. Copy includes no price, battery-life, noise-cancellation, or other unverified performance claims.

## Deliverable

`exports/NOIZ_90s_Earbuds_10s.mp4`: 1080 × 1920, 30 fps, 300 frames, 10 seconds, H.264 video and stereo AAC audio. Soundtrack is original synthesized percussion, bass, chord stabs, and transition noise. No sampled music.

The ad was rendered with Pillow and FFmpeg. It was not authored or rendered in DaVinci Resolve.

## Rebuild

Install Python dependencies `pillow numpy imageio-ffmpeg`, then run:

```sh
python render.py --output exports
```

Windows fonts Impact and Courier New are referenced in `FONT`. On another OS point `FONT` and `fnt()` to equivalent locally licensed fonts. Font files are not redistributed.

`--preview` renders only storyboard and representative stills. The complete render also synthesizes audio and performs a full decode validation. This is a single composited render; animation remains editable through `render.py`.

## Asset provenance

`assets/earbuds.png` was created using the built-in image-generation tool on 2026-10-18. Its original transparent alpha is preserved. No brand reference or third-party product photograph was supplied.

Generation prompt: Premium commercial product photograph cutout on a transparent background; matching wireless in-ear earbuds floating above an open charging case; glossy ivory shells, transparent aqua accents showing electronics, chrome details, black silicone tips; three-quarter front camera; studio softboxes with pink and cyan rim lighting; centered with transparent margin; no text, logo, watermark, backdrop, or props. Full generation brief is in `asset-prompt.txt`.

## Timing

- 0–2.3 s: CUT THE CORD / GOODBYE, TANGLES
- 2.3–4.7 s: ZERO WIRES / ALL YOU
- 4.7–7.2 s: PRESS PLAY / SMALL BUDS / BIG ENERGY
- 7.2–10 s: NOIZ / YOUR WORLD. ON REPEAT. / FIND YOUR FREQUENCY

Visual QA: inspect all four layouts, check transitions, read copy at full and thumbnail sizes. Verification decodes the entire video and audio, checks 10-second duration and 1080 × 1920 dimensions, and confirms 300 frames. Listening on physical speakers remains a human review step.
