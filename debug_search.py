import subprocess
import json

# CONFIGURATION
BASE_URL = "http://localhost:8080/api/v1"
AUTH_TOKEN = "super_secret_admin_token"
INDEX_NAME = "user_vibhin_v1" # Your index name from the UI

def run_curl(endpoint, payload):
    url = f"{BASE_URL}{endpoint}"
    cmd = [
        "curl", "-s", "-X", "POST", url,
        "-H", f"Authorization: {AUTH_TOKEN}",
        "-H", "Content-Type: application/json",
        "-d", json.dumps(payload)
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

print(f"--- 1. CHECKING STATS FOR {INDEX_NAME} ---")
# Try to get index stats to see if vectors are actually there
stats = run_curl(f"/index/{INDEX_NAME}/stats", {})
print(f"Stats Response: {stats}\n")

print("--- 2. TRYING SEARCH (Path A) ---")
# Test search with dummy vector (768 zeros)
dummy_vector = [0.0] * 768
payload = {
    "vector": dummy_vector,
    "k": 1,
    "include_metadata": True
}
response_a = run_curl(f"/index/{INDEX_NAME}/search", payload)
print(f"Search Response: {response_a}\n")

print("--- 3. TRYING SEARCH (Path B - Fallback) ---")
# Test fallback URL style
payload["index_name"] = INDEX_NAME
response_b = run_curl("/search", payload)
print(f"Fallback Response: {response_b}\n")
