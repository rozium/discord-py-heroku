import enum

from sqlalchemy import (
    func,
    Column,
    Integer,
    String,
    Sequence,
    ForeignKey,
    Enum,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase

from owa_discordbot.database import get_session

Base = declarative_base()
Session = get_session()


class BaseModel(AbstractConcreteBase, Base):
    id = Column(Integer, primary_key=True, unique=True)

    def __repr__(self):
        return f"<{self.__class__.__name__} ({self.id})>"


class LangEnum(enum.Enum):
    EN = 1
    ID = 2


class Question(BaseModel):
    __tablename__ = "questions"

    DEFAULT_LANG = "EN"

    text = Column(String(1024))
    lang = Column(Enum(LangEnum))
    question_type = Column(String(32))

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"<Question ({self.id}): [lang: {self.lang.name}, type: {self.question_type}] {self.text}>"

    @classmethod
    def get_random(cls, q_type=None, lang=None):
        Question = cls
        if lang is None:
            lang = LangEnum[cls.DEFAULT_LANG]
        else:
            lang = LangEnum[lang.upper()]
        query = Session.query(
            Question.text, Question.lang, Question.question_type
        ).filter(Question.lang == lang)
        if q_type:
            query = query.filter(Question.question_type == q_type)
        result = query.order_by(func.random()).limit(1).first()
        return result._asdict() if result else None
