from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callbackdata import ModelInfo, Paginator
from utils.limiters import limiter_models, pages_limiter
from data.sql.models.commands import select_all_models, select_model_db, count_models
from middlewares.settings import DEFAULT_LIMIT, DEFAULT_OFFSET


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


def cancel_state_model(type_state: str):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="❌", callback_data="cancel_state_model")
    keyboard_builder.button(text="⬅", callback_data=f"back_{type_state}")
    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()


async def models_show_all(
        type_handler: str,
        limit: int = DEFAULT_LIMIT,
        offset: int = DEFAULT_OFFSET,
        counter: int = 2,
        page: int = 1,
):
    keyboard_builder = InlineKeyboardBuilder()
    models = await select_all_models(limit=limit, offset=offset)
    current_models = limiter_models(models)

    pages = await count_models()
    pages = pages_limiter(pages)

    for model in models:
        keyboard_builder.button(text=model['name'], callback_data=ModelInfo(
            type_handler=type_handler,
            name=model['name'],
            unique_id=model['id'],
        ))

    keyboard_builder.button(text='⬅', callback_data=Paginator(
        action='prev',
        limit=limit,
        offset=offset,
        counter=counter,
        page=page,
        type_handler=type_handler,
    )
                            )
    keyboard_builder.button(text=f'{page}/{pages}', callback_data='show_pages')
    keyboard_builder.button(text='➡', callback_data=Paginator(
        action='next',
        limit=limit,
        offset=offset,
        counter=counter,
        page=page,
        type_handler=type_handler,
    ))

    keyboard_builder.button(text='↩', callback_data='back_manage_model')

    keyboard_builder.adjust(*current_models, 3, 1)

    return keyboard_builder.as_markup()


async def get_model(unique_id: int):
    model = await select_model_db(unique_id)
    return model


def update_model_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='update name ✏', callback_data='update_name')
    keyboard_builder.button(text='update description 📚', callback_data='update_description')
    keyboard_builder.button(text='update photo 📸', callback_data='update_photo')
    keyboard_builder.button(text='update file link 📄', callback_data='update_file_link')
    keyboard_builder.button(text='⬅', callback_data='back_manage_model')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
