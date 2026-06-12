# Task 2 — The Creative Visionary 🎨

## Overview

Generated a complete **Cyberpunk-Corporate** brand identity for a fictional tech startup "NexCore AI" using advanced AI image generation techniques.

## Brand Identity: NexCore AI

**Aesthetic:** Cyberpunk-Corporate — neon-lit precision meets enterprise authority  
**Color Palette:** Deep obsidian (#0A0A0F), Electric cyan (#00F5FF), Neon violet (#8B00FF), Chrome silver (#C0C0C0)  
**Mood:** Powerful, futuristic, trustworthy, intelligent

## Assets Generated (5 Images)

| # | Asset | Tool Used | Dimensions |
|---|-------|-----------|------------|
| 1 | Logo Concept | DALL·E 3 | 1024×1024 |
| 2 | Hero Image (Website) | Midjourney | 1920×1080 |
| 3 | Social Media Banner | DALL·E 3 | 1200×628 |
| 4 | Icon Set (6 icons) | Stable Diffusion | 512×512 each |
| 5 | Brand Character / Mascot | Midjourney | 1024×1024 |

## How to Reproduce

1. Copy each prompt from the `prompts/` folder
2. Paste into your image generation tool of choice
3. For **Midjourney**: use in Discord with `/imagine [prompt]`
4. For **DALL·E 3**: use ChatGPT Plus or the OpenAI API
5. For **Stable Diffusion**: use Automatic1111 or ComfyUI

## Brand Consistency Technique

To maintain consistency across images:
- Always include the same color palette description
- Use the same lighting style: "blue-violet rim lighting, neon underglow"  
- Include the same negative prompts to exclude unwanted elements
- For Midjourney, use `--sref` (style reference) with the logo as the reference image

## Files

| File | Description |
|------|-------------|
| `prompts/01_logo_concept.md` | Logo generation prompt with negative prompts |
| `prompts/02_hero_image.md` | Hero image with lighting and composition specs |
| `prompts/03_social_banner.md` | Social banner with aspect ratio |
| `prompts/04_icon_set.md` | Icon set generation prompt |
| `prompts/05_character_reference.md` | Character for image-to-image consistency |
| `generated_images/` | Place your generated images here |
