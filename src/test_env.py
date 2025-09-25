import os
from dotenv import load_dotenv

load_dotenv()

print("RAPIDAPI_KEY (first 6 chars):", os.getenv("RAPIDAPI_KEY")[:6])
print("RAPIDAPI_HOST:", os.getenv("RAPIDAPI_HOST"))
