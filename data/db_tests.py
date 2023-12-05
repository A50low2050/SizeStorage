import asyncio
from data.postgress_db import db
from middlewares import settings
from data.postgress_db import (
    connect_db,
    add_models
)


async def start_test():
    print('start test')


async def db_test():
    await start_test()
    await db.set_bind(settings.POSTGRES_URL)
    await db.gino.create_all()
    print('create tables')
    await add_models(
        name='model',
        description='test model',
        photo_id='hfuihdu4d3d',
        link_file='www.test.com'
    )

    # await db.gino.drop_all()
    await db.pop_bind().close()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(db_test())
