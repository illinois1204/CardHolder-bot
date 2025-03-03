from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug

from ..buttons.back import backButton

electronicMap = dict(
    mvideo="Mvideo",
    dns="DNS",
    e2e4="E2E4",
    cu="Computer Universe",
)
electronicMap["2droida"] = "2Droida"

electronicMapReverse = {v: k for k, v in electronicMap.items()}


prefix = CategorySlug.Electronic
electronicBoard = [
    [InlineKeyboardButton(text=v, callback_data=f"{prefix}{NAMESPACE_SEPARATOR}{k}")]
    for k, v in electronicMap.items()
]

electronicBoard.append(backButton(CategorySlug.Electronic))

electronicBoardMarkup = InlineKeyboardMarkup(inline_keyboard=electronicBoard)
