from langdetect import detect
from aiogoogletrans import Translator


class TranslateError(Exception):
    def __init__(self):
        super().__init__(f'Неверный язык ввода (поддерживается только RU/EN)')


class TranslateService:
    translator = Translator()

    async def get_eng_string(self, text: str) -> str:
        if self._check_language(text) == 'en':
            return text
        if self._check_language(text) == 'ru':
            return await self._translate_to_eng(text)

        raise TranslateError

    def _check_language(self, text: str):
        return detect(text)

    async def _translate_to_eng(self, text: str) -> str:
        translated = await self.translator.translate(text, 'en')
        return translated.text
