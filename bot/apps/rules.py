from discord.utils import get

async def refresh_rules(bot, channel_id, rules):
    rules_channel = await bot.fetch_channel(channel_id)
    async for msg in rules_channel.history():
        await msg.delete()
    rules_msg = await rules_channel.send(rules)
    await rules_msg.add_reaction('👍')

async def accept_rules(reaction, user, rules_channel):
    if str(reaction.message.channel.id) ==  rules_channel:
        role = get(reaction.message.guild.roles, name='Member')
        await user.add_roles(role)
