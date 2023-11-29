from aiogram.utils.keyboard import InlineKeyboardBuilder


def objects_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add", callback_data="add")
    keyboard_builder.button(text="Update", callback_data="update")
    keyboard_builder.button(text="Delete", callback_data="delete")
    keyboard_builder.button(text="Back", callback_data="back")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()
