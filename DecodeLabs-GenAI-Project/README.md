# 🤖 DecodeLabs Generative AI Internship — All 5 Tasks

> **Team Project** | DecodeLabs GenAI Internship Program | June 2026

---

## 👥 Team Members

| Member | Tasks Handled |
|--------|--------------|
| **Babul Kumar** | Task 1, Task 2, Task 3, Task 4 (core), Task 5 (automation) |
| **Manaswini** | Task 1 (chatbot), Task 3 (RAG app), Task 4 (reels), Task 5 (audit report) |

---

## 📁 Project Structure

```
DecodeLabs-GenAI-Project/
│
├── task-01-system-prompt/          # The System Prompt Architect
│   ├── prompts/
│   │   ├── system_prompt.md        # Core persona system prompt
│   │   └── few_shot_examples.md    # Few-shot prompting examples
│   ├── outputs/
│   │   └── sample_conversation.md  # Demo conversation transcript
│   ├── app.py                      # Interactive chatbot (Groq API)
│   └── README.md
│
├── task-02-creative-visionary/     # The Creative Visionary
│   ├── prompts/
│   │   ├── 01_logo_concept.md
│   │   ├── 02_hero_image.md
│   │   ├── 03_social_banner.md
│   │   ├── 04_icon_set.md
│   │   └── 05_character_reference.md
│   ├── generated_images/           # Put your generated images here
│   └── README.md
│
├── task-03-knowledge-analyst/      # The Knowledge Analyst (RAG)
│   ├── prompts/
│   │   ├── 01_rag_system_prompt.md
│   │   ├── 02_citation_qa_prompt.md
│   │   └── 03_summary_dashboard_prompt.md
│   ├── outputs/
│   │   ├── 01_document_summary.md
│   │   ├── 02_qa_examples.md
│   │   └── 03_summary_dashboard.md
│   ├── app.py                      # Streamlit RAG app (Groq + PyMuPDF)
│   └── README.md
│
├── task-04-multimodal-engine/      # The Multimodal Content Engine
│   ├── main.py                     # Full pipeline: video → reels
│   ├── requirements.txt
│   ├── reels_output.md             # Sample output
│   └── README.md
│
├── task-05-ai-safety-audit/        # The AI Safety & Bias Audit
│   ├── main.py                     # Automated audit script
│   ├── test_prompts.json           # Red-team test cases
│   ├── outputs/
│   │   ├── audit_results.json
│   │   └── AI_Safety_Audit_Report.md
│   ├── screenshots/                # Put bias/redteam screenshots here
│   └── README.md
│
├── .env.example                    # API key template
├── requirements.txt                # Master dependencies
└── README.md                       ← You are here
```

---

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/DecodeLabs-GenAI-Project.git
cd DecodeLabs-GenAI-Project
```

### 2. Create a Virtual Environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys
```bash
cp .env.example .env
# Then open .env and fill in your actual API keys
```

### 5. Run Each Task
```bash
# Task 1 — Travel Bot
python task-01-system-prompt/app.py

# Task 3 — RAG Knowledge Analyst (Streamlit)
streamlit run task-03-knowledge-analyst/app.py

# Task 4 — Multimodal Reels Engine
python task-04-multimodal-engine/main.py

# Task 5 — AI Safety Audit
python task-05-ai-safety-audit/main.py
```

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **LLMs** | GPT-4, Claude, Llama 3.3 70B (via Groq) |
| **Image Gen** | DALL·E 3, Midjourney, Stable Diffusion |
| **Speech-to-Text** | OpenAI Whisper |
| **RAG / Documents** | PyMuPDF (fitz), Claude Projects |
| **Video Processing** | MoviePy, yt-dlp |
| **APIs** | OpenAI API, Groq API, Anthropic API |
| **Frontend** | Streamlit |
| **Safety Testing** | Manual Red-Teaming, Custom Prompt Framework |

---

## 📋 Task Summaries

### ✅ Task 1 — The System Prompt Architect
Built a luxury travel AI persona called **Seraphina** with strict tone constraints, competitor avoidance, and value-based discount handling using Few-Shot Prompting.

### ✅ Task 2 — The Creative Visionary
Generated a **Cyberpunk-Corporate** brand identity with 5 consistent visual assets: Logo, Hero Image, Social Banner, Icon Set, and Brand Character using DALL·E 3 and Midjourney.

### ✅ Task 3 — The Knowledge Analyst (RAG)
Built a Streamlit app that accepts PDF uploads, answers questions with **page-level citations**, and auto-generates a Summary Dashboard extracting Risks, Dates, and Stakeholders.

### ✅ Task 4 — The Multimodal Content Engine
Pipeline that converts a YouTube video → audio → transcript (Whisper) → 5 viral Reels with headlines, captions, B-roll descriptions, and segment quotes (Groq/GPT-4).

### ✅ Task 5 — The AI Safety & Bias Audit
Red-teaming exercise with 8 adversarial test cases across medical, legal, cyber, jailbreak, gender bias, and cultural bias categories. Includes an auto-generated Audit Report and Safety Framework.

---

## 📊 Results Summary

| Task | Status | Key Output |
|------|--------|-----------|
| Task 1 | ✅ Complete | Seraphina persona + working chatbot |
| Task 2 | ✅ Complete | 5 brand-consistent AI images |
| Task 3 | ✅ Complete | RAG Streamlit app with citations |
| Task 4 | ✅ Complete | Automated video → 5 Reels pipeline |
| Task 5 | ✅ Complete | Full AI Audit Report + Safety Framework |

---

## 🔑 API Keys Required

| Key | Used In | Where to Get |
|-----|---------|-------------|
| `GROQ_API_KEY` | Task 1, 3, 4 | [console.groq.com](https://console.groq.com) |
| `OPENAI_API_KEY` | Task 4, 5 | [platform.openai.com](https://platform.openai.com) |

---

## 📜 License

This project was built as part of the **DecodeLabs Generative AI Internship Program**.

---

*Built with ❤️ by Babul Kumar & Manaswini — DecodeLabs GenAI Internship 2026*
