from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from app import bot
from services.states import ModelAdd
from data.sql.commands import add_data_model
from keyboards.inline.models import model_keyboard_tools, cancel_state_model
from filters.is_files import FileCheck

router = Router()


@router.callback_query(F.data == "add_model")
async def model_add(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Start create a new model.\n\n"
                                 "Come up with a new model name",
                                 reply_markup=cancel_state_model())

    await state.set_state(ModelAdd.get_name)


@router.message(ModelAdd.get_name)
async def get_name_model(msg: Message, state: FSMContext):
    await msg.answer(f"Model name is {msg.text}\n\n"
                     "Now add description for model",
                     reply_markup=cancel_state_model())
    await state.update_data(get_name=msg.text)
    await state.set_state(ModelAdd.get_description)


@router.message(ModelAdd.get_description)
async def get_description_model(msg: Message, state: FSMContext):
    await msg.answer(f"Description of model is {msg.text}\n\n"
                     "Now add photo for model",
                     reply_markup=cancel_state_model())
    await state.update_data(get_description=msg.text)
    await state.set_state(ModelAdd.get_photo)


@router.message(ModelAdd.get_photo)
async def get_photo_model(msg: Message, state: FSMContext):
    try:
        photo = await bot.get_file(msg.photo[-1].file_id)
        await msg.answer(f"Photo is a success save.\n\n"
                         "Now add link for download file of model",
                         reply_markup=cancel_state_model())
        await state.update_data(get_photo=photo.file_id)
        await state.set_state(ModelAdd.get_link_file)
    except TypeError:
        await msg.answer('Please, download photo!')


@router.message(FileCheck(), ModelAdd.get_link_file)
async def get_link_file_model(msg: Message, state: FSMContext):
    await state.update_data(get_link_file=msg.text)
    context_data = await state.get_data()

    await msg.answer(
        f"Name Model: {context_data['get_name']}\n"
        f"Description: {context_data['get_description']}\n"
        f"Photo ID: {context_data['get_photo']}\n"
        f"Link: {context_data['get_link_file']}",
        reply_markup=model_keyboard_tools()
    )

    await add_data_model(
        name=context_data['get_name'],
        description=context_data['get_description'],
        photo_id=context_data['get_photo'],
        link_file=context_data['get_link_file']
    )
    await state.clear()


@router.callback_query(F.data == "cancel_state_model")
async def cancel_state(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("Cancel operation.\n"
                                 "You back to manage model",
                                 reply_markup=model_keyboard_tools())


@router.callback_query(F.data == "back_state_model")
async def back_state_model(call: CallbackQuery, state: FSMContext):
    name_state = "ModelAdd"
    current_state = await state.get_state()
    if current_state == f"{name_state}:get_name":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to manage model",
                                     reply_markup=model_keyboard_tools())
    if current_state == f"{name_state}:get_description":
        await state.set_state(ModelAdd.get_name)
        data = await state.get_data()
        await call.message.edit_text(f"Edit name {data['get_name']}",
                                     reply_markup=cancel_state_model())
    if current_state == f"{name_state}:get_photo":
        await state.set_state(ModelAdd.get_description)
        data = await state.get_data()
        await call.message.edit_text(f"Edit description {data['get_description']}",
                                     reply_markup=cancel_state_model())
    if current_state == f"{name_state}:get_link_file":
        await state.set_state(ModelAdd.get_photo)
        data = await state.get_data()
        await call.message.edit_text(f"Edit old photo with id: {data['get_photo']}",
                                     reply_markup=cancel_state_model())
    else:
        return
