import os
from dotenv import load_dotenv
import discord
from keep_alive import keep_alive
from dankmemespost import get_reddit_post
from discord import Embed

# Token
load_dotenv()
token = os.getenv('TOKEN')

# Import the commands extension to support slash commands
from discord.ext import commands

# Set the activity of the bot
activity = discord.Activity(name='Death Grips',
                            type=discord.ActivityType.listening)

# Make the bot
bot = commands.Bot(command_prefix='!',
                   activity=activity,
                   intents=discord.Intents.all())


@bot.event
async def on_ready():
  '''When the bot is ready, print a message and sync the slash commands'''
  print(f'We have logged in as {bot.user}')
  print('Syncing slash commands...')
  try:
    synced = await bot.tree.sync()
  except Exception as e:
    print(f'Error syncing slash commands: {e}')
  print('Slash commands synced successfully ' + str(len(synced)))


# Slash Commands
@bot.tree.command(name='ping', description='A simple ping command')
async def ping(Interaction: discord.Interaction):
  '''A simple ping command'''
  await Interaction.response.send_message('Pong!')


@bot.tree.command(name='avatar', description='Get a user\'s avatar')
async def avatar(Interaction: discord.Interaction, user: discord.User = None):
  '''Get a user's avatar'''
  if user == None:
    await Interaction.response.send_message(Interaction.user.display_avatar)
  else:
    await Interaction.response.send_message(user.display_avatar)


@bot.tree.command(name='dankmeme',
                  description='A random post from r/dankmemes')
async def dankmeme(Interaction: discord.Interaction):
  '''A random post from r/dankmemes'''
  url, permalink, type, thumbnail = get_reddit_post()
  print(thumbnail)
  embed = Embed(title="Random post from r/dankmeme", color=0x3498db)
  if type == None:
    # GIFs have type none but gifs can't be in embed so if the url ends with .gif we will show thumbnail instead
    if url.endswidth('.gif'):
      embed.set_image(thumbnail)
    else:
      embed.set_image(url=url)
  else:
    embed.set_image(url=thumbnail)
  embed.add_field(name="Original Post", value=f"{permalink}", inline=False)
  await Interaction.response.send_message(embed=embed)


# End Slash Commands


# Legacy Commands
@bot.command(name='avatar', description='Get a user\'s avatar')
async def avatar(res, user: discord.User = None):
  '''Get a user's avatar'''
  if user == None:
    await res.send(res.author.display_avatar)
  else:
    await res.send(user.display_avatar)


@bot.command(name='ping', description='A simple ping command')
async def ping(res):
  '''A simple ping command'''
  await res.send('Pong!')


# End Legacy Commands

# Keep Running
keep_alive()

bot.run(token)
