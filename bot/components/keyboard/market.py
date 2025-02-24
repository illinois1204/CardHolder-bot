from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

prefix = CallBackNameSpace.Market
marketBoard = [
    [InlineKeyboardButton(text="InterSpar", callback_data=f"{prefix}_interspar")],
    [InlineKeyboardButton(text="Lenta", callback_data=f"{prefix}_lenta")],
    [InlineKeyboardButton(text="Metro C&C", callback_data=f"{prefix}_metro")],
    [InlineKeyboardButton(text="Lidl", callback_data=f"{prefix}_lidl")],
    [InlineKeyboardButton(text="Auchan", callback_data=f"{prefix}_aucham")],
    [InlineKeyboardButton(text="Kaufland", callback_data=f"{prefix}_kaufland")],
]

marketBoard.append(backButton(CallBackNameSpace.Market))

marketBoardMarkup = InlineKeyboardMarkup(inline_keyboard=marketBoard)
