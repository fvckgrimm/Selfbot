import discord
from discord.ext import commands
import json
import asyncio
import requests
import os
from colorama import *

token = json.loads(open("config.json").read())['token']
bot_prefix = json.loads(open("config.json").read())['prefix']

bot = commands.Bot(command_prefix=bot_prefix, self_bot=True)

def show_on():
  os.system('clear')
  print(f"""{Fore.CYAN}
.dP"Y8 88  88 88 888888 888888 Yb  dP     .dP"Y8 888888 88     888888 88""Yb  dP"Yb  888888 
`Ybo." 88  88 88   88     88    YbdP      `Ybo." 88__   88     88__   88__dP dP   Yb   88   
o.`Y8b 888888 88   88     88     8P       o.`Y8b 88""   88  .o 88""   88""Yb Yb   dP   88   
8bodP' 88  88 88   88     88    dP        8bodP' 888888 88ood8 88     88oodP  YbodP    88     
───────────────────────────────────────────────────────────────────────────────────────────
  """ + Fore.RESET)

@bot.event
async def on_ready():
    show_on()
    message = 'logged in as %s' % bot.user
    uid_message = 'user id %s' % bot.user.id
    print(message)
    print(uid_message)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    else:
        raise error

@bot.command(brief='load cmd extensions')
async def load(ctx, extension):
  bot.load_extension(f'cogs.{extension}')

@bot.command(brief='unload cmd extensions')
async def unload(ctx, extension):
  bot.unload_extension(f'cogs.{extension}')

@bot.command(brief='shutdown selfbot')
async def shutdown(ctx):
  try:
    print('shutting down...')
    raise KeyboardInterrupt
  except KeyboardInterrupt:
    print('\nGoodbye! (^_^)／')
    quit()
  

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token, bot=False)
