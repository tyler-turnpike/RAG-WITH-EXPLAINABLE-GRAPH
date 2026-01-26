import fitz  # PyMuPDF


def ingest_pdf_file(uploaded_file) -> str:
    """
    Extract text from an uploaded PDF file (Streamlit uploader).
    Returns raw text.
    """
    text = ""

    # Open PDF from memory
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()

    return text
