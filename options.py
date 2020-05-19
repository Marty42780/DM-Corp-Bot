from discord import *
from discord.ext import commands
from discord import Guild
'''

Status : 
online / idle / offline / invisible

'''


botStatus = Status.online
botActivity = Game('.help')

startMoneyValue = 5000


# ---------------------------------------------------------------------------- #
#                                     Roles                                    #
# ---------------------------------------------------------------------------- #

def roleFinder(x):
    '''Return all roles for the bot

    Arguments:
        x {[int]} -- [identifiant du role]

ROLES :
    Staff : (1)
        Fondateur : 10
        Admin: 11
        Modérateur: 12
        Staff : 19
    
    Everyone : (2)
        Joueur : 
    '''
    
rAdmin = Guild.get_role(role_id=712361516531449906)
rModération = Guild.get_role(role_id=712361516531449906)
rjoueur = 'Joueur'
