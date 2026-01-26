from typing import List, Dict, Tuple
import numpy as np
from openai import OpenAI
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
client = OpenAI()


def embed_text(text: str) -> List[float]:
    """
    Generate embedding for a given text using OpenAI.
    """
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


MAX_SECTION_CHARS = 1500  # ~375 tokens


def build_section_embeddings(sections):
    section_texts = []
    embeddings = []

    for section in sections.values():
        text = section[:MAX_SECTION_CHARS]  # HARD LIMIT
        section_texts.append(text)
        embeddings.append(embed_text(text))

    return section_texts, embeddings



def retrieve_relevant_sections(
    query: str,
    sections: Dict[str, str],
    top_k: int = 3
) -> List[str]:
    """
    Retrieve top-K most relevant paper sections for a query.
    """
    # Embed query
    query_embedding = np.array(embed_text(query)).reshape(1, -1)

    # Embed sections
    section_texts, section_embeddings = build_section_embeddings(sections)

    # Compute similarity
    similarities = cosine_similarity(query_embedding, section_embeddings)[0]

    # Rank sections
    ranked_indices = np.argsort(similarities)[::-1][:top_k]

    # Return top-k section texts
    return [section_texts[i] for i in ranked_indices]
