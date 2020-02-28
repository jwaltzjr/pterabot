from discord.ext.commands import Bot

from config import config

try:
    prefix = config["COMMAND_PREFIX"]
except KeyError:
    prefix = '!' # default

bot = Bot(command_prefix=prefix)

from bot.events import *
from bot.commands import *
