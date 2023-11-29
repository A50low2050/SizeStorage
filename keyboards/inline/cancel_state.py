from aiogram.utils.keyboard import InlineKeyboardBuilder


def cancel():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Cancel", callback_data="cancel_state")
    keyboard_builder.button(text="Back", callback_data="back_state")
    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()
