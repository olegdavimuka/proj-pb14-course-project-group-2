from aiogram import Bot
from aiogram.types import Message
from keyboards.register_kb import register_keyboard


async def start_handler(message: Message, bot: Bot):
    await bot.send_message(
        message.from_user.id,
        "Вітаю!👋 \nЯ - бот від Projector Alumni Community.💙\n"
        "Я створений, щоб допомогти Вам знайти нові знайомства у нашому комюніті.\n"
        'Для початку Вам необхідно зареєструватися. Тисніть кнопку "Реєстрація"👇 \n',
        reply_markup=register_keyboard,
    )
