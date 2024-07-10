from misc.gamertag import Gamertag
from misc.whitelist import Whitelist

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

@bot.command(description="Check your account information")
async def account(ctx):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    if Whitelist.check(ctx.author.name,'admin') != True:
        if Whitelist.check(ctx.author.name,'user') == True:
            if Whitelist.check(ctx.author.name,'expiry') != 'expired':
                new_embed = discord.Embed(
                title=f"<a:check:1260385835434377266>  {ctx.author.name} Account",
                description=f"```maxlfg->{Whitelist.check(ctx.author.name,'maxlfg')}\nmaxfollowers->{Whitelist.check(ctx.author.name,'followers')}\nexpiry->{Whitelist.check(ctx.author.name,'expiry')}```",
                color=discord.Colour.green()
                )
            else:
                new_embed = discord.Embed(
                title=f"<a:x_No:1260385811061411974>  Account Expired",
                description=f"```Contact an admin to renew your plan.```",
                color=discord.Colour.red()
                )
        else:
            new_embed = discord.Embed(
            title=f"<a:x_No:1260385811061411974>  No Account Found",
            description=f"```Contact an admin to purchase a plan.```",
            color=discord.Colour.red()
            )
    else:
        new_embed = discord.Embed(
            title=f"<a:check:1260385835434377266>  {ctx.author.name} (Admin)",
            description=f"```maxlfg->Inf\nmaxfollowers->Inf\nexpiry->never```",
            color=discord.Colour.green()
            )
    new_embed.set_footer(icon_url=ctx.author.avatar,text=f'Checked account in {str(n)}ms')
    await r.edit(content=None, embed=new_embed)

@bot.command(description="Add a normal user to the db (admin-only)")
async def adduser(ctx, member: discord.Member, expiry: str, maxlfg: str, maxfollowers: str):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    if Whitelist.check(ctx.author.name,'admin') != True:
        new_embed = discord.Embed(
            title=f"<a:x_No:1260385811061411974>  Unauthorized",
            description=f"```Admin required to run this command.```",
            color=discord.Colour.red()
            )
    else:
        Whitelist.adduser(ctx.author.name,member.name,'user',expiry,maxlfg,maxfollowers)
        new_embed = discord.Embed(
            title=f"<a:check:1260385835434377266>  Added User To Database",
            description=f"```maxlfg->{maxlfg}\nmaxfollowers->{maxfollowers}\nexpiry->{expiry}```",
            color=discord.Colour.green()
            )
    new_embed.set_footer(icon_url=ctx.author.avatar,text=f'Added user in {str(n)}ms')
    await r.edit(content=None, embed=new_embed)

@bot.command(description="Add a admin user to the db (admin-only)")
async def addadmin(ctx, member: discord.Member):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    if Whitelist.check(ctx.author.name,'admin') != True:
        new_embed = discord.Embed(
            title=f"<a:x_No:1260385811061411974>  Unauthorized",
            description=f"```Admin required to run this command.```",
            color=discord.Colour.red()
            )
    else:
        Whitelist.adduser(ctx.author.name,member.name,'admin',None,None,None)
        new_embed = discord.Embed(
            title=f"<a:check:1260385835434377266>  Added Admin To Database",
            description=f"```maxlfg->Inf\nmaxfollowers->Inf\nexpiry->never```",
            color=discord.Colour.green()
            )
    new_embed.set_footer(icon_url=ctx.author.avatar,text=f'Added user in {str(n)}ms')
    await r.edit(content=None, embed=new_embed)

@bot.command(description="Check a gamertags availability")
async def gamertag(ctx, gt: str):
    t = time.time()
    embed = discord.Embed(
        title="<a:loading:1260375960415506453>  Executing Command",
        description="Please wait...",
        color=discord.Colour.blurple()
    )
    r = await ctx.respond(embed=embed)
    n = time.time() - t
    n = '{:.2f}'.format(n)
    if Gamertag.check(gt) == True:
        new_embed = discord.Embed(
        title=f"<a:check:1260385835434377266>  {gt}",
        description=f"Gamertag is available",
        color=discord.Colour.green()
        )
    else:
        new_embed = discord.Embed(
        title=f"<a:x_No:1260385811061411974>  {gt}",
        description=f"Gamertag is not available",
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