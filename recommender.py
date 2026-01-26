from openai import OpenAI

client = OpenAI()

MAX_QUESTION_TOKENS = 120  # hard bound for safety


def recommend_questions(answer, evidence_chunks):
    """
    Generate 3 high-quality follow-up research questions
    using only LLM reasoning grounded in evidence.
    """

    if not answer or not evidence_chunks:
        return []

    # Bounded context
    context = evidence_chunks[0][:1000]

    prompt = f"""
You are an AI research assistant.

Based on the following research explanation and supporting evidence,
generate exactly THREE insightful follow-up questions that a researcher
would naturally ask next.

Rules:
- Questions must be concise and non-redundant
- Questions must be technical or conceptual
- Do NOT mention authors, emails, or metadata
- Do NOT repeat the same idea

Explanation:
{answer}

Supporting Evidence:
{context}

Return ONLY the questions as a numbered list.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=MAX_QUESTION_TOKENS,
        temperature=0.4
    )

    # Parse numbered list safely
    lines = response.choices[0].message.content.split("\n")
    questions = [line.lstrip("123.- ").strip() for line in lines if line.strip()]

    return questions[:3]
