import importlib
import pkgutil

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


for module_info in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__package__}.{module_info.name}")
