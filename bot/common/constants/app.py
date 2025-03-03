import os
from enum import StrEnum


class CategorySlug(StrEnum):
    Market = "markets"
    Petrol = "petrol"
    Electronic = "electronics"
    Clothes = "clothes"
    Other = "other"


class SavePrefix(StrEnum):
    Defined = "defined"
    Any = "any"


NAMESPACE_SEPARATOR = ":"

ASSETS_PATH = "bot/components/assets"

STORAGE_PATH = f"{os.getcwd()}/storage"
