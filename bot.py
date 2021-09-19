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

bot = Bot("!") # This is the operator to call the command (!test) 
game = discord.Game('Mewsic')

@bot.command()
async def test(ctx):
    await ctx.send("Command executed")

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    await bot.change_presence(activity=game)

@bot.listen("on_message")
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('👾 Why hello, ' + str(message.author))

@bot.command()
async def test2(ctx, arg1, arg2):
    await ctx.send('You passed {} and {}'.format(arg1, arg2))

@bot.command(pass_context=True)
async def play(ctx):
    print(ctx)
    url = ctx.message.content
    url = url.strip('play2 ')

    # author = ctx.message.author
    # voice_channel = author.voice_channel
    # vc = await bot.join_voice_channel(voice_channel)

    channel = bot.get_channel(int(VC_CHANNEL_ID))
    vc = await channel.connect()  

    player = await vc.create_ytdl_player(url)
    player.start()

# @bot def on_command_error(ctx, error):
#   if instance(error, commands.CommandNotFound):
#       await ctx.send("invalid")

@bot.command()
async def hey1(ctx, arg1, *, arg2):
    await ctx.send(arg2)

# @bot.event
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

bot.run(TOKEN)