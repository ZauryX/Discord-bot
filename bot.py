import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='//')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hi(ctx):

    await ctx.send("@here :smiley: :wave: Hello, dude!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def md(ctx):
    await ctx.send("https://cs11.pikabu.ru/images/big_size_comm/2019-04_4/15554514091733656.png")

@bot.command()
async def an(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/362600663068311554/604012213107425301/iZ77UOIZnEo.jpg")


@bot.command()
async def vid(ctx, a: int):
    await ctx.send(a)


@bot.command()
async def f(ctx):
    embed = discord.Embed(title="F", description="Press f to pay respect", color=0xeee657)
    
   

    await ctx.send(embed=embed)


@bot.command()
async def ban(ctx):
    embed = discord.Embed(title="BAN", description="БАН ТЕБЕ БЛЯ ", color=0xeee657)
    
   

    await ctx.send(embed=embed)




@bot.command()
async def ebe(ctx):
    embed = discord.Embed(title="еъе", description="ЕЪЕ", color=0xeee657)
    
   

    await ctx.send(embed=embed)


@bot.command()
async def nou(ctx):
    embed = discord.Embed(title="nou", description="NO YOU", color=0xeee657)
    
   

    await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="debil", description="debilest bot there is ever.", color=0xeee657)
    
   

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="debil bot", description="A Very debil bot. List of commands are:", color=0xeee657)

    embed.add_field(name="//hi", value="Gives a nice greet message", inline=False)
    embed.add_field(name="//cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="//info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="//help", value="Gives this message", inline=False)
    embed.add_field(name="//an", value="anime pic", inline=False)
    embed.add_field(name="//nou", value="nou", inline=False)
    embed.add_field(name="//ebe", value="еъе", inline=False)
    embed.add_field(name="//ban", value="тупо бан", inline=False)


    await ctx.send(embed=embed)

bot.run('NTY5OTQ1NDYzNzU1ODk4OTAw.XTnuyA.Hu7S-HKIrvRc-iOTzFUjPR3YVdc')