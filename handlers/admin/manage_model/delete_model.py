from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline.models import models_show_all
from utils.callbackdata import ModelInfo

router = Router()


@router.callback_query(F.data == 'delete_model')
async def start_delete_model(call: CallbackQuery):
    markup = await models_show_all(type_handler='delete_model')
    await call.message.edit_text('What kind model you want to delete?', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'delete_model'))
async def delete_model(call: CallbackQuery, callback_data: ModelInfo):
    unique_id = callback_data.unique_id
    await call.message.answer(f'id {unique_id}')
    await call.answer()
