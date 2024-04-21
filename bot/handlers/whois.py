from typing import Any

from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils.formatting import as_list, Text

from bot.keyboards.information import GetInformation
from bot.states.lang_states import States
from bot.utils.whois import get_whois
from bot.loader import bot

router = Router(name='whois')


@router.callback_query(
    GetInformation.filter(F.info)
)
async def language_change(query: CallbackQuery, state=States.LANG) -> Any:
    GetInformation.unpack(query.data)
    data = await state.get_data()
    whois = get_whois(data['LINK'])
    if data['LANG'] == 'ru':
        content = as_list(
            Text('IP: ', whois['query']),
            Text(''),
            Text('Регион: ', whois['regionName']),
            Text('Страна: ', whois['country']),
            Text('Город: ', whois['city']),
            Text(''),
            Text('Провайдер: ', whois['isp']),
            Text('Организация: ', whois['org']),
        )
        await bot.answer_callback_query(query.id, text=content.as_html(), show_alert=True)

    else:
        content = as_list(
            Text('IP: ', whois['query']),
            Text(''),
            Text('Region: ', whois['regionName']),
            Text('Country: ', whois['country']),
            Text('City: ', whois['city']),
            Text(''),
            Text('Provider: ', whois['isp']),
            Text('Organisation: ', whois['org']),
        )
        await bot.answer_callback_query(query.id, text=content.as_html(), show_alert=True)
