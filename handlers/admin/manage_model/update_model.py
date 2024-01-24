from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from app import bot
from keyboards.inline.models import (
    update_model_keyboard,
    models_show_all,
    model_keyboard_tools,
    cancel_state_model,
)
from services.states import ModelUpdate
from utils.callbackdata import ModelInfo
from data.sql.commands import (
    update_name_model_db,
    update_description_model_db,
    update_photo_model_db,
    update_file_link_model_db,
)

router = Router()

TYPE_STATE = 'ModelUpdateState'


@router.callback_query(F.data == 'update_model')
async def start_update_model(call: CallbackQuery) -> None:
    markup = update_model_keyboard()
    await call.message.edit_text('What you want to update?', reply_markup=markup)


@router.callback_query(F.data == 'update_name')
async def update_name(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update name', reply_markup=markup)


@router.callback_query(F.data == 'update_description')
async def update_description(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update description', reply_markup=markup)


@router.callback_query(F.data == 'update_photo')
async def update_photo(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update photo', reply_markup=markup)


@router.callback_query(F.data == 'update_file_link')
async def update_file_link(call: CallbackQuery) -> None:
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update file link', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'update_model'))
async def start_update_model_name(call: CallbackQuery, callback_data: ModelInfo, state: FSMContext) -> None:
    unique_id = callback_data.unique_id
    name = callback_data.name

    if call.message.text.lower() == 'update name':
        await state.update_data(unique_id=unique_id)
        await call.message.edit_text(f'Update a old name for {name}', reply_markup=cancel_state_model(TYPE_STATE))
        await state.set_state(ModelUpdate.get_name)

    if call.message.text.lower() == 'update description':
        await state.update_data(unique_id=unique_id)
        await call.message.edit_text(f'Update a old description for {name}',
                                     reply_markup=cancel_state_model(TYPE_STATE))
        await state.set_state(ModelUpdate.get_description)

    if call.message.text.lower() == 'update photo':
        await state.update_data(unique_id=unique_id)
        await call.message.edit_text(f'Update a old photo for {name}', reply_markup=cancel_state_model(TYPE_STATE))
        await state.set_state(ModelUpdate.get_photo_id)

    if call.message.text.lower() == 'update file link':
        await state.update_data(unique_id=unique_id)
        await call.message.edit_text(f'Update a old file link for {name}', reply_markup=cancel_state_model(TYPE_STATE))
        await state.set_state(ModelUpdate.get_file_link)


@router.message(ModelUpdate.get_name)
async def update_name_model(msg: Message, state: FSMContext) -> None:
    await state.update_data(get_name=msg.text)
    context_data = await state.get_data()

    unique_id = context_data['unique_id']
    new_name = context_data['get_name']

    model = await update_name_model_db(unique_id, new_name)
    await msg.answer(model, reply_markup=model_keyboard_tools())
    await state.clear()


@router.message(ModelUpdate.get_description)
async def update_description_model(msg: Message, state: FSMContext) -> None:
    await state.update_data(get_description=msg.text)
    context_data = await state.get_data()

    unique_id = context_data['unique_id']
    new_description = context_data['get_description']

    model = await update_description_model_db(unique_id, new_description)
    await msg.answer(model, reply_markup=model_keyboard_tools())
    await state.clear()


@router.message(ModelUpdate.get_photo_id)
async def update_photo_model(msg: Message, state: FSMContext) -> None:
    try:
        photo = await bot.get_file(msg.photo[-1].file_id)
        await state.update_data(get_photo_id=photo.file_id)
        context_data = await state.get_data()

        unique_id = context_data['unique_id']
        new_photo_id = context_data['get_photo_id']

        model = await update_photo_model_db(unique_id, new_photo_id)
        await msg.answer(model, reply_markup=model_keyboard_tools())
        await state.clear()
    except TypeError:
        await msg.answer('Please, download photo!')


@router.message(ModelUpdate.get_file_link)
async def update_file_link_model(msg: Message, state: FSMContext) -> None:
    await state.update_data(get_file_link=msg.text)
    context_data = await state.get_data()

    unique_id = context_data['unique_id']
    new_file_link = context_data['get_file_link']

    model = await update_file_link_model_db(unique_id, new_file_link)
    await msg.answer(model, reply_markup=model_keyboard_tools())
    await state.clear()


@router.callback_query(F.data == f"back_{TYPE_STATE}")
async def back_state_model_update(call: CallbackQuery, state: FSMContext) -> None:
    name_state = "ModelUpdate"
    current_state = await state.get_state()

    if current_state == f"{name_state}:get_name":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to update manage", reply_markup=update_model_keyboard())
        await call.answer()

    if current_state == f"{name_state}:get_description":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to update manage", reply_markup=update_model_keyboard())
        await call.answer()

    if current_state == f"{name_state}:get_photo_id":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to update manage", reply_markup=update_model_keyboard())
        await call.answer()

    if current_state == f"{name_state}:get_file_link":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to update manage", reply_markup=update_model_keyboard())
        await call.answer()

    else:
        return
