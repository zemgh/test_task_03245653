import asyncio

from bot import dp, bot
from handlers import router


async def main():
    print('start')
    dp.include_router(router)
    await dp.start_polling(bot)


asyncio.run(main())

