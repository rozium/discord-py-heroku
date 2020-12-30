from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from owa_discordbot import settings

engine = create_engine(settings.DB_HOST, echo=settings.DEBUG)
Session = sessionmaker(bind=engine)


def get_session():
    """
    Wrapper for invoking sessionmaker
    """
    return Session()
