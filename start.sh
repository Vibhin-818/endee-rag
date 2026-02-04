#!/bin/bash

# 1. Start Ollama in the background
echo "🔴 Starting Ollama..."
ollama serve &

# 2. Wait for it to wake up
sleep 5

# 3. Download the models (Required every restart on Railway)
echo "⬇️  Pulling models..."
ollama pull llama3.2:1b
ollama pull nomic-embed-text

# 4. Start your App
echo "🟢 Starting Streamlit..."
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
