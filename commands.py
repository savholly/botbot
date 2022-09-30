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
@bot.command(name="hello", help="Greets the user who called the command.")
async def hello(ctx):
  await ctx.send("Hello " + ctx.author.display_name + "!")

@bot.command(name="dog", help="Returns a random image of a dog.")
async def dog(ctx):
  image = get_dog()
  await ctx.send(image)

@bot.command(name="happy", help="Adds what the user types after !happy to a list to be used with !sad, the list resets when the bot is restarted.")
async def happy(ctx, *, item):
  await ctx.send("Awesome!")
  bot.happylist.append(item)
  print(bot.happylist)

@bot.command(name="sad", help="Returns a randomly selected item from the list populated by !happy.")
async def sad(ctx):
  await ctx.send("Hope this makes you feel better!")
  await ctx.send(random.choice(bot.happylist))

@bot.command(name="calc", help="Performs basic 4 function operations.")
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

@bot.command(name="weather", help="Returns the weather for the city requested by the user.")
async def weather(ctx, q: str):
  temp = get_temp(q)
  condition = get_condition(q)
  description = "The weather is " + condition + " in " + q + " today with a temperature of " + str(temp) + " Fahrenheit!"
  await ctx.send(description)

#add capability to play songs off of youtube

@bot.command(name="cat", help="Returns a random image of a cat.")
async def cat(ctx):
  image = get_cat()
  await ctx.send(image)

#returns random breaking bad quote (avery's favorite)
@bot.command(name="avery", help="Avery is my boyfriend, and his favorite show is Breaking Bad. This command returns a random Breaking Bad quote.")
async def avery(ctx):
  quote = get_avery()
  await ctx.send(quote)

@bot.command(name="coin", help="Returns the results of a coin flip.")
async def coin(ctx):
  choice = random.randint(1,2)
  coin = "Heads!"
  if choice == 1:
    coin = "Tails!"
  await ctx.send(coin)

@bot.command(name="dice", help="Returns the results of a dice role, the number of sides is determined by the user.")
async def dice(ctx, n: int):
  num = random.randint(1, n)
  await ctx.send("You rolled a " + str(num) + "!")

@bot.command(name="joke", help="Returns a random joke.")
async def joke(ctx):
  joke = get_joke()
  await ctx.send(joke)

@bot.command(name="meme", help="Returns a random meme.")
async def meme(ctx):
  meme = get_meme()
  await ctx.send(meme)

@bot.command(name="rockpaperscissors", help="Returns the results of a game of rock, paper, scissors with the bot.")
async def rockpaperscissors(ctx, rps: str):
  rps = rps.lower()
  rps_choices = ["rock", "paper", "scissors"]
  bots_rps = random.choice(rps_choices)
  if bots_rps == "rock":
    if rps == "rock":
      await ctx.send("Rock! It's a tie!")
    elif rps == "paper":
      await ctx.send("Rock! You win!")
    elif rps == "scissors":
      await ctx.send("Rock! You lose!")
    else:
      await ctx.send("You must choose rock, paper, or scissors! You lose!")
  elif bots_rps == "paper":
    if rps == "rock":
      await ctx.send("Paper! You lose!")
    elif rps == "paper":
      await ctx.send("Paper! It's a tie!")
    elif rps == "scissors":
      await ctx.send("Paper! You win!")
    else:
      await ctx.send("You must choose rock, paper, or scissors! You lose!")
  elif bots_rps == "scissors":
    if rps == "rock":
      await ctx.send("Scissors! You win!")
    elif rps == "paper":
      await ctx.send("Scissors! You lose!")
    elif rps == "scissors":
      await ctx.send("Scissors! It's a tie!")


TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)