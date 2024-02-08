import pytest
from gino import Gino
from sqlalchemy import Column, Integer, TEXT, String
from middlewares import settings

db_test = Gino()


class ModelsTest(db_test.Model):
    __tablename__ = 'models_test'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())


async def add_models(name: str, description: str, photo_id: str, link_file: str):
    model = await ModelsTest.create(
        name=name,
        description=description,
        photo_id=photo_id,
        link_file=link_file
    )
    return f'Create model {model.name} is success'


async def select_model(model_id: int):
    model = await ModelsTest.query.where(ModelsTest.id == model_id).gino.first()
    return model


async def delete_model(model_id: int):
    model = await ModelsTest.delete.where(ModelsTest.id == model_id).gino.status()
    return model


async def update_model_name(model_id: int, new_name: str) -> str:
    model = await select_model(model_id)
    await model.update(name=new_name).apply()
    return 'Update name model is success'


async def update_model_description(model_id: int, new_description: str) -> str:
    model = await select_model(model_id)
    await model.update(description=new_description).apply()
    return 'Update description model is success'


async def update_model_photo_id(model_id: int, photo_id: str) -> str:
    model = await select_model(model_id)
    await model.update(photo_id=photo_id).apply()
    return 'Update photo_id model is success'


async def update_model_link(model_id: int, new_link: str) -> str:
    model = await select_model(model_id)
    await model.update(link_file=new_link).apply()
    return 'Update link file model is success'


# Init db
async def start_test_model_db():
    await db_test.set_bind(settings.POSTGRES_URL)
    await db_test.gino.create_all()

    model = await add_models(name='model', description='test model', photo_id='hfuihdu4d3d', link_file='www.test.com')
    return model


# Start Test
@pytest.mark.asyncio
async def test_create_model_db():
    model = await start_test_model_db()
    assert model == f'Create model model is success'
    await ModelsTest.gino.drop()


@pytest.mark.asyncio
async def test_select_model_db():
    await start_test_model_db()
    get_model = await select_model(model_id=1)
    assert get_model is not None

    await ModelsTest.gino.drop()


@pytest.mark.asyncio
async def test_delete_model_db():
    await start_test_model_db()
    model = await delete_model(model_id=1)
    assert model == ('DELETE 1', [])
    await ModelsTest.gino.drop()


@pytest.mark.asyncio
async def test_update_model_db():
    await start_test_model_db()
    update_name = await update_model_name(model_id=1, new_name='update_model')
    update_description = await update_model_description(model_id=1, new_description='test')
    update_photo_id = await update_model_photo_id(model_id=1, photo_id='AWAD56G')
    update_link_file = await update_model_link(model_id=1, new_link='www')
    assert update_name == 'Update name model is success'
    assert update_description == 'Update description model is success'
    assert update_photo_id == 'Update photo_id model is success'
    assert update_link_file == 'Update link file model is success'
    await ModelsTest.gino.drop()
