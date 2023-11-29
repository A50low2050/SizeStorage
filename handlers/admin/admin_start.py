from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from filters.is_admin import AdminFilter
from keyboards.inline.admin_start import admin_keyboard

router = Router()


@router.message(CommandStart(), AdminFilter())
async def welcome_to_admin(msg: Message):
    await msg.answer(f'Hello {msg.from_user.first_name}\n'
                     f'Welcome to admin', reply_markup=admin_keyboard())
