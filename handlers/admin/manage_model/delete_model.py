from aiogram import Router, F
from aiogram.types import CallbackQuery
from data.sql.commands import delete_model_db
from keyboards.inline.models import models_show_all, model_keyboard_tools
from utils.callbackdata import ModelInfo

router = Router()


@router.callback_query(F.data == 'delete_model')
async def start_delete_model(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='delete_model')
    await call.message.edit_text('What kind model you want to delete?', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'delete_model'))
async def delete_model(call: CallbackQuery, callback_data: ModelInfo) -> None:
    unique_id = callback_data.unique_id
    name = callback_data.name

    response = await delete_model_db(unique_id, name)
    await call.message.edit_text(f'{response}', reply_markup=model_keyboard_tools())
    await call.answer()
