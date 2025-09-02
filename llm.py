# llm.py
import os
import requests

HF_API_KEY = os.getenv("HF_API_KEY")  # make sure you add this to .env
MODEL = "mistralai/Mistral-7B-Instruct-v0.2"  # you can change to another free model


def query_hf(prompt, model: str = MODEL, max_new_tokens: int = 150, temperature: float = 0.7):
    """
    Sends a prompt to Hugging Face Inference API and returns the model's response.
    - Default model: Mistral-7B-Instruct (free, good for chat/inference)
    - max_new_tokens: response length
    - temperature: randomness (0.7 = balanced)
    """
    headers = {
        "Authorization": f"Bearer {HF_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": max_new_tokens,
            "temperature": temperature
        }
    }

    try:
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{model}",
            headers=headers,
            json=payload,
            timeout=60
        )

        if response.status_code != 200:
            return f"[ERROR] Hugging Face API failed: {response.status_code} {response.text}"

        data = response.json()
        if isinstance(data, list) and len(data) > 0 and "generated_text" in data[0]:
            return data[0]["generated_text"]
        return "[ERROR] Unexpected Hugging Face response format."

    except Exception as e:
        return f"[ERROR] Hugging Face query failed: {e}"
