from aiogram import Router

from .commands import router as commandRouter
from .messages import endRouter

router = Router()
router.include_router(commandRouter)
router.include_router(endRouter)
