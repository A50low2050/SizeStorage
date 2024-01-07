from middlewares import settings
from data.postgres.schemas import db, Models


async def connect_db():

    await db.set_bind(settings.POSTGRES_URL)
    await db.gino.create_all()
    await db.pop_bind().close()


async def add_models(name: str, description: str, photo_id: str, link_file: str):
    model = await Models.create(
        name=name,
        description=description,
        photo_id=photo_id,
        link_file=link_file
    )
    return f'Create {model.name} is success'


async def select_all_models():
    models = await Models.query.gino.all()
    return models


async def select_model(model_id):
    model = await Models.query.where(Models.id == model_id).gino.first()
    return model


async def update_model_name(model_id, new_name):
    model = await select_model(model_id)
    await model.update(name=new_name).apply()
    return f'Update model is success'


async def delete_model(model_id):
    model = await Models.delete.where(Models.id == model_id).gino.status()
    return model
