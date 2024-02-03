from aiogram import Router, F
from aiogram.types import CallbackQuery
from data.sql.models.commands import delete_model_db, count_models
from keyboards.inline.models import models_show_all, model_keyboard_tools
from middlewares.settings import DEFAULT_LIMIT
from utils.callbackdata import ModelInfo, Paginator

router = Router()

TYPE_HANDLER = 'delete_model'


@router.callback_query(F.data == 'delete_model')
async def start_delete_model(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler=TYPE_HANDLER)
    await call.message.edit_text('What kind model you want to delete?', reply_markup=markup)


@router.callback_query(Paginator.filter(F.action.in_(['next', 'prev']) and F.type_handler == TYPE_HANDLER))
async def next_models(call: CallbackQuery, callback_data: Paginator) -> None:
    limit = callback_data.limit
    offset = callback_data.offset
    counter = callback_data.counter
    page = callback_data.page

    if callback_data.action == 'next':
        max_limit = await count_models()
        if counter < max_limit:
            counter += 2
            offset += 2
            page += 1

            markup = await models_show_all(
                type_handler=TYPE_HANDLER,
                limit=limit,
                offset=offset,
                counter=counter,
                page=page,
            )
            await call.message.edit_text('Your models', reply_markup=markup)
            await call.answer()
        else:
            await call.answer()
    if callback_data.action == 'prev':
        min_limit = DEFAULT_LIMIT
        if counter > min_limit:
            counter -= 2
            offset -= 2
            page -= 1

            markup = await models_show_all(
                type_handler=TYPE_HANDLER,
                limit=limit,
                offset=offset,
                counter=counter,
                page=page,
            )
            await call.message.edit_text('Your models', reply_markup=markup)
            await call.answer()
        else:
            await call.answer()


@router.callback_query(ModelInfo.filter(F.type_handler == TYPE_HANDLER))
async def delete_model(call: CallbackQuery, callback_data: ModelInfo) -> None:
    unique_id = callback_data.unique_id
    name = callback_data.name

    response = await delete_model_db(unique_id, name)
    await call.message.edit_text(f'{response}', reply_markup=model_keyboard_tools())
    await call.answer()
