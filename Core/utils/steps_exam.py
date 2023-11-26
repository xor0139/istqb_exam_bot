from aiogram.fsm.state import StatesGroup, State

class StepsExam(StatesGroup):
    START_EXAM = State()
    GET_ANSWER1 = State()
    GET_ANSWER2 = State()