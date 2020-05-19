from discord import *
from discord.ext import commands
from discord import Guild
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

rAdmin = Guild.get_role(role_id=712361516531449906)
rModération = Guild.get_role(role_id=712361516531449906)
rjoueur = 'Joueur'