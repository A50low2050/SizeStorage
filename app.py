import asyncio
from aiogram import Bot, Dispatcher
from middlewares.settings import config
from data.sql.commands import create_db
from utils.commands import set_commands

bot = Bot(token=config.bots.bot_token, parse_mode="HTML")
dp = Dispatcher()


async def launch_bot() -> None:
    await set_commands(bot)
    await create_db()

    from handlers.admin import admin_start
    from handlers.admin import profile
    from handlers.admin.manage_model import (
        create_model,
        show_model,
        delete_model,
        update_model,
    )
    from handlers.admin.manage_objects import (
        create_object,
        show_object,
    )

    from handlers.users import user_start

    dp.include_routers(
        admin_start.router,
        user_start.router,
        profile.router,

        create_model.router,
        show_model.router,
        delete_model.router,
        update_model.router,

        create_object.router,
        show_object.router,

    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Launch bot success")
    asyncio.run(launch_bot())
