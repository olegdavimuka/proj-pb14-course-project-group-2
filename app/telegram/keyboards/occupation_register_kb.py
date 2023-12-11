from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


occupation_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Dev&Data Science"),
            KeyboardButton(text="Marketing"),
            KeyboardButton(text="Management"),
            KeyboardButton(text="Graphics"),
            KeyboardButton(text="Interface Design"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)
