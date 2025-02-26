from aiogram import F, Router, types
from aiogram.filters import Command

from bot.common.constants.messages import BotMessages
from bot.common.enums.hotpad import HotPadNotes
from bot.components.keyboard.category import categoryBoardMarkup

router = Router()


@router.message(F.text == HotPadNotes.category)
@router.message(Command("category"))
async def _(message: types.Message):
    await message.answer(BotMessages.CategorySelect, reply_markup=categoryBoardMarkup)
