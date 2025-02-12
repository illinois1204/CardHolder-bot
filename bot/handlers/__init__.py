from aiogram import Router

from .commands import router as commandRouter

router = Router()
router.include_router(commandRouter)
