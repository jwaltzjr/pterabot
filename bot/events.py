from bot import bot
from bot.apps import rules, pokecord
from config import config

RULES = config['RULES']
RULES_CHANNEL = config['RULES_CHANNEL']

@bot.event
async def on_ready():
    await rules.refresh_rules(bot, RULES_CHANNEL, RULES)

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    await bot.process_commands(msg)
    await pokecord.check_message(bot, msg)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return
    await rules.accept_rules(reaction, user, RULES_CHANNEL) # Add role if emoji is in rules channel
