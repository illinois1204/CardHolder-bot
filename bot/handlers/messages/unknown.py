from aiogram import Router

endRouter = Router()


@endRouter.message()
async def _(message):
    await message.answer(text="404...")
