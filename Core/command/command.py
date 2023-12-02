from aiogram import Bot
from aiogram.types import BotCommand

async def set_command(bot: Bot):
    commands = [
        BotCommand(command="exam")
    ]

    await bot.set_my_commands(commands)