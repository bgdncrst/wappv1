import discord
from discord.ext import commands

# Config
TOKEN = "MTM1NDc2MjM3MTY4Nzc4MDQzMg.GvAj09.tmj7-425MabHcmBj2K6XjcHlCdN__hHzbFDT0E"
ROLE_NAME = "sms1"
CHANNEL_ID = 1354661396012466317

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Botul {bot.user} este online!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    channel = bot.get_channel(CHANNEL_ID)
    role = discord.utils.get(message.author.roles, name=ROLE_NAME)
    
    if message.channel.id == CHANNEL_ID and role:
        formatted_message = f"```\nWhatsApp APP\n{message.author.display_name}  |  {message.author.id}:\n{message.content}\n```"
        await message.delete()
        await channel.send(formatted_message)
    
    await bot.process_commands(message)

bot.run(TOKEN)
