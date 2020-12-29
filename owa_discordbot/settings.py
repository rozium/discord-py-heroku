import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
env_path = Path(".", ".env")
load_dotenv(env_path)

DEBUG = os.getenv("OWA_DEBUG", default="true").lower() == "true"

OWA_CONFIG = {
    "prefix": os.getenv("OWA_PREFIX"),
    "discord_token": os.getenv("OWA_DISCORD_TOKEN"),
    "csv_dir": os.getenv("OWA_QUESTIONS_CSV"),
}

DB_HOST = os.getenv("DB_HOST")
