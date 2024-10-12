import os

from aiohttp import ClientSession


async def request_weather(city: str) -> dict | str:
    """
    Requests weather data from weatherapi.com.
    """
    token = os.getenv("WEATHERAPI_TOKEN")
    url = os.getenv("WEATHERAPI_URL")
    params = {"key": token, "q": city, "aqi": "no"}
    async with ClientSession() as session:
        async with session.get(url=url, params=params, timeout=3) as response:
            if response.status == 200:
                return await response.json()
            if response.status == 400:
                return f"There is no city {city}."
            if response.status == 403:
                return "Access denied. Check your WEATHERAPI TOKEN!"
            return "Something went wrong."
