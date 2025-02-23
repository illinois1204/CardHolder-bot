from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

categoryBoard = [
    [InlineKeyboardButton(text="Супермаркеты", callback_data="markets")],
    [InlineKeyboardButton(text="АЗС", callback_data="petrol")],
    [InlineKeyboardButton(text="Одежда", callback_data="clothes")],
    [InlineKeyboardButton(text="Техника и электроника", callback_data="electronics")],
    [InlineKeyboardButton(text="Другие", callback_data="other")],
]

categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)
