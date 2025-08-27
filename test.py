import os
import requests

api_key = os.getenv("INTELX_API_KEY")
url = "https://free.intelx.io/intelligent/search"

headers = {
    "x-key": api_key,
    "Content-Type": "application/json"
}

payload = {
    "term": "ransomware",
    "maxresults": 3,
    "media": 0
}

response = requests.post(url, headers=headers, json=payload)

print(f"Status code: {response.status_code}")
print("Response JSON:", response.json())
