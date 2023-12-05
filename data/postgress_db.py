from gino import Gino
from middlewares import settings
from sqlalchemy import Column, Integer, TEXT, String

db = Gino()


class Models(db.Model):
    __tablename__ = 'models'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(20))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())


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
