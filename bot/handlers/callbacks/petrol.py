# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.petrol import petrolBoard, petrolBoardMarkup
from common.constants.messages import BotMessages
from common.enums.namespaces import CallBackNameSpace

router = Router()

__selectMessage = "Выберите АЗС карту"


@router.callback_query(F.data == CallBackNameSpace.Petrol)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(text=__selectMessage, reply_markup=petrolBoardMarkup)


@router.callback_query(F.data == f"{CallBackNameSpace.Petrol}_back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(F.data == f"{CallBackNameSpace.Petrol}_item_back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=__selectMessage,
        reply_markup=petrolBoardMarkup,
    )


@router.callback_query(F.data.in_(set(btn.callback_data for [btn] in petrolBoard)))
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text="Тут штрихкод карты типо...",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[backButton(f"{CallBackNameSpace.Petrol}_item")]
        ),
    )
