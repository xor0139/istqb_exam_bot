from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Вариант A", callback_data="A")
    keyboard_builder.button(text="Вариант B", callback_data="B")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()