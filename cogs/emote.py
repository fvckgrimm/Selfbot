import discord
from discord.ext import commands
import asyncio
import requests

class emote(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(aliases=['e'], brief='enlargen and get link for emotes')
  async def emoji(self, ctx, emoji: discord.Emoji):
    url = emoji.url
    name = emoji.name
    msg = f'emote name: {name} image url: {url}'
    await ctx.message.edit(content=msg)

  @commands.command(aliases=['ae', 'steal'], brief='add emotes to servers')
  @commands.has_permissions(manage_emojis=True)
  async def addemoji(self, ctx, name, url=None):
    url = url or ctx.message.attachments[0].url
    try:
      response = requests.get(url)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        return await ctx.send(self.bot.command_prefix + "The URL you have provided is invalid.")
    if response.status_code == 404:
        return await ctx.send(self.bot.command_prefix + "The URL you have provided leads to a 404.")
    try:
      img = response.content
      emoji = await ctx.guild.create_custom_emoji(name=name, image=img)
    except discord.InvalidArgument:
        return await ctx.send(self.bot.command_prefix + "Invalid image type. Only PNG, JPEG and GIF are supported.")
    await ctx.send(self.bot.command_prefix + "Successfully added the emoji {0.name} <{1}:{0.name}:{0.id}>!".format(emoji, "a" if emoji.animated else ""))

def setup(bot):
  bot.add_cog(emote(bot))