from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext

from bot.common.constants.app import CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.keyboard import category, clothes, electronics, market, petrol
from bot.components.fsm.card import PutCard, ShopInSection

COMPLEX_BOARDS = dict()
COMPLEX_BOARDS[CategorySlug.Market] = market.marketMap
COMPLEX_BOARDS[CategorySlug.Petrol] = petrol.petrolMap
COMPLEX_BOARDS[CategorySlug.Electronic] = electronics.electronicMap
COMPLEX_BOARDS[CategorySlug.Clothes] = clothes.clothesMap

router = Router()


@router.message(
    PutCard.categorySelect, F.text.in_(set(i for i in category.categoryMap.values()))
)
async def _(message: types.Message, state: FSMContext):
    selectedCategory = category.categoryMapReverse[message.text]
    await state.update_data(category=selectedCategory)

    responseMessage, responseKeyboard = (None, None)
    if selectedCategory == CategorySlug.Other:
        responseMessage = BotMessages.WriteYourShop
        responseKeyboard = types.ReplyKeyboardRemove()
    else:
        responseMessage = f"Ок, {BotMessages.ShopSelect.lower()}"
        responseKeyboard = types.ReplyKeyboardMarkup(
            keyboard=[
                [types.KeyboardButton(text=i)]
                for i in COMPLEX_BOARDS[selectedCategory].values()
            ],
            resize_keyboard=True,
        )

    await state.set_state(getattr(ShopInSection, selectedCategory))
    await message.answer(responseMessage, reply_markup=responseKeyboard),


@router.message(PutCard.categorySelect)
async def _(message: types.Message):
    await message.answer("Сори, неизвестная категория :(")
