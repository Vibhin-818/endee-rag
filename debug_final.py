import requests
import json
import random
from langchain_community.embeddings import OllamaEmbeddings

# --- CONFIG ---
URL = "http://127.0.0.1:8080/api/v1"
TOKEN = "secret123"
INDEX = "debug_v1"

print("\n🔍 --- DIAGNOSTIC REPORT ---")

# 1. CHECK MODEL DIMENSIONS
print("\n[1] Checking Embedding Model...")
try:
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vec = embeddings.embed_query("test")
    dim = len(vec)
    print(f"   ✅ Model Output Dimension: {dim}")
except Exception as e:
    print(f"   ❌ Model Error: {e}")
    exit()

# 2. CREATE MATCHING INDEX
print(f"\n[2] Creating Index 'debug_v1' with dim={dim}...")
headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
requests.delete(f"{URL}/index/{INDEX}/delete", headers=headers) # Clean start

payload = {
    "index_name": INDEX, 
    "dim": dim,           # DYNAMICALLY MATCH THE MODEL
    "space_type": "cosine",
    "M": 32, 
    "ef_con": 200
}
res = requests.post(f"{URL}/index/create", headers=headers, json=payload)
print(f"   Status: {res.status_code}")

# 3. INSERT ONE VECTOR
print("\n[3] Inserting 1 Vector...")
data = [{"id": "test_1", "vector": vec}] # Raw List
res = requests.post(f"{URL}/index/{INDEX}/vector/insert", headers=headers, json=data)
print(f"   Status: {res.status_code}")

# 4. CHECK INFO (RAW)
print("\n[4] Reading Database Stats (RAW)...")
res = requests.get(f"{URL}/index/{INDEX}/info", headers=headers)
print(f"   Status: {res.status_code}")
print(f"   Raw Body: '{res.text}'")  # <--- THIS IS KEY

if res.text and "vector_count" in res.text:
    count = res.json().get("vector_count")
    print(f"\n✅ RESULT: Database holds {count} vectors.")
    if count > 0:
        print("   🚀 FIX: Update your app.py to use 'dim={dim}'")
else:
    print("\n❌ RESULT: Database returned empty/invalid stats.")
