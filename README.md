<h1 align="center">City weather bot</h1>

<img src="https://img.shields.io/badge/python3.12-blue">
<img src="https://img.shields.io/badge/aiogram-blue">
<img src="https://img.shields.io/badge/aiohttp-blue">
<img src="https://img.shields.io/badge/weatherapi.com-blue">
<img src="https://img.shields.io/badge/Docker-blue">

## Description
Telegram bot providing weather information in the requested city.



## About the project

Based on Python 3.12, aiogram, aiohttp, weatherapi.com, Docker.

## Installation
1. Create telegram bot token. Speak with @BotFather.
2. Sign up on www.weatherapi.com to get api key. 
3. Clone this repo.


      git clone https://github.com/vinogradovvv/weather_city_bot.git


4. CD to weather_city_bot directory.


      cd ./weather_city_bot


5. Setup enviroment variables. This operation is required!!!

    Copy or rename '.tempate' file to .env, then fill it with your telegram bot token and weatherapi api key.

## Running

    docker-compose up -d
