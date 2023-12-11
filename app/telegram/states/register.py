from aiogram.fsm.state import State, StatesGroup


class RegisterState(StatesGroup):
    reg_name = State()
    reg_age = State()
    reg_city = State()
    reg_occupation = State()
    reg_interests = State()
