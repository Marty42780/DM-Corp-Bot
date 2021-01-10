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

'''
ROLES :
    Staff : (1)
        Fondateur : 10
        Admin: 11
        Modérateur: 12
        Staff : 19
    
    Everyone : (2)
        Joueur : 
'''

def roleFinder(ctx, x):
    '''Retourne le role demandé

    Arguments:
        ctx {} -- [description]
        x {int} -- identifiant du role voir ci-dessus
    '''


    if x == 11:
        return ctx.Guild.get_role(role_id=712361516531449906)
        
    rModération = ctx.Guild.get_role(role_id=712361516531449906)
    rjoueur = 'Joueur'
