from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup, default_state

from bot.common.enums.hotpad import HotPadNotes
from bot.components.keyboard.category import categoryMap as CategoryNameList

router = Router()


class PutCard(StatesGroup):
    category = State()
    shop = State()
    number = State()


@router.message(Command("cancel"), PutCard())
@router.message(F.text.casefold() == "cancel", PutCard())
async def _(message: types.Message, state: FSMContext) -> None:
    await state.clear()
    await message.answer(
        "Операция отменена. Чтобы начать заново нажмите: /add_card",
        # reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(F.text == HotPadNotes["addCard"])
@router.message(Command("add_card"), default_state)
async def _(message: types.Message, state: FSMContext):
    await state.set_state(PutCard.category)
    await message.answer(
        "Добавление карты. Чтобы отменить добавление карты нажмите: /cancel"
    )
    await message.answer(
        "Выберите категорию",
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text=i)] for i in CategoryNameList.values()
            ],
            resize_keyboard=True,
        ),
    )


# @router.message(PutCard.category, F.text.cast(CategoryNameList))
@router.message(PutCard.category, F.text.in_(set(i for i in CategoryNameList.values())))
async def _(message: types.Message, state: FSMContext):
    await state.update_data(category=message.text)
    await state.set_state(PutCard.shop)
    await message.answer(
        "Ок, теперь выберите магазин из этой категории",
        reply_markup=types.ReplyKeyboardRemove(),
    )


# # ###### end routers ############################################
@router.message(PutCard.category)
async def _(message: types.Message):
    await message.answer("Сори неизвестная категория :(")
