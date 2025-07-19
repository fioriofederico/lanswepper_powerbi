import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.lansweeper.com/v2/assets"
CLIENT_ID = os.getenv("LS_CLIENT_ID")
CLIENT_SECRET = os.getenv("LS_CLIENT_SECRET")
CSV_PATH = "assets_data.csv"
