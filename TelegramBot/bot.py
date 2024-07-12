import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from app.handlers import router
from config import API_TOKEN

from database import get_ids

import aioschedule
from datetime import datetime

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

users = get_ids()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        for user_id in users:
            try:
                await bot.send_message(user_id, "Ты не забыл попить воды?")
            except Exception as e:
                logging.error(f"Ошибка отправки сообщения пользователю {user_id}: {e}")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled(10))
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
