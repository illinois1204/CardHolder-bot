from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.components.keyboard import hotpad
from bot.components.fsm.card import PutCard

router = Router()


@router.message(PutCard.numberType, F.text.regexp(r"^\d+$"))
async def _(message: types.Message, state: FSMContext):
    data = await state.update_data(cardNum=message.text)
    await state.clear()
    print(data)
    await message.answer(
        f"Нихуя себе, это твоя карта {message.text} о_О ??",
        reply_markup=hotpad.hotPadMarkup,
    )


@router.message(PutCard.numberType)
async def _(message: types.Message):
    await message.answer("Леее, напиши цифры нормально...")
