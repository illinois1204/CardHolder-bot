# mypy: disable-error-code="union-attr"
import os

from aiogram import F, Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.common.constants.app import ASSETS_PATH, NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.keyboard.category import categoryBoardMarkup
from bot.sql.models.cards import Card
from bot.sql.repository.get_cards import getUserCards
from bot.sql.repository.show_card import findAnyCard

router = Router()


def makeKeyboard(dataList: list[Card]):
    builder = InlineKeyboardBuilder()
    for row in dataList:
        builder.button(
            text=row.name,
            callback_data=f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}{row.file}",
        )

    builder.button(
        text="< назад",
        callback_data=f"{CategorySlug.Other}{NAMESPACE_SEPARATOR}back",
    )
    builder.adjust(1)
    return builder.as_markup()


@router.callback_query(F.data == CategorySlug.Other)
async def _(ctx: types.CallbackQuery):
    shopList = getUserCards(ctx.from_user.id)
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.ShopSelect,
        reply_markup=makeKeyboard(shopList),
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
    await ctx.answer()
    await ctx.message.edit_media(
        reply_markup=makeKeyboard(shopList),
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
            caption=BotMessages.ShopSelect,
        ),
    )


@router.callback_query(F.data)
async def _(ctx: types.CallbackQuery):
    await findAnyCard(ctx)
