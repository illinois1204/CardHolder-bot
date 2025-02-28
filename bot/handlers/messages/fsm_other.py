from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.common.constants.messages import BotMessages
from bot.components.fsm.card import PutCard, ShopInSection

router = Router()


@router.message(ShopInSection.other, F.text.regexp(r"^[0-9a-zA-Zа-яА-ЯёЁ .!$&()_]+$"))
async def _(message: types.Message, state: FSMContext):
    await state.update_data(shop=message.text)
    await state.set_state(PutCard.numberType)
    await message.answer(
        BotMessages.EnterBarcode, reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(ShopInSection.other)
async def _(message: types.Message):
    await message.answer("Непонятный нейминг :(")
