from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug

from ..buttons.back import backButton

petrolMap = dict(
    lukoil="Lukoil",
    gazprome="Gazprome",
    tatneft="TATNeft",
    octan="Octan",
)

petrolMapReverse = {v: k for k, v in petrolMap.items()}


prefix = CategorySlug.Petrol
petrolBoard = [
    [InlineKeyboardButton(text=v, callback_data=f"{[prefix]}{NAMESPACE_SEPARATOR}{k}")]
    for k, v in petrolMap.items()
]

petrolBoard.append(backButton(CategorySlug.Petrol))

petrolBoardMarkup = InlineKeyboardMarkup(inline_keyboard=petrolBoard)
