from owa_discordbot.database import engine
from owa_discordbot.database.models import Base

if __name__ == "__main__":
    Base.metadata.create_all(engine)
