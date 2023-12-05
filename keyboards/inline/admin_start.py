from aiogram.utils.keyboard import InlineKeyboardBuilder


def admin_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Admin", callback_data="admin_start")

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def admin_panel_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Models", callback_data="manage_model")
    keyboard_builder.button(text="Objects", callback_data="manage_object")

    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()

