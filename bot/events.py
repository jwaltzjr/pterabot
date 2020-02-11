from bot import bot
from bot.apps import rules
from config import config

@bot.event
async def on_ready():
    await rules.refresh_rules(bot, config['RULES_CHANNEL'], config['RULES'])

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    await rules.accept_rules(reaction, user, config['RULES_CHANNEL']) # Add role if emoji is in rules channel
