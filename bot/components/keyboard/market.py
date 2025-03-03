from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug

from ..buttons.back import backButton

marketMap = dict(
    interspar="InterSpar",
    lenta="Lenta",
    metro="Metro C&C",
    lidl="Lidl",
    aucham="Auchan",
    kaufland="Kaufland",
)

marketMapReverse = {v: k for k, v in marketMap.items()}


prefix = CategorySlug.Market
marketBoard = [
    [InlineKeyboardButton(text=v, callback_data=f"{prefix}{NAMESPACE_SEPARATOR}{k}")]
    for k, v in marketMap.items()
]

marketBoard.append(backButton(CategorySlug.Market))

marketBoardMarkup = InlineKeyboardMarkup(inline_keyboard=marketBoard)
