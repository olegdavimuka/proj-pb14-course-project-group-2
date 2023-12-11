import asyncio
import logging
import os

import handlers.register
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from dotenv import load_dotenv
from handlers.start import start_handler
from states.register import RegisterState
from utils.commands import set_commands


load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.message.register(start_handler, Command(commands="start"))

dp.message.register(handlers.register.start_register, F.text == "Реєстрація")
dp.message.register(handlers.register.register_name, RegisterState.reg_name)
dp.message.register(handlers.register.register_age, RegisterState.reg_age)
dp.message.register(handlers.register.register_city, RegisterState.reg_city)
dp.message.register(
    handlers.register.register_occupation, RegisterState.reg_occupation
)
dp.message.register(
    handlers.register.register_interests, RegisterState.reg_interests
)


async def main() -> None:
    await set_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
