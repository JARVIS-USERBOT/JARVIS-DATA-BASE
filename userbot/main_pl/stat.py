import Config
from . import *
from JARVISBOT.utils import admin_command
from JARVISBOT.utils import edit_or_reply as eor

group = Config.YOUR_GROUP or "https://t.me/JarvisUserBot_Support"
group_mention = f"[Group]({group})"
channel = Config.YOUR_CHANNEL or "https://t.me/Jarvis_Support_Official"
channel_mention = f"[Channel]({channel})"

def ping(jarvis_op):
  if jarvis_op.fwd_from:
        return
    start = datetime.now()
    message = await jarvis_op.eor("STAT")
    end = datetime.now()
    ms = (end - start).microseconds / 1000

stat_message = f"""
Owner      : {jarvis_mention}
My Group   : {group_mention}
My channel : {channel_mention}
Ping       : {ms}
"""

@bot.on(admin_comannd(pattern = ".stat",outgoing = True))
async def stat(jarvis_op):
  if jarvis_op.fwd_from:
        return
    start = datetime.now()
    message = await jarvis_op.eor("Stats")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await jarvis_op.eor(stat_message)

CmdHelp("stat").add_command("stat", None, "one and only stat command").add_warning(
    "Harmless Module✅"
).add_info("Just Like Alive But no pics used").add_type("Official").add()
