#The ID's have been edited out of the source. 
#You must fill in your own ID's from your client, users, and channels for the bot to funciton. 

from discord.ext import commands
import random

#This sets the prefix for the .command commands. Change the '.' to whatever you want.
client = commands.Bot(command_prefix = '.')

#Just letting you know in terminal that the bot is online.
@client.event
async def on_ready():
    print('I Am Primed')

#A manual way to get the bot to roll. It will send in whatever channel the command was given that it has permissions for.
@client.command()
async def roll(ctx):
    await ctx.send(random.randrange(1,101))

@client.event
async def on_voice_state_update(member, before, after):
    channel = client.get_channel() #Fill with the channel ID you want the bot to send in.
    if member == client.get_user(): #Fill with the User ID you want to use.
        await channel.send(random.randrange(1,101)) #Modify for the dice roll


client.run('') #Your Client ID goes here
