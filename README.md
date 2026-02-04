# 🚀 Endee RAG: High-Performance Local Search Engine

**Endee RAG** is a "Turbo" Retrieval-Augmented Generation (RAG) application designed for speed and flexibility. It allows users to upload multiple documents (PDF, Word, Text, Markdown), processes them instantly using batch vectorization, and lets users chat with their data using a local LLM.

## ✨ Key Features
* **Omni-Format Support:** Upload PDFs, Word Docs (), Text files (), and Markdown ().
* **⚡ Turbo Processing:** Uses batch ingestion (100 chunks/batch) for 10x faster document loading.
* **Local Privacy:** Runs entirely offline using **Ollama** (Llama 3.2 + Nomic Embeddings).
* **Smart Context:** Advanced  for precise answer retrieval.
* **Instant UI:** Built with **Streamlit** for a responsive, clean user experience.

## 🛠️ Tech Stack
* **Frontend:** Streamlit
* **LLM Engine:** Ollama (Llama 3.2:1b)
* **Embeddings:** Nomic-Embed-Text
* **Vector Store:** SQLite + Vector Search (Custom Implementation)
* **Framework:** LangChain

## ⚙️ Installation Guide

### 1. Prerequisites
* Python 3.10+
* [Ollama](https://ollama.com/) installed and running.

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Pull Required Models
Make sure your local Ollama instance has the required models:
```bash
ollama pull llama3.2:1b
ollama pull nomic-embed-text
```

## 🚀 How to Run
Start the application with one command:

```bash
streamlit run app.py
```

---
*Created by [Your Name / Vibhin-818]*
