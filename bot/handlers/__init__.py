from aiogram import Router

from .callbacks import clothes, electronics, market, petrol, other
from .commands import base, client
from .messages import (
    fsm_add_card,
    fsm_card_typing,
    fsm_clothes,
    fsm_electronics,
    fsm_market,
    fsm_other,
    fsm_petrol,
    shared,
)

router = Router()

router.include_routers(shared.interceptRouter)

router.include_routers(
    base.router,
    client.router,
    market.router,
    petrol.router,
    clothes.router,
    electronics.router,
    other.router,
    fsm_add_card.router,
    fsm_card_typing.router,
    fsm_market.router,
    fsm_petrol.router,
    fsm_other.router,
    fsm_clothes.router,
    fsm_electronics.router,
)

router.include_router(shared.endRouter)
