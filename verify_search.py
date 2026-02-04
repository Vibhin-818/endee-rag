import requests
import json
import random
import msgpack

# --- CONFIG ---
URL = "http://127.0.0.1:8080/api/v1"
TOKEN = "secret123"
INDEX = "search_test_v1"

print("🔍 --- SEARCH DIAGNOSTIC ---")

# 1. SETUP: Create Index
print("\n[1] Creating Index...")
headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
requests.delete(f"{URL}/index/{INDEX}/delete", headers=headers)
requests.post(f"{URL}/index/create", headers=headers, json={
    "index_name": INDEX, "dim": 768, "space_type": "cosine", "M": 32, "ef_con": 200
})

# 2. INSERT: Known Vector
print("[2] Inserting 1 Vector...")
# We use a random vector for testing
vec = [random.random() for _ in range(768)]
# ID is "test_target" (String)
requests.post(f"{URL}/index/{INDEX}/vector/insert", headers=headers, json=[
    {"id": "test_target", "vector": vec}
])

# 3. SEARCH: Look for that EXACT vector
print("[3] Searching for it...")
search_payload = {"vector": vec, "k": 1}
# Request BINARY response
res = requests.post(
    f"{URL}/index/{INDEX}/search", 
    headers={"Authorization": TOKEN, "Content-Type": "application/json", "Accept": "application/msgpack"},
    json=search_payload
)

print(f"   Status: {res.status_code}")
print(f"   Content-Type: {res.headers.get('Content-Type')}")

# 4. DECODE AND INSPECT
print("\n[4] Inspecting Response Data types...")
if res.status_code == 200:
    try:
        # Decode MsgPack
        data = msgpack.unpackb(res.content, raw=False) # raw=False tries to decode strings
        print(f"   RAW DATA: {data}")
        
        # Check type of the first result
        if isinstance(data, list) and len(data) > 0:
            first_id = data[0].get('id')
            print(f"   ID Value: {first_id}")
            print(f"   ID Type:  {type(first_id)}") # <--- THIS IS WHAT WE NEED
            
            if isinstance(first_id, bytes):
                print("\n❌ PROBLEM FOUND: Server returned BYTES, App expects STRINGS.")
            else:
                print("\n✅ Data types look correct (String).")
                
        elif isinstance(data, dict):
            # Handle {"matches": [...]} structure
            matches = data.get("matches", []) or data.get("results", [])
            if matches:
                first_id = matches[0].get('id')
                print(f"   ID Value: {first_id}")
                print(f"   ID Type:  {type(first_id)}")
            else:
                print("   ❌ Search returned empty list/dict.")
                
    except Exception as e:
        print(f"   ❌ Decode Error: {e}")
else:
    print(f"   ❌ Server Error: {res.text}")
