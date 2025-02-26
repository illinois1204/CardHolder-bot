# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.market import marketBoard, marketBoardMarkup

router = Router()

__selectMessage = "Выберите карту Супермаркета"


@router.callback_query(F.data == CategorySlug.Market)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(text=__selectMessage, reply_markup=marketBoardMarkup)


@router.callback_query(F.data == f"{CategorySlug.Market}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data == f"{CategorySlug.Market}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=__selectMessage,
        reply_markup=marketBoardMarkup,
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in marketBoard)))
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text="Тут штрихкод карты типо...",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                backButton(f"{CategorySlug.Market}{NAMESPACE_SEPARATOR}item")
            ]
        ),
    )
