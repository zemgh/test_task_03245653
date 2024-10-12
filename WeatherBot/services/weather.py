import json

import aiohttp
import os

from dotenv import load_dotenv

from services.translate import TranslateService, TranslateError


class WeatherService:
    city: str = None

    def __init__(self, translator: TranslateService):
        self.translator = translator

        load_dotenv()
        self._API_URL = os.getenv('WEATHER_API_URL')
        self._API_KEY = os.getenv('WEATHER_API_KEY')

    async def get_current_weather(self, city: str) -> str:
        self.city = city

        try:
            city = await self.translator.get_eng_string(city)
            params = await self._get_params(city)

            async with aiohttp.ClientSession() as session:
                response = await session.get(f'{self._API_URL}/current.json', params=params)
                data = await response.json()
                return await self._get_weather_info(data)

        except TranslateError as e:
            return str(e)

        except aiohttp.ClientError:
            # log e
            return 'Ошибка сервера погоды'

        except Exception as e:
            # log e
            return f'Ошибка сервера: {e}'

    async def _get_params(self, city: str) -> dict:
        city = await self.translator.get_eng_string(city)
        params = {
            'key': self._API_KEY,
            'q': city
        }

        return params

    async def _get_weather_info(self, response: json) -> str:
        if response.get('error'):
            if response['error'].get('code') == 1006:
                return 'Увы, такого города не существует :('

        data = await self._get_weather_data(response)
        lst = [f'{key}: {value}' for key, value in data.items()]
        string = '\n'.join(lst)

        return string

    async def _get_weather_data(self, response: json) -> dict:
        en_city = response['location']['name']
        description = response['current']['condition']['text']

        ru_description = await self.translator.translate_to_ru(description)
        city_string = en_city if en_city == self.city else f'{self.city.capitalize()} / {en_city}'

        data = {
            'Город': f'{city_string}',
            'Температура': int(response['current']['temp_c']),
            'Влажность': int(response['current']['humidity']),
            'Описание': ru_description
        }

        return data
