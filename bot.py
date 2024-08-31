import discord
from discord.ext import commands
import random
import os


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)




@bot.command()
async def calculator(ctx, operation:str, number1:int, number2:int):
    if operation == "add":
        result = number1 + number2
        await ctx.send(f"The result of the addition is...{result}")
    elif operation == "subtract":
        result = number1 - number2
        await ctx.send(f"The result of the subtraction is...{result}")
    elif operation == "multiply":
        result = number1 * number2
        await ctx.send(f"The result of the multiplication is...{result}")
    elif operation == "divide" and number2 != 0:
        result = number1 / number2
        await ctx.send(f"The result of the division is...{result}")
    else:
        await ctx.send("Cannot complete the operation.")


@bot.command()
async def helpme(ctx):
    await ctx.send(f"Available commands: heh; hello; calculator; meme; meme2; meme_list")


@bot.command()
async def meme(ctx):
    meme_list = ["img/meme1.jpg", "img/meme2.jpg", "img/meme3.jpg"]
    y = random.choice(meme_list)
    with open(y, "rb") as f:
        picture = discord.File(f)
        await ctx.send(file=picture)


@bot.command()
async def meme2(ctx):
    memes_list = os.listdir("img")
    z = random.choice(memes_list)
    with open(f"img/{z}", "rb") as y:
        picture = discord.File(y)
        await ctx.send(file = picture)
@bot.command()
async def meme_list(ctx):
    memes_list = os.listdir("img")
    await ctx.send(f"List of memes: {memes_list}")
    
        


bot.run("Token goes here!")