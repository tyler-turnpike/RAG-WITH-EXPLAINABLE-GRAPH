
# **Explainable Research Paper Explainer (RAG-based)**

## **Overview**

This project implements an **Explainable Retrieval-Augmented Generation (RAG)** system for understanding **research papers**. Users can upload a PDF, ask questions, and receive **grounded answers**, along with **supporting evidence**, an **LLM-generated explanation (knowledge) graph**, and **recommended follow-up questions**.

Unlike standard QA systems, this application emphasizes **transparency and trust** by explicitly showing how answers are derived from the source document.

---

## **Key Features**

* PDF-based **question answering**
* **Evidence-grounded answers** (no hallucination)
* Automatic **research paper sectioning**
* **Semantic retrieval** using embeddings
* **Knowledge graph construction** from answers and evidence
* Context-aware **follow-up question recommendations**
* Interactive **Streamlit web interface**

---

## **System Pipeline**

```
PDF Upload
   ↓
PDF → Text Extraction
   ↓
High-signal Section Segmentation
   ↓
Semantic Retrieval (Embeddings + Similarity)
   ↓
Grounded Answer Generation
   ↓
Explanation Graph Construction
   ↓
Recommended Follow-up Questions
```

Each stage is modular, inspectable, and explainable.

---

## **Project Structure**

```
project/
│
├── app.py                  # Streamlit application
├── pipeline.py             # Full RAG pipeline orchestration
│
├── document_ingestor.py    # PDF → text extraction
├── paper_loader.py         # Section segmentation
├── retriever.py            # Semantic retrieval (embeddings)
├── answer_generator.py     # Grounded answer generation
├── graph_builder.py        # Knowledge graph construction
├── recommender.py          # Follow-up question generation
├── ui_components.py        # UI rendering (graph, evidence, questions)
│
├── requirements.txt
├── .env
└── README.md
```

---

## **Technologies Used**

* **Python**
* **Streamlit** – Web interface
* **OpenAI API** – Embeddings and LLM reasoning
* **PyMuPDF (fitz)** – PDF text extraction
* **scikit-learn** – Cosine similarity
* **NetworkX & PyVis** – Knowledge graph creation and visualization
* **NumPy**

---

## **How It Works**

1. **PDF Upload**
   Users upload a research paper via the Streamlit UI.

2. **Text Extraction**
   The PDF is converted to raw text in memory.

3. **Section Segmentation**
   Only meaningful sections (abstract, introduction, method, etc.) are retained.

4. **Semantic Retrieval**
   Query and sections are embedded and compared using cosine similarity.

5. **Answer Generation**
   Answers are generated strictly from retrieved evidence with bounded tokens.

6. **Knowledge Graph Construction**
   Key concepts and relationships are extracted into a structured graph.

7. **Follow-up Questions**
   Three context-aware research questions are generated for deeper exploration.

---

## **Running the Application**

### **1. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **2. Set OpenAI API Key**

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

### **3. Run the App**

```bash
streamlit run app.py
```

---

## **Example Use Cases**

* Understanding complex research papers quickly
* Academic literature review
* Demonstrating **Explainable AI**
* Internship, interview, or project demonstrations
* RAG system prototyping

---

## **Explainability Principles**

* Answers are **strictly grounded in retrieved evidence**
* Knowledge graphs expose **conceptual relationships**
* No black-box responses
* Clear traceability from answer → evidence → document

---

## **Future Enhancements**

* Interactive graph filtering
* Multi-paper comparison
* Persistent vector database
* Citation-level highlighting
* Exportable explanations

---

