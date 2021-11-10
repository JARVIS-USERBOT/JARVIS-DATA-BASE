import asyncio
from collections import deque
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd
from . import *
CmdHelp("clock").add_command(
   'clock', None, 'Check Fake Limitiation'
).add()

@borg.on(admin_cmd(pattern=r"clock"))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("🕛🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙🕚"))
    for _ in range(60):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)
