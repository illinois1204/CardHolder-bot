import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from .components import menu
from .handlers import router

load_dotenv()
BOT = Bot(token=os.getenv("BOT_TOKEN", "None"))
DP = Dispatcher()
DP.include_router(router)


# @DP.message()
# async def _(message):
#     await message.answer(text="404...")


async def main():
    logging.basicConfig(level=logging.INFO)
    await BOT.set_my_commands(menu.Menu)
    await DP.start_polling(BOT)


asyncio.run(main())
