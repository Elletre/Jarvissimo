FROM python:3.8-slim

RUN pip install python-telegram-bot schedule pytz

WORKDIR /app

COPY . .

CMD ["python", "bot.py"]
