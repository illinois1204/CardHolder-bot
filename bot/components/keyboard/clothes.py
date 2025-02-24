from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

prefix = CallBackNameSpace.Clothes
clothesBoard = [
    [InlineKeyboardButton(text="H&M", callback_data=f"{prefix}_h_and_m")],
    [InlineKeyboardButton(text="JG", callback_data=f"{prefix}_jg")],
    [InlineKeyboardButton(text="Sport Master", callback_data=f"{prefix}_sport_master")],
    [InlineKeyboardButton(text="Colins", callback_data=f"{prefix}_colins")],
    [InlineKeyboardButton(text="Zara", callback_data=f"{prefix}_zara")],
]

clothesBoard.append(backButton(CallBackNameSpace.Clothes))

clothesBoardMarkup = InlineKeyboardMarkup(inline_keyboard=clothesBoard)
