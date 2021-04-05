import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='[')
channel = bot.get_channel(828677514184491059)


@bot.event
async def on_ready():
    await channel.send('機器人測試')


bot.run("ODI4NjcyNDY3OTQwNjcxNDg4.YGs_YA.SxgSXhvsaWG9-Q7tgLUkkL6Woxg")
