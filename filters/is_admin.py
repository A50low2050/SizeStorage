from aiogram.filters import BaseFilter
from middlewares.settings import config
from aiogram.types import Message


class AdminFilter(BaseFilter):

    async def __call__(self, message: Message):
        if message.from_user.id == int(config.bots.admin_id):
            return True
