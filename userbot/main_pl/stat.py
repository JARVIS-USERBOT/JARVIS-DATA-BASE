import Config
from . import *
from JARVISBOT.utils import admin_command
from JARVISBOT.utils import edit_or_reply as eor

group = Config.YOUR_GROUP or "https://t.me/JarvisUserBot_Support"
group_mention = f"[Group]({group})"
channel = Config.YOUR_CHANNEL or "https://t.me/Jarvis_Support_Official"
channel_mention = f"[Channel]({channel})"

stat_message = f"""
Owner      : {jarvis_mention}
My Group   : {group_mention}
My channel : {channel_mention}
"""
"""
@bot.on(admin_comannd(pattern = ".stat",outgoing = True))
async def stat(jarvis_op):
"""
