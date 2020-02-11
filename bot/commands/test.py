from bot import bot

@bot.command(name='test')
async def test(ctx):
    await ctx.send('The test was successful!')
