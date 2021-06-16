# Modules
import discord
from discord.ext import commands
from discord import guild
import discord.utils


# Files

from options import PREFIX
from log import *
from fonc import russianTranslate
# from module import BAP_Bot

client = commands.Bot(command_prefix=".")

@client.command(name="ping")
async def ping(ctx):
    pingval = str(round(client.latency *1000))
    await ctx.send(f'> ***понг ! ' + pingval + 'ms***')
    log (str(ctx.author), "Pinged", str(ctx.channel), pingval + "ms")

@client.command(name="del")
async def delete(ctx, number: int):
    messages = await ctx.channel.history(limit=number + 1).flatten()
    for each_message in messages:
        await each_message.delete()
    log(str(ctx.author), "Deleted", str(ctx.channel), str(number) + " messages")


@client.command(name="rus")
async def rus(ctx, *arg):
    for unit in arg:
        entreesss = "".join(unit)
    await ctx.message.delete()
    await ctx.send("**" + str(ctx.author.name) + "** : " + russianTranslate(entreesss))
    log(str(ctx.author), "Russianed", "Tranform \"" + entreesss + "\" to Russian")
    
@client.command(name="gulag")
async def gulag(ctx):
    await ctx.message.delete()
    await ctx.send('<@!' + str(ctx.author.id) + '>' + " отправить в ГУЛАГ (SEND TO GULAG)")
    await ctx.send("https://tenor.com/view/of-to-gulag-gif-19230867")
    log(str(ctx.author), "Gulaged", str(ctx.channel), "RUSSIAN")
    

@client.command(name="togulag")
async def togulag(ctx, someoneToSendToGulag):
    theVictimId = someoneToSendToGulag.replace('<@!', '').replace('>', '')
    theVictim = client.get_user(theVictimId)
    gulagRole = discord.utils.get(ctx.guild.roles, id="854351131026260010")
    await client.add_roles(theVictim, gulagRole)