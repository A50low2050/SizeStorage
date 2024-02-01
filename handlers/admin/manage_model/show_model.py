from aiogram import Router, F
from aiogram.types import CallbackQuery
from app import bot
from utils.callbackdata import ModelInfo, Paginator
from keyboards.inline.models import (
    models_show_all,
    get_model,
    model_keyboard_tools,
    back_to_models_keyboard,
)
from data.sql.models.commands import count_models
from middlewares.settings import DEFAULT_LIMIT

router = Router()

TYPE_HANDLER = 'show_model'


@router.callback_query(F.data == 'show_model')
async def show_models(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler=TYPE_HANDLER)
    await call.message.edit_text('Your models', reply_markup=markup)


@router.callback_query(Paginator.filter(F.action == 'next'))
async def next_models(call: CallbackQuery, callback_data: Paginator) -> None:
    limit = callback_data.limit
    offset = callback_data.offset

    max_limit = await count_models()

    if limit < max_limit:
        limit += 2
        offset += 1

        markup = await models_show_all(type_handler=TYPE_HANDLER, limit=limit, offset=offset)
        await call.message.edit_text('Your models', reply_markup=markup)
    await call.answer()


@router.callback_query(Paginator.filter(F.action == 'prev'))
async def prev_models(call: CallbackQuery, callback_data: Paginator) -> None:
    limit = callback_data.limit
    offset = callback_data.offset

    min_limit = DEFAULT_LIMIT
    if limit > min_limit:
        limit -= 2
        offset -= 1

        markup = await models_show_all(type_handler=TYPE_HANDLER, limit=limit, offset=offset)
        await call.message.edit_text('Your models', reply_markup=markup)
    await call.answer()


@router.callback_query(ModelInfo.filter(F.type_handler == TYPE_HANDLER))
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


@router.callback_query(F.data == 'back_manage_model')
async def back_category(call: CallbackQuery) -> None:
    await call.message.edit_text('Back to manage model', reply_markup=model_keyboard_tools())


@router.callback_query(F.data == 'back_models')
async def back_to_models(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler=TYPE_HANDLER)
    await call.message.answer('Back to models', reply_markup=markup)
    await call.answer()
