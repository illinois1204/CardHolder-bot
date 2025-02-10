from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

backBtn = [InlineKeyboardButton(text="< назад", callback_data="back")]

###############################################################################

categoryBoard = [
    [InlineKeyboardButton(text="АЗС", callback_data="petrol")],
    [InlineKeyboardButton(text="Супермаркеты", callback_data="markets")],
    [InlineKeyboardButton(text="Стройка", callback_data="building")],
    [InlineKeyboardButton(text="Техника", callback_data="tech")],
]

categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)

###############################################################################


petrolBoard = [
    [InlineKeyboardButton(text="Lukoil", callback_data="fruit")],
    [InlineKeyboardButton(text="Gazprome", callback_data="tea")],
    [InlineKeyboardButton(text="TATNeft", callback_data="coffee")],
    [InlineKeyboardButton(text="Octan", callback_data="sweet")],
]
petrolBoard.append(backBtn)
petrolBoardMarkup = InlineKeyboardMarkup(inline_keyboard=petrolBoard)
