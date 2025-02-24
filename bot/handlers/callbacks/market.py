# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.market import marketBoard, marketBoardMarkup
from common.constants.messages import BotMessages
from common.enums.namespaces import CallBackNameSpace

router = Router()

__selectMessage = "Выберите карту Супермаркета"


@router.callback_query(F.data == CallBackNameSpace.Market)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(text=__selectMessage, reply_markup=marketBoardMarkup)


@router.callback_query(F.data == f"{CallBackNameSpace.Market}_back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(F.data == f"{CallBackNameSpace.Market}_item_back")
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
            inline_keyboard=[backButton(f"{CallBackNameSpace.Market}_item")]
        ),
    )
