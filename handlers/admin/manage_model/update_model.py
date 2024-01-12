from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.inline.models import (
    update_model_keyboard,
    models_show_all,
    model_keyboard_tools,
    cancel_state_model,
)
from services.states import ModelUpdate
from utils.callbackdata import ModelInfo
from data.sql.commands import update_name_model_db

router = Router()

TYPE_STATE = 'ModelUpdateState'


@router.callback_query(F.data == 'update_model')
async def start_update_model(call: CallbackQuery):
    markup = update_model_keyboard()
    await call.message.edit_text('What you want to update?', reply_markup=markup)


@router.callback_query(F.data == 'update_name')
async def update_name(call: CallbackQuery):
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update name', reply_markup=markup)


@router.callback_query(F.data == 'update_description')
async def update_description(call: CallbackQuery):
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('Update description', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'update_model'))
async def start_update_model_name(call: CallbackQuery, callback_data: ModelInfo, state: FSMContext):
    unique_id = callback_data.unique_id
    name = callback_data.name

    if call.message.text.lower() == 'update name':
        await state.update_data(unique_id=unique_id)
        await call.message.edit_text(f'Update a old name for {name}', reply_markup=cancel_state_model(TYPE_STATE))
        await state.set_state(ModelUpdate.get_name)

    if call.message.text.lower() == 'update description':
        await call.message.edit_text('update')


@router.message(ModelUpdate.get_name)
async def update_name_model(msg: Message, state: FSMContext):
    await state.update_data(get_name=msg.text)
    context_data = await state.get_data()

    unique_id = context_data['unique_id']
    new_name = context_data['get_name']

    model = await update_name_model_db(unique_id, new_name)
    await msg.answer(model, reply_markup=model_keyboard_tools())
    await state.clear()


@router.callback_query(F.data == f"back_{TYPE_STATE}")
async def back_state_model_update(call: CallbackQuery, state: FSMContext):
    name_state = "ModelUpdate"
    current_state = await state.get_state()
    if current_state == f"{name_state}:get_name":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to manage model",
                                     reply_markup=model_keyboard_tools())
