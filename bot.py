# bot.py
import os

import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
from apiclient.discovery import build  # youtube api

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
YOUTUBE_KEY = os.getenv('YOUTUBE_KEY')
VC_CHANNEL_ID =  os.getenv('VC_CHANNEL_ID')

client = discord.Client()

bot = Bot("$") # This is the operator to call the command (!test) 

@bot.command()
async def test(ctx):
    await ctx.send("Command executed")
  

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # channel = client.get_channel(int(VC_CHANNEL_ID))
    # await channel.connect()    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('👾 Why hello, ' + str(message.author))

@bot.command()
async def test2(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))

@bot.command(pass_context=True)
async def play2(ctx):
    print(ctx)
    url = ctx.message.content
    url = url.strip('play2 ')

    # author = ctx.message.author
    # voice_channel = author.voice_channel
    # vc = await client.join_voice_channel(voice_channel)

    channel = client.get_channel(int(VC_CHANNEL_ID))
    vc = await channel.connect()  

    player = await vc.create_ytdl_player(url)
    player.start()

# @client.event
# async def on_message(self, ctx):
#     print(self)
#     print("---------")
#     print(ctx)
#     if self.content.startswith('play'):
#         youtube = build("youtube", "v3", developerKey=YOUTUBE_KEY)
#         search_response = youtube.search().list(q=ctx.message.content.split(
#             ' ', 2)[2], part="id,snippet", maxResults=1, type="video").execute()
#         if len(search_response.get('items')) == 0:
#             await ctx.send("No videos found.")
#         else:
#             vidid = search_response.get('items')[0]['id']['videoId']
#             vidurl = "https://www.youtube.com/watch?v=" + vidid
#             yt_url = "http://www.youtube.com/oembed?url={0}&format=json".format(
#                 vidurl)
#             metadata = await self.get_json(yt_url)
#             data = discord.Embed(
#                 title="**__Search Result__**", colour=discord.Colour(value=11735575))
#             data.add_field(name="Video Title", value=metadata[
#                             'title'], inline=False)
#             data.add_field(name="Video Uploader", value=metadata[
#                             'author_name'], inline=False)
#             data.add_field(name="Video Link",
#                             value=vidurl, inline=False)
#             data.set_image(
#                 url="https://i.ytimg.com/vi/{}/hqdefault.jpg".format(vidid))
#             data.set_footer(
#                 text="Made with \U00002665 by Francis#6565. Support server: https://discord.gg/yp8WpMh")
#             try:
#                 await ctx.send(embed=data)
#                 # statsd.increment('bot.commands.run', 1)
#             except discord.HTTPException:
#                 # statsd.increment('bot.commands.errored', 1)
#                 # logger.exception("Missing embed links perms")
#                 await ctx.send("Looks like the bot doesn't have embed links perms... It kinda needs these, so I'd suggest adding them!")

client.run(TOKEN)