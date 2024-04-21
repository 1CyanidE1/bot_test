from typing import Any
import emoji

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from sqlalchemy.exc import NoResultFound
from aiogram.utils.formatting import as_list, Text, Bold, Italic

from bot.keyboards.language import language_choice_keyboard, language_change_keyboard, LanguageChoice
from bot.models.models import session, User
from bot.states.lang_states import States
from bot.utils.data_validate import validate_data


router = Router(name='start')


@router.message(
    # F.chat.type == ChatType.PRIVATE,
    CommandStart()
)
async def start_command(message: Message) -> Any:
    validate_data(message)
    await message.answer(
        f"{emoji.emojize(':globe_with_meridians:')} Choose your language",
        reply_markup=language_choice_keyboard()
    )


@router.callback_query(
    LanguageChoice.filter(F.lang_code)
)
async def language_choice(query: CallbackQuery, state=States.LANG):
    callback_data = LanguageChoice.unpack(query.data)
    lang_code = callback_data.lang_code

    try:
        user = session.query(User).filter(User.id == query.from_user.id).one()
        user.lang = lang_code
        session.commit()
        await state.update_data(LANG=lang_code)
        await state.get_data()
        if lang_code == 'ru':
            content = as_list(
                Text(f'{emoji.emojize(":waving_hand:")} Привет! Меня зовут ', Bold('Imager.')),
                Text("Я - Бот для создания веб-скриншотов. "),
                Text('Чтобы получить скриншот - отправьте URL адрес сайта.'),
                Text('Например, wikipedia.org'),
                Text(''),
                Text('• С помощью бота вы можете проверять подозрительные'),
                Text('ссылки. (', Italic('Айпилоггеры, фишинговые веб-сайты, скримеры и т.п'), '.)'),
                Text(''),
                Text('• Вы также можете добавить меня в свои чаты, и я смогу'),
                Text('проверять ссылки, которые отправляют пользователи.'),
                Text(''),
                Text(Bold('Imager'), ' использует ', Bold('chromedriver.')),
                Text('Работает с протоколами ', Bold('http, https.')),

            )
            await query.message.edit_text(
                text=content.as_markdown(),
                reply_markup=await language_change_keyboard(state)
            )
        else:
            content = as_list(
                Text(f'{emoji.emojize(":waving_hand:")} Welcome! My name is ', Bold('Imager.')),
                Text("I'm here for creating capture a website screenshot. To get a "),
                Text('screenshot - submit the URL of the Website.'),
                Text(''),
                Text('For example wikipedia.org'),
                Text(''),
                Text('• With the help of the bot, you can check suspicious links. (', Italic('IP-loggers,')),
                Text(Italic('phishing websites, screamers, etc'), '.)'),
                Text(''),
                Text('• You can also add me to your chats so that I can check the links'),
                Text('that the group chat members send.'),
                Text(''),
                Text(Bold('Imager'), ' uses ', Bold('chromedriver.')),
                Text('Works with protocols ', Bold('http, https.')),

            )
            await query.message.edit_text(
                text=content.as_markdown(),
                reply_markup=await language_change_keyboard(state)
            )
    except NoResultFound:
        user = User(
            id=query.from_user.id,
            name=query.from_user.first_name,
            username=query.from_user.username,
            lang=lang_code
        )
        session.add(user)
        session.commit()
    finally:
        session.close()
