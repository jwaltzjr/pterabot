from config import config

POKE_CHANNELS = config['POKE_CHANNELS']

async def check_message(bot, msg):
    if msg.content.startswith('p!'):
        if str(msg.channel.id) not in POKE_CHANNELS:
            await msg.channel.send('Are you trying to access Pokecord? '
                'That only works in the Pokecord channels!')
