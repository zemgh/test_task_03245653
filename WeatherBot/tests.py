import pytest

from services.translate import TranslateService


@pytest.mark.asyncio
async def test_translate():
    translator = TranslateService()

    # Ввод RU
    ru_string = 'тест'
    result = await translator.get_eng_string(ru_string)
    assert result == 'test'

    # Ввод EN
    en_string = 'test'
    result = await translator.get_eng_string(en_string)
    assert result == 'test'