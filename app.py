import streamlit as st
import networkx as nx

from document_ingestor import ingest_pdf_file
from pipeline import run_pipeline
from ui_components import (
    render_graph,
    render_evidence,
    render_recommended_questions,
)


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Explainable Research Paper Explainer",
    layout="wide"
)

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 2.5rem;
        padding-bottom: 3rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    h1 { font-size: 2.4rem; }
    h2 { font-size: 1.8rem; margin-top: 2.5rem; }
    h3 { font-size: 1.4rem; margin-top: 2rem; }

    .stMarkdown p {
        font-size: 1.05rem;
        line-height: 1.7;
    }

    .section {
        margin-top: 3rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Title & Description
# -----------------------------
st.title("📄 Explainable Research Paper Explainer")
st.write(
    "Upload a research paper (PDF), ask a question, and receive a **grounded answer**, "
    "an **LLM-generated knowledge graph**, supporting evidence, and **follow-up questions**."
)

# -----------------------------
# PDF Upload
# -----------------------------
uploaded_pdf = st.file_uploader(
    "Upload a research paper (PDF)",
    type=["pdf"]
)

# -----------------------------
# Question Input
# -----------------------------
query = st.text_input(
    "Ask a question about the paper",
    placeholder="e.g., How does RAG prevent hallucinations?"
)

# -----------------------------
# Run Pipeline
# -----------------------------
if uploaded_pdf and query:

    print("DEBUG: PDF uploaded")
    print("DEBUG: Query received:", query)

    # Enforce query length (≤100 words)
    if len(query.split()) > 100:
        st.error("Please limit your question to 100 words.")
        st.stop()

    with st.spinner("Processing paper and generating explanation..."):
        # 1. Convert PDF to text
        document_text = ingest_pdf_file(uploaded_pdf)
        print("DEBUG: Document text length:", len(document_text))

        # 2. Run full pipeline
        result = run_pipeline(
            document_text=document_text,
            query=query
        )

    print("DEBUG: Pipeline result keys:", result.keys())

    st.success("Analysis complete!")

    # -----------------------------
    # Answer
    # -----------------------------
    st.subheader("✅ Answer")
    answer = result.get("answer", "No answer could be generated.")
    print("DEBUG: Answer:", answer)
    st.write(answer)

    # -----------------------------
    # Knowledge Graph
    # -----------------------------
    st.subheader("🧠 Explanation (Knowledge Graph)")

    graph = result.get("graph")

    print("DEBUG: Raw graph value:", graph)
    print("DEBUG: Raw graph type:", type(graph))
    print("DEBUG: Is nx.Graph?", isinstance(graph, nx.Graph))

    if isinstance(graph, dict):
        print("DEBUG: Graph dict keys:", graph.keys())
        print("DEBUG: Dict edges:", graph.get("edges"))

    if graph is None:
        print("DEBUG: Graph is None")
        st.info("No knowledge graph could be constructed from the retrieved evidence.")

    elif isinstance(graph, nx.Graph) and graph.number_of_edges() == 0:
        print("DEBUG: Graph is nx.Graph with 0 edges")
        st.info("The paper does not contain enough structured concepts to form a graph.")

    else:
        print("DEBUG: Calling render_graph()")
        render_graph(graph)

    # -----------------------------
    # Supporting Evidence
    # -----------------------------
    evidence = result.get("evidence", [])
    print("DEBUG: Evidence type:", type(evidence))
    print("DEBUG: Evidence count:", len(evidence) if evidence else 0)

    if evidence:
        render_evidence(evidence)
    else:
        st.info("No supporting evidence was retrieved.")

    # -----------------------------
    # Recommended Follow-up Questions
    # -----------------------------
    questions = result.get("recommended_questions", [])
    print("DEBUG: Questions type:", type(questions))
    print("DEBUG: Questions count:", len(questions) if questions else 0)

    if questions:
        render_recommended_questions(questions)
    else:
        st.info("No follow-up questions could be generated.")
