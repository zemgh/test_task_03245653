FROM python:3.12.0-alpine

WORKDIR /app/bot

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip
COPY ./requirements.txt /app/bot
RUN pip install -r requirements.txt

EXPOSE 80

COPY . /app/bot