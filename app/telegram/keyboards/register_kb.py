from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


register_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Реєстрація")]],
    resize_keyboard=True,
    one_time_keyboard=True,
)
