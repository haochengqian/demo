#-*- coding:utf-8 –*-
import os
from sqlalchemy import Column, String, Integer, Float, create_engine
from sqlalchemy.orm import  sessionmaker
from sqlalchemy.ext.declarative import declarative_base

current_dir = os.path.dirname(os.path.abspath(__file__))
BaseModel = declarative_base()

db_name = os.path.join(current_dir, 'socialNet.sqlite')
engine = create_engine('sqlite:///{}'.format(db_name))

SocialNetSession = sessionmaker(bind=engine)

class Scholar(BaseModel):
    __tablename__ = 'scholar'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    university = Column(String(200), nullable=True)
    department = Column(String(400), nullable=True)

    @classmethod
    def add(cls, id, name, university, department):
        session = SocialNetSession()
        record = cls(id=id, name=name, university=university, department=department)
        session.add(record)
        session.commit()
        return True

    @classmethod
    def select(cls, name):
        session = SocialNetSession()
        query = session.query(cls.id, name)
        result = query.all()
        session.commit()
        return result

class RelationShip(BaseModel):
    __tablename__ = 'relationship'

    rowid = Column(Integer, primary_key=True)
    id1 = Column(Integer, nullable=False)
    id2 = Column(Integer, nullable=False)
    assos1 = Column(String, nullable=True)
    assos2 = Column(String, nullable=True)

    @classmethod
    def add(cls, rowid, id1, id2, assos1, assos2):
        session = SocialNetSession()
        record = cls(rowid=rowid,id1=id1, id2=id2, assos1=assos1, assos2=assos2)
        session.add(record)
        session.commit()
        return True

    @classmethod
    def select(cls, id):
        session = SocialNetSession()
        query = session.query(id)
        result = query.all()
        session.commit()
        return result

def init_socialNet_tables():
    if os.path.exists(db_name):
        os.remove(db_name)

    with open(db_name, 'w') as f:
        pass

    BaseModel.metadata.create_all(bind=engine, tables=[RelationShip.__table__,
                                                       Scholar.__table__])