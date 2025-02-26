from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.common.enums.hotpad import HotPadNotes

hotpad = [[KeyboardButton(text=note.value)] for note in HotPadNotes]

hotPadMarkup = ReplyKeyboardMarkup(
    keyboard=hotpad, resize_keyboard=True, one_time_keyboard=False
)
