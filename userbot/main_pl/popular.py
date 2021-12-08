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


@bot.on(admin_cmd(pattern=f"attack$"))
@bot.on(sudo_cmd(pattern=f"attack$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 20)
    event = await edit_or_reply(event, "**ATTACK**")
    animation_chars = [
    "Attack In Progress",
    "Missile Launch in: 10",
    "Missile Launch in: 9",
    "Missile Launch in: 8",
    "Missile Launch in: 7",
    "Missile Launch in: 6",
    "Missile Launch in: 5",
    "Missile Launch in: 4",
    "Missile Launch in: 3",
    "Missile Launch in: 2",
    "Missile Launch in: 1",
    "Missile Launch in: 0",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully"
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile"
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed \n\nPakistan Destroyed",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed \n\nPakistan Destroyed \n\nError",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed \n\nPakistan Destroyed \n\n_____",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed \n\nPakistan Destroyed \n\nError",
    "Missile Launch in: 0 \n\nLaunched Missile Successfully \n\nLaunched 5 Missile \n\nU.S.A Destroyed \n\nChaina Destroyed \n\nEgypt Destroyed \n\nPakistan Destroyed \n\nError \n\nLost Connection"
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 20])

CmdHelp("Popular").add_command(
  "lol", None,"Lol Animation"
).add_command(
  "attack", None,"Attack Animation"
).add
