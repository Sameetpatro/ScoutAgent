# hf_utils.py
import os
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

# You can switch models here if needed
API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

def query_hf(prompt: str) -> str:
    payload = {"inputs": prompt}
    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, list) and "generated_text" in data[0]:
            return data[0]["generated_text"]
        elif isinstance(data, dict):
            return data.get("generated_text", str(data))
        else:
            return str(data)
    except Exception as e:
        return f"[ERROR] {str(e)}"
