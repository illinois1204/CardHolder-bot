from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug

from ..buttons.back import backButton

clothesMap = dict(
    h_and_m="H&M",
    jg="JG",
    sport_master="Sport Master",
    colins="Colins",
    zara="Zara",
)

clothesMapReverse = {v: k for k, v in clothesMap.items()}

prefix = CategorySlug.Clothes
clothesBoard = [
    [InlineKeyboardButton(text=v, callback_data=f"{[prefix]}{NAMESPACE_SEPARATOR}{k}")]
    for k, v in clothesMap.items()
]

clothesBoard.append(backButton(CategorySlug.Clothes))

clothesBoardMarkup = InlineKeyboardMarkup(inline_keyboard=clothesBoard)
