import csv
import random
from pathlib import Path
from typing import List

import discord

from owa_discordbot.logger import owa_logger


class OwaClient(discord.Client):
    """
    Subclass of discord client for Owa Bot.
    """
    def __init__(self, config=None):
        super().__init__()
        if config is None:
            raise ValueError("No config provided")
        self._config = config
        self._prefix = self._config["prefix"]
        self._questions: List[str] = []
        self._load_question_csv(self._config["csv_dir"])
        self._discord_token = self._config["discord_token"]

    def _load_question_csv(self, csv_dir:str):
        csv_dir = Path(csv_dir)
        with open(csv_dir, "r") as csv_file:
            data = csv.reader(csv_file)
            headers = next(data, None)
            for row in data:
                self._questions.append(row[0])

    async def on_ready(self):
        """
        Client behavior on successful deployment.
        """
        owa_logger.info("Logged in as %s!", self.user)

    async def on_message(self, message):
        """
        Handle user inputs.
        """
        if message.content.startswith(self._prefix):
            cmd = message.content.split(self._prefix)[1]
            if cmd in ["q", "question"]:
                picked_question = random.choice(self._questions)
                await message.channel.send(picked_question)
            elif cmd in ["help", "h"]:
                await message.channel.send(
                    f"-- OwaOwa Bot v0.1 --\n"
                    f"Prefix: `{self._prefix}`\n\n"
                    f"Command:\n`q` for random question\n`h` for help\n\n"
                    f"Example: `{self._prefix}help`"
                )

    def run(self,  *args, **kwargs):
        return super().run(self._discord_token, *args, **kwargs)
