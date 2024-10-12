import json

import aiohttp
import os

from dotenv import load_dotenv

from services.translate import TranslateService, TranslateError


class WeatherService:
    def __init__(self, translate: TranslateService):
        self.translate = translate

        load_dotenv()
        self._API_URL = os.getenv('WEATHER_API_URL')
        self._API_KEY = os.getenv('WEATHER_API_KEY')

    async def get_current_weather(self, city: str) -> str:
        params = self._get_params(city)

        try:
            async with aiohttp.ClientSession() as session:
                response = await session.get(f'{self._API_URL}/current.json', params=params)
                data = await response.json()
                return self._get_weather_info(data)

        except TranslateError as e:
            return str(e)

        except aiohttp.ClientError:
            # log e
            return 'Ошибка сервера погоды'

        except Exception as e:
            # log e
            return f'Ошибка сервера: {e}'


    async def _get_params(self, city: str) -> dict:
        city = await self.translate.get_eng_string(city)
        return {
            'key': self._API_KEY,
            'q': city
        }


    def _get_weather_info(self, response: json) -> str:
        data = self._get_weather_data(response)
        lst = [f'{key}: {value}' for key, value in data.items()]
        string = '\n'.join(lst)

        return string


    def _get_weather_data(self, response: json) -> dict:
        return {
            'Температура': int(response['current']['temp_c']),
            'Влажность': int(response['current']['humidity']),
            'Описание': response['current']['condition']['text']
        }