import random
from . import *
from JARVISBOT.utils import admin_cmd,sudo_cmd,eor
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

#hello_message = ["Hi Guys","Hi!","Hello There","I Am Back",f"{jarvis_mention} arived!"]
#hello_rand = random.choice(hello_message)

@bot.on(admin_cmd(pattern = "hi",outgoing = True))
@bot.on(sudo_cmd(pattern = "hi",allow_sudo = True))
async def hi(tony):
  tony.eor()
