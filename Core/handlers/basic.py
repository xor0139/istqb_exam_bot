from aiogram import Bot
from aiogram.types import Message
from Core.keyboards.inline import get_inline_keyboard
from aiogram.fsm.context import FSMContext

from Core.utils.steps_exam import StepsExam


async def get_start(message: Message, state: FSMContext):
    txt = f"Здравсвтвуйте, {message.from_user.first_name}!\n" \
    "Я бот экзаменатор ISTQB, я помогу тебе подготовится к экзаменам Foundation level," \
    "на сегодняшний день я могу задавать вопросы из билетов версий А и В Syllabus 2018.\n" \
    "В конце экзамена я отвечу на твои ответы словами Верно или Неверно," \
    "это для того что бы ты сам смог разобраться, где совершил ошибку.\n" \
    "Как будешь готов, отправь текст /A или /B, в зависимости от того, какую версию билетов хотите решать."
    await message.answer(txt)
