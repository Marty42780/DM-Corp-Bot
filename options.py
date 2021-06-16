from discord import *
from discord.ext import commands
from discord import Guild
import os

'''
Status : 
online / idle / offline / invisible
'''

CLIENT_TOKEN = os.environ.get('TOKEN')    
PREFIX = "!"
botStatus = Status.online
botActivity = Game('Manger des raviolis')
