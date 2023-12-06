from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from Core.utils.steps_exam import StepsExam
from Core.Dictonary import QuestionsA, AnswersA, AnswersB, QuestionsB
from Core.utils.match_answer import match
from aiogram.types import FSInputFile


async def start_exam_A(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} {QuestionsA.INTRO}")
    await state.set_state(StepsExam.START_EXAM_A)

async def qwestion1_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION1)
    await state.set_state(StepsExam.GET_ANSWER1_A)

async def qwestion2_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION2)
    await state.update_data(answer1=message.text)
    await state.set_state(StepsExam.GET_ANSWER2_A)

async def qwestion3_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION3)
    await state.update_data(answer2=message.text)
    await state.set_state(StepsExam.GET_ANSWER3_A)

async def qwestion4_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION4)
    await state.update_data(answer3=message.text)
    await state.set_state(StepsExam.GET_ANSWER4_A)

async def qwestion5_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION5)
    await state.update_data(answer4=message.text)
    await state.set_state(StepsExam.GET_ANSWER5_A)

async def qwestion6_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION6)
    await state.update_data(answer5=message.text)
    await state.set_state(StepsExam.GET_ANSWER6_A)

async def qwestion7_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION7)
    await state.update_data(answer6=message.text)
    await state.set_state(StepsExam.GET_ANSWER7_A)

async def qwestion8_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION8)
    await state.update_data(answer7=message.text)
    await state.set_state(StepsExam.GET_ANSWER8_A)

async def qwestion9_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION9)
    await state.update_data(answer8=message.text)
    await state.set_state(StepsExam.GET_ANSWER9_A)

async def qwestion10_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION10)
    await state.update_data(answer9=message.text)
    await state.set_state(StepsExam.GET_ANSWER10_A)

async def qwestion11_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION11)
    await state.update_data(answer10=message.text)
    await state.set_state(StepsExam.GET_ANSWER11_A)

async def qwestion12_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION12)
    await state.update_data(answer11=message.text)
    await state.set_state(StepsExam.GET_ANSWER12_A)

async def qwestion13_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION13)
    await state.update_data(answer12=message.text)
    await state.set_state(StepsExam.GET_ANSWER13_A)

async def qwestion14_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION14)
    await state.update_data(answer13=message.text)
    await state.set_state(StepsExam.GET_ANSWER14_A)

async def qwestion15_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION15)
    await state.update_data(answer14=message.text)
    await state.set_state(StepsExam.GET_ANSWER15_A)

async def qwestion16_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION16)
    await state.update_data(answer15=message.text)
    await state.set_state(StepsExam.GET_ANSWER16_A)

async def qwestion17_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION17)
    await state.update_data(answer16=message.text)
    await state.set_state(StepsExam.GET_ANSWER17_A)

async def qwestion18_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION18)
    await state.update_data(answer17=message.text)
    await state.set_state(StepsExam.GET_ANSWER18_A)

async def qwestion19_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION19)
    await state.update_data(answer18=message.text)
    await state.set_state(StepsExam.GET_ANSWER19_A)

async def qwestion20_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION20)
    await state.update_data(answer19=message.text)
    await state.set_state(StepsExam.GET_ANSWER20_A)

async def qwestion21_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION21)
    await state.update_data(answer20=message.text)
    await state.set_state(StepsExam.GET_ANSWER21_A)

async def qwestion22_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION22)
    await state.update_data(answer21=message.text)
    await state.set_state(StepsExam.GET_ANSWER22_A)

async def qwestion23_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION23)
    await state.update_data(answer22=message.text)
    await state.set_state(StepsExam.GET_ANSWER23_A)

async def qwestion24_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION24)
    await state.update_data(answer23=message.text)
    await state.set_state(StepsExam.GET_ANSWER24_A)

async def qwestion25_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION25)
    await state.update_data(answer24=message.text)
    await state.set_state(StepsExam.GET_ANSWER25_A)

async def qwestion26_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION26)
    await state.update_data(answer25=message.text)
    await state.set_state(StepsExam.GET_ANSWER26_A)

async def qwestion27_A(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/27A.png")
    await message.answer_photo(image, caption=QuestionsA.QUESTION27)
    # await message.answer(QuestionsA.QUESTION27)
    await state.update_data(answer26=message.text)
    await state.set_state(StepsExam.GET_ANSWER27_A)

async def qwestion28_A(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/28A.png")
    await message.answer_photo(image, caption=QuestionsA.QUESTION28)
    # await message.answer(QuestionsA.QUESTION28)
    await state.update_data(answer27=message.text)
    await state.set_state(StepsExam.GET_ANSWER28_A)

async def qwestion29_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION29)
    await state.update_data(answer28=message.text)
    await state.set_state(StepsExam.GET_ANSWER29_A)

async def qwestion30_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION30)
    await state.update_data(answer29=message.text)
    await state.set_state(StepsExam.GET_ANSWER30_A)

