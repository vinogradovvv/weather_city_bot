import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from dotenv import load_dotenv

from weather_api.funcs import request_weather

load_dotenv()
BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
WEATHERAPI_URL = getenv("WEATHERAPI_URL")
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    Handle `/start` command
    """
    await message.answer(
        f"Hello, {message.from_user.full_name}!\nPlease input city name."
    )


@dp.message()
async def get_weather(message: Message) -> None:
    """
    Handle incoming messages.
    """
    city = message.text
    weather_data = await request_weather(city)
    if isinstance(weather_data, dict):
        city_name = weather_data["location"].get("name")
        temperature = weather_data["current"].get("temp_c")
        condition = weather_data["current"]["condition"].get("text")
        text = (
            f"In {city_name} city now:\n"
            f"\tcondition: {condition}\n"
            f"\ttemperature: {temperature}"
        )
    else:
        text = str(weather_data)
    text += "\n\nPlease input city name."
    await message.answer(text=text)


async def start_bot() -> None:
    """
    Initialize Bot instance and run events dispatching.
    """
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(BOT_TOKEN)
    await dp.start_polling(bot)
