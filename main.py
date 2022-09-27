import discord
from discord.ext import commands
import os
import random
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.videos = ['https://www.youtube.com/watch?v=V2qH7Rkzq24', 'https://www.youtube.com/watch?v=G92E3FWnHm0', 'https://www.youtube.com/watch?v=0DPZ9b9ZZr4']
bot.happylist = []
@bot.command()
async def hello(ctx):
  await ctx.send("Hello " + ctx.author.display_name)
@bot.command()
async def dog(ctx):
  await ctx.send(random.choice(bot.videos))
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
bot.run('OTU5MjY2OTM4Mzc3MzY3NTUz.GbXRsp.JdyA15XRk93jroxfNtI_2VdWboID31m6DGqW0o')