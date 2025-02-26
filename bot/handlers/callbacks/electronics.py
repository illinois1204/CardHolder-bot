# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.electronics import electronicBoard, electronicBoardMarkup

router = Router()


@router.callback_query(F.data == CategorySlug.Electronic)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.ShopSelect, reply_markup=electronicBoardMarkup
    )


@router.callback_query(F.data == f"{CategorySlug.Electronic}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data
    == f"{CategorySlug.Electronic}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.ShopSelect,
        reply_markup=electronicBoardMarkup,
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in electronicBoard)))
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text="Тут штрихкод карты типо...",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                backButton(f"{CategorySlug.Electronic}{NAMESPACE_SEPARATOR}item")
            ]
        ),
    )
