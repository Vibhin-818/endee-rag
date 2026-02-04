import requests

URL = "http://localhost:8080/api/v1"
HEADERS = {"Authorization": "super_secret_admin_token"}

try:
    # 1. Test Health/Connection
    print("Testing connection...")
    requests.get(f"{URL}/index/list", headers=HEADERS, timeout=5)
    print("✅ Connection OK")

    # 2. Test Index Creation
    print("Testing Index Creation...")
    payload = {"name": "test_index", "dimension": 768, "metric": "cosine"}
    res = requests.post(f"{URL}/index/create", json=payload, headers=HEADERS)
    print(f"Index Create Status: {res.status_code}")
    print(f"Response: {res.text}")

except Exception as e:
    print(f"❌ ERROR: {e}")
