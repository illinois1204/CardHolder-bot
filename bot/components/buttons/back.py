from aiogram.types import InlineKeyboardButton

from bot.common.constants.app import NAMESPACE_SEPARATOR


def backButton(namespace: str) -> list[InlineKeyboardButton]:
    return [InlineKeyboardButton(text="< назад", callback_data=f"{namespace}{NAMESPACE_SEPARATOR}back")]
