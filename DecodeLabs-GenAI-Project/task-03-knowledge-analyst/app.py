"""
Task 3 — The Knowledge Analyst (RAG Concepts)
DecodeLabs GenAI Internship

A Streamlit app that implements RAG for legal document intelligence.
Answers questions with page-level citations and generates a Summary Dashboard.

Run:
    pip install groq pymupdf streamlit python-dotenv
    streamlit run app.py
"""

import os
import streamlit as st
import fitz  # PyMuPDF
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

# ─── Page Config ────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Knowledge Analyst | DecodeLabs",
    page_icon="📚",
    layout="wide"
)

# ─── Styles ─────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0a0a0f; }
    .stApp { background-color: #0d0d1a; }
    h1 { color: #00f5ff !important; }
    h2, h3 { color: #8b00ff !important; }
    .stButton > button {
        background-color: #00f5ff;
        color: black;
        font-weight: bold;
        border-radius: 8px;
    }
    .risk-box { background-color: #2d0000; border-left: 4px solid #ff4444; 
                padding: 10px; border-radius: 4px; margin: 5px 0; }
    .date-box { background-color: #001a2d; border-left: 4px solid #00f5ff; 
                padding: 10px; border-radius: 4px; margin: 5px 0; }
    .stake-box { background-color: #0d001a; border-left: 4px solid #8b00ff; 
                 padding: 10px; border-radius: 4px; margin: 5px 0; }
</style>
""", unsafe_allow_html=True)

# ─── Header ─────────────────────────────────────────────────────
st.title("📚 AI Knowledge Analyst")
st.markdown("**RAG-Powered Legal Document Intelligence** | DecodeLabs GenAI Internship")
st.divider()

# ─── Initialize Groq ────────────────────────────────────────────
@st.cache_resource
def get_client():
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return None
    return Groq(api_key=api_key)

client = get_client()

if not client:
    st.error("⚠️ GROQ_API_KEY not found. Add it to your .env file.")
    st.code("GROQ_API_KEY=your_key_here", language="bash")
    st.stop()


# ─── PDF Processing ─────────────────────────────────────────────
def extract_text_with_pages(pdf_file) -> list[dict]:
    """Extract text from each page of a PDF."""
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    pages = []
    for i, page in enumerate(doc):
        text = page.get_text()
        if text.strip():  # skip blank pages
            pages.append({"page": i + 1, "text": text})
    return pages


def build_context(pages: list[dict], max_chars: int = 14000) -> str:
    """Build a context string with page markers, respecting token limits."""
    context = ""
    for p in pages:
        block = f"\n\n--- PAGE {p['page']} ---\n{p['text']}"
        if len(context) + len(block) > max_chars:
            context += "\n\n[Document truncated for context length. Upload shorter documents for full analysis.]"
            break
        context += block
    return context


# ─── LLM Functions ──────────────────────────────────────────────
def ask_question(context: str, question: str) -> str:
    """Ask a question about the document with citation enforcement."""
    prompt = f"""You are a legal document analyst with expertise in contract law.

RULES (follow strictly):
1. Answer ONLY using information found in the document below.
2. For EVERY fact or claim, cite the page number like this: [Page X]
3. If the answer is not in the document, respond: "This information is not found in the provided document."
4. Do NOT use your general knowledge. Only use the document.
5. Be concise and professional.

DOCUMENT:
{context}

QUESTION: {question}

Answer with citations:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=800,
    )
    return response.choices[0].message.content


def generate_summary(context: str) -> str:
    """Generate a one-paragraph executive summary of the document."""
    prompt = f"""You are a senior legal analyst. Write a concise 3-4 sentence executive summary 
of this document. Focus on: what type of document it is, who the parties are, and the main purpose.
Cite key page numbers where relevant.

DOCUMENT:
{context}

Executive Summary:"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=300,
    )
    return response.choices[0].message.content


def extract_dashboard_data(context: str) -> str:
    """Extract Risks, Dates, and Stakeholders in structured format."""
    prompt = f"""You are a legal document analyst. Analyze this document and extract:

1. RISKS: List up to 6 potential risks, penalties, liabilities, or obligations (with page citations)
2. DATES: List all important dates, deadlines, and timeframes (with page citations)
3. STAKEHOLDERS: List all parties, companies, individuals, and organizations mentioned

DOCUMENT:
{context}

Respond in EXACTLY this format (no extra text):
RISKS:
- [Page X] Risk description here
- [Page X] Risk description here

DATES:
- [Page X] Date/deadline description here
- [Page X] Date/deadline description here

STAKEHOLDERS:
- Stakeholder name and role here
- Stakeholder name and role here"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
        max_tokens=600,
    )
    return response.choices[0].message.content


def parse_dashboard(raw: str) -> dict:
    """Parse the structured dashboard response into sections."""
    sections = {"RISKS": [], "DATES": [], "STAKEHOLDERS": []}
    current = None
    for line in raw.split("\n"):
        line = line.strip()
        if line.startswith("RISKS:"):
            current = "RISKS"
        elif line.startswith("DATES:"):
            current = "DATES"
        elif line.startswith("STAKEHOLDERS:"):
            current = "STAKEHOLDERS"
        elif line.startswith("- ") and current:
            sections[current].append(line[2:])
    return sections


# ─── Main UI ────────────────────────────────────────────────────
uploaded_file = st.file_uploader(
    "📎 Upload a Legal Document or Contract (PDF)",
    type=["pdf"],
    help="Upload any PDF — contracts, agreements, reports, technical documents"
)

if uploaded_file:
    with st.spinner("🔍 Reading and indexing document..."):
        pages = extract_text_with_pages(uploaded_file)
        context = build_context(pages)

    col1, col2, col3 = st.columns(3)
    col1.metric("📄 Pages Indexed", len(pages))
    col2.metric("📝 Characters Extracted", f"{len(context):,}")
    col3.metric("🤖 Model", "Llama 3.3 70B")

    st.success(f"✅ Document loaded successfully — {len(pages)} pages indexed")

    # Executive Summary
    with st.expander("📋 Executive Summary", expanded=True):
        if st.button("Generate Summary"):
            with st.spinner("Summarizing..."):
                summary = generate_summary(context)
            st.write(summary)

    st.divider()

    # Tabs
    tab1, tab2 = st.tabs(["💬 Ask Questions (with Citations)", "📊 Summary Dashboard"])

    # ── Tab 1: Q&A ────────────────────────────────────────────────
    with tab1:
        st.subheader("Ask anything about the document")
        st.caption("Every answer will include page citations from the original document.")

        # Suggested questions
        st.markdown("**Quick Questions:**")
        q_cols = st.columns(3)
        suggestions = [
            "What are the termination conditions?",
            "What are the payment terms?",
            "Who are the parties to this agreement?",
            "What penalties apply for breach?",
            "What is the contract duration?",
            "What are the confidentiality obligations?",
        ]
        selected_q = None
        for i, q in enumerate(suggestions):
            if q_cols[i % 3].button(q, key=f"q{i}"):
                selected_q = q

        question = st.text_input(
            "Or type your own question:",
            value=selected_q or "",
            placeholder="e.g. What happens if payment is late?"
        )

        if st.button("🔍 Ask", type="primary") and question:
            with st.spinner("Analyzing document..."):
                answer = ask_question(context, question)
            st.markdown("### Answer")
            st.info(answer)

    # ── Tab 2: Dashboard ─────────────────────────────────────────
    with tab2:
        st.subheader("Auto-Extracted Intelligence Dashboard")
        st.caption("AI automatically identifies Risks, Dates, and Stakeholders from the document.")

        if st.button("🚀 Generate Dashboard", type="primary"):
            with st.spinner("Extracting key intelligence..."):
                raw_dashboard = extract_dashboard_data(context)
                data = parse_dashboard(raw_dashboard)

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown("### 🚨 Risks & Liabilities")
                if data["RISKS"]:
                    for item in data["RISKS"]:
                        st.markdown(
                            f'<div class="risk-box">⚠️ {item}</div>',
                            unsafe_allow_html=True
                        )
                else:
                    st.info("No risks found or document too short.")

            with col2:
                st.markdown("### 📅 Important Dates")
                if data["DATES"]:
                    for item in data["DATES"]:
                        st.markdown(
                            f'<div class="date-box">📅 {item}</div>',
                            unsafe_allow_html=True
                        )
                else:
                    st.info("No dates found.")

            with col3:
                st.markdown("### 👥 Stakeholders")
                if data["STAKEHOLDERS"]:
                    for item in data["STAKEHOLDERS"]:
                        st.markdown(
                            f'<div class="stake-box">👤 {item}</div>',
                            unsafe_allow_html=True
                        )
                else:
                    st.info("No stakeholders identified.")

else:
    st.info("👆 Upload a PDF document to begin. The AI will analyze it and answer your questions with citations.")

    st.markdown("""
    ### How this works
    
    1. **Upload** any PDF contract or legal document
    2. **Ask questions** and get answers citing exact page numbers  
    3. **Generate Dashboard** to auto-extract Risks, Dates, and Stakeholders
    4. The AI only uses your document — no hallucination from general knowledge
    
    ### Example use cases
    - Review employment contracts before signing
    - Quickly understand a vendor agreement
    - Identify risks in partnership agreements
    - Extract key dates from lease contracts
    """)
