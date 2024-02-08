from gino import Gino
from sqlalchemy import Column, Integer, TEXT, String

db = Gino()


class Models(db.Model):
    __tablename__ = 'models'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(70))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())


class Objects(db.Model):
    __tablename__ = 'objects'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(70))
    description = Column(TEXT())
    photo_id = Column(TEXT())
    link_file = Column(TEXT())
