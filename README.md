
<img width="1357" height="580" alt="a4" src="https://github.com/user-attachments/assets/756c234c-c082-48f2-adf6-b61b042f2eba" />
<img width="1365" height="594" alt="a3" src="https://github.com/user-attachments/assets/376fa425-5838-4f25-8144-6666ffd9c382" />
<img width="1034" height="547" alt="a2" src="https://github.com/user-attachments/assets/01562988-6728-4097-9aab-ca9db6f8e9f4" />
<img width="1017" height="497" alt="a1" src="https://github.com/user-attachments/assets/ae188533-b4b7-42c0-b1bc-1d3faae2a15e" />






# 🚀 Endee RAG: High-Performance Distributed Search Engine

**Endee RAG** is a specialized Retrieval-Augmented Generation (RAG) system capable of "chatting" with documents at lightning speed.

Unlike standard AI apps, Endee RAG uses a **"Two-Brain" Architecture**: it offloads heavy mathematical vector search to a custom **C++ Backend (Endee Server)** while managing user logic in a **Python Frontend**, ensuring zero latency and 100% data privacy on local Cloud VMs.

## 🏗️ System Architecture
The system operates on a hybrid storage model:



[Image of client server architecture diagram]


1.  **Frontend (The Interface):** Streamlit app that handles file uploads and user queries. It talks to the backend via HTTP API.
2.  **Backend (The Muscle):** A C++ Vector Database optimized with AVX2 instructions for high-speed similarity search on Port 8080.
3.  **Intelligence Layer:** Llama 3.2 (LLM) and Nomic Embeddings running locally via Ollama.
4.  **Text Store:** SQLite database (\`rag_memory.db\`) for storing raw document content.

## ✨ Key Features
* **🚀 Hardware Accelerated:** Uses C++ AVX2 optimizations for millisecond-level vector retrieval.
* **💾 Hybrid Storage:** Splits data between SQLite (Text) and C++ Engine (Vectors) for maximum efficiency.
* **📄 Omni-Format Support:** Processes PDFs, Word Docs (\`.docx\`), Text (\`.txt\`), and Markdown (\`.md\`).
* **🔒 Privacy-First:** Runs entirely offline on your VM. No data leaves your server.

## 🛠️ Tech Stack
* **Frontend:** Python 3.10+, Streamlit, LangChain
* **Backend:** C++ 17, CMake (Custom Vector Engine)
* **AI Engine:** Ollama (Llama 3.2:1b + Nomic-Embed-Text)
* **Database:** SQLite + Custom Vector Store

## ⚙️ Installation & Setup (VM Deployment)

### 1. Prerequisites
* Ubuntu 20.04/22.04 VM
* C++ Compiler (GCC) & CMake
* Python 3.10+ & Pip

### 2. Setup Intelligence Layer (Ollama)
\`\`\`bash
curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama3.2:1b
ollama pull nomic-embed-text
\`\`\`

### 3. Build & Start Backend (C++ Server)
Compile the high-performance engine:
\`\`\`bash
mkdir build && cd build
cmake ..
make
\`\`\`
Start the server in the background (Port 8080):
\`\`\`bash
nohup ./ndd_server --port 8080 &
\`\`\`

### 4. Setup & Start Frontend (Python)
Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`
Start the User Interface:
\`\`\`bash
streamlit run app.py
\`\`\`

## 🚀 Usage
1.  Open your browser and navigate to \`http://<YOUR-VM-IP>:8501\`.
2.  **Upload Tab:** Select PDF or Word documents. The system will split them and send vectors to the C++ engine.
3.  **Chat Tab:** Ask questions. The Python app will query the C++ backend for context and generate an answer using Llama 3.2.

---
*Built by Vibhin-818*

