# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.clothes import clothesBoard, clothesBoardMarkup
from common.constants.messages import BotMessages
from common.enums.namespaces import CallBackNameSpace

router = Router()


@router.callback_query(F.data == CallBackNameSpace.Clothes)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.ShopSelect, reply_markup=clothesBoardMarkup
    )


@router.callback_query(F.data == f"{CallBackNameSpace.Clothes}_back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(F.data == f"{CallBackNameSpace.Clothes}_item_back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.ShopSelect,
        reply_markup=clothesBoardMarkup,
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in clothesBoard)))
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text="Тут штрихкод карты типо...",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[backButton(f"{CallBackNameSpace.Clothes}_item")]
        ),
    )
