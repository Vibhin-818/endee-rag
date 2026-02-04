
<img width="1357" height="580" alt="a4" src="https://github.com/user-attachments/assets/756c234c-c082-48f2-adf6-b61b042f2eba" />
<img width="1365" height="594" alt="a3" src="https://github.com/user-attachments/assets/376fa425-5838-4f25-8144-6666ffd9c382" />
<img width="1034" height="547" alt="a2" src="https://github.com/user-attachments/assets/01562988-6728-4097-9aab-ca9db6f8e9f4" />
<img width="1017" height="497" alt="a1" src="https://github.com/user-attachments/assets/ae188533-b4b7-42c0-b1bc-1d3faae2a15e" />




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
