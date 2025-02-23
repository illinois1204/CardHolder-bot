from aiogram import Router

from .callbacks import clothes, electronics, market, petrol
from .commands import base, client
from .messages import unknown

router = Router()
router.include_routers(
    base.router,
    client.router,
    market.router,
    petrol.router,
    clothes.router,
    electronics.router,
)
router.include_router(unknown.endRouter)
