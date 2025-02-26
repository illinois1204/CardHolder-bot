# mypy: disable-error-code="union-attr"
from aiogram import F, Router, types

from bot.common.constants.app import NAMESPACE_SEPARATOR, CategorySlug
from bot.common.constants.messages import BotMessages
from bot.components.buttons.back import backButton
from bot.components.keyboard.category import categoryBoardMarkup
from bot.components.keyboard.petrol import petrolBoard, petrolBoardMarkup

router = Router()

__selectMessage = "Выберите АЗС карту"


@router.callback_query(F.data == CategorySlug.Petrol)
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(text=__selectMessage, reply_markup=petrolBoardMarkup)


@router.callback_query(F.data == f"{CategorySlug.Petrol}{NAMESPACE_SEPARATOR}back")
async def _(ctx: types.CallbackQuery):
    await ctx.answer()
    await ctx.message.edit_text(
        text=BotMessages.CategorySelect,
        reply_markup=categoryBoardMarkup,
    )


@router.callback_query(
    F.data == f"{CategorySlug.Petrol}{NAMESPACE_SEPARATOR}item{NAMESPACE_SEPARATOR}back"
)
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
            inline_keyboard=[
                backButton(f"{CategorySlug.Petrol}{NAMESPACE_SEPARATOR}item")
            ]
        ),
    )
