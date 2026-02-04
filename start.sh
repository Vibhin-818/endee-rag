#!/bin/bash

# Start Ollama in the background
echo "🔴 Starting Ollama Server..."
ollama serve &

# Wait a few seconds for Ollama to wake up
sleep 5

# Pull the models (This happens on every deploy)
echo "⬇️  Downloading AI Models (Llama 3.2 & Nomic)..."
ollama pull llama3.2:1b
ollama pull nomic-embed-text

# Start the Streamlit App
echo "🟢 Starting Endee RAG..."
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
