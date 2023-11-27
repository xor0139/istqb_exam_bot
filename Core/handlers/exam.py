from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from Core.keyboards.inline import get_inline_keyboard
from Core.utils.steps_exam import StepsExam
from Core.Dictonary import QuestionsA, AnswersA
from Core.utils.match_answer import match

async def start_exam_A(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} {QuestionsA.INTRO}")
    await state.set_state(StepsExam.START_EXAM)

async def qwestion1_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION1)
    await state.set_state(StepsExam.GET_ANSWER1)

async def qwestion2_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION2)
    await state.update_data(answer1=message.text)
    await state.set_state(StepsExam.GET_ANSWER2)

async def qwestion3_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION3)
    await state.update_data(answer2=message.text)
    await state.set_state(StepsExam.GET_ANSWER3)

async def qwestion4_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION4)
    await state.update_data(answer3=message.text)
    await state.set_state(StepsExam.GET_ANSWER4)

async def qwestion5_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION5)
    await state.update_data(answer4=message.text)
    await state.set_state(StepsExam.GET_ANSWER5)

async def qwestion6_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION6)
    await state.update_data(answer5=message.text)
    await state.set_state(StepsExam.GET_ANSWER6)

async def qwestion7_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION7)
    await state.update_data(answer6=message.text)
    await state.set_state(StepsExam.GET_ANSWER7)

async def qwestion8_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION8)
    await state.update_data(answer7=message.text)
    await state.set_state(StepsExam.GET_ANSWER8)

async def qwestion9_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION9)
    await state.update_data(answer8=message.text)
    await state.set_state(StepsExam.GET_ANSWER9)

async def qwestion10_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION10)
    await state.update_data(answer9=message.text)
    await state.set_state(StepsExam.GET_ANSWER10)

async def finish_A(message: Message, state: FSMContext):
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
    f"Вопрос #11: {await match(str(answers.get('answer11')), AnswersA.ANSWER11)}\n"
    f"Вопрос #12: {await match(str(answers.get('answer12')), AnswersA.ANSWER12)}\n"
    f"Вопрос #13: {await match(str(answers.get('answer13')), AnswersA.ANSWER13)}\n"
    f"Вопрос #14: {await match(str(answers.get('answer14')), AnswersA.ANSWER14)}\n"
    f"Вопрос #15: {await match(str(answers.get('answer15')), AnswersA.ANSWER15)}\n"
    f"Вопрос #16: {await match(str(answers.get('answer16')), AnswersA.ANSWER16)}\n"
    f"Вопрос #17: {await match(str(answers.get('answer17')), AnswersA.ANSWER17)}\n"
    f"Вопрос #18: {await match(str(answers.get('answer18')), AnswersA.ANSWER18)}\n"
    f"Вопрос #19: {await match(str(answers.get('answer19')), AnswersA.ANSWER19)}\n"
    f"Вопрос #20: {await match(str(answers.get('answer20')), AnswersA.ANSWER20)}\n"
    f"Вопрос #21: {await match(str(answers.get('answer21')), AnswersA.ANSWER21)}\n"
    f"Вопрос #22: {await match(str(answers.get('answer22')), AnswersA.ANSWER22)}\n"
    f"Вопрос #23: {await match(str(answers.get('answer23')), AnswersA.ANSWER23)}\n"
    f"Вопрос #24: {await match(str(answers.get('answer24')), AnswersA.ANSWER24)}\n"
    f"Вопрос #25: {await match(str(answers.get('answer25')), AnswersA.ANSWER25)}\n"
    f"Вопрос #26: {await match(str(answers.get('answer26')), AnswersA.ANSWER26)}\n"
    f"Вопрос #27: {await match(str(answers.get('answer27')), AnswersA.ANSWER27)}\n"
    f"Вопрос #28: {await match(str(answers.get('answer28')), AnswersA.ANSWER28)}\n"
    f"Вопрос #29: {await match(str(answers.get('answer29')), AnswersA.ANSWER29)}\n"
    f"Вопрос #30: {await match(str(answers.get('answer30')), AnswersA.ANSWER30)}\n"
    f"Вопрос #31: {await match(str(answers.get('answer31')), AnswersA.ANSWER31)}\n"
    f"Вопрос #32: {await match(str(answers.get('answer32')), AnswersA.ANSWER32)}\n"
    f"Вопрос #33: {await match(str(answers.get('answer33')), AnswersA.ANSWER33)}\n"
    f"Вопрос #34: {await match(str(answers.get('answer34')), AnswersA.ANSWER34)}\n"
    f"Вопрос #35: {await match(str(answers.get('answer35')), AnswersA.ANSWER35)}\n"
    f"Вопрос #36: {await match(str(answers.get('answer36')), AnswersA.ANSWER36)}\n"
    f"Вопрос #37: {await match(str(answers.get('answer37')), AnswersA.ANSWER37)}\n"
    f"Вопрос #38: {await match(str(answers.get('answer38')), AnswersA.ANSWER38)}\n"
    f"Вопрос #39: {await match(str(answers.get('answer39')), AnswersA.ANSWER39)}\n"
    f"Вопрос #40: {await match(str(answers.get('answer40')), AnswersA.ANSWER40)}\n"
    await message.answer(txt)
    await state.clear()