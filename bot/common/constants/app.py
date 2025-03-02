from enum import StrEnum


class CategorySlug(StrEnum):
    Market = "markets"
    Petrol = "petrol"
    Electronic = "electronics"
    Clothes = "clothes"
    Other = "other"


NAMESPACE_SEPARATOR = ":"

ASSETS_PATH = "bot/components/assets"
