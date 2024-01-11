from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.inline.models import update_model_keyboard, models_show_all
from services.states import ModelUpdate
from utils.callbackdata import ModelInfo

router = Router()


@router.callback_query(F.data == 'update_model')
async def start_update_model(call: CallbackQuery):
    await call.message.edit_text('What you want to update?', reply_markup=update_model_keyboard())


@router.callback_query(F.data == 'update_name')
async def update_name(call: CallbackQuery):
    markup = await models_show_all(type_handler='update_model')
    await call.message.edit_text('update_name', reply_markup=markup)


@router.callback_query(ModelInfo.filter(F.type_handler == 'update_model'))
async def start_update_model_name(call: CallbackQuery, callback_data: ModelInfo, state: FSMContext):
    name = callback_data.name

    await call.message.edit_text(f'Create a new name for {name}')
    await state.set_state(ModelUpdate.get_name)


@router.message(ModelUpdate.get_name)
async def get_update_name_model(msg: Message, state: FSMContext):
    await state.update_data(get_name=msg.text)
    context_data = await state.get_data()
    await msg.answer(context_data['get_name'])
    await state.clear()
