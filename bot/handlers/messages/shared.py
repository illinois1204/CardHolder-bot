from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

import bot.common.constants.texts as BotTexts
from bot.components.keyboard import hotpad
from bot.components.fsm.card import PutCard, ShopInSection

seenStates = StateFilter(
    PutCard(),
    ShopInSection(),
)

interceptRouter = Router()
endRouter = Router()


@interceptRouter.message(Command("cancel"), seenStates)
@interceptRouter.message(F.text.casefold() == "cancel", seenStates)
async def globalCancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        BotTexts.CancelOperationAddCard,
        reply_markup=hotpad.hotPadMarkup,
    )


@endRouter.message()
async def notFound(message):
    await message.answer(text="Обработчик не найден...")
