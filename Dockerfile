FROM python:3.10-slim

# 1. Install system tools (curl for Ollama, build-essential for some python libs)
RUN apt-get update && apt-get install -y curl build-essential && rm -rf /var/lib/apt/lists/*

# 2. Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# 3. Set up the app
WORKDIR /app

# 4. Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your project files
COPY . .

# 6. Setup the startup script
COPY start.sh .
RUN chmod +x start.sh

# 7. Railway Configuration
ENV PORT=8501
EXPOSE 8501

# 8. Run the start script
CMD ["./start.sh"]
