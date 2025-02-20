from aiogram.types import BotCommand

Menu: list[BotCommand] = [
    BotCommand(command="/start", description="Запуск бота"),
    BotCommand(command="/help", description="Информация по использованию"),
    BotCommand(command="/category", description="Категории"),
    BotCommand(command="/list_cards", description="Список всех карт"),
    BotCommand(command="/add_card", description="Добавить карту")
]
