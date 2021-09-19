# bot.py
import os

import discord
from dotenv import load_dotenv
from apiclient.discovery import build  # youtube api

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_KEY = os.getenv('YOUTUBE_KEY')
VC_CHANNEL_ID =  os.getenv('VC_CHANNEL_ID')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_ready():
    channel = client.get_channel(VC_CHANNEL_ID)
    await channel.connect()    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('👾 Why hello, ' + str(message.author))

client.run(TOKEN)