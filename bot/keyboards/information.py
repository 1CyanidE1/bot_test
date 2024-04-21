from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
import emoji


class GetInformation(CallbackData, prefix="information"):
    info: bool


async def information_keyboard(state) -> InlineKeyboardMarkup:
    data = await state.get_data()
    if data['LANG'] == 'ru':
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"{emoji.emojize(':open_book:')} Дополнительная информация",
                        callback_data=GetInformation(info=True).pack()
                    ),
                ]
            ]
        )
    else:
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text=f"{emoji.emojize(':open_book:')} More information",
                        callback_data=GetInformation(info=True).pack()
                    ),
                ]
            ]
        )
