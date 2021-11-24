import random
from . import *
from JARVISBOT.utils import admin_cmd,sudo_cmd,eor
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

ts = "Tony Stark"
jarvis_mention = f"[{DEFAULTUSER or ts}](tg://user?id={TonyStark})"

hello_message = ["Hi Guys","Hi!","Hello There","I Am Back",f"{jarvis_mention} arived!"]
bye_message = ["Bye","I Am Going!",f"{jarvis_mention} going","Adios"]

hello_rand = random.choice(hello_message)
bye_rand = random.choice(bye_message)

@bot.on(admin_cmd(pattern = "hi$",outgoing = True))
@bot.on(sudo_cmd(pattern = "hi$",allow_sudo = True))
async def hi(tony):
  tony.eor(hello_rand)

@bot.on(admin_cmd(pattern = "bye$",outgoing = True))
@bot.on(sudo_cmd(pattern = "bye$",allow_sudo= True))
async def bye(tony):
  tiny.eor(bye_rand)


CmdHelp("greeting").add_command(
   'hi', None, 'some random hello messages'
).add().add_command(
   'bye', None, 'some random bye messages'
).add()
