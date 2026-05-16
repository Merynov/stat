from aiogram.fsm.state import StatesGroup, State


class EditProfileState(StatesGroup):
    waiting_name = State()
