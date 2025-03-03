import uuid

import barcode
from barcode.writer import ImageWriter

from bot.common.constants.app import STORAGE_PATH, CategorySlug, SavePrefix


async def saveCard(user: str, data: dict):
    EAN = barcode.get_barcode_class("ean13")
    if len(data["cardCode"]) > 13:
        EAN = barcode.get_barcode_class("code128")

    if data["category"] == CategorySlug.Other:
        fileName = uuid.uuid4()
        savePrefix = SavePrefix.Any
    else:
        fileName = f"{user}_{data["category"]}_{data["shop"]}"
        savePrefix = SavePrefix.Defined

    with open(f"{STORAGE_PATH}/{savePrefix}/{fileName}.jpeg", "wb") as f:
        EAN(data["cardCode"], writer=ImageWriter()).write(f)
