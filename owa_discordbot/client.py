from typing import List

import discord

from owa_discordbot.logger import owa_logger
from owa_discordbot.database.models import Question


class OwaClient(discord.Client):
    """
    Subclass of discord client for Owa Bot.
    """

    NO_QUESTION_MSG = "Sorry, no question matching your request was found."

    def __init__(self, config=None, db=None):
        super().__init__()
        if config is None:
            raise ValueError("No config provided")
        if db is None:
            raise ValueError("No database connection provided.")
        self._config = config
        self._prefix = self._config["prefix"]
        self._questions: List[str] = []
        self._discord_token = self._config["discord_token"]

    async def on_ready(self):
        """
        Client behavior on successful deployment.
        """
        owa_logger.info("Logged in as %s!", self.user)

    async def _send_help(self, message):
        await message.channel.send(
            f"-- OwaOwa Bot v0.1 --\n"
            f"Prefix: `{self._prefix}`\n\n"
            f"Commands:\n"
            f"- `question [type]`, `q [type]`: Request random question.\n"
            f"\t\tAvailable types: `topic`, `wyr` (would you rather).\n"
            f"- `help`, `h`: Show this message.\n\n"
            f"Example: `{self._prefix}help`"
        )

    async def _send_unknown_cmd(self, complete_cmd, message):
        await message.channel.send(
            f"Unknown command: {complete_cmd}.\n"
            f"Use `{self._prefix} help` to see available commands."
        )

    async def on_message(self, message):
        """
        Handle user inputs.
        """
        if message.content.startswith(self._prefix):
            user_inputs = message.content.split(" ")
            cmd = user_inputs[1]
            if cmd in ["q", "question"]:
                if len(user_inputs) > 3:
                    self._send_help()
                else:
                    try:
                        question = Question.get_random(q_type=user_inputs[2])
                    except IndexError:
                        question = Question.get_random()
                    owa_logger.debug("Queried question: %s", question)
                    if question:
                        await message.channel.send(question.get("text"))
                    else:
                        await message.channel.send(self.NO_QUESTION_MSG)
            elif cmd in ["help", "h"]:
                await self._send_help(message)
            else:
                await self._send_unknown_cmd(cmd, message)

    def run(self, *args, **kwargs):
        return super().run(self._discord_token, *args, **kwargs)
