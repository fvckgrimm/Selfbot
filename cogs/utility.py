import discord
from discord.ext import commands
import asyncio
import random

def random_line(fname):
  lines = open(fname).read().splitlines()
  return random.choice(lines)

class utility(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(brief='get api latency')
  async def ping(self, ctx):
    await ctx.message.edit(content=f":ping_pong:`Ping: {round(self.bot.latency * 1000)}ms`")

  @commands.command(aliases=['av'], brief='get avatar link form a user')
  async def avatar(self, ctx, user: discord.User = None):
    if not user:
      user = self.bot.user
    avatar = user.avatar_url_as(static_format='png', size=1024)
    await ctx.send(avatar)

  @commands.command(brief='give x amount of cokies to users in given list')
  async def cookie(self, ctx, amount:int=None):
    try:
      if amount is None:
        await ctx.send(f'Useage: {ctx.prefix}cookie [amount]', delete_after=1.5)
      else:
        for each in range(0,amount):        
          rcookie = random_line('tatsuIDs.txt')
          await ctx.send('t!cookie {id}'.format(id=rcookie))
          await asyncio.sleep(5)
    except Exception as e:
      await ctx.send(f'Error: {e}', delete_after=1.5)

  @commands.command(brief='rep a random tatsu user from a given list')
  async def rep(self, ctx):
    await ctx.message.delete()
    rep = random_line('tatsuIDs.txt')
    await ctx.send(f't!rep {rep}')

  @commands.command(aliases=['cl'], brief='clears own messages from channel history')
  async def clear(self, ctx, amount:int=None):
    if not amount:
      amount = 500
    async for ctx.message in ctx.channel.history(limit=int(amount) + 1):
      if ctx.message.author == self.bot.user:
        if ctx.message.is_system():
          pass
        else:
          await ctx.message.delete()

def setup(bot):
  bot.add_cog(utility(bot))
