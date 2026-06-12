# Prompt 5 — Brand Character & Image-to-Image Consistency

## Tool: Midjourney (with --cref)

### Step 1 — Generate Base Character
```
A futuristic AI brand mascot character: a sleek humanoid android with a 
chrome-silver geometric faceplate, glowing cyan eye lenses, wearing a dark 
structured corporate suit with neon violet accent piping. Gender-neutral. 
Standing confidently in a corporate pose. Dark studio background with 
subtle neon underglow. Ultra-detailed, 3D render style, 8K. 
Cyberpunk-corporate aesthetic.
--ar 1:1 --v 6 --q 2 --s 750
```

### Step 2 — Variations Using Character Reference

**Scene A — At a holographic workstation:**
```
The NexCore AI android mascot seated at a sleek holographic desk reviewing 
glowing data dashboards, chrome faceplate, cyan eyes, dark suit, 
office with floor-to-ceiling city view at night
--cref [PASTE BASE IMAGE URL HERE] --cw 100 --ar 16:9 --v 6
```

**Scene B — Presenting to audience:**
```
The NexCore AI android mascot standing and gesturing toward a large holographic 
projection screen showing neural network diagrams, same chrome appearance, 
corporate auditorium with audience silhouettes
--cref [PASTE BASE IMAGE URL HERE] --cw 100 --ar 16:9 --v 6
```

### Why This Matters
Using `--cref` ensures your brand character looks the same across every image 
without needing a 3D model or illustrator. This is the image-to-image technique 
that creates visual brand consistency at scale.

### Consistency Checklist
- [x] Same faceplate design across all scenes
- [x] Same cyan eye color
- [x] Same dark corporate suit
- [x] Same cyberpunk-corporate color palette
- [x] Same lighting style (neon underglow, rim light)
