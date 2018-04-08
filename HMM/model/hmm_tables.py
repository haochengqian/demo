import os

from sqlalchemy import  Column, String, Integer, Float, create_engine, desc

from sqlalchemy.orm import  sessionmaker

from common import current_dir, BaseModel

db_name = os.path.join(current_dir, 'hmm.sqlite')
engine = create_engine('sqlite:///{}'.format(db_name))
HMMSession = sessionmaker(bind = engine)

class Transition(BaseModel):
    __tablename__ = 'transition'
    id = Column(Integer, primary_key=True)
    previous = Column(String(1), nullable=False)
    behind = Column(String(1), nullable=False)
    probability = Column(Float, nullable=False)

    def add(cls, previous, behind, probability):
        session = HMMSession()
        record = cls(previous=previous, behind=behind, probability=probability)
        session.add(record)
        session.commit()
        return record

    def join_emission(cls, pinyin, character):
        session = HMMSession()
        query = session.query(cls.behind,
                              Emission.probability + cls.probability).\
            join(Emission, Emission.character == cls.behind).\
            filter(cls.previous == character).\
            filter(Emission.pinyin == pinyin).\
            order_by(desc(Emission.probability + cls.probability))
        result = query.first()
        session.commit()
        return result

class Emission(BaseModel):
    __tablename__ = 'emission'
    id = Column(Integer, primary_key=True)
    character = Column(String(1), nullable=False)
    pinyin = Column(String(7), nullable=False)
    probability = Column(Float, nullable=False)

    def add(cls, character, pinyin, probability):
        session = HMMSession()
        record = cls(character=character, pinyin=pinyin, probability=probability)
        session.add(record)
        session.commit()
        return record

    def join_starting(cls, pinyin, limit=10):
        session = HMMSession()
        query = session.query(cls.character,
                              cls.probability + Starting.probability).\
            join(Starting, cls.character == Starting.character).\
            filter(cls.pinyin == pinyin).\
            order_by(desc(cls.probability + Starting.probability)).\
            limit(limit)
        result = query.all()
        session.commit()
        return result

class Starting(BaseModel):
    __tablename__ = 'starting'
    id = Column(Integer, primary_key=True)
    character = Column(String(1), nullable=False)
    probability = Column(Float, nullable=False)

    def add(cls, character, probability):
        session = HMMSession()
        record = cls(character=character, probability=probability)
        session.add(record)
        session.commit()
        return record