import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from services.translate import TranslateService
from services.weather import WeatherService

TRANSLATE_SERVICE = TranslateService()
WEATHER_SERVICE = WeatherService(TRANSLATE_SERVICE)

load_dotenv()
API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)