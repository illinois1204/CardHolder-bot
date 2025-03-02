# mypy: disable-error-code="union-attr"
import os

from aiogram import F, Router, types

from bot.common.constants.app import ASSETS_PATH, NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.clothes import clothesBoard, clothesBoardMarkup, clothesMap

router = Router()


@router.callback_query(F.data == CategorySlug.Clothes)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.ShopSelect, reply_markup=clothesBoardMarkup
    )


@router.callback_query(F.data == f"{CategorySlug.Clothes}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data
    == f"{CategorySlug.Clothes}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_media(
        reply_markup=clothesBoardMarkup,
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
            caption=BotMessages.ShopSelect,
        ),
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in clothesBoard)))
async def _(ctx: types.CallbackQuery):
    item_key = ctx.data.split(NAMESPACE_SEPARATOR).pop()
    await ctx.answer()
    await ctx.message.edit_media(
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/code.png"),
            caption=clothesMap[item_key],
        ),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                backButton(f"{CategorySlug.Clothes}{NAMESPACE_SEPARATOR}item")
            ]
        ),
    )
