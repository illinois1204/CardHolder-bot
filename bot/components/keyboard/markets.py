from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from ._index import backButton

marketBoard = [
    [InlineKeyboardButton(text="InterSpar", callback_data="interspar")],
    [InlineKeyboardButton(text="Lenta", callback_data="lenta")],
    [InlineKeyboardButton(text="Metro C&C", callback_data="metro")],
    [InlineKeyboardButton(text="Lidl", callback_data="lidl")],
    [InlineKeyboardButton(text="Auchan", callback_data="aucham")],
    [InlineKeyboardButton(text="Kaufland", callback_data="kaufland")],
]

marketBoard.append(backButton)
marketBoardMarkup = InlineKeyboardMarkup(inline_keyboard=marketBoard)
