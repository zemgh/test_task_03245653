from aiogram import types, Router
from aiogram.filters import CommandStart

from bot import WEATHER_SERVICE

router = Router()


@router.message(CommandStart())
async def start(message: types.Message):
    print(message.__dict__)
    start_text = 'Введите название города'
    await message.answer(start_text)


@router.message()
async def get_weather(message: types.Message):
    city = message.text

    weather_string = await WEATHER_SERVICE.get_current_weather(city)
    await message.reply(weather_string)

