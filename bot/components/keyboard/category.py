from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

categoryBoard = [
    [InlineKeyboardButton(text="Супермаркеты", callback_data=CallBackNameSpace.Market)],
    [InlineKeyboardButton(text="АЗС", callback_data=CallBackNameSpace.Petrol)],
    [InlineKeyboardButton(text="Одежда", callback_data=CallBackNameSpace.Clothes)],
    [
        InlineKeyboardButton(
            text="Техника и электроника", callback_data=CallBackNameSpace.Electronics
        )
    ],
    [InlineKeyboardButton(text="Другие", callback_data=CallBackNameSpace.Other)],
]

categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)