async def qwestion31_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION31)
    await state.update_data(answer30=message.text)
    await state.set_state(StepsExam.GET_ANSWER31_A)

async def qwestion32_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION32)
    await state.update_data(answer31=message.text)
    await state.set_state(StepsExam.GET_ANSWER32_A)

async def qwestion33_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION33)
    await state.update_data(answer32=message.text)
    await state.set_state(StepsExam.GET_ANSWER33_A)

async def qwestion34_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION34)
    await state.update_data(answer33=message.text)
    await state.set_state(StepsExam.GET_ANSWER34_A)

async def qwestion35_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION35)
    await state.update_data(answer34=message.text)
    await state.set_state(StepsExam.GET_ANSWER35_A)

async def qwestion36_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION36)
    await state.update_data(answer35=message.text)
    await state.set_state(StepsExam.GET_ANSWER36_A)

async def qwestion37_A(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/37A.png")
    await message.answer_photo(image, caption=QuestionsA.QUESTION37)
    # await message.answer(QuestionsA.QUESTION37)
    await state.update_data(answer36=message.text)
    await state.set_state(StepsExam.GET_ANSWER37_A)

async def qwestion38_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION38)
    await state.update_data(answer37=message.text)
    await state.set_state(StepsExam.GET_ANSWER38_A)

async def qwestion39_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION39)
    await state.update_data(answer38=message.text)
    await state.set_state(StepsExam.GET_ANSWER39_A)

async def qwestion40_A(message: Message, state: FSMContext):
    await message.answer(QuestionsA.QUESTION40)
    await state.update_data(answer39=message.text)
    await state.set_state(StepsExam.GET_ANSWER40_A)

async def finish_A(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} экзамен завершен!")
    await state.update_data(answer40=message.text)
    answers = await state.get_data()
    txt = f"Ваш результат:\n" \
    f"Вопрос #1: {await match(str(answers.get('answer1')), AnswersA.ANSWER1)}\n" \
    f"Вопрос #2: {await match(str(answers.get('answer2')), AnswersA.ANSWER2)}\n" \
    f"Вопрос #3: {await match(str(answers.get('answer3')), AnswersA.ANSWER3)}\n" \
    f"Вопрос #4: {await match(str(answers.get('answer4')), AnswersA.ANSWER4)}\n" \
    f"Вопрос #5: {await match(str(answers.get('answer5')), AnswersA.ANSWER5)}\n" \
    f"Вопрос #6: {await match(str(answers.get('answer6')), AnswersA.ANSWER6)}\n" \
    f"Вопрос #7: {await match(str(answers.get('answer7')), AnswersA.ANSWER7)}\n" \
    f"Вопрос #8: {await match(str(answers.get('answer8')), AnswersA.ANSWER8)}\n" \
    f"Вопрос #9: {await match(str(answers.get('answer9')), AnswersA.ANSWER9)}\n" \
    f"Вопрос #10: {await match(str(answers.get('answer10')), AnswersA.ANSWER10)}\n" \
    f"Вопрос #11: {await match(str(answers.get('answer11')), AnswersA.ANSWER11)}\n" \
    f"Вопрос #12: {await match(str(answers.get('answer12')), AnswersA.ANSWER12)}\n" \
    f"Вопрос #13: {await match(str(answers.get('answer13')), AnswersA.ANSWER13)}\n" \
    f"Вопрос #14: {await match(str(answers.get('answer14')), AnswersA.ANSWER14)}\n" \
    f"Вопрос #15: {await match(str(answers.get('answer15')), AnswersA.ANSWER15)}\n" \
    f"Вопрос #16: {await match(str(answers.get('answer16')), AnswersA.ANSWER16)}\n" \
    f"Вопрос #17: {await match(str(answers.get('answer17')), AnswersA.ANSWER17)}\n" \
    f"Вопрос #18: {await match(str(answers.get('answer18')), AnswersA.ANSWER18)}\n" \
    f"Вопрос #19: {await match(str(answers.get('answer19')), AnswersA.ANSWER19)}\n" \
    f"Вопрос #20: {await match(str(answers.get('answer20')), AnswersA.ANSWER20)}\n" \
    f"Вопрос #21: {await match(str(answers.get('answer21')), AnswersA.ANSWER21)}\n" \
    f"Вопрос #22: {await match(str(answers.get('answer22')), AnswersA.ANSWER22)}\n" \
    f"Вопрос #23: {await match(str(answers.get('answer23')), AnswersA.ANSWER23)}\n" \
    f"Вопрос #24: {await match(str(answers.get('answer24')), AnswersA.ANSWER24)}\n" \
    f"Вопрос #25: {await match(str(answers.get('answer25')), AnswersA.ANSWER25)}\n" \
    f"Вопрос #26: {await match(str(answers.get('answer26')), AnswersA.ANSWER26)}\n" \
    f"Вопрос #27: {await match(str(answers.get('answer27')), AnswersA.ANSWER27)}\n" \
    f"Вопрос #28: {await match(str(answers.get('answer28')), AnswersA.ANSWER28)}\n" \
    f"Вопрос #29: {await match(str(answers.get('answer29')), AnswersA.ANSWER29)}\n" \
    f"Вопрос #30: {await match(str(answers.get('answer30')), AnswersA.ANSWER30)}\n" \
    f"Вопрос #31: {await match(str(answers.get('answer31')), AnswersA.ANSWER31)}\n" \
    f"Вопрос #32: {await match(str(answers.get('answer32')), AnswersA.ANSWER32)}\n" \
    f"Вопрос #33: {await match(str(answers.get('answer33')), AnswersA.ANSWER33)}\n" \
    f"Вопрос #34: {await match(str(answers.get('answer34')), AnswersA.ANSWER34)}\n" \
    f"Вопрос #35: {await match(str(answers.get('answer35')), AnswersA.ANSWER35)}\n" \
    f"Вопрос #36: {await match(str(answers.get('answer36')), AnswersA.ANSWER36)}\n" \
    f"Вопрос #37: {await match(str(answers.get('answer37')), AnswersA.ANSWER37)}\n" \
    f"Вопрос #38: {await match(str(answers.get('answer38')), AnswersA.ANSWER38)}\n" \
    f"Вопрос #39: {await match(str(answers.get('answer39')), AnswersA.ANSWER39)}\n" \
    f"Вопрос #40: {await match(str(answers.get('answer40')), AnswersA.ANSWER40)}\n"
    ball = txt.count("Верно") * 2.5
    await message.answer(f"Ваш процент верных ответов: {ball}%")
    await message.answer(txt)
    await state.clear()

