from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Start the bot"),
        BotCommand(command="help", description="Help with the bot functions"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
