"""
Configuration file for data collection.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Fetch configuration values from environment variables
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")

# Parse CHANNELS_TO_SCRAPE as a list
CHANNELS_TO_SCRAPE = os.getenv("CHANNELS_TO_SCRAPE", "").split(",")

RAW_DATA_FILE = os.getenv("RAW_DATA_FILE", "data/raw_data.json")
IMAGE_DIR = os.getenv("IMAGE_DIR", "data/images/")
