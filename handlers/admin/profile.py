from aiogram import Router, F
from aiogram.types import CallbackQuery
from keyboards.inline.admin_start import admin_panel_keyboard
from keyboards.inline.models import model_keyboard_tools
from keyboards.inline.objects import objects_keyboard_tools

router = Router()


@router.callback_query(F.data == "admin_start")
async def admin_profile(call: CallbackQuery):
    await call.message.edit_text("Choose category, please", reply_markup=admin_panel_keyboard())
    await call.answer()


@router.callback_query(F.data == "manage_model")
async def models_tools(call: CallbackQuery):
    await call.message.answer("What do you doing", reply_markup=model_keyboard_tools())
    await call.answer()


@router.callback_query(F.data == "objects")
async def objects_tools(call: CallbackQuery):
    await call.message.edit_text("What do you doing", reply_markup=objects_keyboard_tools())
    await call.answer()


@router.callback_query(F.data == "back_profile")
async def back_profile(call: CallbackQuery):
    await call.message.edit_text('Back to profile', reply_markup=admin_panel_keyboard())
