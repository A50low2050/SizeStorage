# import asyncio
# from unittest.mock import AsyncMock
# import pytest
# from aiogram.filters import BaseFilter
# from aiogram.types import Message
# from middlewares.settings import config
#
# test_id_user = '567172443'
#
#
# class AdminFilter(BaseFilter):
#
#     async def __call__(self, message: Message) -> bool:
#         if message.from_user.id == int(config.bots.admin_id):
#             return True
#
#
# @pytest.mark.asyncio
# async def test_filter_is_admin_true():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#
#     try:
#         admin_filter = AdminFilter()
#
#         message = AsyncMock()
#         message.from_user.id = int(config.bots.admin_id)
#
#         result = await admin_filter(message)
#
#         assert result is True
#     finally:
#         loop.close()
#
#
# @pytest.mark.asyncio
# async def test_filter_is_admin_false():
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#
#     try:
#         admin_filter = AdminFilter()
#
#         message = AsyncMock()
#         message.from_user.id = int(test_id_user)
#
#         result = await admin_filter(message)
#
#         assert result is None
#     finally:
#         loop.close()
