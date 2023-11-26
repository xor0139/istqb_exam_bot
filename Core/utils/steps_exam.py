from aiogram.fsm.state import StatesGroup, State

class StepsExam(StatesGroup):
    START_EXAM = State()
    GET_ANSWER1 = State()
    GET_ANSWER2 = State()
    GET_ANSWER3 = State()
    GET_ANSWER4 = State()
    GET_ANSWER5 = State()
    GET_ANSWER6 = State()
    GET_ANSWER7 = State()
    GET_ANSWER8 = State()
    GET_ANSWER9 = State()
    GET_ANSWER10 = State()