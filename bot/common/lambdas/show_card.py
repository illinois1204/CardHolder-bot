import os

from aiogram import types

from bot.common.constants.app import (
    ASSETS_PATH,
    NAMESPACE_SEPARATOR,
    STORAGE_PATH,
    CategorySlug,
    SavePrefix,
)
from bot.components.buttons.back import backButton


async def findCardResult(ctx: types.CallbackQuery, slug: CategorySlug, slugMap: dict):
    item_key = ctx.data.split(NAMESPACE_SEPARATOR).pop()

    fileName = f"{ctx.from_user.id}_{slug}_{item_key}.jpeg"
    filePath = f"{STORAGE_PATH}/{SavePrefix.Defined}/{fileName}"

    if os.path.exists(filePath):
        captionText = slugMap[item_key]
        mediaData = types.FSInputFile(filePath)
    else:
        captionText = "карта отсутствует"
        mediaData = types.FSInputFile(f"{os.getcwd()}/{ASSETS_PATH}/404.png")

    await ctx.answer()
    await ctx.message.edit_media(
        media=types.InputMediaPhoto(media=mediaData, caption=captionText),
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[backButton(f"{slug}{NAMESPACE_SEPARATOR}item")]
        ),
    )
