
# ! Remove this before publishing code!!
token = "MTA2MjE3MDU2NzU4ODk4NzAyMQ.GuibLT.16tk_pZvPEIL8HdMyrmQdpXhemFcStOa2ovSwo"
# This example requires the 'message_content' intent.

import discord

# Import the commands extension to support slash commands
from discord.ext import commands

# Set the activity of the bot
activity = discord.Activity(name='Ross Crunkle His Toes', type=discord.ActivityType.watching)

# Make the bot
bot = commands.Bot(command_prefix='!', activity=activity, intents=discord.Intents.all())

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

bot.run(token)
