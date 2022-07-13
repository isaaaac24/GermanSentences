from main import Base
from sqlalchemy import Column, Integer, String


class Sentence(Base):
    __tablename__ = 'sentences'

    sID = Column(Integer, primary_key=True)
    sentence = Column(String(1000))
    word_count = Column(Integer)
