from aiogram.utils.keyboard import InlineKeyboardBuilder


def objects_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add", callback_data="add_object")
    keyboard_builder.button(text="Update", callback_data="update_object")
    keyboard_builder.button(text="Delete", callback_data="delete_object")
    keyboard_builder.button(text="Show", callback_data="show_object")
    keyboard_builder.button(text="Back", callback_data="back_profile")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


def cancel_state_object():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Cancel", callback_data="cancel_state_object")
    keyboard_builder.button(text="Back", callback_data="back_state_object")
    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()
