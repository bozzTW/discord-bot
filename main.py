import discord
import os

token = os.getenv("DC_TOKEN")
client = discord.Client()

######################################################
# channel = client.get_channel(828677514184491059)
# channel 不能宣告出來使用 會噴錯 我也不知道為什麼
######################################################





# @client.event
# async def on_ready():
#     print('>> {0.user} 已經登入 <<'.format(client))
    # await client.get_channel(828677514184491059).send(">> 霸氣測試 beta 0.2 <<")


@client.event
async def on_voice_state_update(member, before, after):
    name = member.nick
    if name is None:
        name = member
        name = "123"
        # name.rfind(#)
    # if after.channel is not None:
    #     await client.get_channel(828677514184491059).send(f"{name} 進來了")
    # if after.channel is None:
    #     await client.get_channel(828677514184491059).send(f"{name} 出來了")
    for guild in client.guilds:
        for channel in guild.channels:
            print(channel)
            print(type(channel))
            print(channel.name)

client.run(token)
