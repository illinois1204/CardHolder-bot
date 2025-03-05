from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.state import default_state

from bot.common.constants import texts as BotText
from bot.components.keyboard.hotpad import hotPadMarkup

router = Router()


@router.message(CommandStart(), default_state)
async def _(message: types.Message):
    await message.answer(text=BotText.Start, reply_markup=hotPadMarkup)
    # assert message.from_user is not None
    # await message.answer(text=f"Hello, {message.from_user.full_name}! I am Bot o_O")


@router.message(Command("help"), default_state)
async def _(message: types.Message):
    await message.answer(BotText.Help, parse_mode=ParseMode.HTML)
