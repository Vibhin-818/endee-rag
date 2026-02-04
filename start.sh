#!/bin/bash
echo "🔴 Starting Ollama..."
ollama serve &
sleep 5
echo "⬇️  Pulling models..."
ollama pull llama3.2:1b
ollama pull nomic-embed-text
echo "🟢 Starting Streamlit..."
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
