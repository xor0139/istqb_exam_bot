from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Вариант 1", callback_data="1")
    keyboard_builder.button(text="Вариант 2", callback_data="2")
    keyboard_builder.button(text="Вариант 3", callback_data="3")
    keyboard_builder.button(text="Вариант 4", callback_data="4")
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()