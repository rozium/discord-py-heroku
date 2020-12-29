import enum

from sqlalchemy import (
    Column,
    Integer,
    String,
    Sequence,
    ForeignKey,
    Enum,
    UniqueConstraint,
)
from sqlalchemy.ext.declarative import declarative_base, AbstractConcreteBase

Base = declarative_base()


class BaseModel(AbstractConcreteBase, Base):
    id = Column(Integer, primary_key=True)

    def __repr__(self):
        f"<{self.__class__.__name__} ({self.id})>"


class LangEnum(enum.Enum):
    EN = 1
    ID = 2


class QuestionType(BaseModel):
    __tablename__ = "question_types"

    name = Column(String(32))

    def __repr__(self):
        f"<QuestionType ({self.id}): {self.text} ({self.tag})."


class Questions(BaseModel):
    __tablename__ = "questions"

    text = Column(String(1024))
    lang = Column(Enum(LangEnum))

    def __repr__(self):
        f"<Question ({self.id}): [{self.lang}] {self.text}."


class QuestionTypeMapping(BaseModel):
    __tablename__ = "question_type_mapping"

    question_id = Column(Integer, ForeignKey("questions.id"))
    type_id = Column(Integer, ForeignKey("question_types.id"))

    __table_args__ = (
        UniqueConstraint(
            "question_id",
            "type_id",
            name="_question_type_mapping_uc",
        ),
    )
