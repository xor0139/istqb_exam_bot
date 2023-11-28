from aiogram import Bot
from aiogram.types import Message
from Core.keyboards.inline import get_inline_keyboard
from aiogram.types import FSInputFile
async def get_start(message: Message):
    pass


async def get_inline(message: Message, bot: Bot):
    await message.answer(f"Ответь пожалуйста на вопрос", reply_markup=get_inline_keyboard())