async def start_exam_B(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} {QuestionsB.INTRO}")
    await state.set_state(StepsExam.START_EXAM_B)

async def qwestion1_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION1)
    await state.set_state(StepsExam.GET_ANSWER1_B)

async def qwestion2_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION2)
    await state.update_data(answer1=message.text)
    await state.set_state(StepsExam.GET_ANSWER2_B)

async def qwestion3_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION3)
    await state.update_data(answer2=message.text)
    await state.set_state(StepsExam.GET_ANSWER3_B)

async def qwestion4_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION4)
    await state.update_data(answer3=message.text)
    await state.set_state(StepsExam.GET_ANSWER4_B)

async def qwestion5_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION5)
    await state.update_data(answer4=message.text)
    await state.set_state(StepsExam.GET_ANSWER5_B)

async def qwestion6_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION6)
    await state.update_data(answer5=message.text)
    await state.set_state(StepsExam.GET_ANSWER6_B)

async def qwestion7_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION7)
    await state.update_data(answer6=message.text)
    await state.set_state(StepsExam.GET_ANSWER7_B)

async def qwestion8_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION8)
    await state.update_data(answer7=message.text)
    await state.set_state(StepsExam.GET_ANSWER8_B)

async def qwestion9_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION9)
    await state.update_data(answer8=message.text)
    await state.set_state(StepsExam.GET_ANSWER9_B)

async def qwestion10_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION10)
    await state.update_data(answer9=message.text)
    await state.set_state(StepsExam.GET_ANSWER10_B)

async def qwestion11_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION11)
    await state.update_data(answer10=message.text)
    await state.set_state(StepsExam.GET_ANSWER11_B)

async def qwestion12_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION12)
    await state.update_data(answer11=message.text)
    await state.set_state(StepsExam.GET_ANSWER12_B)

async def qwestion13_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION13)
    await state.update_data(answer12=message.text)
    await state.set_state(StepsExam.GET_ANSWER13_B)

async def qwestion14_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION14)
    await state.update_data(answer13=message.text)
    await state.set_state(StepsExam.GET_ANSWER14_B)

