from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

HotPadNotes = dict(
    category="Категории", allCarts="Список всех карт", addCard="Добавить карту"
)

hotpad = [[KeyboardButton(text=note)] for note in HotPadNotes.values()]

hotPadMarkup = ReplyKeyboardMarkup(
    keyboard=hotpad, resize_keyboard=True, one_time_keyboard=False
)
