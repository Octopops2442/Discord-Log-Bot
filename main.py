import discord
import datetime
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '|', intents=intents)
array = []

@client.event
async def on_ready():
    print("Jr is online")

    guild = client.get_guild(758354362249510923)
    
    for member in guild.members:
        array.append(member)

@client.command()
async def gName(ctx):
    await ctx.send(client.get_guild)

@client.event
async def on_message(message):
    file = "./Data/" + str(message.author) + ".txt"

    try:
        f = open(file,"a")
        messageContent = message.content
        f.write(messageContent + "\t" + str(datetime.datetime.now()) + "\n")

    except IOError:
        f = open(file,"w+")
        messageContent = message.content
        f.write(messageContent + "\t" + str(datetime.datetime.now()) + "\n")

    finally:
        f.close()


client.run('ODc0NjI1ODQzODQ5MjI0MjEy.YRJsyg.yqq2fbSPT71K1uj9ag3zl0jgjzw')
