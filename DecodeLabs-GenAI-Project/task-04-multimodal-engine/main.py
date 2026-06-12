"""
Task 4 — The Multimodal Content Engine
DecodeLabs GenAI Internship

Pipeline: YouTube URL → Audio → Transcript (Whisper) → 5 Viral Reels (Groq)

Run:
    pip install groq openai-whisper yt-dlp moviepy python-dotenv
    Also install ffmpeg: https://ffmpeg.org/download.html
    python main.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# ─── Configuration ──────────────────────────────────────────────
AUDIO_PATH = "audio.mp3"
TRANSCRIPT_PATH = "transcript.txt"
OUTPUT_PATH = "reels_output.md"
WHISPER_MODEL = "base"  # options: tiny, base, small, medium, large-v3


def check_dependencies():
    """Check all required packages are installed."""
    missing = []
    try:
        import yt_dlp
    except ImportError:
        missing.append("yt-dlp")
    try:
        import whisper
    except ImportError:
        missing.append("openai-whisper")
    try:
        from groq import Groq
    except ImportError:
        missing.append("groq")

    if missing:
        print(f"❌ Missing packages: {', '.join(missing)}")
        print(f"Run: pip install {' '.join(missing)}")
        sys.exit(1)

    if not os.getenv("GROQ_API_KEY"):
        print("❌ GROQ_API_KEY not found in .env file")
        sys.exit(1)

    print("✅ All dependencies found")


def download_audio(youtube_url: str) -> bool:
    """Download audio from a YouTube URL using yt-dlp."""
    import yt_dlp

    print(f"\n⬇️  Downloading audio from: {youtube_url}")

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": "audio.%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
        "quiet": True,
        "no_warnings": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=True)
            title = info.get("title", "Unknown")
            duration = info.get("duration", 0)
            print(f"✅ Downloaded: '{title}' ({duration // 60}:{duration % 60:02d})")
            return True
    except Exception as e:
        print(f"❌ Download failed: {e}")
        return False


def transcribe_audio(audio_path: str = AUDIO_PATH) -> str:
    """Transcribe audio file using OpenAI Whisper (runs locally)."""
    import whisper

    if not Path(audio_path).exists():
        print(f"❌ Audio file not found: {audio_path}")
        sys.exit(1)

    print(f"\n🎙️  Transcribing audio with Whisper ({WHISPER_MODEL})...")
    print("   This may take 1-3 minutes depending on video length and hardware.")

    model = whisper.load_model(WHISPER_MODEL)
    result = model.transcribe(audio_path, verbose=False)
    transcript = result["text"].strip()

    # Save transcript
    with open(TRANSCRIPT_PATH, "w", encoding="utf-8") as f:
        f.write(transcript)

    word_count = len(transcript.split())
    print(f"✅ Transcription complete — {word_count} words")
    return transcript


def load_transcript(path: str = TRANSCRIPT_PATH) -> str:
    """Load an existing transcript file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def generate_reels(transcript: str) -> str:
    """Use Groq LLM to identify viral segments and generate Reels content."""
    from groq import Groq

    print("\n🤖 Generating viral Reels content with AI...")

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""You are a viral social media expert and content strategist with 10 years of experience 
creating short-form content that gets millions of views on Instagram Reels, TikTok, and YouTube Shorts.

Given this video transcript, identify the 5 MOST engaging and shareable segments.
For each segment, create complete social media assets.

SELECTION CRITERIA for viral segments:
- Contains a surprising insight, strong opinion, or counterintuitive fact
- Has an emotional hook (inspiration, humor, relatable pain, or shock)
- Can be understood without context from the rest of the video
- Is 30-90 seconds when spoken aloud

For each of the 5 segments, generate:
1. VIRAL HEADLINE — punchy, under 10 words, creates curiosity or FOMO
2. CAPTION — 3 sentences: (1) attention hook, (2) value statement, (3) call-to-action with emoji
3. B-ROLL DESCRIPTION — specific visual shots, transitions, and text overlays for this reel
4. SEGMENT QUOTE — the exact most quotable line from this part of the transcript

TRANSCRIPT:
{transcript[:6000]}

Format EXACTLY as follows for each reel:

REEL 1:
Headline: [under 10 words]
Caption: [3 sentences with CTA and emoji]
B-Roll: [specific visual descriptions, 2-3 sentences]
Quote: "[exact quotable line from transcript]"

REEL 2:
[same format]

[continue for all 5 reels]"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2000,
    )

    return response.choices[0].message.content


def save_output(reels_content: str, transcript: str):
    """Save results to a formatted markdown file."""
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("# 🎬 Generated Short-Form Reels\n")
        f.write("*Generated by DecodeLabs Multimodal Content Engine*\n\n")
        f.write("---\n\n")
        f.write(reels_content)
        f.write("\n\n---\n\n")
        f.write("## 📝 Full Transcript\n\n")
        f.write(f"```\n{transcript}\n```\n")

    print(f"\n💾 Saved to {OUTPUT_PATH}")


def main():
    print("=" * 60)
    print("  🎥 DecodeLabs Multimodal Content Engine")
    print("  Video → Transcript → 5 Viral Reels")
    print("=" * 60)

    check_dependencies()

    # Check if transcript already exists (skip re-download/transcribe)
    if Path(TRANSCRIPT_PATH).exists() and Path(TRANSCRIPT_PATH).stat().st_size > 100:
        print(f"\n📄 Found existing transcript: {TRANSCRIPT_PATH}")
        use_existing = input("Use existing transcript? (y/n): ").strip().lower()
        if use_existing == "y":
            transcript = load_transcript()
            print(f"✅ Loaded transcript — {len(transcript.split())} words")
        else:
            transcript = None
    else:
        transcript = None

    if not transcript:
        print("\nChoose input method:")
        print("  1. YouTube URL")
        print("  2. Local video file (video.mp4)")
        print("  3. Local audio file (audio.mp3)")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == "1":
            url = input("Enter YouTube URL: ").strip()
            if not download_audio(url):
                sys.exit(1)
            transcript = transcribe_audio()

        elif choice == "2":
            if not Path("video.mp4").exists():
                print("❌ video.mp4 not found in current directory")
                sys.exit(1)
            # Extract audio from video
            try:
                from moviepy import VideoFileClip
                print("\n🎬 Extracting audio from video.mp4...")
                clip = VideoFileClip("video.mp4")
                clip.audio.write_audiofile("audio.mp3", verbose=False, logger=None)
                clip.close()
                print("✅ Audio extracted")
            except ImportError:
                print("❌ Install moviepy: pip install moviepy")
                sys.exit(1)
            transcript = transcribe_audio()

        elif choice == "3":
            if not Path("audio.mp3").exists():
                print("❌ audio.mp3 not found in current directory")
                sys.exit(1)
            transcript = transcribe_audio()

        else:
            print("❌ Invalid choice")
            sys.exit(1)

    # Generate Reels content
    reels_content = generate_reels(transcript)

    # Display output
    print("\n" + "=" * 60)
    print(reels_content)
    print("=" * 60)

    # Save to file
    save_output(reels_content, transcript)

    print(f"\n✅ Done! Check {OUTPUT_PATH} for your 5 viral Reels.")
    print("📱 Share these scripts with your video editor or use CapCut/Runway for production.")


if __name__ == "__main__":
    main()