async def qwestion15_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION15)
    await state.update_data(answer14=message.text)
    await state.set_state(StepsExam.GET_ANSWER15_B)

async def qwestion16_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION16)
    await state.update_data(answer15=message.text)
    await state.set_state(StepsExam.GET_ANSWER16_B)

async def qwestion17_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION17)
    await state.update_data(answer16=message.text)
    await state.set_state(StepsExam.GET_ANSWER17_B)

async def qwestion18_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION18)
    await state.update_data(answer17=message.text)
    await state.set_state(StepsExam.GET_ANSWER18_B)

async def qwestion19_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION19)
    await state.update_data(answer18=message.text)
    await state.set_state(StepsExam.GET_ANSWER19_B)

async def qwestion20_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION20)
    await state.update_data(answer19=message.text)
    await state.set_state(StepsExam.GET_ANSWER20_B)

async def qwestion21_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION21)
    await state.update_data(answer20=message.text)
    await state.set_state(StepsExam.GET_ANSWER21_B)

async def qwestion22_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION22)
    await state.update_data(answer21=message.text)
    await state.set_state(StepsExam.GET_ANSWER22_B)

async def qwestion23_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION23)
    await state.update_data(answer22=message.text)
    await state.set_state(StepsExam.GET_ANSWER23_B)

async def qwestion24_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION24)
    await state.update_data(answer23=message.text)
    await state.set_state(StepsExam.GET_ANSWER24_B)

async def qwestion25_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION25)
    await state.update_data(answer24=message.text)
    await state.set_state(StepsExam.GET_ANSWER25_B)

async def qwestion26_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION26)
    await state.update_data(answer25=message.text)
    await state.set_state(StepsExam.GET_ANSWER26_B)

async def qwestion27_B(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/27A.png")
    await message.answer_photo(image, caption=QuestionsB.QUESTION27)
    await state.update_data(answer26=message.text)
    await state.set_state(StepsExam.GET_ANSWER27_B)

async def qwestion28_B(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/28A.png")
    await message.answer_photo(image, caption=QuestionsB.QUESTION28)
    await state.update_data(answer27=message.text)
    await state.set_state(StepsExam.GET_ANSWER28_B)

async def qwestion29_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION29)
    await state.update_data(answer28=message.text)
    await state.set_state(StepsExam.GET_ANSWER29_B)

async def qwestion30_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION30)
    await state.update_data(answer29=message.text)
    await state.set_state(StepsExam.GET_ANSWER30_B)

async def qwestion31_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION31)
    await state.update_data(answer30=message.text)
    await state.set_state(StepsExam.GET_ANSWER31_B)

async def qwestion32_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION32)
    await state.update_data(answer31=message.text)
    await state.set_state(StepsExam.GET_ANSWER32_B)

async def qwestion33_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION33)
    await state.update_data(answer32=message.text)
    await state.set_state(StepsExam.GET_ANSWER33_B)

async def qwestion34_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION34)
    await state.update_data(answer33=message.text)
    await state.set_state(StepsExam.GET_ANSWER34_B)

async def qwestion35_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION35)
    await state.update_data(answer34=message.text)
    await state.set_state(StepsExam.GET_ANSWER35_B)

async def qwestion36_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION36)
    await state.update_data(answer35=message.text)
    await state.set_state(StepsExam.GET_ANSWER36_B)

async def qwestion37_B(message: Message, state: FSMContext):
    image = FSInputFile("Core/image/37A.png")
    await message.answer_photo(image, caption=QuestionsB.QUESTION37)
    await state.update_data(answer36=message.text)
    await state.set_state(StepsExam.GET_ANSWER37_B)

async def qwestion38_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION38)
    await state.update_data(answer37=message.text)
    await state.set_state(StepsExam.GET_ANSWER38_B)

async def qwestion39_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION39)
    await state.update_data(answer38=message.text)
    await state.set_state(StepsExam.GET_ANSWER39_B)

async def qwestion40_B(message: Message, state: FSMContext):
    await message.answer(QuestionsB.QUESTION40)
    await state.update_data(answer39=message.text)
    await state.set_state(StepsExam.GET_ANSWER40_B)

