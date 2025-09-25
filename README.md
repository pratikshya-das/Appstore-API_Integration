App Store API Integration Project
Overview

This project was part of a technical assignment for an AI Engineer role.
The main objective was to integrate the Apple App Store Scraper API (via RapidAPI), handle rate limits, and prepare the data for integration with the Google Play Store Kaggle dataset.

# What I Implemented

Setup of Python project with virtual environment (venv)

Proper use of .env file to manage API keys securely

App Store API Integration:

Fetch app details (name, category, developer, ratings, etc.)

Fetch app reviews (user, rating, text, timestamp, etc.)

Implemented rate limit handling with retries + exponential backoff

Saved API results into data/ folder as JSON for reproducibility

# Project Structure
appstore-api/
│
├── data/                     # Data folder
│   ├── googleplaystore.csv   # Kaggle dataset (to be integrated)
│   ├── 364709193_details.json
│   ├── 364709193_reviews_page1.json
│
├── src/                      # Source code
│   ├── appstore_fetch.py     # First test script for API calls
│   ├── api_client.py         # Main client with retry & save
│   └── merge_with_kaggle.py  # (not completed)Merge Kaggle + API data
│
├── .env.example              # Example env file (API_KEY, HOST)
├── README.md                 # Project documentation

# How to Run

Clone this repo

Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Add your RapidAPI credentials in .env:

RAPIDAPI_KEY=your_key_here
RAPIDAPI_HOST=appstore-scrapper-api.p.rapidapi.com


Run the API client:

python src/api_client.py
## Next Steps (Not Fully Completed Yet)

Clean and normalize the Kaggle Google Play dataset

Merge with Apple App Store data into a unified schema


## Notes

This repo demonstrates API integration + rate limit handling

I am eager to learn and extend this project further.