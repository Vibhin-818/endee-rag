import requests
import json
import time

# --- CONFIG ---
BASE_URL = "http://localhost:8080/api/v1"
TOKEN = "secret123"
HEADERS = {"Authorization": TOKEN, "Content-Type": "application/json"}
INDEX = "doctor_test_v1"

def print_step(msg): print(f"\n🔹 {msg}")
def print_success(msg): print(f"✅ {msg}")
def print_fail(msg): print(f"❌ {msg}")

# 1. SETUP
print_step("Checking Database Health...")
try:
    r = requests.get(f"{BASE_URL}/health", timeout=2)
    if r.status_code == 200: print_success("Database is Online")
    else: 
        print_fail(f"Database Error: {r.status_code}")
        exit()
except:
    print_fail("Cannot connect to localhost:8080. Is Docker running?")
    exit()

# 2. CREATE FRESH INDEX
print_step(f"Creating Test Index '{INDEX}'...")
payload = {"index_name": INDEX, "dim": 768, "space_type": "cosine"}
requests.post(f"{BASE_URL}/index/create", headers=HEADERS, json=payload)
time.sleep(1) # Wait for creation

# 3. DEFINE TEST DATA (1 Vector)
dummy_vector = [0.1] * 768
item = {"id": "test_1", "vector": dummy_vector, "metadata": {"text": "hello"}}

# 4. BRUTE FORCE INGESTION FORMATS
formats = [
    ("Format A (Standard)", {"vectors": [item]}),
    ("Format B (Raw List)", [item]),
    ("Format C (Explicit Name)", {"index_name": INDEX, "vectors": [item]}),
    ("Format D (Key='data')", {"data": [item]})
]

for name, data in formats:
    print_step(f"Testing {name}...")
    
    # Try insert
    try:
        url = f"{BASE_URL}/index/{INDEX}/insert"
        r = requests.post(url, headers=HEADERS, json=data)
        print(f"   Response: {r.status_code} (Text: {r.text[:50]}...)")
    except Exception as e:
        print(f"   Request Failed: {e}")
        continue

    # CHECK IF IT WORKED (Did count go up?)
    time.sleep(1) # Allow flush
    try:
        stats = requests.get(f"{BASE_URL}/index/{INDEX}/stats", headers=HEADERS).json()
        count = stats.get("vector_count", 0)
        print(f"   VECTOR COUNT: {count}")
        
        if count > 0:
            print_success(f"WINNER FOUND! Use {name}")
            exit() # Stop, we found the solution
    except:
        print("   Could not read stats.")

print_fail("All formats failed. The issue might be the 'Nomic' dimension (768).")
