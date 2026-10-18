# Project State

## Previous reel
The five-second MOTION IN FIVE reel is delivered in outputs/. It was rendered with Pillow/FFmpeg. DaVinci Resolve 21.1.1 is installed and launched to Project Manager, but Windows captures timed out, accessibility clicks failed with coordinate input geometry unavailable, and bundled ResolvePython scriptapp returned None. Do not claim native Resolve authoring or repeat these failed paths without changed conditions.

## Current campaign — NOIZ earbuds, 2026-10-18
User requested a ten-second earbuds ad in the style of the GitHub 90s graphic-design repository. GitHub connector identified the user's public repository remriel/90s-graphic-design-site. Read README.md, page.tsx and globals.css. Checkout: work/90s-reference. No AGENTS.md or prior project docs in that clone. Original website is unchanged.

Design follows exact source palette: black #080808, paper #fffdf1, pink #ff2ba6, aqua #00e7dc, yellow #fff200, purple #6236ff. Impact headlines with black outlines and shadows, Courier New labels, retro browser frame, ticker, halftone. NOIZ is a fictional brand because no product was specified. No technical performance or price claims.

Built-in image generation created a transparent photograph of ivory/aqua earbuds and open case. Preserved alpha and copied into campaigns/noiz/assets/earbuds.png. Exact prompt in asset-prompt.txt. No third-party product photos or sampled music.

Architecture: campaigns/noiz/render.py uses Pillow for deterministic typography and compositing, numpy/wave for original stereo percussion, bass and chord stabs, imageio-ffmpeg for H.264/AAC encoding and full decode validation. Dependencies: pillow, numpy, imageio-ffmpeg. Windows Impact and Courier New fonts, not redistributed.

Four beats: CUT THE CORD (0–2.3s), ZERO WIRES (2.3–4.7s), retro NOW PLAYING (4.7–7.2s), NOIZ end card (7.2–10s). 1080x1920, 30fps, 300 frames, stereo audio. Final files in outputs/noiz/. Source and exports belong on branch codex/noiz-earbuds-reel in the existing GitHub repository.

Assumption: a vertical fictional earbuds campaign fits the brief. If actual earbuds are specified, replace asset and brand/copy before using as a real product advertisement. FCPXML from the earlier reel is flattened and its Resolve import is untested.

RESUME HERE: ten-second NOIZ campaign is complete and verified. Deliverables are in outputs/noiz and source/export in campaigns/noiz on codex/noiz-earbuds-reel. Check git remote if continuing repository work. For creative revisions use render.py and preserve the source product alpha. Prior five-second reel remains intact. Native Resolve automation remains unresolved.
