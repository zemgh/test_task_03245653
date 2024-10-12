from aiogram import types, Router
from aiogram.filters import CommandStart

from services.translate import TranslateService
from services.weather import WeatherService

TRANSLATE_SERVICE = TranslateService()
WEATHER_SERVICE = WeatherService

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    start_text = 'Введите название города (RU/EN)'
    await message.answer(start_text)


@router.message()
async def get_weather(message: types.Message):
    service = WEATHER_SERVICE(TRANSLATE_SERVICE)
    city = message.text

    weather_string = await service.get_current_weather(city)
    await message.reply(weather_string)

