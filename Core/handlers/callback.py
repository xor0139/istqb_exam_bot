from aiogram import Bot
from aiogram.types import CallbackQuery

async def select_answer(call: CallbackQuery, bot: Bot):
    variant = call.data
    answer = f"{call.message.from_user.first_name} вы выбрали вариант {variant}"
    await call.message.answer(answer)
    await call.answer()