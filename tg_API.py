import logging
import os
import time

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f"{user_id=} {user_full_name} {time.asctime()}")

    await message.reply(
        f"Hello, {user_full_name}! Welcome to our networking bot. Please follow the instructions to register.very llongggg statement"
    )


@dp.message_handler(commands=["register"])
async def register_handler(message: types.Message):
    await message.reply("Please provide your registration details...")


if __name__ == "__main__":
    executor.start_polling(dp)
