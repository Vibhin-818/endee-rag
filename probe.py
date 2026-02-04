import requests
import json
import random
import os

# --- CONFIG ---
URL = "http://127.0.0.1:8080/api/v1"
TOKEN = "secret123"
INDEX = "probe_test_v1"
HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}

def run():
    print(f"🔍 PROBING ENDEE AT {URL}...")

    # 1. DELETE OLD INDEX (Clean Slate)
    requests.delete(f"{URL}/index/{INDEX}/delete", headers=HEADERS)

    # 2. CREATE INDEX (Standard 768)
    print("1️⃣  Creating Index (Dim: 768)...")
    res = requests.post(f"{URL}/index/create", headers=HEADERS, json={
        "index_name": INDEX, "dim": 768, "space_type": "cosine", "precision": "int8"
    })
    print(f"   Status: {res.status_code} | {res.text}")

    # 3. GENERATE DUMMY VECTOR
    # We create a random vector of EXACTLY 768 floats
    vec = [random.random() for _ in range(768)]
    payload = [{"id": "test_doc_1", "vector": vec}]

    # 4. INSERT
    print("2️⃣  Inserting 1 Vector...")
    url = f"{URL}/index/{INDEX}/vector/insert"
    res = requests.post(url, headers=HEADERS, json=payload)
    print(f"   Status: {res.status_code} | Response: {res.text}")

    # 5. CHECK COUNT
    print("3️⃣  Checking Vector Count...")
    res = requests.get(f"{URL}/index/{INDEX}/info", headers=HEADERS)
    data = res.json()
    count = data.get("vector_count", 0)
    print(f"   COUNT: {count}")

    if count > 0:
        print("\n✅ SUCCESS! The DB works. The issue is your PDF Embedding Model output size.")
    else:
        print("\n❌ FAILURE! The DB rejected the data.")
        print("   Dumping Server Logs to see WHY...")
        os.system("docker logs endee-server | tail -n 20")

if __name__ == "__main__":
    run()
