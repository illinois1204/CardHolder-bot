from aiogram.fsm.state import State, StatesGroup


class PutCard(StatesGroup):
    categorySelect = State()
    numberType = State()


class ShopInSection(StatesGroup):
    markets = State()
    petrol = State()
    electronics = State()
    clothes = State()
    other = State()
