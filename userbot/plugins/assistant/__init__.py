# PYTHONBOT Assistant
from . import *
from telethon import Button, custom

from userbot import bot

from userbot import ALIVE_NAME
OWNER_NAME = ALIVE_NAME or "TONY STARK"
OWNER_ID = bot.uid


me = bot.me.first_name
hu = bot.uid

python_mention = f"[{me}](tg://user?id={hu})"
JARVIS_logo = "./userbot/resources/pics/-6163428037589314866_121.jpg"
JARVIS_logo1 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
JARVIS_logo2 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
JARVIS_logo4 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
JARVIS_logo3 = "./userbot/resources/pics/-4965507108355287505_121.jpg"
JARVISversion = "𝚅1.0"

perf = "[ JARVISBOT ]"


DEVLIST = [
    "2033517108"
]

async def setit(event, name, value):
    try:
        event.set(name, value)
    except BaseException:
        return await event.edit("`Something Went Wrong`")


def get_back_button(name):
    button = [Button.inline("« Bᴀᴄᴋ", data=f"{name}")]
    return button
