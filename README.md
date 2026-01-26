#  Explainable Research Paper Explainer (RAG-based)

##  Overview

This project implements an **Explainable Retrieval-Augmented Generation (RAG)** system for **research paper understanding**.
Unlike standard QA systems, this application not only answers user questions but also **explicitly shows where the answer comes from** using **retrieved evidence, extracted entities, and an explanation graph**.

The system is designed to work directly with **research paper PDFs**, making it suitable for academic exploration, literature review, and explainable AI demonstrations.

---

##  Key Objectives

* Enable **question answering over research papers**
* Ensure **answers are grounded in the source document**
* Provide **transparent explanations** via entities and relationships
* Support **interactive PDF upload** through a web interface
* Suggest **meaningful follow-up questions** for guided exploration

---

##  System Architecture

The system follows a **modular and explainable pipeline**:

```
PDF Upload (Streamlit)
        ↓
PDF → Text Extraction
        ↓
Text Segmentation (High-signal sections)
        ↓
Semantic Retrieval (OpenAI embeddings)
        ↓
Entity Extraction (spaCy)
        ↓
Explanation Graph Construction
        ↓
Grounded Answer Generation
        ↓
Recommended Follow-up Questions
```

Each stage is explicitly implemented and inspectable, ensuring transparency and debuggability.

---

##  Project Structure

```
RAG_with_explainable_graph/
│
├── data/
│   ├── papers/          # Optional preloaded papers
│   └── processed/       # Debug / intermediate outputs
│
├── src/
│   ├── document_ingestor.py     # PDF → text
│   ├── paper_loader.py          # Text segmentation
│   ├── retriever.py             # Semantic retrieval
│   ├── entity_extractor.py      # Entity extraction
│   ├── graph_builder.py         # Explanation graph
│   ├── answer_generator.py      # Grounded answer generation
│   ├── recommender.py           # Recommended questions
│   └── pipeline.py              # Full pipeline orchestration
│
├── app/
│   ├── app.py                   # Streamlit app
│   └── ui_components.py         # Reusable UI components
│
├── requirements.txt
├── .env
└── README.md
```

---

##  Technologies Used

* **Python 3**
* **Streamlit** – Web interface
* **OpenAI API** – Embeddings & answer generation
* **spaCy** – Entity extraction
* **NetworkX** – Explanation graph construction
* **PyMuPDF (fitz)** – PDF text extraction
* **scikit-learn** – Similarity computation

---

##  How It Works (Step-by-Step)

1. **PDF Upload**
   The user uploads a research paper PDF via the Streamlit interface.

2. **Document Ingestion**
   The PDF is converted to raw text in memory (no manual file handling).

3. **Text Segmentation**
   Only high-signal sections (Abstract, Introduction, Method, etc.) are retained.

4. **Semantic Retrieval**
   OpenAI embeddings are used to retrieve the most relevant sections for the user’s query.

5. **Entity Extraction**
   Key concepts are extracted from the retrieved evidence using deterministic NLP rules.

6. **Explanation Graph**
   Entities are connected based on co-occurrence to form a local explanation graph.

7. **Grounded Answer Generation**
   The final answer is generated **strictly from retrieved evidence**, preventing hallucination.

8. **Recommended Questions**
   The system suggests three context-aware follow-up questions to guide exploration.

---

##  Running the Application

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###   Set OpenAI API Key

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

###  Run Streamlit App

```bash
streamlit run app/app.py
```

Open the displayed local URL in your browser.

---

##  Example Use Cases

* Understanding complex research papers quickly
* Exploring methodologies and limitations of academic work
* Demonstrating **explainable AI** concepts
* Academic demos, hackathons, and interviews

---

##  Explainability & Trustworthiness

This system avoids black-box behavior by:

* Retrieving explicit evidence before answering
* Extracting entities directly from source text
* Constructing a visible explanation graph
* Constraining the language model to retrieved context only

As a result, **every answer can be traced back to the paper**.

---

##  Future Enhancements

* Interactive graph visualization
* Section-wise citation highlighting
* Multi-paper comparison
* Persistent vector storage
* User-clickable recommended questions

---

##  Final Note

This project is intentionally designed to balance **AI capability with transparency**.
It demonstrates not just *what* the answer is — but **why that answer should be trusted**.

