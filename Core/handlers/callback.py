from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from Core.utils.steps_exam import StepsExam


async def select_answer(call: CallbackQuery, state: FSMContext):
    dat = call.data
    await state.set_state(StepsExam.INTRO_A)
