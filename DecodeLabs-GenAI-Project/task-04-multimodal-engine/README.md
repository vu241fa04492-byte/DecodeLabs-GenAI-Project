# Task 4 — The Multimodal Content Engine 🎥

## Overview

An automated pipeline that transforms a YouTube video (or local video file) into 5 short-form social media Reels with viral headlines, captions, B-roll descriptions, and segment quotes.

## Workflow

```
YouTube URL / video.mp4
       ↓
   yt-dlp (download audio)
       ↓
   Whisper (speech-to-text)
       ↓
   transcript.txt
       ↓
   Groq LLM (viral segment detection)
       ↓
   5 Reels with:
   ├── Viral Headline (< 10 words)
   ├── Caption (hook + value + CTA)
   ├── B-roll Description
   └── Segment Quote
       ↓
   reels_output.md / reels_output.txt
```

## How to Run

### Option A — YouTube URL (requires yt-dlp + ffmpeg)
```bash
pip install groq openai-whisper yt-dlp python-dotenv
pip install moviepy  # for local video files

python main.py
# When prompted: Enter YouTube URL: https://youtube.com/watch?v=...
```

### Option B — Local Video File
```bash
# Place your video as video.mp4 in this folder
python main_local.py
```

### Requirements
- `GROQ_API_KEY` in `.env` file
- `ffmpeg` installed (for audio extraction)
  - Windows: `winget install ffmpeg` or download from ffmpeg.org
  - Mac: `brew install ffmpeg`
  - Linux: `apt install ffmpeg`

## Files

| File | Description |
|------|-------------|
| `main.py` | Full pipeline: YouTube URL → Reels output |
| `requirements.txt` | Python dependencies |
| `reels_output.md` | Sample output from a test video |
| `transcript.txt` | Auto-generated transcript |

## Sample Output Format

```
REEL 1:
Headline: This One Habit Changed Everything About My Productivity
Caption: Most people waste 3 hours a day without knowing it. Here's the simple 
         shift that saved mine. Try this for 7 days and report back. 👇
B-Roll: Time-lapse of a morning routine, close-up of a phone being put face-down, 
        split-screen before/after productivity graphs
Quote: "The moment I stopped checking my phone first thing in the morning, 
        everything changed."
```

## Why Whisper?

OpenAI Whisper is open-source, runs locally, and achieves near-human transcription 
accuracy across 99 languages. The `base` model runs on CPU; use `large-v3` for best quality.
