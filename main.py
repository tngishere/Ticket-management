class bobt:
  def __init__(self, bot):
    self.bot = bot

  async def loadcog(self, fn: str):
    self.bot.load_extension('cogs.' + fn[:-3])

  def run(self, token):
    self.bot.run(token)

from nextcord.ext import commands
from nextcord import Intents
import asyncio
from os import listdir, environ, system
bot = bobt(commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None))
async def main():
  global bot
  tasks: list = []
  for fn in listdir('cogs'):
    if fn.endswith(".py"):
      tasks.append(asyncio.create_task(bot.loadcog(fn)))
  for i in tasks: await i
asyncio.run(main())
bot.run(environ['token'])
