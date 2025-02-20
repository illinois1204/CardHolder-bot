from aiogram import F, Router, types

from bot.components.keyboard.petrol import petrolBoardMarkup

# from bot.main import BOT      # TODO: This is circle import, need to fix

router = Router()


# @router.callback_query(F.data == "markets")
# async def _(ctx: types.CallbackQuery):
#     await BOT.edit_message_text(
#         chat_id=ctx.message.chat.id,
#         message_id=ctx.message.message_id,
#         text="Выберите АЗС карту",
#         reply_markup=petrolBoardMarkup,
#     )


# @router.callback_query(F.data == "back")
# async def back(ctx: CallbackQuery):
#     await BOT.edit_message_text(
#         chat_id=ctx.message.chat.id,
#         message_id=ctx.message.message_id,
#         text="Select category",
#         reply_markup=kb.categoryBoardMarkup,
#     )
