from aiogram import Bot, Dispatcher
import asyncio
import logging
from Core.handlers.basic import get_start
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

    dp.message.register(exam.start_exam_A, Command(commands=["A", "a", "A", "a"]))
    dp.message.register(exam.qwestion1_A, StepsExam.START_EXAM_A)
    dp.message.register(exam.qwestion2_A, StepsExam.GET_ANSWER1_A)
    dp.message.register(exam.qwestion3_A, StepsExam.GET_ANSWER2_A)
    dp.message.register(exam.qwestion4_A, StepsExam.GET_ANSWER3_A)
    dp.message.register(exam.qwestion5_A, StepsExam.GET_ANSWER4_A)
    dp.message.register(exam.qwestion6_A, StepsExam.GET_ANSWER5_A)
    dp.message.register(exam.qwestion7_A, StepsExam.GET_ANSWER6_A)
    dp.message.register(exam.qwestion8_A, StepsExam.GET_ANSWER7_A)
    dp.message.register(exam.qwestion9_A, StepsExam.GET_ANSWER8_A)
    dp.message.register(exam.qwestion10_A, StepsExam.GET_ANSWER9_A)
    dp.message.register(exam.qwestion11_A, StepsExam.GET_ANSWER10_A)
    dp.message.register(exam.qwestion12_A, StepsExam.GET_ANSWER11_A)
    dp.message.register(exam.qwestion13_A, StepsExam.GET_ANSWER12_A)
    dp.message.register(exam.qwestion14_A, StepsExam.GET_ANSWER13_A)
    dp.message.register(exam.qwestion15_A, StepsExam.GET_ANSWER14_A)
    dp.message.register(exam.qwestion16_A, StepsExam.GET_ANSWER15_A)
    dp.message.register(exam.qwestion17_A, StepsExam.GET_ANSWER16_A)
    dp.message.register(exam.qwestion18_A, StepsExam.GET_ANSWER17_A)
    dp.message.register(exam.qwestion19_A, StepsExam.GET_ANSWER18_A)
    dp.message.register(exam.qwestion20_A, StepsExam.GET_ANSWER19_A)
    dp.message.register(exam.qwestion21_A, StepsExam.GET_ANSWER20_A)
    dp.message.register(exam.qwestion22_A, StepsExam.GET_ANSWER21_A)
    dp.message.register(exam.qwestion23_A, StepsExam.GET_ANSWER22_A)
    dp.message.register(exam.qwestion24_A, StepsExam.GET_ANSWER23_A)
    dp.message.register(exam.qwestion25_A, StepsExam.GET_ANSWER24_A)
    dp.message.register(exam.qwestion26_A, StepsExam.GET_ANSWER25_A)
    dp.message.register(exam.qwestion27_A, StepsExam.GET_ANSWER26_A)
    dp.message.register(exam.qwestion28_A, StepsExam.GET_ANSWER27_A)
    dp.message.register(exam.qwestion29_A, StepsExam.GET_ANSWER28_A)
    dp.message.register(exam.qwestion30_A, StepsExam.GET_ANSWER29_A)
    dp.message.register(exam.qwestion31_A, StepsExam.GET_ANSWER30_A)
    dp.message.register(exam.qwestion32_A, StepsExam.GET_ANSWER31_A)
    dp.message.register(exam.qwestion33_A, StepsExam.GET_ANSWER32_A)
    dp.message.register(exam.qwestion34_A, StepsExam.GET_ANSWER33_A)
    dp.message.register(exam.qwestion35_A, StepsExam.GET_ANSWER34_A)
    dp.message.register(exam.qwestion36_A, StepsExam.GET_ANSWER35_A)
    dp.message.register(exam.qwestion37_A, StepsExam.GET_ANSWER36_A)
    dp.message.register(exam.qwestion38_A, StepsExam.GET_ANSWER37_A)
    dp.message.register(exam.qwestion39_A, StepsExam.GET_ANSWER38_A)
    dp.message.register(exam.qwestion40_A, StepsExam.GET_ANSWER39_A)
    dp.message.register(exam.finish_A, StepsExam.GET_ANSWER40_A)

    dp.callback_query.register(select_answer)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start_bot())