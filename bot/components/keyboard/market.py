from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

marketBoard = [
    [InlineKeyboardButton(text="InterSpar", callback_data=f"{CallBackNameSpace.Market}_interspar")],
    [InlineKeyboardButton(text="Lenta", callback_data=f"{CallBackNameSpace.Market}_lenta")],
    [InlineKeyboardButton(text="Metro C&C", callback_data=f"{CallBackNameSpace.Market}_metro")],
    [InlineKeyboardButton(text="Lidl", callback_data=f"{CallBackNameSpace.Market}_lidl")],
    [InlineKeyboardButton(text="Auchan", callback_data=f"{CallBackNameSpace.Market}_aucham")],
    [InlineKeyboardButton(text="Kaufland", callback_data=f"{CallBackNameSpace.Market}_kaufland")],
]

marketBoard.append(backButton(CallBackNameSpace.Market))

marketBoardMarkup = InlineKeyboardMarkup(inline_keyboard=marketBoard)
