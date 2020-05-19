import discord
from discord.ext import commands

'''

Status : 
online / idle / offline / invisible

'''

botStatus = discord.Status.online
botActivity = discord.Game('.help')

startMoneyValue = 5000


# ---------------------------------------------------------------------------- #
#                                     Roles                                    #
# ---------------------------------------------------------------------------- #

rAdmin = discord.guild.Role()

rjoueur = 'Joueur'