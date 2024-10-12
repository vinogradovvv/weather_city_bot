import asyncio

from telegram_bot.weather_bot import start_bot
from utils.start_check import env_check

env_check()
asyncio.run(start_bot())

if __name__ == "__main__":
    env_check()
    asyncio.run(start_bot())
