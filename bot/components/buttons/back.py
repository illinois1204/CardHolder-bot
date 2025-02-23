from aiogram.types import InlineKeyboardButton


def backButton(namespace: str) -> list[InlineKeyboardButton]:
    return [InlineKeyboardButton(text="< назад", callback_data=f"{namespace}_back")]
