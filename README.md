
<img width="1357" height="580" alt="a4" src="https://github.com/user-attachments/assets/756c234c-c082-48f2-adf6-b61b042f2eba" />
<img width="1365" height="594" alt="a3" src="https://github.com/user-attachments/assets/376fa425-5838-4f25-8144-6666ffd9c382" />
<img width="1034" height="547" alt="a2" src="https://github.com/user-attachments/assets/01562988-6728-4097-9aab-ca9db6f8e9f4" />
<img width="1017" height="497" alt="a1" src="https://github.com/user-attachments/assets/ae188533-b4b7-42c0-b1bc-1d3faae2a15e" />






Here is the step-by-step procedure of how the Endee RAG project was built, from the very first command to the final deployment. You can include this in your report's "Methodology" section.
Phase 1: Environment Setup (The Foundation)
We started by setting up a robust development environment on a Google Cloud VM to handle the heavy AI processing.
Cloud VM Provisioning:
Created a Google Cloud Compute Engine instance (e2-standard-4) with Ubuntu 22.04.
Configured SSH access to securely manage the server remotely.
System Dependencies:
Updated the Linux package manager (apt update).
Installed essential tools: git, curl, python3-pip, cmake, and build-essential (for compiling the C++ backend).
Python Environment:
Created a virtual environment to keep libraries organized:
Bash
python3 -m venv venv_rag
source venv_rag/bin/activate


Phase 2: The Intelligence Layer (AI Models)
We set up the local AI "brains" using Ollama so the system could work offline without paying for OpenAI API keys.
Installing Ollama:
Ran the official install script: curl -fsSL https://ollama.com/install.sh | sh.
Pulling Models:
Downloaded the Llama 3.2 (1B) model for generating answers (lightweight and fast).
Downloaded the Nomic-Embed-Text model for converting text into vectors.
Verification:
Tested the models in the terminal to ensure they could accept prompts and generate text.
Phase 3: The Backend Storage (The "Two-Brain" System)
We designed a hybrid storage architecture to optimize performance.
Vector Database (Endee C++ Server):
Cloned the custom C++ vector engine repository.
Compiled the engine using cmake to enable hardware accelerations (AVX2).
Configured the server to run on Port 8080, exposing endpoints like /insert and /search.
Text Database (SQLite):
Designed a relational database schema (user_docs table) to store the raw English text.
Implemented rag_memory.db to link Vector IDs (from Endee) to actual content.
Phase 4: The Application Logic (Streamlit Frontend)
We built the user interface and the "glue" code in Python (app.py).
UI Construction:
Used Streamlit to create a clean web interface with tabs for "File Upload" and "Chat".
Added session state management to handle user logins and chat history.
Ingestion Pipeline:
Integrated PyPDF2 and python-docx to extract text from user files.
Implemented Recursive Text Splitting to chop documents into 1000-character chunks.
Created the Batch Processor to send vectors to the C++ server and text to SQLite simultaneously.
Retrieval Logic:
Built the search function: Input -> Vector -> Endee Search -> ID List -> SQLite Lookup -> LLM Context.
Phase 5: Deployment & version Control
1. VM Configuration:
Provisioned a Google Cloud Compute Engine instance (Ubuntu 22.04).
Configured Firewall rules to allow traffic on Port 8501 (Streamlit) and Port 8080 (Endee Backend).
Established SSH access for remote management.
2. Backend Deployment (The "Endee" Brain):
Compilation: Compiled the C++ source code directly on the VM using cmake and make to optimize for the specific server CPU (AVX2 instructions).
Execution: Started the Endee Vector Database as a background daemon using nohup to ensure it keeps running even after SSH disconnection.
Bash
nohup ./ndd_server --port 8080 &


Verification: Verified the server was listening using netstat -tuln | grep 8080.
3. Frontend Deployment (The Interface):
Environment: Set up a dedicated Python virtual environment (venv) to isolate dependencies.
Execution: Deployed the Streamlit application on Port 8501, also using nohup for persistence.
Bash
nohup streamlit run app.py --server.port 8501 &


4. Linking Streamlit to Endee:
The critical link was established in app.py via a configuration constant.
We pointed the Python EndeeClient to the local loopback address of the running C++ service:
Python
# app.py configuration
ENDEE_URL = "http://127.0.0.1:8080/api/v1"


This enabled the Python frontend to offload heavy vector search tasks to the C++ backend via high-speed HTTP requests (REST API) with zero network latency (since both run on the same VM).


