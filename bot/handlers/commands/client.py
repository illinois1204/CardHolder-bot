import os

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

import bot.common.constants.texts as BotTexts
from bot.common.constants.app import ASSETS_PATH
from bot.common.constants.messages import BotMessages
from bot.common.enums.hotpad import HotPadNotes
from bot.components.fsm.card import PutCard
from bot.components.keyboard.category import categoryBoardMarkup, categoryMap

router = Router()


@router.message(F.text == HotPadNotes["category"])
@router.message(Command("category"))
async def _(message: types.Message):
    await message.answer_photo(
        photo=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
        caption=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.message(F.text == HotPadNotes.addCard, default_state)
@router.message(Command("add_card"), default_state)
async def _(message: types.Message, state: FSMContext):
    await state.set_state(PutCard.categorySelect)

    await message.answer(BotTexts.AddCard)
    await message.answer(
        "Выберите категорию",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[[types.KeyboardButton(text=i)] for i in categoryMap.values()],
            resize_keyboard=True,
        ),
    )
