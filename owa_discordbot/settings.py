import os
import logging
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()
env_path = Path(".", ".env")
load_dotenv(env_path)

DEBUG = os.getenv("DEBUG", default="true").lower() == "true"

LOG_LEVEL = os.getenv("LOG_LEVEL", default="debug").upper()
if LOG_LEVEL not in ["NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
    raise ValueError(f"Invalid log level: {LOG_LEVEL}")
LOG_LEVEL = getattr(logging, LOG_LEVEL)

OWA_CONFIG = {
    "prefix": os.getenv("OWA_PREFIX"),
    "discord_token": os.getenv("OWA_DISCORD_TOKEN"),
    "csv_dir": os.getenv("OWA_QUESTIONS_CSV"),
}

DB_DEBUG = os.getenv("DB_DEBUG", default="true").lower() == "true"
DB_HOST = os.getenv("DB_HOST")
