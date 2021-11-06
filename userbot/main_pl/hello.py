import random
from JARVIS.utlis import admin_command,sudo_command,edit_or_reply
from userbot.cmdhelp import CmdHelp
from . import *

hello_message = ["Hello","Hi","Hello there","I am here , hello!","Hey"]
hello_message_random = random.choice(hello_message)

@bot.on(admin_command(pattern = "hi$"))
@bot.on(sudo_command(patten = "hi$"))
async def hi(event):
  id = event.chat_id
  await bot.send_message(id,hello_message_random)

CmdHelp("hi").add_command(
    'bot', None, 'Sends a random greeting message'
).add_type(
    "Official"
).add()
