import os
import requests
from dotenv import load_dotenv

# Load API key and host from .env
load_dotenv()
API_KEY = os.getenv("RAPIDAPI_KEY")
HOST = os.getenv("RAPIDAPI_HOST")

print("API Key starts with:", API_KEY[:6])
print("Host:", HOST)

# ✅ Correct endpoint from your RapidAPI code snippet
url = "https://appstore-scrapper-api.p.rapidapi.com/v1/app-store-api/reviews"

# Example params (App Store ID for Instagram is 364709193)
params = {
    "id": "364709193",     # App Store ID
    "sort": "mostRecent",  # sort by mostRecent or mostHelpful
    "page": "1",
    "country": "us",
    "lang": "en"
}

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": HOST
}

# Send request
response = requests.get(url, headers=headers, params=params)

print("Status code:", response.status_code)

# Print JSON response (first 500 characters)
print("Response text (first 500 chars):\n", response.text[:500])
