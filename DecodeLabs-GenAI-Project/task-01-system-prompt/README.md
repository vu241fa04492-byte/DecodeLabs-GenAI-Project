# Task 1 — The System Prompt Architect 🏨

## Overview

Designed a professional AI persona **"Seraphina"** for a luxury travel agency using advanced system prompting, persona engineering, and few-shot prompting techniques.

## Key Concepts Demonstrated

- **System Prompt Engineering** — defining tone, constraints, and persona boundaries
- **Persona Engineering** — creating a believable, consistent luxury brand voice
- **Few-Shot Prompting** — teaching the model ideal responses via examples
- **Behavioral Constraints** — no competitors mentioned, no flat discounts
- **Knowledge Boundaries** — model stays in role under adversarial pressure

## How to Run

```bash
# Install dependencies
pip install groq python-dotenv

# Add your GROQ_API_KEY to the .env file

# Run the chatbot
python app.py
```

## Files

| File | Description |
|------|-------------|
| `app.py` | Interactive terminal chatbot using Groq + Llama 3.3 |
| `prompts/system_prompt.md` | The full system prompt with persona rules |
| `prompts/few_shot_examples.md` | 3 few-shot example interactions |
| `outputs/sample_conversation.md` | Sample demo conversation output |

## Persona: Seraphina

- **Role:** Elite Experience Designer at Luxe Horizon Travel
- **Experience:** 15+ years curating bespoke itineraries for HNWIs
- **Tone:** Sophisticated, poised, deeply attentive
- **Constraints:** No competitor mentions, no percentage discounts, no casual language

## Design Decisions

**Why Few-Shot Prompting?**
The luxury tone is subtle — "no problem" vs "with absolute pleasure." Few-shot examples train the model on the exact register without lengthy rules.

**Why Groq (Llama 3.3)?**
Free, fast, and the 70B model handles persona maintenance well. Easily swappable to GPT-4 or Claude.
