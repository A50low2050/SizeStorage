import asyncio
from data.postgres.schemas import db
from middlewares import settings
from data.postgres.commands import (
    add_models,
    select_all_models,
    select_model,
    delete_model,
    update_model_name,
    update_model_description,
    update_model_photo_id,
    update_model_link,
)


async def start_test():
    print('start test')


async def connect_postgres():
    await db.set_bind(settings.POSTGRES_URL)
    await db.gino.create_all()
    print('Success connect and create table')


async def db_test_conn_and_create():
    await start_test()
    await connect_postgres()
    model = await add_models(
        name='model',
        description='test model',
        photo_id='hfuihdu4d3d',
        link_file='www.test.com'
    )
    print(model)

    await db.pop_bind().close()


async def db_test_delete():
    await db.set_bind(settings.POSTGRES_URL)
    await db.gino.drop_all()
    print('Success delete table')


async def db_test_select_all_models():
    await start_test()
    await connect_postgres()
    models = await select_all_models()
    print(models)
    await db.pop_bind().close()


async def db_test_select_model(model_id):
    await start_test()
    await connect_postgres()
    model = await select_model(model_id)
    print(model)
    await db.pop_bind().close()


async def db_test_delete_model(model_id):
    await start_test()
    await connect_postgres()
    model = await delete_model(model_id)
    print(model)
    await db.pop_bind().close()


async def db_test_update_model_name(model_id, new_name):
    await start_test()
    await connect_postgres()
    model = await update_model_name(model_id, new_name)
    print(model)
    await db.pop_bind().close()


async def db_test_update_model_description(model_id, new_description):
    await start_test()
    await connect_postgres()
    model = await update_model_description(model_id, new_description)
    print(model)
    await db.pop_bind().close()


async def db_test_update_model_photo_id(model_id, photo_id):
    await start_test()
    await connect_postgres()
    model = await update_model_photo_id(model_id, photo_id)
    print(model)
    await db.pop_bind().close()


async def db_test_update_model_link_file(model_id, new_link):
    await start_test()
    await connect_postgres()
    model = await update_model_link(model_id, new_link)
    print(model)
    await db.pop_bind().close()


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

loop.run_until_complete(
   db_test_conn_and_create()
)
