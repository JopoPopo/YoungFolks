import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_api():
    print("--- Testing GET /hello ---")
    hello_res = requests.get(f"{BASE_URL}/hello")
    print(f"Status: {hello_res.status_code}")
    print(f"Response: {hello_res.json()}\n")

    print("--- Testing GET /data (Before POST) ---")
    data_before = requests.get(f"{BASE_URL}/data")
    print(f"Items in list: {len(data_before.json()['campuses'])}\n")

    print("--- Testing POST /data ---")
    new_campus = {
        "id": 4,
        "campus": "I-75 Center",
        "lat": 26.01,
        "lon": -80.39
    }
    # This 'json=' parameter automatically sets the Header to 'application/json'
    post_res = requests.post(f"{BASE_URL}/data", json=new_campus)
    print(f"Status: {post_res.status_code}")
    print(f"Response: {post_res.json()}\n")

    print("--- Testing GET /data (After POST) ---")
    data_after = requests.get(f"{BASE_URL}/data")
    print(f"Items in list: {len(data_after.json()['campuses'])}")
    print(f"Full Data: {json.dumps(data_after.json(), indent=2)}")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("ERROR: Make sure your Flask app is running in another terminal!")