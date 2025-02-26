from aiogram import Router

from .callbacks import clothes, electronics, market, petrol
from .commands import base, client
from .fsm import put_card
from .messages import unknown

router = Router()
router.include_routers(
    base.router,
    client.router,
    market.router,
    petrol.router,
    clothes.router,
    electronics.router,
    put_card.router,
)
router.include_router(unknown.endRouter)
