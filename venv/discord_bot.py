import time
import discord
import asyncio
from discord.ext import tasks, commands


TOKEN = 'Nzc3NTM2NTcyNzY5MDQyNDMz.X7E3XA.-84GMFS_mJ95tledHneOthhKcBI'
bot = discord.Client()
@bot.event
async def on_ready():
    channel = bot.get_channel(777523196387131394)

    await channel.send('test')

    await bot.close()


bot.run(TOKEN)



""""
async def io_related(name):
    print(f'{name} started')
    await asyncio.sleep(1)
    print(f'{name} finished')


async def main():
    await asyncio.gather(
        io_related('first'),
        io_related('second'),
    )  # 1s + 1s = over 1s


if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
"""