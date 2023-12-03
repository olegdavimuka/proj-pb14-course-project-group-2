import asyncio
import logging
import os
import time

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
# from aiogram import executor
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    logging.info(f"{user_id=} {user_full_name} {time.asctime()}")

    await message.reply(
        f"Hello, {user_full_name}! Welcome to our networking bot. Please follow the instructions to register."
    )


@dp.message()
async def register_handler(message: types.Message):
    await message.reply("Please provide your registration details...")


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    # executor.start_polling(dp)
    asyncio.run(main())
