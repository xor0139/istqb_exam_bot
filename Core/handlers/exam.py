from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from Core.keyboards.inline import get_inline_keyboard
from Core.utils.steps_exam import StepsExam
from Core.Dictonary import QuestionsA, AnswersA
from Core.utils.match_answer import match

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

async def qwestion3(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION3)
    await state.update_data(answer2=message.text)
    await state.set_state(StepsExam.GET_ANSWER3)

async def qwestion4(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION4)
    await state.update_data(answer3=message.text)
    await state.set_state(StepsExam.GET_ANSWER4)

async def qwestion5(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION5)
    await state.update_data(answer4=message.text)
    await state.set_state(StepsExam.GET_ANSWER5)

async def qwestion6(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION6)
    await state.update_data(answer5=message.text)
    await state.set_state(StepsExam.GET_ANSWER6)

async def qwestion7(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION7)
    await state.update_data(answer6=message.text)
    await state.set_state(StepsExam.GET_ANSWER7)

async def qwestion8(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION8)
    await state.update_data(answer7=message.text)
    await state.set_state(StepsExam.GET_ANSWER8)

async def qwestion9(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION9)
    await state.update_data(answer8=message.text)
    await state.set_state(StepsExam.GET_ANSWER9)

async def qwestion10(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION10)
    await state.update_data(answer9=message.text)
    await state.set_state(StepsExam.GET_ANSWER10)

async def finish(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} экзамен завершен!")
    await state.update_data(answer10=message.text)
    answers = await state.get_data()
    txt = f"Ваши результат:\n" \
        f"Вопрос #1: {await match(str(answers.get('answer1')), AnswersA.ANSWER1)}\n" \
        f"Вопрос #2: {await match(str(answers.get('answer2')), AnswersA.ANSWER2)}\n" \
        f"Вопрос #3: {await match(str(answers.get('answer3')), AnswersA.ANSWER3)}\n" \
        f"Вопрос #4: {await match(str(answers.get('answer4')), AnswersA.ANSWER4)}\n" \
        f"Вопрос #5: {await match(str(answers.get('answer5')), AnswersA.ANSWER5)}\n" \
        f"Вопрос #6: {await match(str(answers.get('answer6')), AnswersA.ANSWER6)}\n" \
        f"Вопрос #7: {await match(str(answers.get('answer7')), AnswersA.ANSWER7)}\n" \
        f"Вопрос #8: {await match(str(answers.get('answer8')), AnswersA.ANSWER8)}\n" \
        f"Вопрос #9: {await match(str(answers.get('answer9')), AnswersA.ANSWER9)}\n" \
        f"Вопрос #10: {await match(str(answers.get('answer10')), AnswersA.ANSWER10)}\n"
    await message.answer(txt)
    await state.clear()