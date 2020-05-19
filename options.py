import discord
from discord.ext import commands
import time

'''
===== VERSIONS =====

1.1.0 : 01/04/2020
    '' serveur discord pas en marche
    '' Première versions pas fini de test

    Updates Mineurs :
    v1.1.0 (02/04/2020) : Logs
==================== 

Status : 
online / idle / offline / invisible

'''

botStatus = discord.Status.online
botActivity = discord.Game('Bonjour le serveur !')

version = 1.1

startMoneyValue = 5000