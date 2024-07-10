from misc.gamertag import Gamertag

import discord
import time

bot = discord.Bot()

@bot.event
async def on_ready():
    print('commands loaded, bot is ready.')

@bot.command(description="Bot hosts latency")
async def ping(ctx):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    l = int(bot.latency * 1000)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    new_embed = discord.Embed(
        title="<a:114:1260377863069368452>  Latency Fetched",
        description=f"The bots latency is currently `{str(l)}ms`",
        color=discord.Colour.blurple()
    )
    new_embed.set_footer(icon_url=ctx.author.avatar,text=f'Fetched latency in {str(n)}ms')
    await r.edit(content=None, embed=new_embed)

@bot.command(description="Bot hosts latency")
async def gamertag(ctx, gt: str):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    l = int(bot.latency * 1000)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    if Gamertag.check(gt) == True:
        new_embed = discord.Embed(
        title=f"<a:check:1260385835434377266>  {gt}",
        description=f"Gamertag is available! :D",
        color=discord.Colour.green()
        )
    else:
        new_embed = discord.Embed(
        title=f"<a:x_No:1260385811061411974>  {gt}",
        description=f"Gamertag is not available. :(",
        color=discord.Colour.red()
        )
    new_embed.set_footer(icon_url=ctx.author.avatar,text=f'Checked gamertag in {str(n)}ms')
    await r.edit(content=None, embed=new_embed)

class Bot():
    def __init__(self) -> None:
        pass # init does nothing in this case xd

    @staticmethod
    def start(token: str) -> None:
        bot.run(token)