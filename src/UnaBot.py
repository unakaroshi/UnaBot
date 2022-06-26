# UnaBot.py
from discord.ext import commands
import DiceHandler

async def unahelpCommand():
    async def unahelp(ctx):
        response = "Try !rd 5W6"
        await ctx.send(response) 

async def memberArrived():
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!\r\nTry **!unahelp** for help.'
    )

async def rollDice():
    async def rollDice(ctx):
        response = DiceHandler.handleDiceRequest(ctx.message.content)
        await ctx.send(response) 
        #for elem in ctx.args:
        #    print (elem)   


    TOKEN = os.getenv('DISCORD_TOKEN')
    #webhook
    https://discord.com/api/webhooks/990623027320483890/aarUd4_oer-m4hpNAuKkJAudYdbM5iPfmLy7YEeBHh5QxG42PJ3DV8f3AX5_9ZdrsY0I
    
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print(f'{bot.user.name} has connected to Discord!')

    @bot.event
    async def on_member_join(member):

    @bot.command(name='unahelp')
    

        
    @bot.command(name="rd")
    async def rollDice(ctx):
        response = DiceHandler.handleDiceRequest(ctx.message.content)
        await ctx.send(response) 
        #for elem in ctx.args:
        #    print (elem)    
    


