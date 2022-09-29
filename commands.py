#commands.py
import discord
from discord.ext import commands
import os
import random
from dotenv import load_dotenv
#grab helpers
from helpers import *
load_dotenv('.env')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.happylist = []
@bot.command()
async def hello(ctx):
  await ctx.send("Hello " + ctx.author.display_name + "!")

@bot.command()
async def dog(ctx):
  image = get_dog()
  await ctx.send(image)

@bot.command()
async def happy(ctx, *, item):
  await ctx.send("Awesome!")
  bot.happylist.append(item)
  print(bot.happylist)

@bot.command()
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happylist))

@bot.command()
async def calc(ctx, x: float, fn: str, y: float):
  if fn == "+":
    await ctx.send(x + y)
  elif fn == "-":
    await ctx.send(x - y)
  elif fn == "*":
    await ctx.send(x * y)
  elif fn == "/":
    await ctx.send(x / y)
  else:
    await ctx.send("We only support 4 function operations")

@bot.command()
async def weather(ctx, q: str):
  temp = get_temp(q)
  condition = get_condition(q)
  description = "The weather is " + condition + " in " + q + " today with a temperature of " + str(temp) + " Fahrenheit!"
  await ctx.send(description)

#add capability to play songs off of youtube

@bot.command()
async def cat(ctx):
  image = get_cat()
  await ctx.send(image)

#returns random breaking bad quote (avery's favorite)
@bot.command()
async def avery(ctx):
  quote = get_avery()
  await ctx.send(quote)

@bot.command()
async def coin(ctx):
  choice = random.randint(1,2)
  coin = "Heads!"
  if choice == 1:
    coin = "Tails!"
  await ctx.send(coin)

@bot.command()
async def dice(ctx, n: int):
  num = random.randint(1, n)
  await ctx.send("You rolled a " + str(num) + "!")


TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)