from typing import Dict, Any

from paper_loader import segment_text
from retriever import retrieve_relevant_sections
from answer_generator import generate_answer
from graph_builder import build_knowledge_graph
from recommender import recommend_questions


def run_pipeline(
    document_text: str,
    query: str,
    top_k: int = 3
) -> Dict[str, Any]:
    """
    Full explainable RAG pipeline
    """

    # 1. Segment document
    sections = segment_text(document_text)
    if not sections:
        return {
            "answer": "No meaningful content could be extracted.",
            "graph": None,
            "evidence": [],
            "recommended_questions": []
        }

    # 2. Retrieve evidence
    evidence_chunks = retrieve_relevant_sections(
        query=query,
        sections=sections,
        top_k=top_k
    )

    # 3. Generate answer (bounded)
    answer = generate_answer(
        query=query,
        evidence_chunks=evidence_chunks,
        max_tokens=250
    )

    # 4. Build knowledge graph from answer + evidence
    graph = build_knowledge_graph(
        answer=answer,
        evidence_chunks=evidence_chunks,
        max_words=100
    )
    

    




    # 5. Generate follow-up questions
    recommended_questions = recommend_questions(
        answer=answer,
        evidence_chunks=evidence_chunks
    )

    return {
        "answer": answer,
        "graph": graph,
        "evidence": evidence_chunks,
        "recommended_questions": recommended_questions
    }
