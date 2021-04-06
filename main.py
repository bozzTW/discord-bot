import discord
from discord.ext import commands
import os

token = os.getenv("DC_TOKEN")

bot = commands.Bot(command_prefix='[')
channel = bot.get_channel(828677514184491059)

@bot.event
async def on_ready():
    await channel.send('機器人測試')
    print("I am online")

# @bot.event
# async def on_ready():
#     # await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Listening to .help"))
#     print("I am online")


# @bot.event()
# async def on_():
#     channel

bot.run(token)


import discord
from discord.ext import commands
import os

# client = commands.Bot(command_prefix=".")
# token = os.getenv("DC_TOKEN")
#
# @client.event
# async def on_ready() :
#     await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
#     print("I am online")
#
# @client.command()
# async def ping(ctx) :
#     await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")
#
# @client.command(name="whoami")
# async def whoami(ctx) :
#     await ctx.send(f"You are {ctx.message.author.name}")
#
# @client.command()
# async def clear(ctx, amount=3) :
#     await ctx.channel.purge(limit=amount)
#
#
# client.run(token)