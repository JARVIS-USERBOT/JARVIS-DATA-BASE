import asyncio
from collections import deque

from telethon.tl.functions.users import GetFullUserRequest

from userbot import *
from JARVISBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp

@bot.on(admin_cmd(pattern=f"lol$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(0,100)
    await edit_or_reply(event, "**LOL**")
    animation_chars = [
    "😂🤣😂🤣😂🤣😂🤣","🤣😂🤣😂🤣😂🤣😂"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 2])
CmdHelp("Popular").add_command(
  "lol", None,"Lol Animation"
)
