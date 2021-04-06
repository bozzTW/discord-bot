import discord
from discord.ext import commands
import os

token = os.getenv("DC_TOKEN")
client = discord.Client()

# channel = client.get_channel(828677514184491059)
##################
# channel 不能宣告出來使用 會噴錯 我也不知道為什麼
##################


@client.event
async def on_ready():
    print('>> {0.user} 已經登入 <<'.format(client))
    await client.get_channel(828677514184491059).send(">> 霸氣測試 beta 0.2 <<")


@client.event
async def on_voice_state_update(member, before, after):
    if after.channel is not None:
        await client.get_channel(828677514184491059).send(f"{member} 進來了")
    if after.channel is None:
        await client.get_channel(828677514184491059).send(f"{member} 出來了")


client.run(token)
