import discord
import os
from discord.ext import commands
import pickle
import time
from options import *

#v1.1.0

client = commands.Bot(command_prefix = '.', help_command = None)


def timeLog():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime('[%d/%m/%Y %H:%M:%S]', named_tuple)
    return time_string

@client.event
async def on_ready():
    print (client.user.name)
    print (client.user.id)
    await client.change_presence(status=botStatus, activity=botActivity)
    print ('status : ' +  str(botStatus))
    print ('activity : ' + str(botActivity))
    print ('version : ' + str(version))
    print ('\n====== Bot is ready ======\n')
    logsFile = open ('logs.txt', 'a')
    logsFile.write(timeLog() + ' ===== Bot started =====')
    logsFile.close()



# ---------------------------------------------------------------------------- #
#                               Commandes de base                              #
# ---------------------------------------------------------------------------- #

@client.command()
async def ping(ctx):
    await ctx.send(f'> ***Pong ! {round(client.latency *1000)}ms***')

@client.command()
async def help(ctx):
    await ctx.send ('```py\n" Commandes disponnibles : "```')
    await ctx.send ('')



@client.command()
async def report(ctx, someone, *raisons):
    await ctx.channel.purge(limit=1)
    nameAuthor = str(ctx.author.id)
    await ctx.send ('> ' + someone + ' a été report par <@' + nameAuthor + '> pour la raison : *{}*'.format(' '.join(raisons)))


# ---------------------------------------------------------------------------- #
#                                Commandes admin                               #
# ---------------------------------------------------------------------------- #

# @client.command()
# @commands.has_role(roleFinder(ctx, 11))
# async def clear(ctx, amount=1000):
#     await ctx.channel.purge(limit=amount+1)

# @client.command()
# @commands.has_role(rModération)
# async def mute(ctx):
#     Member = Guild.get_member(a)
#     await Member.edit(roles.append('Mute'))



# ---------------------------------------------------------------------------- #
#                                     DEBUG                                    #
# ---------------------------------------------------------------------------- #



@client.event
async def on_command_error(ctx, error):
    if isinstance (error, commands.MissingRequiredArgument):
        await ctx.send ('```diff\n- Erreur : Arguments manquants```')
    else:
        if isinstance (error, commands.CommandNotFound):
            await ctx.send ('```diff\n- Erreur : Commande inconnue```')
        else:
            if isinstance (error, commands.CheckFailure):
                await ctx.send ('```diff\n- Erreur : Vous n\'avez pas la permissions de faire ça```')
            else:
                pass



client.run('NjYwMTcwMDE2ODY3NzQ1Nzky.XgY9PQ.x6O20NzgpbonuPwKtvknpAgC7NY')
