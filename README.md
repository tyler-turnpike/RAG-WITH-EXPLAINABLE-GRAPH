
# **Explainable Research Paper Explainer (RAG-based System)**

## 📌 Overview

This project implements an **Explainable Retrieval-Augmented Generation (RAG)** system that helps users understand **research papers** in a transparent and trustworthy way. Users can upload a PDF, ask questions, and receive **evidence-grounded answers**, an **LLM-generated explanation graph**, and **context-aware follow-up questions**.

Unlike standard QA systems, this application focuses on **explainability**, clearly showing how answers are derived from the source document. 

---

## 🚀 Key Features

* PDF-based **question answering**
* **Evidence-grounded responses** to reduce hallucinations
* Automatic **research paper section segmentation**
* **Semantic retrieval** using embeddings and cosine similarity
* **Knowledge graph generation** from answers and evidence
* **Follow-up question recommendations**
* Interactive **Streamlit web interface**

---

## 🧠 System Pipeline

```
PDF Upload
   ↓
Text Extraction
   ↓
High-Signal Section Segmentation
   ↓
Semantic Retrieval (Embeddings)
   ↓
Grounded Answer Generation
   ↓
Knowledge Graph Construction
   ↓
Follow-up Question Recommendation
```

Each stage is modular, inspectable, and explainable.

---

## 🏗️ Project Structure

```
project/
│
├── app.py                  # Streamlit application
├── pipeline.py             # End-to-end RAG pipeline
│
├── document_ingestor.py    # PDF → text extraction
├── paper_loader.py         # Section segmentation
├── retriever.py            # Semantic retrieval
├── answer_generator.py     # Evidence-grounded answers
├── graph_builder.py        # Knowledge graph generation
├── recommender.py          # Follow-up question generation
├── ui_components.py        # UI rendering (graph, evidence)
│
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Web interface
* **OpenAI API** – LLM reasoning & embeddings
* **PyMuPDF (fitz)** – PDF text extraction
* **scikit-learn** – Cosine similarity
* **NumPy**

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Set OpenAI API Key

Create a `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📚 Example Use Cases

* Understanding complex research papers quickly
* Academic literature review
* Demonstrating **Explainable AI**
* LLM / RAG system prototyping
* Internship and interview demonstrations

---

## 🔍 Explainability Principles

* Answers are **strictly grounded in retrieved evidence**
* Knowledge graphs expose **conceptual relationships**
* Clear traceability from **answer → evidence → document**
* No black-box responses

---

## 🔮 Future Enhancements

* Multi-paper comparison
* Persistent vector database
* Citation-level highlighting
* Interactive graph filtering
* Exportable explanations

---
