import requests, os

import os
print("HuggingFace Key:", os.getenv("HUGGINGFACE_API_KEY"))

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

print(query({"inputs": "Translate English to French: 'Hello, how are you?'" }))
