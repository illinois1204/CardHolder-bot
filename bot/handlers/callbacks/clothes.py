# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.clothes import clothesBoardMarkup
from common.constants.messages import BotMessages

router = Router()


@router.callback_query(F.data == "clothes")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text="Выберите карту магазина", reply_markup=clothesBoardMarkup
    )


@router.callback_query(F.data == "back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )
