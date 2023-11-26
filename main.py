from aiogram import Bot, Dispatcher
import asyncio
import logging
from Core.handlers.basic import get_start, get_inline
from Core.settings import settings
from aiogram.types import message, ContentType
from aiogram.filters import Command
from Core.handlers.callback import select_answer
from Core.handlers import exam
from Core.utils.steps_exam import StepsExam

async def start_bot():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(name)s "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token)

    dp = Dispatcher()
    dp.message.register(get_start, Command(commands=["start", "go"]))
    dp.message.register(get_inline, Command(commands="inline"))
    dp.message.register(exam.start_exam, Command(commands="exam"))
    dp.message.register(exam.qwestion1, StepsExam.START_EXAM)
    dp.message.register(exam.qwestion2, StepsExam.GET_ANSWER1)
    dp.message.register(exam.finish, StepsExam.GET_ANSWER2)
    dp.callback_query.register(select_answer)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start_bot())