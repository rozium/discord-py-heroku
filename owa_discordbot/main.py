from owa_discordbot import settings
from owa_discordbot.client import OwaClient
from owa_discordbot.database import get_session

client = OwaClient(config=settings.OWA_CONFIG, db=get_session())
client.run()
