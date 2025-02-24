from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

prefix = CallBackNameSpace.Petrol
petrolBoard = [
    [InlineKeyboardButton(text="Lukoil", callback_data=f"{prefix}_lukoil")],
    [InlineKeyboardButton(text="Gazprome", callback_data=f"{prefix}_gazprome")],
    [InlineKeyboardButton(text="TATNeft", callback_data=f"{prefix}_tatneft")],
    [InlineKeyboardButton(text="Octan", callback_data=f"{prefix}_octan")],
]

petrolBoard.append(backButton(CallBackNameSpace.Petrol))

petrolBoardMarkup = InlineKeyboardMarkup(inline_keyboard=petrolBoard)
