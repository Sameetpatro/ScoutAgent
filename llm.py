import subprocess

def query_ollama(prompt, model="phi3:mini", num_predict=150):
    """
    Sends a prompt to Ollama and returns the model's response.
    - Default model: phi3:mini (lightweight & fast)
    - num_predict: limits max tokens so it doesn’t hang
    Requires Ollama installed & running locally.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", model, f"--num-predict", str(num_predict)],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60  # prevent infinite hang
        )

        if result.returncode != 0:
            return f"[ERROR] Ollama failed: {result.stderr.decode('utf-8').strip()}"

        output = result.stdout.decode("utf-8").strip()

        # Sometimes Ollama outputs metadata → keep only last block of text
        if "{" in output and "}" in output:
            # try to cut metadata
            parts = output.split("}")
            output = parts[-1].strip()

        return output or "[No response from Ollama]"
    except subprocess.TimeoutExpired:
        return "[ERROR] Ollama took too long to respond (timeout)."
    except Exception as e:
        return f"[ERROR] Ollama query failed: {e}"
