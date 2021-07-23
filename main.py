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
    target_channel = "測試"
    # name = member.nick
    # if name is None:
    #     name = str(member)
    #     index = name.rfind("#")
    #     name = name[0:index]


    # 找到名字是上面設定的的頻道並指派super_id
    super_id = 0
    for guild in client.guilds:
        for channel in guild.channels:
            if type(channel) is discord.channel.TextChannel:
                if channel.name == target_channel:
                    super_id = channel.id
                    break
    embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
    embedVar.add_field(name="Field1", value="hi", inline=False)
    embedVar.add_field(name="Field2", value="hi2", inline=False)
    await client.get_channel(super_id).send(embed=embedVar)
    # await client.get_channel(super_id).send("測試中")

    # if before.channel is None:
    #     await client.get_channel(super_id).send(f"{name}跑去{after.channel.name}了")
    # if before.channel is not None and after.channel is not None:
    #     await client.get_channel(super_id).send(f"{name}還跑去{after.channel.name}了")
    # if after.channel is None:
    #     await client.get_channel(super_id).send(f"{name}出來了")

client.run(token)

