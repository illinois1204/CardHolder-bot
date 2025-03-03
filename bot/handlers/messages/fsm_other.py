from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.common.constants.messages import BotMessages
from bot.components.fsm.card import PutCard, ShopInSection
from bot.components.keyboard import hotpad
from bot.sql.repository.save_card import isExistCard

router = Router()


@router.message(ShopInSection.other, F.text.regexp(r"^[0-9a-zA-Zа-яА-ЯёЁ .!$&()_]+$"))
async def _(message: types.Message, state: FSMContext):
    if isExistCard(message.from_user.id, message.text):
        await state.clear()
        await message.answer(
            BotMessages.CardNameExists,
            reply_markup=hotpad.hotPadMarkup,
        )
        return

    await state.update_data(shop=message.text)
    await state.set_state(PutCard.numberType)
    await message.answer(
        BotMessages.EnterBarcode,
        reply_markup=types.ReplyKeyboardRemove(),
    )


@router.message(ShopInSection.other)
async def _(message: types.Message):
    await message.answer("Непонятный нейминг :(")
