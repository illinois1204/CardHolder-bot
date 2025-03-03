from typing import List

from bot.sql.driver import sql
from bot.sql.models.cards import Card


def getUserCards(user: str) -> List[Card]:
    return sql.query(Card).filter(Card.user == user).all()
