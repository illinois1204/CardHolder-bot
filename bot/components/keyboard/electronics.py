from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

prefix = CallBackNameSpace.Electronics
electronicBoard = [
    [InlineKeyboardButton(text="Mvideo", callback_data=f"{prefix}_mvideo")],
    [InlineKeyboardButton(text="DNS", callback_data=f"{prefix}_dns")],
    [InlineKeyboardButton(text="E2E4", callback_data=f"{prefix}_e2e4")],
    [InlineKeyboardButton(text="2Droida", callback_data=f"{prefix}_2droida")],
    [InlineKeyboardButton(text="Computer Universe", callback_data=f"{prefix}_cu")],
]

electronicBoard.append(backButton(CallBackNameSpace.Electronics))

electronicBoardMarkup = InlineKeyboardMarkup(inline_keyboard=electronicBoard)
