from discord.utils import get

from bot import bot
from config import config

USER_ROLES = config['USER_ROLES']

@bot.command(name='role')
async def role(ctx, *args):
    for arg in args:
        role = get(ctx.guild.roles, name=arg)
        if role:
            if arg in USER_ROLES:
                await ctx.author.add_roles(role)
                await ctx.send(f'Congrats! You now have the {arg} role!')
            else:
                await ctx.send(f'Sorry! You don\'t have permission to assign the {arg} role!')
        else:
            await ctx.send(f'Sorry! I can\'t find the {arg} role! FYI, discord roles are case-sensitive.')

@bot.command(name='rm-role')
async def rm_role(ctx, *args):
    for arg in args:
        role = get(ctx.guild.roles, name=arg)
        if role:
            if role in ctx.author.roles:
                if arg in USER_ROLES:
                    await ctx.author.remove_roles(role)
                    await ctx.send(f'You have removed the {arg} role.')
                else:
                    await ctx.send(f'Sorry! You don\'t have permission to deassign the {arg} role!')
            else:
                await ctx.send(f'Sorry! You don\'t have the {arg} role!')
        else:
            await ctx.send(f'Sorry! I can\'t find the {arg} role! FYI, discord roles are case-sensitive.')
