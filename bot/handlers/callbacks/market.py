# mypy: disable-error-code="union-attr"
import os

from aiogram import F, Router, types

from bot.common.constants.app import ASSETS_PATH, NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.market import marketBoard, marketBoardMarkup, marketMap
from bot.sql.repository.show_card import findDefinedCard

router = Router()

__selectMessage = "Выберите карту Супермаркета"


@router.callback_query(F.data == CategorySlug.Market)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=__selectMessage, reply_markup=marketBoardMarkup
    )


@router.callback_query(F.data == f"{CategorySlug.Market}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data == f"{CategorySlug.Market}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_media(
        reply_markup=marketBoardMarkup,
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
            caption=__selectMessage,
        ),
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in marketBoard)))
async def _(ctx: types.CallbackQuery):
    await findDefinedCard(ctx, CategorySlug.Market, marketMap)
