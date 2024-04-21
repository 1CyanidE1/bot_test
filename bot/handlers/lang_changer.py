from typing import Any
import emoji

from aiogram import Router, F
from aiogram.types import CallbackQuery

from bot.keyboards.language import language_choice_keyboard, LanguageChange

router = Router(name='lang_changer')


@router.callback_query(
    LanguageChange.filter(F.request)
)
async def language_change(query: CallbackQuery) -> Any:
    LanguageChange.unpack(query.data)
    await query.message.edit_text(
        f'{emoji.emojize(":globe_with_meridians:")} Choose language',
        reply_markup=language_choice_keyboard()
    )
