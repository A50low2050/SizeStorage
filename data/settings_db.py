from data.sql_db import create_db
from data.postgress_db import connect_db


async def set_db(status: str = None):
    if status.lower() == 'testing':
        print('Set and CREATE SQLITE in our bot')
        return await create_db()
    if status.lower() == 'launch':
        print('Set and CREATE POSTGRES in our bot')
        return await connect_db()
    else:
        print('Status not is define')
