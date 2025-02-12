from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

backButton = [InlineKeyboardButton(text="< назад", callback_data="back")]

categoryBoard = [
    [InlineKeyboardButton(text="АЗС", callback_data="petrol")],
    [InlineKeyboardButton(text="Супермаркеты", callback_data="markets")],
    [InlineKeyboardButton(text="Стройка", callback_data="building")],
    [InlineKeyboardButton(text="Техника", callback_data="household")],
]

categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)
