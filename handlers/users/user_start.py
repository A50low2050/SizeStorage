from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def welcome_user(message: Message) -> None:
    await message.reply(f'your id: {message.from_user.id}')
