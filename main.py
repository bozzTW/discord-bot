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

######################################################
# Same problem, this could not take outer var into @event
# Whoever knew this please tell me why


# super_id = 0
# for guild in client.guilds:
#     for channel in guild.channels:
#         if type(channel) is discord.channel.TextChannel:
#             if channel.name == "機器人通知":
#                 super_id = channel.id
#                 break
######################################################


@client.event
async def on_voice_state_update(member, before, after):
    name = member.nick
    if name is None:
        name = str(member)
        index = name.rfind("#")
        name = name[0:index]

    super_id = 0
    for guild in client.guilds:
        for channel in guild.channels:
            if type(channel) is discord.channel.TextChannel:
                if channel.name == "機器人通知":
                    super_id = channel.id
                    break

    print(before)
    print(after)

    # if after.channel is not None:
    #     await client.get_channel(super_id).send(f"{name}進來了")
    # if after.channel is None:
    #     await client.get_channel(super_id).send(f"{name}出來了")

client.run(token)