async def finish_B(message: Message, state: FSMContext):
    await message.answer(f"{message.from_user.first_name} экзамен завершен!")
    await state.update_data(answer40=message.text)
    answers = await state.get_data()
    txt = f"Ваш результат:\n" \
    f"Вопрос #1: {await match(str(answers.get('answer1')), AnswersB.ANSWER1)}\n" \
    f"Вопрос #2: {await match(str(answers.get('answer2')), AnswersB.ANSWER2)}\n" \
    f"Вопрос #3: {await match(str(answers.get('answer3')), AnswersB.ANSWER3)}\n" \
    f"Вопрос #4: {await match(str(answers.get('answer4')), AnswersB.ANSWER4)}\n" \
    f"Вопрос #5: {await match(str(answers.get('answer5')), AnswersB.ANSWER5)}\n" \
    f"Вопрос #6: {await match(str(answers.get('answer6')), AnswersB.ANSWER6)}\n" \
    f"Вопрос #7: {await match(str(answers.get('answer7')), AnswersB.ANSWER7)}\n" \
    f"Вопрос #8: {await match(str(answers.get('answer8')), AnswersB.ANSWER8)}\n" \
    f"Вопрос #9: {await match(str(answers.get('answer9')), AnswersB.ANSWER9)}\n" \
    f"Вопрос #10: {await match(str(answers.get('answer10')), AnswersB.ANSWER10)}\n" \
    f"Вопрос #11: {await match(str(answers.get('answer11')), AnswersB.ANSWER11)}\n" \
    f"Вопрос #12: {await match(str(answers.get('answer12')), AnswersB.ANSWER12)}\n" \
    f"Вопрос #13: {await match(str(answers.get('answer13')), AnswersB.ANSWER13)}\n" \
    f"Вопрос #14: {await match(str(answers.get('answer14')), AnswersB.ANSWER14)}\n" \
    f"Вопрос #15: {await match(str(answers.get('answer15')), AnswersB.ANSWER15)}\n" \
    f"Вопрос #16: {await match(str(answers.get('answer16')), AnswersB.ANSWER16)}\n" \
    f"Вопрос #17: {await match(str(answers.get('answer17')), AnswersB.ANSWER17)}\n" \
    f"Вопрос #18: {await match(str(answers.get('answer18')), AnswersB.ANSWER18)}\n" \
    f"Вопрос #19: {await match(str(answers.get('answer19')), AnswersB.ANSWER19)}\n" \
    f"Вопрос #20: {await match(str(answers.get('answer20')), AnswersB.ANSWER20)}\n" \
    f"Вопрос #21: {await match(str(answers.get('answer21')), AnswersB.ANSWER21)}\n" \
    f"Вопрос #22: {await match(str(answers.get('answer22')), AnswersB.ANSWER22)}\n" \
    f"Вопрос #23: {await match(str(answers.get('answer23')), AnswersB.ANSWER23)}\n" \
    f"Вопрос #24: {await match(str(answers.get('answer24')), AnswersB.ANSWER24)}\n" \
    f"Вопрос #25: {await match(str(answers.get('answer25')), AnswersB.ANSWER25)}\n" \
    f"Вопрос #26: {await match(str(answers.get('answer26')), AnswersB.ANSWER26)}\n" \
    f"Вопрос #27: {await match(str(answers.get('answer27')), AnswersB.ANSWER27)}\n" \
    f"Вопрос #28: {await match(str(answers.get('answer28')), AnswersB.ANSWER28)}\n" \
    f"Вопрос #29: {await match(str(answers.get('answer29')), AnswersB.ANSWER29)}\n" \
    f"Вопрос #30: {await match(str(answers.get('answer30')), AnswersB.ANSWER30)}\n" \
    f"Вопрос #31: {await match(str(answers.get('answer31')), AnswersB.ANSWER31)}\n" \
    f"Вопрос #32: {await match(str(answers.get('answer32')), AnswersB.ANSWER32)}\n" \
    f"Вопрос #33: {await match(str(answers.get('answer33')), AnswersB.ANSWER33)}\n" \
    f"Вопрос #34: {await match(str(answers.get('answer34')), AnswersB.ANSWER34)}\n" \
    f"Вопрос #35: {await match(str(answers.get('answer35')), AnswersB.ANSWER35)}\n" \
    f"Вопрос #36: {await match(str(answers.get('answer36')), AnswersB.ANSWER36)}\n" \
    f"Вопрос #37: {await match(str(answers.get('answer37')), AnswersB.ANSWER37)}\n" \
    f"Вопрос #38: {await match(str(answers.get('answer38')), AnswersB.ANSWER38)}\n" \
    f"Вопрос #39: {await match(str(answers.get('answer39')), AnswersB.ANSWER39)}\n" \
    f"Вопрос #40: {await match(str(answers.get('answer40')), AnswersB.ANSWER40)}\n"
    ball = txt.count("Верно") * 2.5
    await message.answer(f"Ваш процент верных ответов: {ball}%")
    await message.answer(txt)
    await state.clear()