'''
========= BAP-Bot =========

> BOT DISCORD DU BAP

GitHub : https://github.com/Marty42780/BAP-Bot

Hébergé sur Heroku : https://dashboard.heroku.com/apps/bap-bot
'''

# Modules

import discord
import platform
import os
from discord.ext import commands

# Files

from fonc import *
from options import *
from command import * # Avec le client
from log import *

# alpha 0.1
# 773887468838846504
# Definition du Bot dans commande

if __name__ == "__main__":
    @client.event
    async def on_ready():
        print ("\nNom : " + client.user.name + "    |  id : " + str(client.user.id))
        await client.change_presence(status=botStatus, activity=botActivity)
        print ('status : ' +  str(botStatus) + '  |  activity : ' + str(botActivity))
        print ('\n=========== Bot is ready ===========\n')
        log("Server", "Started Bot", "", platform.node())
    
    client.run(CLIENT_TOKEN)
