import os
from dotenv import load_dotenv

load_dotenv()

"""API KEYS OF DATA SOURCE SITES"""
INSTA_KEY = os.getenv("INSTA_API_KEY")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
FMP_API_KEY = os.getenv("FMP_API_KEY")

MONGODB_HOST = os.getenv("MONGODB_HOST")

ALLOW_HOSTS = os.getenv("ALLOW_HOSTS")