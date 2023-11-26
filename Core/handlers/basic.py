from aiogram import Bot
from aiogram.types import Message
from Core.keyboards.inline import get_inline_keyboard

async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f"Привет {message.from_user.first_name}")

async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Ответь пожалуйста на вопрос", reply_markup=get_inline_keyboard())