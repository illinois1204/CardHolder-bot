from aiogram import Router, types
from aiogram.filters import Command, CommandStart

from bot.components.keyboard._index import categoryBoardMarkup
from common.constants.texts import BotText

router = Router()


@router.message(CommandStart())
async def _(message: types.Message):
    await message.answer(BotText.Start)
    # assert message.from_user is not None
    # await message.answer(text=f"Hello, {message.from_user.full_name}! I am Bot o_O")


@router.message(Command("help"))
async def _(message: types.Message):
    await message.answer("Пока нет информации...")


@router.message(Command("category"))
async def _(message: types.Message):
    await message.answer(
        "Выберите категорию для определения карт:", reply_markup=categoryBoardMarkup
    )
