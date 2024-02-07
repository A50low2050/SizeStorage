from aiogram import Router, F
from aiogram.types import CallbackQuery
from app import bot
from middlewares.settings import DEFAULT_LIMIT
from utils.callbackdata import ObjectInfo, Paginator
from keyboards.inline.objects import (
    objects_keyboard_tools,
    objects_show_all,
    get_object,
    back_to_objects_keyboard,
    count_objects,
)

router = Router()

TYPE_HANDLER = 'show_object'


@router.callback_query(F.data == 'show_object')
async def show_objects(call: CallbackQuery) -> None:
    markup = await objects_show_all(type_handler=TYPE_HANDLER)
    await call.message.edit_text('Your objects', reply_markup=markup)


@router.callback_query(Paginator.filter(F.action.in_(['next', 'prev']) and F.type_handler == TYPE_HANDLER))
async def next_models(call: CallbackQuery, callback_data: Paginator) -> None:
    limit = callback_data.limit
    offset = callback_data.offset
    counter = callback_data.counter
    page = callback_data.page

    if callback_data.action == 'next':
        max_limit = await count_objects()
        if counter < max_limit:
            counter += 2
            offset += 2
            page += 1

            markup = await objects_show_all(
                type_handler=TYPE_HANDLER,
                limit=limit,
                offset=offset,
                counter=counter,
                page=page,
            )
            await call.message.edit_text('Your objects', reply_markup=markup)
            await call.answer()
        else:
            await call.answer()
    if callback_data.action == 'prev':
        min_limit = DEFAULT_LIMIT
        if counter > min_limit:
            counter -= 2
            offset -= 2
            page -= 1

            markup = await objects_show_all(
                type_handler=TYPE_HANDLER,
                limit=limit,
                offset=offset,
                counter=counter,
                page=page,
            )
            await call.message.edit_text('Your objects', reply_markup=markup)
            await call.answer()
        else:
            await call.answer()


@router.callback_query(ObjectInfo.filter(F.type_handler == TYPE_HANDLER))
async def show_model(call: CallbackQuery, callback_data: ObjectInfo) -> None:
    unique_id = callback_data.unique_id
    data = await get_object(unique_id)
    markup = await back_to_objects_keyboard()
    await bot.send_photo(chat_id=call.message.chat.id,
                         photo=data['photo_id'],
                         caption=f"Name: {data['name']}\n"
                                 f"Description: {data['description']}\n"
                                 f"Link: {data['link_file']}",
                         reply_markup=markup)
    await call.answer()


@router.callback_query(F.data == 'back_manage_object')
async def back_category(call: CallbackQuery) -> None:
    await call.message.edit_text('Back to manage object', reply_markup=objects_keyboard_tools())


@router.callback_query(F.data == 'back_objects')
async def back_to_models(call: CallbackQuery) -> None:
    markup = await objects_show_all(type_handler=TYPE_HANDLER)
    await call.message.answer('Back to objects', reply_markup=markup)
    await call.answer()
