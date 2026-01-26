from openai import OpenAI

client = OpenAI()

def generate_answer(
    query: str,
    evidence_chunks: list[str],
    max_tokens: int = 250
) -> str:
    """
    Generate a grounded answer using retrieved evidence.
    Output length is strictly controlled.
    """

    # Keep prompt small
    context = "\n\n".join(evidence_chunks[:3])
    context = context[:1500]  # HARD CONTEXT LIMIT

    prompt = f"""
You are an AI research assistant.

Answer the question strictly using the provided evidence.
If the evidence is insufficient, say so clearly.

Question:
{query}

Evidence:
{context}

Answer in at most {max_tokens} tokens.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a precise academic assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.2
    )

    return response.choices[0].message.content.strip()
