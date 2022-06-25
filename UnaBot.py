# UnaBot.py
import os

from discord.ext import commands
import random
import MessageHandler
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
    response = "Try !gotquote"
    await ctx.send(response) 

@bot.command(name='gotquote')
async def gotquote(ctx):
    response = MessageHandler.generateQuote()
    await ctx.send(response) 
    
@bot.command(name="rd")
async def rollDice(ctx):
    #for elem in ctx.args:
    #    print (elem)    
    parts = ctx.message.content.split()
    if len(parts) != 2:
        await ctx.send("I don't understand")
        return
    
    param = parts[1].upper()        
    parts = param.split("W")
    
    
    
        
    if len(parts) < 2 or len(parts) > 2: 
        await ctx.send("I don't understand")
        return
    
    dice_number = int(parts[0])
    dice_sides = int(parts[1])
        
    
    if (dice_number < 1) or (dice_number > 100):
      await ctx.send("Yeah, try to bug me. (Only Dicenumbers between 1 and 100, please")  
      return
  
    if (dice_sides < 3):
      await ctx.send("How the f... can you build a {} sided dice? Try better next time.".format(dice_sides))
      return
    
    if (dice_sides > 100):
      await ctx.send("How many sides does your dice have? Are you Alex?")  
      return
  
    if dice_number == 1:
      await ctx.send("Your result is: {}".format(random.randrange(1,dice_sides)))
      return
    
    result = 0
    response = "Rolling {} dices...\n\n".format(dice_number)
    for i in range(0,dice_number):
        number =  random.randrange(1,dice_sides)
        response += "{:2d}. Dice: {:3d}\n".format(i+1, number)
        
        result = result + number
      
    response += "--------------\n"
    response += "Total: {:5d}".format(result)
    print (response)    
    await ctx.send(response) 
    
        
    
        
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

