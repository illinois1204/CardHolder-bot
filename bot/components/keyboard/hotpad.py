from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from common.enums.hotpad import HotPadNotes

hotpad = [[KeyboardButton(text=note)] for note in HotPadNotes.values()]

hotPadMarkup = ReplyKeyboardMarkup(
    keyboard=hotpad, resize_keyboard=True, one_time_keyboard=False
)
