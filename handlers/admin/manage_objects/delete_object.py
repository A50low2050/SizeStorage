from aiogram import Router, F
from aiogram.types import CallbackQuery
from data.sql.objects.commands import delete_object_db
from keyboards.inline.objects import objects_show_all, objects_keyboard_tools
from utils.callbackdata import ObjectInfo

router = Router()

TYPE_HANDLER = 'delete_object'


@router.callback_query(F.data == 'delete_object')
async def start_delete_model(call: CallbackQuery) -> None:
    markup = await objects_show_all(type_handler=TYPE_HANDLER)
    await call.message.edit_text('What kind object you want to delete?', reply_markup=markup)


@router.callback_query(ObjectInfo.filter(F.type_handler == TYPE_HANDLER))
async def delete_model(call: CallbackQuery, callback_data: ObjectInfo) -> None:
    unique_id = callback_data.unique_id
    name = callback_data.name

    response = await delete_object_db(unique_id, name)
    await call.message.edit_text(f'{response}', reply_markup=objects_keyboard_tools())
    await call.answer()
