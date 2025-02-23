from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .back import backButton

petrolBoard = [
    [InlineKeyboardButton(text="Lukoil", callback_data="lukoil")],
    [InlineKeyboardButton(text="Gazprome", callback_data="gazprome")],
    [InlineKeyboardButton(text="TATNeft", callback_data="tatneft")],
    [InlineKeyboardButton(text="Octan", callback_data="octan")],
]

petrolBoard.append(backButton)

petrolBoardMarkup = InlineKeyboardMarkup(inline_keyboard=petrolBoard)
