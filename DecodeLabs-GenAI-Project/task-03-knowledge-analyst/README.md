# Task 3 — The Knowledge Analyst (RAG) 📚

## Overview

A Streamlit web app that implements a **Retrieval-Augmented Generation (RAG)** workflow for legal document intelligence. Upload any PDF contract and get cited answers + an auto-generated Summary Dashboard.

## How to Run

```bash
# Install dependencies
pip install groq pymupdf streamlit python-dotenv

# Add GROQ_API_KEY to .env file

# Launch the app
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

## Features

| Feature | Description |
|---------|-------------|
| 📄 PDF Upload | Upload any contract or legal PDF |
| 💬 Q&A with Citations | Ask questions, get answers citing [Page X] |
| 🚨 Risk Extraction | Auto-identifies liabilities and risks |
| 📅 Date Extraction | Pulls all important dates and deadlines |
| 👥 Stakeholder Mapping | Identifies all parties mentioned |
| 🛡️ Hallucination Guard | Model only answers from the document |

## RAG Workflow Explained

```
PDF Upload
    ↓
Page-by-page text extraction (PyMuPDF)
    ↓
Context string built with page markers: "--- PAGE 1 ---"
    ↓
User question + context sent to LLM
    ↓
LLM answers ONLY from document, cites [Page X]
    ↓
Answer displayed with source references
```

## Hallucination Prevention Strategy

The system prompt includes strict rules:
- "Answer ONLY using information from the document"
- "For every fact, cite the exact page number like [Page X]"
- "If the answer is not in the document, say so explicitly"
- No general knowledge allowed

## Files

| File | Description |
|------|-------------|
| `app.py` | Full Streamlit RAG application |
| `prompts/01_rag_system_prompt.md` | Core RAG system prompt design |
| `prompts/02_citation_qa_prompt.md` | Q&A with citation enforcement |
| `prompts/03_summary_dashboard_prompt.md` | Dashboard extraction prompt |
| `outputs/` | Sample outputs from a test document |
