import asyncio
from data.postgress_db import connect_db


async def start_test():
    print('start test')


async def db_test():
    await start_test()
    await connect_db()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(db_test())
