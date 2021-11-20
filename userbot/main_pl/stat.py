import Config
from . import *
from JARVISBOT.utils import admin_command
from JARVISBOT.utils import edit_or_reply as eor

group = Config.YOU_GROUP

stat_message = f"""
Owner : {jarvis_mention}
"""

@bot.on(admin_comannd(pattern = ".stat",outgoing = True))
async def stat(jarvis_op):
  
