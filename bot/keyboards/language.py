from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
import emoji


class LanguageChoice(CallbackData, prefix="language"):
    lang_code: str


class LanguageChange(CallbackData, prefix="language_change"):
    request: bool


def language_choice_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Русский",
                    callback_data=LanguageChoice(lang_code='ru').pack()
                ),
                InlineKeyboardButton(
                    text="English",
                    callback_data=LanguageChoice(lang_code='en').pack()
                )
            ]
        ]
    )


async def language_change_keyboard(state) -> InlineKeyboardMarkup:
    data = await state.get_data()
    if data['LANG'] == 'ru':
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"{emoji.emojize(':globe_with_meridians:')} Выбор языка",
                        callback_data=LanguageChange(request=True).pack()
                    ),
                ]
            ]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"{emoji.emojize(':globe_with_meridians:')} Language",
                        callback_data=LanguageChange(request=True).pack()
                    ),
                ]
            ]
        )
