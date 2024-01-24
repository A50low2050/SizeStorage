from aiogram import Router, F
from aiogram.types import CallbackQuery
from app import bot
from utils.callbackdata import ModelInfo
from keyboards.inline.models import (
    models_show_all,
    get_model,
    model_keyboard_tools,
    back_to_models_keyboard,
)

router = Router()


@router.callback_query(F.data == 'show_model')
async def show_models(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='show_model')
    await call.message.edit_text('Your models', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'show_model'))
async def show_model(call: CallbackQuery, callback_data: ModelInfo) -> None:
    unique_id = callback_data.unique_id
    data = await get_model(unique_id)
    markup = await back_to_models_keyboard()
    await bot.send_photo(chat_id=call.message.chat.id,
                         photo=data['photo_id'],
                         caption=f"Name: {data['name']}\n"
                                 f"Description: {data['description']}\n"
                                 f"Link: {data['link_file']}",
                         reply_markup=markup)
    await call.answer()


@router.callback_query(F.data == 'back_manage')
async def back_category(call: CallbackQuery) -> None:
    await call.message.edit_text('Back to manage', reply_markup=model_keyboard_tools())


@router.callback_query(F.data == 'back_models')
async def back_to_models(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='show_model')
    await call.message.answer('Back to models', reply_markup=markup)
    await call.answer()
