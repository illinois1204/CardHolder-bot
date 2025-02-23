import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from .components import menu
from .handlers import router

load_dotenv()


async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=os.getenv("BOT_TOKEN", "None"))
    DP = Dispatcher()
    DP.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(menu.Menu)
    await DP.start_polling(bot)


asyncio.run(main())
