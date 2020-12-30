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

    text = Column(String(1024))
    lang = Column(Enum(LangEnum))
    question_type = Column(String(32))

    def __str__(self):
        return self.text

    def __repr__(self):
        return f"<Question ({self.id}): [lang: {self.lang.name}, tag: {self.question_type}] {self.text}>"

    @classmethod
    def get_random(cls):
        Question = cls
        return (
            Session.query(Question.text, Question.lang)
            .order_by(func.random())
            .limit(1)
            .first()
        )._asdict()
