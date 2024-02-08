import pytest
from gino import Gino
from sqlalchemy import Column, Integer, TEXT, String
from middlewares import settings

db_test = Gino()


class ObjectsTest(db_test.Model):
    __tablename__ = 'objects_test'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())


async def add_object(name: str, description: str, photo_id: str, link_file: str):
    object_db = await ObjectsTest.create(
        name=name,
        description=description,
        photo_id=photo_id,
        link_file=link_file
    )
    return f'Create object {object_db.name} is success'


async def select_object(object_id: int):
    object_db = await ObjectsTest.query.where(ObjectsTest.id == object_id).gino.first()
    return object_db


async def delete_object(object_id: int):
    object_db = await ObjectsTest.delete.where(ObjectsTest.id == object_id).gino.status()
    return object_db


async def update_object_name(object_id: int, new_name: str) -> str:
    object_db = await select_object(object_id)
    await object_db.update(name=new_name).apply()
    return 'Update name object is success'


async def update_object_description(object_id: int, new_description: str) -> str:
    object_db = await select_object(object_id)
    await object_db.update(description=new_description).apply()
    return 'Update description object is success'


async def update_object_photo_id(object_id: int, photo_id: str) -> str:
    object_db = await select_object(object_id)
    await object_db.update(photo_id=photo_id).apply()
    return 'Update photo_id object is success'


async def update_object_link(object_id: int, new_link: str) -> str:
    object_db = await select_object(object_id)
    await object_db.update(link_file=new_link).apply()
    return 'Update link file object is success'


# Init db
async def start_test_object_db():
    await db_test.set_bind(settings.POSTGRES_URL)
    await db_test.gino.create_all()

    object_db = await add_object(
        name='object',
        description='test object',
        photo_id='hfuihdu4d3d',
        link_file='www.test.com'
    )
    return object_db


@pytest.mark.asyncio
async def test_create_object_db():
    object_db = await start_test_object_db()
    assert object_db == f'Create object object is success'
    await ObjectsTest.gino.drop()


@pytest.mark.asyncio
async def test_select_object_db():
    await start_test_object_db()
    get_object = await select_object(object_id=1)
    assert get_object is not None

    await ObjectsTest.gino.drop()


@pytest.mark.asyncio
async def test_delete_object_db():
    await start_test_object_db()
    object_db = await delete_object(object_id=1)
    assert object_db == ('DELETE 1', [])
    await ObjectsTest.gino.drop()


@pytest.mark.asyncio
async def test_update_object_db():
    await start_test_object_db()
    update_name = await update_object_name(object_id=1, new_name='update_object')
    update_description = await update_object_description(object_id=1, new_description='test')
    update_photo_id = await update_object_photo_id(object_id=1, photo_id='AWAD56G')
    update_link_file = await update_object_link(object_id=1, new_link='www')
    assert update_name == 'Update name object is success'
    assert update_description == 'Update description object is success'
    assert update_photo_id == 'Update photo_id object is success'
    assert update_link_file == 'Update link file object is success'
    await ObjectsTest.gino.drop()
