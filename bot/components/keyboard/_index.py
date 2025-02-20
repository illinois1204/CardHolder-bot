from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

backButton = [InlineKeyboardButton(text="< назад", callback_data="back")]

categoryBoard = [
    [InlineKeyboardButton(text="Супермаркеты", callback_data="markets")],
    [InlineKeyboardButton(text="АЗС", callback_data="petrol")],
    [InlineKeyboardButton(text="Стройка", callback_data="building")],
    [InlineKeyboardButton(text="Техника", callback_data="household")],
    [InlineKeyboardButton(text="Другие", callback_data="other")],
]

categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)
