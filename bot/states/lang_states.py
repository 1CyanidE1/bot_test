from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    LANG = State(),
    LINK = State()
