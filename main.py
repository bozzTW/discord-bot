import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')
channel = bot.get_channel(828677514184491059)


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Listening to .help"))
    print("I am online")


bot.run("ODI4NjcyNDY3OTQwNjcxNDg4.YGs_YA.SxgSXhvsaWG9-Q7tgLUkkL6Woxg")
