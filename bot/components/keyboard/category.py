from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import CategorySlug

categoryMap = dict()
categoryMap[CategorySlug.Market] = "Супермаркеты"
categoryMap[CategorySlug.Petrol] = "АЗС"
categoryMap[CategorySlug.Electronic] = "Техника и электроника"
categoryMap[CategorySlug.Clothes] = "Одежда"
categoryMap[CategorySlug.Other] = "Другие"

categoryMapReverse = {v: k for k, v in categoryMap.items()}

categoryBoard = [
    [InlineKeyboardButton(text=v, callback_data=k)] for k, v in categoryMap.items()
]
categoryBoardMarkup = InlineKeyboardMarkup(inline_keyboard=categoryBoard)
