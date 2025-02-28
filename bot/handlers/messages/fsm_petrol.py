from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.common.constants.messages import BotMessages
from bot.components.fsm.card import PutCard, ShopInSection
from bot.components.keyboard.petrol import petrolMap, petrolMapReverse

router = Router()


@router.message(ShopInSection.petrol, F.text.in_(set(i for i in petrolMap.values())))
async def _(message: types.Message, state: FSMContext):
    await state.update_data(shop=petrolMapReverse[message.text])
    await state.set_state(PutCard.numberType)
    await message.answer(
        BotMessages.EnterBarcode, reply_markup=types.ReplyKeyboardRemove()
    )


@router.message(ShopInSection.petrol)
async def _(message: types.Message):
    await message.answer(BotMessages.UnknownShop)
