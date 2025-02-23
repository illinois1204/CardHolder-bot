from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

clothesBoard = [
    [InlineKeyboardButton(text="H&M", callback_data="h_and_m")],
    [InlineKeyboardButton(text="JG", callback_data="jg")],
    [InlineKeyboardButton(text="Sport Master", callback_data="sport_master")],
    [InlineKeyboardButton(text="Colins", callback_data="colins")],
    [InlineKeyboardButton(text="Zara", callback_data="zara")],
]

clothesBoard.append(backButton(CallBackNameSpace.Clothes))

clothesBoardMarkup = InlineKeyboardMarkup(inline_keyboard=clothesBoard)
