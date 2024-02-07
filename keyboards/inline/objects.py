from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.sql.objects.commands import select_all_objects, select_object_db, count_objects
from middlewares.settings import DEFAULT_LIMIT, DEFAULT_OFFSET
from utils.callbackdata import ObjectInfo, Paginator
from utils.limiters import transform_keyboard, pages_limiter


def objects_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add ✍", callback_data="add_object")
    keyboard_builder.button(text="Update 🔄", callback_data="update_object")
    keyboard_builder.button(text="Delete 🗑️", callback_data="delete_object")
    keyboard_builder.button(text="Show 🔎", callback_data="show_object")
    keyboard_builder.button(text="⬅", callback_data="back_profile")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


async def back_to_objects_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='⬅', callback_data='back_objects')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def objects_show_all(
        type_handler: str,
        limit: int = DEFAULT_LIMIT,
        offset: int = DEFAULT_OFFSET,
        counter: int = 2,
        page: int = 1,

):
    keyboard_builder = InlineKeyboardBuilder()
    objects = await select_all_objects(limit=limit, offset=offset)
    #
    current_objects = transform_keyboard(objects)
    pages = await count_objects()
    pages = pages_limiter(pages)

    for object in objects:
        keyboard_builder.button(text=object['name'], callback_data=ObjectInfo(
            type_handler=type_handler,
            name=object['name'],
            unique_id=object['id'],
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

    keyboard_builder.button(text='⬅', callback_data='back_manage_object')
    keyboard_builder.adjust(*current_objects, 3, 1)
    return keyboard_builder.as_markup()


async def get_object(unique_id: int):
    object = await select_object_db(unique_id)
    return object


def cancel_state_object(type_state: str):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="❌", callback_data="cancel_state_object")
    keyboard_builder.button(text="⬅", callback_data=f"back_{type_state}")
    keyboard_builder.adjust(2)

    return keyboard_builder.as_markup()


def update_object_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='update name ✏', callback_data='update_name_obj')
    keyboard_builder.button(text='update description 📚', callback_data='update_description_obj')
    keyboard_builder.button(text='update photo 📸', callback_data='update_photo_obj')
    keyboard_builder.button(text='update file link 📄', callback_data='update_file_link_obj')
    keyboard_builder.button(text='⬅', callback_data='back_manage_object')
    keyboard_builder.adjust(2)
    return keyboard_builder.as_markup()
