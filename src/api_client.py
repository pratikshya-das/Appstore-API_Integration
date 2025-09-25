import os
import time
import json
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env for API keys
load_dotenv()
API_KEY = os.getenv("RAPIDAPI_KEY")
HOST = os.getenv("RAPIDAPI_HOST")

HEADERS = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": HOST,
}

# Create a folder for saving data
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


def save_json(data, filename: str):
    """Save Python dict/list as JSON file inside data/ folder"""
    filepath = DATA_DIR / filename
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved JSON -> {filepath}")


def fetch_app_details(app_id: str, country="us", lang="en", max_retries=3):
    """Fetch app details with retry logic"""
    url = f"https://{HOST}/v1/app-store-api/detail"
    params = {"id": app_id, "country": country, "lang": lang}

    retries = 0
    backoff = 1
    while retries < max_retries:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            save_json(data, f"{app_id}_details.json")
            return data
        else:
            print(f"⚠️ Failed with {response.status_code}: {response.text}")
            retries += 1
            time.sleep(backoff)
            backoff *= 2
    return None


def fetch_app_reviews(app_id: str, page=1, country="us", lang="en", max_retries=3):
    """Fetch app reviews with retry logic"""
    url = f"https://{HOST}/v1/app-store-api/reviews"
    params = {
        "id": app_id,
        "page": page,
        "country": country,
        "lang": lang,
        "sort": "mostRecent",
    }

    retries = 0
    backoff = 1
    while retries < max_retries:
        response = requests.get(url, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            save_json(data, f"{app_id}_reviews_page{page}.json")
            return data
        else:
            print(f"⚠️ Failed with {response.status_code}: {response.text}")
            retries += 1
            time.sleep(backoff)
            backoff *= 2
    return None


if __name__ == "__main__":
    app_id = "364709193"  # Example: Instagram

    print("\n📥 Fetching app details...")
    details = fetch_app_details(app_id)

    print("\n📥 Fetching app reviews (page 1)...")
    reviews = fetch_app_reviews(app_id, page=1)
