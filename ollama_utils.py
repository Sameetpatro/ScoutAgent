import subprocess

def query_ollama(prompt, model="llama3"):
    """
    Sends a prompt to Ollama and returns the model's response.
    Requires Ollama to be installed and running locally.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        output = result.stdout.decode("utf-8").strip()
        return output
    except Exception as e:
        return f"[ERROR] Ollama query failed: {e}"
