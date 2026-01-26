import streamlit as st
import networkx as nx
import ast
import json
import re
from typing import List
from pyvis.network import Network
import tempfile
import streamlit.components.v1 as components
import os


def parse_graph_string(graph_str):
    """
    Convert LLM-produced graph string into a Python dict.
    """
    # Remove ```json ``` wrappers
    cleaned = re.sub(r"```json|```", "", graph_str).strip()

    # Convert tuple-style edges to list-style edges
    cleaned = cleaned.replace("(", "[").replace(")", "]")

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        try:
            return ast.literal_eval(cleaned)
        except Exception:
            return None



def dict_to_nx_digraph(graph_dict):
    G = nx.DiGraph()

    for node in graph_dict.get("nodes", []):
        G.add_node(node)

    for src, rel, tgt in graph_dict.get("edges", []):
        G.add_edge(src, tgt, label=rel)

    return G


# --------------------------------------------------
# Answer Rendering
# --------------------------------------------------
def render_answer(answer: str) -> None:
    """Render the generated answer."""
    st.subheader("✅ Answer")
    st.write(answer)


# --------------------------------------------------
# Entity Rendering
# --------------------------------------------------
def render_entities(entities: List[str]) -> None:
    """Render extracted entities."""
    st.subheader("🔍 Key Entities")

    if not entities:
        st.write("No entities could be extracted from the evidence.")
        return

    for entity in entities:
        st.markdown(f"- **{entity}**")


# --------------------------------------------------
# Graph Rendering
# --------------------------------------------------


def render_graph(graph):
    st.subheader("🕸️ Explanation Graph")

    print("RENDER_GRAPH type:", type(graph))

    # --- STRING → STRUCTURED ---
    if isinstance(graph, str):
        parsed = parse_graph_string(graph)
        if not parsed:
            st.error("Failed to parse graph text.")
            st.code(graph)
            return
        graph = parsed

    # --- DICT → NETWORKX ---
    if isinstance(graph, dict):
        G = dict_to_nx_digraph(graph)
    elif isinstance(graph, nx.Graph):
        G = graph
    else:
        st.error(f"Unsupported graph type: {type(graph)}")
        return

    if G.number_of_edges() == 0:
        st.info("No relationships to display.")
        return

    # --- VISUALIZE WITH ARROWS ---
    net = Network(height="500px", width="100%", directed=True)
    net.from_nx(G)

    for u, v, data in G.edges(data=True):
        if "label" in data:
            net.edges[-1]["label"] = data["label"]
            net.edges[-1]["arrows"] = "to"

    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as f:
        net.save_graph(f.name)
        components.html(open(f.name).read(), height=550)

    os.unlink(f.name)

# --------------------------------------------------
# Evidence Rendering
# --------------------------------------------------
def render_evidence(evidence_chunks: List[str]) -> None:
    """Render retrieved evidence supporting the answer."""
    st.subheader("📚 Supporting Evidence")

    if not evidence_chunks:
        st.write("No supporting evidence available.")
        return

    for idx, chunk in enumerate(evidence_chunks, start=1):
        with st.expander(f"Evidence Chunk {idx}"):
            st.write(chunk)


# --------------------------------------------------
# Recommended Questions Rendering
# --------------------------------------------------
def render_recommended_questions(questions: List[str]) -> None:
    """Render recommended follow-up questions."""
    st.subheader("💡 Recommended Follow-up Questions")

    if not questions:
        st.write("No recommendations available.")
        return

    for question in questions:
        st.markdown(f"- {question}")
