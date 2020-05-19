import discord
import os
from discord.ext import commands
import pickle
import time
from options import *

#v1.1.0

client = commands.Bot(command_prefix = '.', help_command = None)
comptesBanque = pickle.load(open('files/comptesBanqueFile', 'rb'))

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

@client.command()
async def ping(ctx):
    await ctx.send(f'> ***Pong ! {round(client.latency *1000)}ms***')

@client.command()
async def help(ctx):
    await ctx.send ('```py\n" Commandes disponnibles : "```')
    await cxt.send

@client.command()
async def clear(ctx, amount=1000):
    await ctx.channel.purge(limit=amount+1)

'''
------------------------------------------------------------ DEBUG ------------------------------------------------------------
'''

@client.command()
@commands.has_role('Developpeur')
async def comptesbanqueprint(ctx):
    await print (comptesBanque)
    await ctx.send(f'> *Printed*')

'''
------------------------------------------------------------ BANQUE ------------------------------------------------------------
'''
@client.command()
async def money(ctx):
    nameAuthor = str(ctx.author.id)
    if not nameAuthor in comptesBanque:
        comptesBanque[nameAuthor] = startMoneyValue
    await ctx.send (f'> **Hey <@' + nameAuthor + '> , tu as ' + str(comptesBanque[nameAuthor]) + '$**')
    print (nameAuthor)
    pickle.dump(comptesBanque, open('files/comptesBanqueFile', 'wb'))


@client.command()
async def banque(ctx, *arg):
    if len(arg) > 3:
        await ctx.send ("```diff\n- Erreur : Trop d'argument (.banque help)```")
    else:
        if len(arg) == 0:
            await ctx.send ('```diff\n- Erreur : Arguments manquants (.banque help)```')
        else:
            if arg[0] == 'help':
                await ctx.send ('```py\n" Commandes disponnibles : "```')
                await ctx.send ('```css\n.banque help\n.banque set [pseudo] [$]       --> Met le compte de [pseudo] a [$]\n.banque add [pseudo] [$]       --> Ajoute [$] au compte de [pseudo]\n.banque remove [pseudo] [$]    --> Enleve [$] au compte de [pseudo]\n.banque reset [pseudo] [$]     --> Efface le compte de [pseudo]\n.banque view [pseudo]          --> Voir le compte de [pseudo]\n```')
            else:
                pseudo = arg[1]
                pseudo = pseudo.replace('<@!','')
                pseudo = pseudo.replace('>','')

                if arg[0] == 'set':
                    if not pseudo in comptesBanque:
                        comptesBanque[pseudo] = startMoneyValue
                    comptesBanque[pseudo] = int(arg[2])
                    await ctx.send ('<@!' + pseudo + '> a maintenant ' + str(comptesBanque[pseudo]))

                if arg[0] == 'add':
                    if not pseudo in comptesBanque:
                        comptesBanque[pseudo] = startMoneyValue
                    comptesBanque[pseudo] += int(arg[2])
                    await ctx.send ('<@!' + pseudo + '> a maintenant ' + str(comptesBanque[pseudo]))

                if arg[0] == 'remove':
                    if not pseudo in comptesBanque:
                        comptesBanque[pseudo] = startMoneyValue
                    comptesBanque[pseudo] -= int(arg[2])
                    await ctx.send ('<@!' + pseudo + '> a maintenant ' + str(comptesBanque[pseudo]))

                if arg[0] == 'reset':
                    comptesBanque[pseudo] = startMoneyValue
                    await ctx.send ('<@!' + pseudo + '> a maintenant ' + str(comptesBanque[pseudo]))

                if arg[0] == 'view':
                    if not pseudo in comptesBanque:
                        comptesBanque[pseudo] = startMoneyValue
                    await ctx.send ('<@!' + pseudo + '> a ' + str(comptesBanque[pseudo]))

    pickle.dump(comptesBanque, open('files/comptesBanqueFile', 'wb'))

'''
------------------------------------------------------------ TRADE ------------------------------------------------------------
'''

@client.command()
async def trade(ctx, *arg):
    if len(arg) > 3:
        await ctx.send ("```diff\n- Erreur : Trop d'argument (.trade help)```")
    else:
        if len(arg) == 0:
            await ctx.send ('```diff\n- Erreur : Arguments manquants (.trade help)```')
        else:
            if arg[0] == 'help':
                await ctx.send ('```py\n" Commandes disponnibles : "```')
                await ctx.send ('```css\n.trade help\n.trade donner [pseudo] [$]     --> Demande a [pseudo] de trader [$] (pour lui)\n.trade recevoir [pseudo] [$]   --> Demande a [pseudo] de trader [$] (pour moi)\n```')
            else:
                pseudo = arg[1]
                pseudo = pseudo.replace('<@!','')
                pseudo = pseudo.replace('>','')

                if arg[0] == 'set':
                    if not pseudo in comptesBanque:
                        comptesBanque[pseudo] = startMoneyValue
                    comptesBanque[pseudo] = int(arg[2])
                    await ctx.send ('<@!' + pseudo + '> a maintenant ' + str(comptesBanque[pseudo]))



@client.command()
async def report(ctx, someone, *raisons):
    await ctx.channel.purge(limit=1)
    nameAuthor = str(ctx.author.id)
    await ctx.send ('> ' + someone + ' a été report par <@' + nameAuthor + '> pour la raison : *{}*'.format(' '.join(raisons)))

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

client.run('NjYwMTcwMDE2ODY3NzQ1Nzky.XoZDsA.VcQVj69wojesmKrrZ54Ng_fiSgo')


