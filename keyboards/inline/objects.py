from aiogram.utils.keyboard import InlineKeyboardBuilder
from data.sql.commands import select_all_objects, select_object_db
from utils.callbackdata import ObjectInfo


def objects_keyboard_tools():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Add", callback_data="add_object")
    keyboard_builder.button(text="Update", callback_data="update_object")
    keyboard_builder.button(text="Delete", callback_data="delete_object")
    keyboard_builder.button(text="Show", callback_data="show_object")
    keyboard_builder.button(text="Back", callback_data="back_profile")

    keyboard_builder.adjust(4)
    return keyboard_builder.as_markup()


async def back_to_objects_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='⬅', callback_data='back_objects')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def objects_show_all(type_handler: str):
    keyboard_builder = InlineKeyboardBuilder()
    objects = await select_all_objects()

    for object in objects:
        keyboard_builder.button(text=object['name'], callback_data=ObjectInfo(
            type_handler=type_handler,
            name=object['name'],
            unique_id=object['id'],
        ))
    keyboard_builder.button(text='⬅', callback_data='back_manage_object')
    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


async def get_object(unique_id: int):
    object = await select_object_db(unique_id)
    return object


def cancel_state_object(type_state: str):
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text="Cancel", callback_data="cancel_state_object")
    keyboard_builder.button(text="Back", callback_data=f"back_{type_state}")
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
