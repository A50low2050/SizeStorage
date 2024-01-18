from unittest.mock import AsyncMock
import pytest
from handlers.admin.admin_start import welcome_to_admin
from keyboards.inline.admin_start import admin_keyboard


@pytest.mark.asyncio
async def test_welcome_admin():
    msg = AsyncMock()
    await welcome_to_admin(msg)
    msg.answer.assert_called_with(f'Hello {msg.from_user.first_name} ✌\n'
                                  f'Welcome to admin', reply_markup=admin_keyboard())
