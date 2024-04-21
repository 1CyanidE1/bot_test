import time
from typing import Any
import emoji

from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.utils.formatting import as_list, Text, Bold, TextLink


from bot.keyboards.information import information_keyboard
from bot.utils.data_validate import validate_data
from bot.utils.link_writer import fill_link
from bot.utils.scheme import ensure_scheme
from bot.utils.screen_as import get_screenshot
from bot.loader import bot

router = Router(name='links')


@router.message(
    F.text.regexp(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,'
                  r'})(\.[a-zA-Z0-9]{2,})?')
)
async def handle_url(message: types.Message, state=FSMContext) -> Any:
    await state.update_data(LINK=message.text)
    data = await state.get_data()
    start_time = time.time()

    if data['LANG'] == 'ru':
        operation_message = await message.reply(
            f"{emoji.emojize(':high_voltage:')} Запрос отправлен на сайт"
        )

    else:
        operation_message = await message.reply(
            f"{emoji.emojize(':high_voltage:')} Request sent to website"
        )

    validate_data(message)
    link = ensure_scheme(message.text)

    if link:
        data = await state.get_data()
        screenshot_url, title, file_name = await get_screenshot(
            link,
            message.from_user.id
        )
        fill_link(message, link, file_name)

        if data['LANG'] == 'ru':
            end_time = time.time()

            content = as_list(
                Text(Bold(title)),
                Text('', TextLink('\u200B', url=screenshot_url)),
                Text(Bold('Сайт: '), link),
                Text(Bold('Время обработки: '), f'{round(end_time - start_time, 2)} сек'),
            )
        else:
            end_time = time.time()

            content = as_list(
                Text(Bold(title)),
                Text('', TextLink('\u200B', url=screenshot_url)),
                Text(Bold('Website: '), link),
                Text(Bold('Time of processing: '), f'{round(end_time - start_time, 2)} sec'),
            )

        await bot.edit_message_text(
            text=content.as_markdown(),
            chat_id=message.chat.id,
            message_id=operation_message.message_id,
            reply_markup=await information_keyboard(state)
        )

    else:
        if data['LANG'] == 'ru':
            content = as_list(
                Text('Кажется, сайт на который ведет ваша ссылка не отвечает.'),
                Text(''),
                Text('Проверьте ссылку или повторите попытку позже'),
            )
            await bot.edit_message_text(
                text=content.as_markdown(),
                chat_id=message.chat.id,
                message_id=operation_message.message_id
            )
        else:
            content = as_list(
                Text("Seems like your link isn't working."),
                Text(''),
                Text('Check the link or try again later'),
            )
            await bot.edit_message_text(
                text=content.as_markdown(),
                chat_id=message.chat.id,
                message_id=operation_message.message_id,
                reply_markup=await information_keyboard(state)
            )
