from aiogoogletrans import Translator

from lingua import Language, LanguageDetectorBuilder


class TranslateError(Exception):
    def __init__(self):
        super().__init__(f'Неверный язык ввода (поддерживается только RU/EN)')


class TranslateService:
    translator = Translator()
    languages = [Language.ENGLISH, Language.RUSSIAN]

    def __init__(self):
        self.detector = LanguageDetectorBuilder.from_languages(*self.languages).build()

    async def get_eng_string(self, text: str) -> str:
        if self._check_language(text) == Language.ENGLISH:
            return text
        if self._check_language(text) == Language.RUSSIAN:
            return await self._translate_to_eng(text)

        raise TranslateError

    async def translate_to_ru(self, text: str) -> str:
        translated = await self.translator.translate(text, 'ru')
        return translated.text

    def _check_language(self, text: str):
        return self.detector.detect_language_of(text)

    async def _translate_to_eng(self, text: str) -> str:
        translated = await self.translator.translate(text, 'en')
        return translated.text