from aiogram import Router, types
from aiogram.filters import Command, CommandStart

from bot.components.keyboard._index import categoryBoardMarkup

router = Router()


@router.message(CommandStart())
async def _(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}! I am Bot o_O")


@router.message(Command("help"))
async def _(message: types.Message):
    await message.answer("Пока нет информации...")


@router.message(Command("category"))
async def _(msg: types.Message):
    await msg.answer(
        "Выберите категорию для определения карт:", reply_markup=categoryBoardMarkup
    )
