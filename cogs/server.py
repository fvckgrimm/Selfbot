import discord
from discord.ext import commands
import asyncio

class server(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['sc'], brief='checks the number of servers you\'re in')
  async def servers(self, ctx):
    servers = 'currently in ' + str(len(self.bot.guilds)) + ' servers'
    await ctx.message.edit(content=servers)

  @commands.command(aliases=['ns'], brief= 'creates a new server')
  async def newserv(self, ctx, message=None):
    message = message or 'emote storage'
    await self.bot.create_guild(name=message)

  @commands.command(brief='bans member from server')
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member:discord.User=None, reason=None):
    if member == None or member == ctx.author:
      await ctx.send('You cannot ban yourslef')
      return
    if reason == None:
      reason = 'being stupid'
    message = f'You have been banned from {ctx.guild.name} for {reason}'
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} is banned!")

  @commands.command(brief='kicks members from server')
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member:discord.User=None, reason=None):
    if member == None or member == None:
      await ctx.send('You cannot kick yourself')
      return
    if reason == None:
      reason = 'being stupid'
    message = f'You have been kicked from {ctx.guild.name} for {reason}'
    await member.send(message)
    await ctx.guild.kick(member, reason=reason)
    await ctx.channel.send(f"{member} was kicked!")

  @commands.command(brief='purge messages in a channel')
  @commands.has_permissions(manage_messages=True)
  async def purge(self, ctx, amount=0):
    try:
      await ctx.channel.purge(limit=amount + 1)
    except Exception as e:
      await ctx.send(f'Error: {e}', delete_after=1.5)

def setup(bot):
  bot.add_cog(server(bot))
