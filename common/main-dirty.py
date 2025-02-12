import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import BotCommand, CallbackQuery, Message

# from app import kb
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("BOT_TOKEN", "None"))
dp = Dispatcher()


menu: list[BotCommand] = [
    BotCommand(command="/start", description="Запуск бота"),
    BotCommand(command="/help", description="Информация по использованию"),
    BotCommand(command="/list_cards", description="Список всех карт"),
    BotCommand(command="/category", description="Список категорий"),
]


# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer(text=f"Hello, {message.from_user.full_name}! I am Bot o_O")


# @dp.message(Command("help"))
# async def help(message: Message):
#     await message.answer("Пока нет информации...")


# @dp.message(Command("category"))
# async def listCategory(msg: Message):
#     await msg.answer(
#         "Выберите категорию для определения карт:", reply_markup=kb.categoryBoardMarkup
#     )


# @dp.callback_query(F.data == "petrol")
# async def petrolCategory(ctx: CallbackQuery):
#     await bot.edit_message_text(
#         chat_id=ctx.message.chat.id,
#         message_id=ctx.message.message_id,
#         text="Выберите АЗС карту",
#         reply_markup=kb.petrolBoardMarkup,
#     )


# @dp.callback_query(F.data == "back")
# async def back(ctx: CallbackQuery):
#     await bot.edit_message_text(
#         chat_id=ctx.message.chat.id,
#         message_id=ctx.message.message_id,
#         text="Select category",
#         reply_markup=kb.categoryBoardMarkup,
#     )


@dp.message()
async def echo_message(message: Message):
    await message.answer(text="404...")


async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.set_my_commands(menu)
    await dp.start_polling(bot)


asyncio.run(main())
