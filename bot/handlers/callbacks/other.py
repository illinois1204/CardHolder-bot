# mypy: disable-error-code="union-attr"
import os

from aiogram import F, Router, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.common.constants.app import ASSETS_PATH, NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.sql.repository.get_cards import getUserCards
from bot.sql.repository.show_card import findAnyCard

router = Router()


@router.callback_query(F.data == CategorySlug.Other)
async def _(ctx: types.CallbackQuery):
    shopList = getUserCards(ctx.from_user.id)
    board = [
        [
            InlineKeyboardButton(
                text=row.name,
                callback_data=f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}{row.file}",
            )
        ]
        for row in shopList
    ]
    board.append(backButton(CategorySlug.Other))

    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.ShopSelect,
        reply_markup=InlineKeyboardMarkup(inline_keyboard=board),
    )


@router.callback_query(F.data == f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data == f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    shopList = getUserCards(ctx.from_user.id)
    board = [
        [
            InlineKeyboardButton(
                text=row.name,
                callback_data=f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}{row.file}",
            )
        ]
        for row in shopList
    ]
    board.append(backButton(CategorySlug.Other))

    await ctx.answer()
    await ctx.message.edit_media(
        reply_markup=InlineKeyboardMarkup(inline_keyboard=board),
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
            caption=BotMessages.ShopSelect,
        ),
    )


@router.callback_query(F.data)
async def _(ctx: types.CallbackQuery):
    await findAnyCard(ctx)
