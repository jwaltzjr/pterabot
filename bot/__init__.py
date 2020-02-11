from discord.ext.commands import Bot

bot = Bot(command_prefix='!')

from bot.events import *
from bot.commands import *
