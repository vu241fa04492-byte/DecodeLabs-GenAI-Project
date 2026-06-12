# RAG System Prompt Design

## Philosophy

The core challenge in RAG is preventing the model from "hallucinating" — answering from its 
training data instead of the provided document. This prompt enforces strict grounding.

## RAG System Prompt

```
You are a legal document analyst with expertise in contract law.

RULES (follow all strictly):
1. Answer ONLY using information found in the provided document.
2. For EVERY fact or claim, cite the page number: [Page X]
3. If the answer is not in the document, say: 
   "This information is not found in the provided document."
4. Do NOT use your general knowledge or training data.
5. Be concise, professional, and neutral.
6. If the document is ambiguous, say so and quote the relevant passage.

DOCUMENT:
[CONTEXT INJECTED HERE]
```

## Why These Rules Work

| Rule | Problem It Solves |
|------|-------------------|
| "Answer ONLY from document" | Prevents training data bleed-through |
| "Cite [Page X] for every fact" | Forces the model to retrieve, not generate |
| "Say Not Found explicitly" | Prevents confident guessing on missing info |
| "Do NOT use general knowledge" | Redundant reinforcement — LLMs need this twice |
| Low temperature (0.1) | Reduces creativity, increases faithfulness |

## Context Building Strategy

Pages are injected with markers:
```
--- PAGE 1 ---
[page 1 text]

--- PAGE 2 ---
[page 2 text]
```

This lets the model reference page numbers accurately in citations.

## Limitations

- Context window limits to ~14,000 characters (~8-12 pages)
- For 500-page documents, implement chunking + vector search (FAISS, ChromaDB)
- This implementation is a direct injection RAG — suitable for demo/internship
