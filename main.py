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
        index = name.rfind("#")
        name = name[0:index]
    mega_id = 0
    for guild in client.guilds:
        for channel in guild.channels:
            if type(channel) is discord.channel.TextChannel:
                print("Type OK")
                print(channel.name)
                print(channel.id)
                # if channel.name is "機器人通知":
                #     print("Name OK")
                #     mega_id = channel.id
                #     print(mega_id)
                #     break

    if after.channel is not None:
        await client.get_channel(mega_id).send(f"{name}進來了")
    if after.channel is None:
        await client.get_channel(mega_id).send(f"{name}出來了")

client.run(token)
