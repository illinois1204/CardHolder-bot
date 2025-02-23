from aiogram import F, Router, types
from aiogram.filters import Command

from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.hotpad import HotPadNotes
from common.constants.messages import BotMessages

router = Router()


@router.message(F.text == HotPadNotes["category"])
@router.message(Command("category"))
async def _(message: types.Message):
    await message.answer(BotMessages.CategorySelect, reply_markup=categoryBoardMarkup)
