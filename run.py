import os
import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv, find_dotenv

from app.handlers.game_1 import game_1_router

load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_router(game_1_router)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")