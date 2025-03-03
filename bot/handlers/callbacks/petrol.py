# mypy: disable-error-code="union-attr"
import os

from aiogram import F, Router, types

from bot.common.constants.app import ASSETS_PATH, NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.common.lambdas.show_card import findCardResult
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.petrol import petrolBoard, petrolBoardMarkup, petrolMap

router = Router()

__selectMessage = "Выберите АЗС карту"


@router.callback_query(F.data == CategorySlug.Petrol)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=__selectMessage, reply_markup=petrolBoardMarkup
    )


@router.callback_query(F.data == f"{CategorySlug.Petrol}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_caption(
        caption=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data == f"{CategorySlug.Petrol}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_media(
        reply_markup=petrolBoardMarkup,
        media=types.InputMediaPhoto(
            media=types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/scan-me.jpg"),
            caption=__selectMessage,
        ),
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in petrolBoard)))
async def _(ctx: types.CallbackQuery):
    await findCardResult(ctx, CategorySlug.Petrol, petrolMap)
