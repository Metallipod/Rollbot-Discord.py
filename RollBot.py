#The ID's have been edited out of the source. 
#You must fill in your own ID's from your client, users, and channels for the bot to function. 
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
    my_channel = client.get_channel() #Replace with the channel ID you want the bot to send in.

    dice_roll = random.randrange(1,101)#Modify for the dice roll

    if member == client.get_user(): #Replace with the User ID you want to use.
        if after.channel == client.get_channel(): #Fill in the channel ID in get_channel with the channel you want to check on join. 
            if member == client.get_user(): #Replace with the User ID you want to use.
                await my_channel.send('No whammy, nooo whammmies')
                await my_channel.send(f'`{dice_roll}`')

client.run('') #Replace with your client ID found in Client Secret. 
