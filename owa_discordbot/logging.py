import logging

from owa_discordbot import settings

FORMAT = "%(asctime)s [%(module)s.%(funcName)s] %(levelname)s : %(message)s"
logging.basicConfig(format=FORMAT)
owa_logger = logging.getLogger("owa_logger")
owa_logger.setLevel(settings.LOG_LEVEL)
