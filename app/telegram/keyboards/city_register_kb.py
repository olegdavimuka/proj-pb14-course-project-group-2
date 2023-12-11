from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


city_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Київ"),
            KeyboardButton(text="Львів"),
            KeyboardButton(text="Дніпро"),
            KeyboardButton(text="Одеса"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
