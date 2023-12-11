from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


age_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="18-24"),
            KeyboardButton(text="25-36"),
            KeyboardButton(text="37-50"),
            KeyboardButton(text="51-..."),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
