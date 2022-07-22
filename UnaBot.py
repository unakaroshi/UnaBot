# UnaBot.py
import os
import discord
from discord.ext import commands
import DiceHandler
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.guilds=True
intents.members=True
intents.presences=True
intents.messages=True
intents.guild_messages=True
#intents = discord.Intents( guilds=True,members=True,presences=True)
#intents.
bot = commands.Bot(command_prefix='!', intents=intents)



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
    embed=discord.Embed(title="Help for the fantastic UnaBot", 
                        description=
                        """
                        **__!rd-Command (roll dice)__**
                          Roll a various number (1-100) of n-sided dices.
                          Only DND style dices are allowed (D4, D6, D8, D10, D12, D20 and D100)
                          
                          The parameter consists of the number of dices the letter "d" (for 
                          dice) or "w" (for Würfel) and the number of sides the dices should 
                          have. Here are some examples:
                           !rd 5w6
                           !rd 5d6
                           !rd 8d10
                           !rd 1w100
                           
                        **__!ase-Commond (AttribSchwerExtrem)__**
                        For Cthulu RPG you sometimes need a half or a fifth of the
                        value of you attribute. This function helps you calculate 
                        this. For example:
                           !ase 99
                           !ase 50
                           !ase 66
                        """, 
                        color=0x22A7F0)
    #response = "Try !rd 5w6"
    await ctx.send(embed=embed) 


    
@bot.command(name="rd")
async def rollDice(ctx, arg = None):
    
    available_dice_sides = [4,6,8,10,12,20,100]
    
    dice_number, dice_sides = DiceHandler.parseRollCommand(arg)
    
    if dice_sides not in available_dice_sides:
        await ctx.send("Only D4, D6, D8, D10, D12, D20 and D100 are allowed")
        return
    
    dicerolls = DiceHandler.rollDices(dice_number, dice_sides)
    dice_name = "D{}".format(dice_sides)    
    if dice_number == 1:
        desc = "You've rolled **{}**".format(sum(dicerolls))
    else:
        desc = "{}\n============\n**Total: {}**".format(", ".join(str(elem) for elem in dicerolls), sum(dicerolls))        
                                                        
        
    embed=discord.Embed(title="{} rolls {} {}".format(ctx.author.display_name, dice_number, dice_name), 
                        description=desc,
                        color=0x22A7F0)
    
    await ctx.send(embed=embed)
    

@bot.command(name="ase")
async def ASE(ctx,arg):
    difficult = int(int(arg)//2)
    extrem = int(int(arg)//5)
    await ctx.send("Schwer: {}   Extrem: {}".format(difficult, extrem))
        
        
#@bot.listen()
#async def on_member_update(before, after):   
    
 #   if before.status == after.status                          \
 #           or before.desktop_status == discord.Status.online \
 #           or before.web_status == discord.Status.online     \
 #           or before.mobile_status == discord.Status.online:
#      return
    
 #   if after.desktop_status == discord.Status.online          \
 #           or after.web_status == discord.Status.online      \
 #           or after.mobile_status == discord.Status.online:
                
 #       embed=discord.Embed(title="Hello, **{}**.\r\n".format(after.name), 
 #                       description="Type **!unahelp** to get help.",
 #                       color=0x22A7F0)    
        
 #       await after.create_dm()
 #       await after.dm_channel.send(embed=embed)
       
  
     
bot.run(TOKEN)

