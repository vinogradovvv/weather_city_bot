FROM python:3.12-alpine

COPY requirements.txt /weather_bot/
RUN pip install --no-cache-dir -r /weather_bot/requirements.txt

COPY ./ /weather_bot/

WORKDIR /weather_bot

CMD ["python3", "./main.py"]
