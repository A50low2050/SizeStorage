from gino import Gino
from middlewares import settings
from sqlalchemy import Column, Integer, TEXT, String

db = Gino()


class Models(db.Model):
    __tablename__ = 'models'

    id = Column(Integer(), primary_key=True)
    name = Column(String(20))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())


async def connect_db():

    await db.set_bind(settings.POSTGRES_URL)
    await db.gino.create_all()
    await db.pop_bind().close()
