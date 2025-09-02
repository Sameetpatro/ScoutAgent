import requests
from bs4 import BeautifulSoup

def fetch_page_text(url: str):
    """
    Fetches visible text from a webpage using BeautifulSoup.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract visible text only
        texts = [t.get_text(strip=True) for t in soup.find_all(["p", "h1", "h2", "h3"])]
        return "\n".join(texts[:20])  # first 20 chunks for brevity
    except Exception as e:
        return f"[ERROR] Failed to fetch {url}: {e}"
