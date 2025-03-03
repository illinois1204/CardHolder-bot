from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.common.lambdas.save_card import saveCard
from bot.components.fsm.card import PutCard
from bot.components.keyboard import hotpad

router = Router()


@router.message(PutCard.numberType, F.text.len() >= 12, F.text.regexp(r"^\d+$"))
async def _(message: types.Message, state: FSMContext):
    data = await state.update_data(cardNumber=message.text)
    data["cardCode"] = message.text

    await saveCard(message.from_user.id, data)

    await state.clear()
    await message.answer(
        "Данные карты сохранены",
        reply_markup=hotpad.hotPadMarkup,
    )


@router.message(PutCard.numberType)
async def _(message: types.Message):
    await message.answer("Леее, напиши цифры нормально...")
