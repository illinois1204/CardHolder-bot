from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from common.enums.namespaces import CallBackNameSpace

from ..buttons.back import backButton

electronicBoard = [
    [InlineKeyboardButton(text="Mvideo", callback_data="mvideo")],
    [InlineKeyboardButton(text="DNS", callback_data="dns")],
    [InlineKeyboardButton(text="E2E4", callback_data="e2e4")],
    [InlineKeyboardButton(text="2Droida", callback_data="2droida")],
    [InlineKeyboardButton(text="Computer Universe", callback_data="computer_universe")],
]

electronicBoard.append(backButton(CallBackNameSpace.Electronics))

electronicBoardMarkup = InlineKeyboardMarkup(inline_keyboard=electronicBoard)
