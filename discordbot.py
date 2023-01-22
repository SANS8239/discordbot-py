from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = commands.Bot(command_prefix='/',intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.dnd, activity = discord.Game("멍멍..."))
  


@client.event
async def on_message(message) :
    if "씨발" in message.content :
        await message.delete()
        await message.author.send("욕설 나빠 멍멍")
        await message.logchan.send(em = discord.Embed(title = "멍멍", description = f"{message.author.mention} 욕설사용"))
    elif "병신" in message.content :
        await message.delete()
        await message.author.send("욕설 나빠 멍멍")
        await message.logchan.send(em = discord.Embed(title = "멍멍", description = f"{message.author.mention} 욕설사용"))
    elif "개새끼" in message.content :
        await message.delete()
        await message.author.send("욕설 나빠 멍멍")
        await message.logchan.send(em = discord.Embed(title = "멍멍", description = f"{message.author.mention} 욕설사용"))
    elif "니엄마" in message.content :
        await message.delete()
        await message.author.send("멍멍 너 정지")
        await message.logchan.send(em = discord.Embed(title = "멍멍", description = f"{message.author.mention} 욕설사용"))
    elif "니애미" in message.content :
        await message.delete()
        await message.author.send("멍멍 너 정지")
        await message.logchan.send(em = discord.Embed(title = "멍멍", description = f"{message.author.mention} 욕설사용"))


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
