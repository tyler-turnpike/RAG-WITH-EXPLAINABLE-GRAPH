import re
from typing import Dict


# Sections we consider meaningful for reasoning
SECTION_HEADERS = [
    "abstract",
    "introduction",
    "method",
    "methodology",
    "approach",
    "limitations",
    "conclusion"
]


def normalize_text(text: str) -> str:
    """
    Normalize text for consistent processing.
    """
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def segment_text(text: str) -> Dict[str, str]:
    """
    Segment raw research paper text into high-signal sections.
    """
    text = normalize_text(text)
    sections = {}

    for i, header in enumerate(SECTION_HEADERS):
        pattern = rf"\b{header}\b"
        match = re.search(pattern, text)

        if not match:
            continue

        start = match.end()
        end = len(text)

        for next_header in SECTION_HEADERS[i + 1:]:
            next_match = re.search(rf"\b{next_header}\b", text[start:])
            if next_match:
                end = start + next_match.start()
                break

        content = text[start:end].strip()

        # Filter very small or noisy sections
        if len(content.split()) > 50:
            sections[header] = content

    return sections
