import time
import discord
import asyncio
from discord.ext import tasks, commands


TOKEN = 'discod bot toker'
bot = discord.Client()
@bot.event
async def on_ready():
    #you add the id of you channel
    channel = bot.get_channel(777523196387131394)

    await channel.send('test')

    await bot.close()


bot.run(TOKEN)



