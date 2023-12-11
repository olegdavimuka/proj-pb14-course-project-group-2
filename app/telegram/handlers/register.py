from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.age_register_kb import age_keyboard
from keyboards.city_register_kb import city_keyboard
from keyboards.occupation_register_kb import occupation_keyboard
from states.register import RegisterState

from app.db.user_repository import UserRepository


AGE_RANGES = ["18-24", "25-36", "37-50", "51-..."]
CITY_OPTIONS = ["Київ", "Львів", "Дніпро", "Одеса"]
OCCUPATION_OPTIONS = [
    "Dev&Data Science",
    "Marketing",
    "Management",
    "Graphics",
    "Interface Design",
]


async def start_register(message: Message, state: FSMContext):
    await message.answer(
        "Розпочнемо заповнення анкети📓 \n✨ Вкажіть Ваше імʼя ✨"
    )
    await state.set_state(RegisterState.reg_name)


async def register_name(message: Message, state: FSMContext):
    await message.answer(
        f"Приємно познайомитись, {message.text}!\n ✨ Вкажіть Ваш вік ✨\n",
        reply_markup=age_keyboard,
    )
    await state.update_data(reg_name=message.text)
    await state.set_state(RegisterState.reg_age)


async def register_age(message: Message, state: FSMContext):
    selected_age = message.text
    if selected_age not in AGE_RANGES:
        await message.answer("Будь ласка, виберіть вік за допомогою кнопок.")
    else:
        await message.answer(
            "✨ Вкажіть Вашe місто ✨\n", reply_markup=city_keyboard
        )
        await state.update_data(reg_age=message.text)
        await state.set_state(RegisterState.reg_city)


async def register_city(message: Message, state: FSMContext):
    selected_age = message.text
    if selected_age not in CITY_OPTIONS:
        await message.answer("Будь ласка, виберіть місто за допомогою кнопок.")
    else:
        await message.answer(
            "✨ Виберіть вашу сферу діяльності ✨\n",
            reply_markup=occupation_keyboard,
        )
        await state.update_data(reg_city=message.text)
        await state.set_state(RegisterState.reg_occupation)


async def register_occupation(message: Message, state: FSMContext):
    selected_occupation = message.text

    if selected_occupation not in OCCUPATION_OPTIONS:
        await message.answer(
            "Будь ласка, виберіть сферу діяльності за допомогою кнопок."
        )
    else:
        await message.answer("✨ Вкажіть Ваші захоплення та інтереси ✨\n")
        await state.update_data(reg_occupation=message.text)
        await state.set_state(RegisterState.reg_interests)


async def register_interests(message: Message, state: FSMContext):
    await state.update_data(reg_interests=message.text)

    reg_data = await state.get_data()
    register_name = reg_data.get("reg_name")
    register_age = reg_data.get("reg_age")
    register_city = reg_data.get("reg_city")
    register_occupation = reg_data.get("reg_occupation")
    register_interests = reg_data.get("reg_interests")

    msg = f"Ваш профіль: \nІмʼя: {register_name} \nВік: {register_age} \nМісто: {register_city} \n Сфера діяльності: {register_occupation}\nІнтереси: {register_interests}\n"
    await message.answer(msg)

    user_repository = UserRepository()
    user_repository.add_user(reg_data)
    await state.clear()
