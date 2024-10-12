import os
import sys

from dotenv import load_dotenv


def env_check() -> None:
    """
    Check if .env file exists and has all needed params.
    """
    if not os.path.exists("./.env"):
        sys.exit("No .env file! Please create .env file from template and fill it.")
    load_dotenv()
    if not os.getenv("TELEGRAM_BOT_TOKEN"):
        sys.exit("Please check your telegram bot token.")
    if not os.getenv("WEATHERAPI_TOKEN"):
        sys.exit("Please check your weatherapi token.")
    if not os.getenv("WEATHERAPI_URL"):
        sys.exit("Please check your weatherapi url.")
