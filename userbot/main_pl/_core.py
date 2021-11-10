import asyncio
import os
import io
from datetime import datetime
from pathlib import Path
from telethon import events, functions, types
from telethon.tl.types import InputMessagesFilterDocument
from JARVISBOT.utils import *
from userbot import *
from . import *
DELETE_TIMEOUT = 5
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "『jarvisẞø†』"
jarvis = bot.uid
JARVIS = f"[{DEFAULTUSER}](tg://user?id={jarvis})"

@bot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    message_id = event.message.id
    thumb = JARVIS_logo2
    input_str = event.pattern_match.group(1)
    omk = f"**⍟ 𝙿𝚕𝚞𝚐𝚒𝚗 𝚗𝚊𝚖𝚎 ≈** `{input_str}`\n**⍟ 𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝙱𝚢 ≈** {jarvis_mention}\n\n⚡ **[jarvisẞø†](https://t.me/jarvis_Userbot_Support)** ⚡"
    the_plugin_file = "./userbot/main_pl/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        lauda = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            thumb=thumb,
            caption=omk,
            force_document=True,
            allow_cache=False,
            reply_to=message_id,
        )
        await event.delete()
    else:
        await edit_or_reply(event, "File not found in data base")

@bot.on(admin_cmd(pattern="install$", outgoing=True))
@bot.on(sudo_cmd(pattern="install$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    a = "__𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚒𝚗𝚐.__"
    b = 1
    await event.edit(a)
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(  # pylint:disable=E0602
                await event.get_reply_message(),
                "./userbot/main_pl/"  # pylint:disable=E0602
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "**Commands found in** `{}` (sudo included)\n".format((os.path.basename(downloaded_file_name)))
                    for i in CMD_LIST[shortname]:
                        string += "  •  `" + i 
                        string += "`\n"
                        if b == 1:
                            a = "__𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚒𝚗𝚐..__"
                            b = 2
                        else:
                            a = "__𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚒𝚗𝚐...__"
                            b = 1
                        await event.edit(a)
                    return await event.edit(f"✅ **𝙸𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍 𝙼𝚘𝚍𝚞𝚕𝚎** :- `{shortname}` \n✨ BY :- {jarvis_mention}\n\n{string}\n\n        ⚡ **[『jarvisẞø†』](t.me/Pythoon_Userbot_Support)**\n ⚠️Dont Try To Install External Plugin⚠️\n Click Here for Uninstall 👉`.uninstall {shortname}`⚡", link_preview=False)
                return await event.edit(f"Installed module `{os.path.basename(downloaded_file_name)}`")
            else:
                os.remove(downloaded_file_name)
                return await event.edit(f"**𝐅𝐚𝐢𝐥𝐞𝐝 𝐓𝐨 𝐈𝐧𝐬𝐭𝐚𝐥𝐥** \n`𝐄𝐫𝐫𝐨𝐫`\n𝐌𝐨𝐝𝐮𝐥𝐞 𝐀𝐥𝐫𝐞𝐚𝐝𝐲 𝐈𝐧𝐬𝐭𝐚𝐥𝐥𝐞𝐝 𝐎𝐫 𝐔𝐧𝐤𝐧𝐨𝐰 𝐅𝐨𝐫𝐦𝐚𝐭")
        except Exception as e: 
            await event.edit(f"**Failed to Install** \n`Error`\n{str(e)}")
            return os.remove(downloaded_file_name)
    
@bot.on(admin_cmd(pattern=r"uninstall (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"uninstall (?P<shortname>\w+)", allow_sudo=True))
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path =f"./userbot/main_pl/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await event.edit(f"**𝚄𝚗𝚒𝚜𝚝𝚊𝚕𝚕𝚎𝚍**`{shortname}` 𝚂𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢")
    except OSError as e:
        await event.edit("Error: %s : %s" % (dir_path, e.strerror))

@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"upload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await event.edit(f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await event.edit(
            "Successfully unloaded {shortname}\n{}".format(
                shortname, str(e)
            )
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await event.edit(f"Successfully loaded `{shortname}`")
    except Exception as e:
        await event.edit(
            f"Sorry, could not load {shortname} because of the following error.\n{str(e)}"
        )



@bot.on(admin_cmd(pattern=r"cmds"))
@bot.on(sudo_cmd(pattern=r"cmds", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    cmd = "ls userbot/main_pl"
    thumb = JARVIS_logo1
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"♥️List Of main_pl In 𝖑𝖊ɠêɳ̃dẞø✞︎ 🇮🇳 :- \n\n{o}\n\n<><><><><><><><><><><><><><><><><><><><><><><><>\nHELP:- If you want to know the commands for a plugin, do :- \n.plinfo <plugin name> without the < > brackets. \nJoin https://t.me/Legend_Userbot for help."
    if len(OUTPUT) > 69:
        with io.BytesIO(str.encode(OUTPUT)) as out_file:
            out_file.name = "cmnds_list.text"
            JARVIS_file = await bot.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                thumb=thumb,
                reply_to=reply_to_id,
            )
            await edit_or_reply(JARVIS_file, f"**Output Too Large. This is the file for the list of main_pl in ✞︎t͛ẞ̸ jarvisẞø✞︎ .\n\n**BY :- {DEFAULTUSER}**")
            await event.delete()



CmdHelp("core").add_command(
  "install", "<reply to a .py file>", "Installs the replied jarvis file if suitable to userbot codes. (TEMPORARILY DISABLED AS HACKERS MAKE YOU INSTALL SOME main_pl AND GET YOUR DATA)"
).add_command(
  "uninstall", "<plugin name>", "Uninstalls the given plugin from userbot. To get that again do .restart", "uninstall alive"
).add_command(
  "load", "<plugin name>", "Loades the unloaded plugin to your userbot", "load alive"
).add_command(
  "unload", "<plugin name>", "Unloads the plugin from your userbot", "unload alive"
).add_command(
  "send", "<file name>", "Sends the given file from your userbot server, if any.", "send alive"
).add_command(
  "cmds", None, "Gives out the list of modules in JARVISBOT."
).add_type(
  "Official"
).add()
