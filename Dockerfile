FROM python:3.10-slim

# Install system dependencies (curl is needed for Ollama)
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

# Install Ollama (The AI Engine)
RUN curl -fsSL https://ollama.com/install.sh | sh

# Set working directory
WORKDIR /app

# Copy python requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Make the startup script executable
RUN chmod +x start.sh

# Expose the port Railway uses
ENV PORT=8501
EXPOSE 8501

# Run the startup script
CMD ["./start.sh"]
