from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from keyboards.inline.objects import objects_keyboard_tools, cancel_state_object
from services.states import ObjectAdd
from app import bot
from data.sql_db import add_data_object

router = Router()


@router.callback_query(F.data == 'add_object')
async def start_object(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Start create a new object.\n"
                                 "Come up with a new object name",
                                 reply_markup=cancel_state_object()
                                 )

    await state.set_state(ObjectAdd.get_name)


@router.message(ObjectAdd.get_name)
async def get_name_object(msg: Message, state: FSMContext):
    await msg.answer(f"Object name is \r\n{msg.text}\r\n"
                     "Now add description for object", reply_markup=cancel_state_object())
    await state.update_data(get_name=msg.text)
    await state.set_state(ObjectAdd.get_description)


@router.message(ObjectAdd.get_description)
async def get_description_object(msg: Message, state: FSMContext):
    await msg.answer(f"Description of object is \r\n{msg.text}\r\n"
                     "Now add photo for object", reply_markup=cancel_state_object())
    await state.update_data(get_description=msg.text)
    await state.set_state(ObjectAdd.get_photo)


@router.message(ObjectAdd.get_photo)
async def get_photo_object(msg: Message, state: FSMContext):
    try:
        photo = await bot.get_file(msg.photo[-1].file_id)
        await msg.answer(f"Photo is a success save.\n\n"
                         "Now add link for download file of object", reply_markup=cancel_state_object())
        await state.update_data(get_photo=photo.file_id)
        await state.set_state(ObjectAdd.get_link_file)

    except TypeError:
        await msg.answer('Please, download photo!')


@router.message(ObjectAdd.get_link_file)
async def get_link_file_object(msg: Message, state: FSMContext):
    await state.update_data(get_link_file=msg.text)
    context_data = await state.get_data()

    await msg.answer(
        f"Name Object: {context_data['get_name']}\n"
        f"Description: {context_data['get_description']}\n"
        f"Photo ID: {context_data['get_photo']}\n"
        f"Link: {context_data['get_link_file']}",
        reply_markup=cancel_state_object()
    )

    await add_data_object(
        name=context_data['get_name'],
        description=context_data['get_description'],
        photo_id=context_data['get_photo'],
        link_file=context_data['get_link_file']
    )
    await state.clear()


@router.callback_query(F.data == "cancel_state_object")
async def cancel_state(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text("Cancel operation.\n"
                                 "You back in manage object", reply_markup=objects_keyboard_tools())


@router.callback_query(F.data == "back_state_object")
async def back_state_object(call: CallbackQuery, state: FSMContext):
    name_state = "ObjectAdd"
    current_state = await state.get_state()
    if current_state == f"{name_state}:get_name":
        await state.set_data({})
        await state.clear()
        await call.message.edit_text("Back to manage object",
                                     reply_markup=objects_keyboard_tools())
    if current_state == f"{name_state}:get_description":
        await state.set_state(ObjectAdd.get_name)
        data = await state.get_data()
        await call.message.edit_text(f"Edit name {data['get_name']}",
                                     reply_markup=cancel_state_object())
    if current_state == f"{name_state}:get_photo":
        await state.set_state(ObjectAdd.get_description)
        data = await state.get_data()
        await call.message.edit_text(f"Edit description {data['get_description']}",
                                     reply_markup=cancel_state_object())
    if current_state == f"{name_state}:get_link_file":
        await state.set_state(ObjectAdd.get_photo)
        data = await state.get_data()
        await call.message.edit_text(f"Edit old photo with id: {data['get_photo']}",
                                     reply_markup=cancel_state_object())
    else:
        return
