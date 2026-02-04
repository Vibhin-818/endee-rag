
<img width="1357" height="580" alt="a4" src="https://github.com/user-attachments/assets/756c234c-c082-48f2-adf6-b61b042f2eba" />
<img width="1365" height="594" alt="a3" src="https://github.com/user-attachments/assets/376fa425-5838-4f25-8144-6666ffd9c382" />
<img width="1034" height="547" alt="a2" src="https://github.com/user-attachments/assets/01562988-6728-4097-9aab-ca9db6f8e9f4" />
<img width="1017" height="497" alt="a1" src="https://github.com/user-attachments/assets/ae188533-b4b7-42c0-b1bc-1d3faae2a15e" />






Here is the comprehensive Methodology & Deployment Guide formatted specifically for your README.md.

You can append this section to your existing README or use it to replace the "Installation" section to reflect the full VM-based "Two-Brain" setup.

⚙️ Methodology: How We Built Endee RAG
This project was built in 5 Strategic Phases to ensure high performance, modularity, and zero-latency local execution on a Cloud VM.

Phase 1: Environment Setup (The Foundation)
We established a robust development environment on Google Cloud to handle heavy AI processing.

Cloud Provisioning: Deployed a Google Cloud Compute Engine instance (e2-standard-4) running Ubuntu 22.04.

System Dependencies: Updated Linux repositories and installed essential build tools (git, curl, python3-pip, cmake, build-essential) required for compiling the C++ backend.

Python Isolation: Created a dedicated virtual environment (venv_rag) to manage dependencies cleanly.

Phase 2: The Intelligence Layer (AI Models)
We configured local AI "brains" using Ollama to enable offline capabilities without external API costs.

Engine Setup: Installed the Ollama runtime via the official shell script.

Model Acquisition:

Llama 3.2 (1B): Selected for its lightweight footprint and fast generation speed.

Nomic-Embed-Text: Chosen for high-quality vector embeddings.

Verification: Validated model inference directly in the terminal to ensure system readiness.

Phase 3: The Backend Storage (The "Two-Brain" System)
We designed a hybrid storage architecture to optimize for both speed and data integrity.

Vector Database (Endee C++ Server):

Cloned and compiled the custom C++ vector engine using cmake to enable AVX2 hardware acceleration.

Configured the server to listen on Port 8080, exposing high-performance REST endpoints (/insert, /search).

Text Database (SQLite):

Designed a relational schema (user_docs table) to store raw English text.

Implemented rag_memory.db to act as the persistent link between Vector IDs and readable content.

Phase 4: The Application Logic (Streamlit Frontend)
We built the user interface and "glue" logic in Python (app.py).

UI Construction: Developed a clean, tabbed interface ("File Upload", "Chat") using Streamlit, complete with session state management.

Ingestion Pipeline: Integrated PyPDF2 and python-docx for text extraction and implemented Recursive Text Splitting to chunk documents into 1,000-character segments.

Retrieval Logic: Engineered the core search pipeline:

Input → Vector → Endee Search (C++) → ID List → SQLite Lookup → LLM Context

Phase 5: Deployment & Integration (VM-Based)
Finalizing the deployment of the "Two-Brain" architecture on the cloud VM.

1. VM Configuration
Provisioned the Ubuntu 22.04 instance.

Configured firewall rules to allow ingress traffic on Port 8501 (Frontend) and Port 8080 (Backend).

Secured remote management via SSH keys.

2. Backend Deployment (The "Endee" Brain)
Compilation: Built the C++ source code directly on the VM to optimize for the specific CPU instruction set (AVX2).

Execution: Deployed the Vector Database as a background daemon using nohup for persistence.

Bash

nohup ./ndd_server --port 8080 &
Verification: Confirmed active listening ports using netstat -tuln | grep 8080.

3. Frontend Deployment (The Interface)
Environment: Activated the venv to isolate Python dependencies.

Execution: Launched the Streamlit application as a background service.

Bash

nohup streamlit run app.py --server.port 8501 &
4. Linking Streamlit to Endee
The critical integration point was established in app.py. We configured the Python EndeeClient to communicate with the local C++ service via the loopback address:

Python

# app.py configuration
ENDEE_URL = "http://127.0.0.1:8080/api/v1"
Result: This architecture enables the Python frontend to offload computationally expensive vector search tasks to the C++ backend via high-speed HTTP requests, achieving near-zero network latency.
