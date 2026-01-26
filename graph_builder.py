from openai import OpenAI

client = OpenAI()


def build_knowledge_graph(
    answer: str,
    evidence_chunks: list[str],
    max_words: int = 100
) -> dict | None:
    """
    Build a concise, LLM-generated knowledge graph
    from the answer and supporting evidence.
    """


    if not answer or not evidence_chunks:
        return None

    # Keep context small
    context = "\n\n".join(evidence_chunks[:2])
    context = context[:1200]

    prompt = f"""
You are an AI system that converts explanations into knowledge graphs.

Using the answer and evidence below, extract:
- Key concepts (nodes)
- Relationships between them (edges)

Return the result as JSON with:
- "nodes": list of strings
- "edges": list of (source, relation, target)

Keep the entire response under {max_words} words.

Answer:
{answer}

Evidence:
{context}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate concise knowledge graphs."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=300
    )

    content = response.choices[0].message.content.strip()


    return(content)
