from aiogram import Router

from .callbacks import markets
from .commands import router as commandRouter
from .messages import endRouter

router = Router()
router.include_routers(commandRouter, markets.router)
router.include_router(endRouter)
