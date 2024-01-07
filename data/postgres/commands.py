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
    return f'Update name model is success'


async def update_model_description(model_id, new_description):
    model = await select_model(model_id)
    await model.update(description=new_description).apply()
    return f'Update description model is success'


async def update_model_photo_id(model_id, photo_id):
    model = await select_model(model_id)
    await model.update(photo_id=photo_id).apply()
    return f'Update photo_id model is success'


async def update_model_link(model_id, new_link):
    model = await select_model(model_id)
    await model.update(link_file=new_link).apply()
    return f'Update link file model is success'


async def delete_model(model_id):
    model = await Models.delete.where(Models.id == model_id).gino.status()
    return model
