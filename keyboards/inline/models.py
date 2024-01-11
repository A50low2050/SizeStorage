from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callbackdata import ModelInfo
from data.sql.commands import select_all_models, select_model_db


def model_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add ✍", callback_data="add_model")
    keyboard_builder.button(text="Update 🔄", callback_data="update_model")
    keyboard_builder.button(text="Delete 🗑️", callback_data="delete_model")
    keyboard_builder.button(text="Show 🔎", callback_data="show_model")
    keyboard_builder.button(text="⬅", callback_data="back_profile")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


async def back_to_models_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='⬅', callback_data='back_models')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def cancel_state_model():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="❌", callback_data="cancel_state_model")
    keyboard_builder.button(text="⬅", callback_data="back_state_model")
    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()


async def models_show_all(type_handler):
    keyboard_builder = InlineKeyboardBuilder()
    models = await select_all_models()

    for model in models:
        keyboard_builder.button(text=model['name'], callback_data=ModelInfo(
            type_handler=type_handler,
            name=model['name'],
            unique_id=model['id'],
        ))
    keyboard_builder.button(text='⬅', callback_data='back_manage')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def get_model(unique_id):
    model = await select_model_db(unique_id)
    return model
