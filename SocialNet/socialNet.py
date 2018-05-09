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
    name = Column(String(10), nullable=True)
    university = Column(String, nullable=True)
    department = Column(String, nullable=True)

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

    id = Column(Integer, primary_key=True)
    relation = Column(String, nullable=True)

    @classmethod
    def add(cls, id, relation):
        session = SocialNetSession()
        record = cls(id=id, relation=relation)
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