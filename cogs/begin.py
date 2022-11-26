from nextcord.ext import commands
import nextcord
from data import set, category
class ticket_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Begin", style = nextcord.ButtonStyle.green)
  async def ticket(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    msg = await interaction.response.send_message("Loading...", ephemeral = True)
    for channel in interaction.guild.channels:
      if channel.name == f'begin-{interaction.user.id}':
        await interaction.response.send_message(f'You already have a ticket.\n{channel.mention}', ephemeral=True)
        return
    channel = await interaction.guild.create_text_channel(f'begin-{interaction.user.id}', category=interaction.guild.get_channel(category))
    await channel.send(embed=nextcord.Embed(title="The staff will soon be here", description="You will soon make millions with us..", color=0x2ecc71))
    await msg.edit(f"Here's your ticket.\n{channel.mention}")
    msg = await channel.send("@everyone")
    await msg.delete()

class Begin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener("on_ready")
  async def sending(self):
    channel_id = set['begin']
    channel = self.bot.get_channel(channel_id)
    await channel.purge(limit=1)
    view = ticket_buttons()
    await channel.send(embed=nextcord.Embed(title="Join us.", description="Be a futur TNG member.\nMake millions with us.", color = 0x3498db), view=view)
    await view.wait()

def setup(bot):
  bot.add_cog(Begin(bot))
