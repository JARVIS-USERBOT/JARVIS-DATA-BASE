"""
Get Random Emoji as Image..
Syntax : `.randomoji`
"""
from userbot.cmdhelp import CmdHelp

import os
from LEGENDBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from multiutility import EmojiCreator

Emoji = EmojiCreator()

@borg.on(admin_cmd(pattern="randomoji", outgoing=True))  # pylint:disable=E0602
async def _(event):
    mmmm = await edit_or_reply(event, "**Generating Your Random Emoji ⏰✍️**")
    emoji = Emoji.get_random()
    await event.respond("**--- Random Emoji For You ---**", file=emoji)
    os.remove(emoji)
    await mmmm.delete()

CmdHelp("randomemoji").add_command(
  "randomoji", None, "Get Random Emoji as Image."
).add()
