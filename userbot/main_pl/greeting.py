import random
from . import *
from JARVISBOT.utils import admin_cmd,sudo_cmd,edit_or_reply
from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

ts = "Tony Stark"
jarvis_mention = f"[{JARVIS_USER}](tg://user?id={TonyStark})"

hello_message = ["Hi Guys","Hi!","Hello There","I Am Back",f"{jarvis_mention} arived!"]
bye_message = ["Bye","I Am Going!",f"{jarvis_mention} going","Adios"]

hello_rand = random.choice(hello_message)
bye_rand = random.choice(bye_message)

@bot.on(admin_cmd(pattern = "hi$",outgoing = True))
@bot.on(sudo_cmd(pattern = "hi$",allow_sudo = True))
async def hi(event):
  event = await event.edit_or_reply(event,hello_rand)

@bot.on(admin_cmd(pattern = "bye$",outgoing = True))
@bot.on(sudo_cmd(pattern = "bye$",allow_sudo= True))
async def bye(event):
  event = await event.edit_or_reply(event,bye_rand)


CmdHelp("greeting").add_command(
  "hi", None, "Sends a random hello message"
).add_command(
  "bye", None, "Sends a random bye message"
).add_command
