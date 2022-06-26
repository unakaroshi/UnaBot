# UnaBot.py
import os

from discord.ext import commands

import DiceHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!\r\nTry **!unahelp** for help.'
    )

@bot.command(name='unahelp')
async def unahelp(ctx):
    response = "Try !rd 5W6"
    await ctx.send(response) 


    
@bot.command(name="rd")
async def rollDice(ctx):
    response = DiceHandler.handleDiceRequest(ctx.message.content)
    await ctx.send(response) 
    #for elem in ctx.args:
    #    print (elem)    
    
        
    
        
@bot.listen()
async def on_member_update(before, after):
    #if before.status == after.status:
    #    return
    print(str(before.joined_at)) # Uhrzeit wann Member gejoint ist
    print(str(before.activities)) # Seine Aktivitäten
    print(str(before.guild)) # Der Server
    print(str(before.nick))# Nicknames
    print(str(before.mobile_status)) # der Mobile Status
    print(str(before.desktop_status)) # der Desktop Status
    print(str(before.web_status)) # Der Web Status
    print(str(before.roles)) # Die Rolle 
     
bot.run(TOKEN)

