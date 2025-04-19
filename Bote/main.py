import asyncio
import os

from dotenv import load_dotenv, find_dotenv
from aiogram import Bot, Dispatcher, types

from Kbds import reply
from Handlers.All_commands import user_router

# bote initialization + taking token
load_dotenv(find_dotenv())
dp = Dispatcher()
bot = Bot(token = os.getenv('Token'))

dp.include_router(user_router)

async def main():
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)

asyncio.run(main())
