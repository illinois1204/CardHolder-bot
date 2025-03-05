from enum import StrEnum


class BotMessages(StrEnum):
    CategorySelect = "Выберите категорию для определения карт:"
    ShopSelect = "Выберите карту магазина:"
    WriteYourShop = "Ок, напиши название магазина:"
    UnknownShop = "Сори, магазин не обнаружен :("
    EnterBarcode = "Теперь введи номер дисконтной карты (Barcode) от 12 цифр:"
    CardNameExists = "Карта с таким названием уже существует. Проверьте список!"
