from discord import Embed

from bot import bot
from bot.apps import twitch

@bot.command(name='live')
async def live(ctx, user):
    current_stream = twitch.Stream(user)
    if current_stream.is_live:
        embed = Embed(title=current_stream.title, url=f'https://twitch.tv/{user}')
        embed.set_image(url=current_stream.thumbnail)
        await ctx.send(f'{current_stream.user} is currently live, playing (disabled-for-testing)!', embed=embed)
    else:
        await ctx.send('{user} is not currently live.')
