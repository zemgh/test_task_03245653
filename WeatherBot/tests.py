import pytest

from services.translate import TranslateService


@pytest.mark.asyncio
async def test_translate():
    translator = TranslateService()

    # RU > ENG
    ru_string = 'тест'
    result = await translator.get_eng_string(ru_string)
    assert result == 'test'

    # ENG > RU
    en_string = 'test'
    result = await translator.translate_to_ru(en_string)
    assert result == 'тест'





