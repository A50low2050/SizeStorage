from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callbackdata import ModelInfo
from data.sql_db import select_all_models, select_model_db


def model_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add", callback_data="add_model")
    keyboard_builder.button(text="Update", callback_data="update_model")
    keyboard_builder.button(text="Delete", callback_data="delete_model")
    keyboard_builder.button(text="Show", callback_data="show_model")
    keyboard_builder.button(text="Back", callback_data="back_profile")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


def back_to_models():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='Back', callback_data='back_models')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def models_show_all():
    keyboard_builder = InlineKeyboardBuilder()
    models = await select_all_models()

    for model in models:
        keyboard_builder.button(text=str(model[1]), callback_data=ModelInfo(name=model[1], unique_id=model[0]))
    keyboard_builder.button(text='Back', callback_data='back_manage')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def get_model(unique_id):
    model = await select_model_db(unique_id)
    return model[0]
