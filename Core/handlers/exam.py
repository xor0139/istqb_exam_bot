from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from Core.keyboards.inline import get_inline_keyboard
from Core.utils.steps_exam import StepsExam
from Core.Dictonary import QuestionsA

async def start_exam(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} {QuestionsA.INTRO}")
    await state.set_state(StepsExam.START_EXAM)

async def qwestion1(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION1)
    await state.set_state(StepsExam.GET_ANSWER1)

async def qwestion2(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION2)
    await state.update_data(answer1=message.text)
    await state.set_state(StepsExam.GET_ANSWER2)

async def finish(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} FINISH")
    await state.update_data(answer2=message.text)
    answers = await state.get_data()
    txt = f"""Ваши ответы:\n
              Ответ 1: {answers.get('answer1')}\n
              Ответ 2: {answers.get('answer2')}\n"""
    await message.answer(txt)
    await state.clear()