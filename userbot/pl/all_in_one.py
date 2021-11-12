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
from userbot.Config import Config
import asyncio

import requests
from telethon import functions
from . import *
from userbot import ALIVE_NAME, CMD_LIST, SUDO_LIST
from JARVISBOT.utils import admin_cmd, edit_or_reply, sudo_cmd

perf = "[ IN JARVISBOT ]"

import requests
from telethon import functions
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot, BotInlineDisabledError as noinline, YouBlockedUserError

import asyncio
import datetime
from datetime import datetime

from telethon import events
from telethon.tl import functions, types
from userbot import CMD_HELP
from userbot import ALIVE_NAME, JARVISversion
from JARVISBOT.utils import admin_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "TONY STARK"

JARVIS = bot.uid


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

msg = f"""
**⚜ JARVIS-BOT ⚜**

  •        [♥️ 𝚁𝚎𝚙𝚘 ♥️](https://github.com/JARVIS-USERBOT/JARVIS-BOT)
  •        [♦️ Deploy ♦️]()

  •  ©️ Love from @Its_py ™
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="repo$"))
@bot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def repo(event):
    try:
        python = await bot.inline_query(botname, "repo")
        await python[0].click(event.chat_id)
        if event.sender_id == Legendl_Mr_Hacker:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


@bot.on(admin_cmd(pattern="data ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="data ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "jarvisbot_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            python = await eor(event, "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await python.edit("Unblock @Botfather first.")
                await python.edit(f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}op` again to get the help menu.")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**⚠️ 𝙴𝚁𝚁𝙾𝚁 !!** \n𝙿𝚕𝚎𝚊𝚜𝚎 𝚁𝚎-𝙲𝚑𝚎𝚌𝚔 BOT_TOKEN & BOT_USERNAME on Heroku.")
@bot.on(admin_cmd(pattern="help ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="help ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    tgbotusername = Config.BOT_USERNAME
    chat = "@Botfather"
    if tgbotusername is not None:
        try:
            results = await event.client.inline_query(tgbotusername, "jarvisbot_help")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except noinline:
            python = await eor(event, "**Inline Mode is disabled.** \n__Turning it on, please wait for a minute...__")
            async with bot.conversation(chat) as conv:
                try:
                    first = await conv.send_message("/setinline")
                    second = await conv.get_response()
                    third = await conv.send_message(tgbotusername)
                    fourth = await conv.get_response()
                    fifth = await conv.send_message(perf)
                    sixth = await conv.get_response()
                    await bot.send_read_acknowledge(conv.chat_id)
                except YouBlockedUserError:
                    return await python.edit("Unblock @Botfather first.")
                await python.edit(f"**Turned On Inline Mode Successfully.** \n\nDo `{l1}op` again to get the help menu.")
            await bot.delete_messages(
                conv.chat_id, [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id]
            )
    else:
        await eor(event, "**⚠️ 𝙴𝚁𝚁𝙾𝚁 !!** \n𝙿𝚕𝚎𝚊𝚜𝚎 𝚁𝚎-𝙲𝚑𝚎𝚌𝚔 BOT_TOKEN & BOT_USERNAME on Heroku.")



@bot.on(admin_cmd(pattern="plinfo(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="plinfo(?: |$)(.*)", allow_sudo=True))
async def pythonbott(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, str(CMD_HELP[args]))
        else:
            await eor(event, "**⚠️ 𝙴𝚛𝚛𝚘𝚛 !** \n𝙽𝚎𝚎𝚍 𝚊 Plugin 𝚗𝚊𝚖𝚎 𝚝𝚘 𝚜𝚑𝚘𝚠 𝚙𝚕𝚞𝚐𝚒𝚗 𝚒𝚗𝚏𝚘")
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += f"`♦️`"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                if sira == i.index(i[-1]):
                    string += "`"
                else:
                    string += "`, "
            string += "\n"
        await eor(event, "Please Specify A Module Name Of Which You Want Info" + "\n\n" + string)


@borg.on(events.NewMessage(outgoing=True))  # pylint:disable=E0602
async def set_not_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    came_back = datetime.now()
    afk_end = came_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message = event.message.message
    if ".afk" not in current_message and "yes" in USER_AFK:  # pylint:disable=E0602
        JARVISBOT = await borg.send_message(
            event.chat_id,
            "🔥ι αм ϐαϲκ αℓινє !\n**и𝔬 𝔏οиgєя 𝔞ƒκ.**\n⏱️ `աαs αƒk fοя:``"
            + total_afk_time
            + "`", file=JARVISpic
        )
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                "#AFKFALSE \nSet AFK mode to False\nReply to pic and use .afk reason"
                + "🔥ι αм ϐαϲκ αℓινє\n**𝔑𝔬 𝔏𝔬𝔫𝔤𝔢𝔯 𝔞𝔣𝔨.**\n⏱️ `աαs αբk for:``"
                + total_afk_time
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await borg.send_message(  # pylint:disable=E0602
                event.chat_id,
                "Please set `PRIVATE_GROUP_BOT_API_ID` "
                + "for the proper functioning of afk functionality "
                + "Ask in @JarvisUserBot_Support to get help setting this value\n\n `{}`".format(str(e)),
                reply_to=event.message.id,
                silent=True,
            )
        await asyncio.sleep(5)
        await JARVISBOT.delete()
        USER_AFK = {}  # pylint:disable=E0602
        afk_time = None  # pylint:disable=E0602


@borg.on(
    events.NewMessage(  # pylint:disable=E0602
        incoming=True, func=lambda e: bool(e.mentioned or e.is_private)
    )
)
async def on_afk(event):
    if event.fwd_from:
        return
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    cum_back = datetime.now()
    afk_end = cum_back.replace(microsecond=0)
    if afk_start != {}:
        total_afk_time = str((afk_end - afk_start))
    current_message_text = event.message.message.lower()
    if "afk" in current_message_text:
        # userbot's should not reply to other userbot's
        # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
        return False
    if USER_AFK and not (await event.get_sender()).bot:
        msg = None
        
        message_to_reply = (
            f"⚜️𓆩[{DEFAULTUSER}](tg://user?id={JARVIS})𓆪 ιѕ Cûřřently unavailable\n\n•♦️•Ꮮ𝚊𝚜𝚝 𝚂𝚎𝚎𝚗 : `{total_afk_time}`\n"
            + f"•♦️•Ꭱ𝚎𝚊𝚜𝚘𝚗 : `{reason}`"
  if reason
           else f"ᎻᎬᎽ Տιя / Ꮇιѕѕ🤔!\nᏆ αм ϲυяяєиτℓγ υиαναιℓαϐℓє😛. ι яєρℓγ υ αƒτєя ϲοмє ϐαϲκοиℓιиє.\n__Since when, you ask? From__ `{total_afk_time}`\nI'll be back when I feel to come🚶😛"
        )
        msg = await event.reply(message_to_reply, file=JARVISpic)
        await asyncio.sleep(2)
        if event.chat_id in last_afk_message:  # pylint:disable=E0602
            await last_afk_message[event.chat_id].delete()  # pylint:disable=E0602
        last_afk_message[event.chat_id] = msg  # pylint:disable=E0602


@borg.on(admin_cmd(pattern=r"afk (.*)", outgoing=True))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    JARVIS = await event.get_reply_message()
    global USER_AFK  # pylint:disable=E0602
    global afk_time  # pylint:disable=E0602
    global last_afk_message  # pylint:disable=E0602
    global afk_start
    global afk_end
    global reason
    global JARVISpic
    USER_AFK = {}
    afk_time = None
    last_afk_message = {}
    afk_end = {}
    start_1 = datetime.now()
    afk_start = start_1.replace(microsecond=0)
    reason = event.pattern_match.group(1)
    JARVISpic = await event.client.download_media(JARVIS)
    if not USER_AFK:  # pylint:disable=E0602
        last_seen_status = await borg(  # pylint:disable=E0602
            functions.account.GetPrivacyRequest(types.InputPrivacyKeyStatusTimestamp())
        )
        if isinstance(last_seen_status.rules, types.PrivacyValueAllowAll):
            afk_time = datetime.datetime.now()  # pylint:disable=E0602
        USER_AFK = f"yes: {reason} {JARVISpic}"  # pylint:disable=E0602
        if reason:
            await borg.send_message(
                event.chat_id, f"🌷𝙸'𝙼 𝙶𝚘𝚒𝚗𝚐 𝙰𝚏𝚔🚶 \n🔥𝚁𝚎𝚊𝚜𝚘𝚗:- `{reason}`", file=JARVISpic
            )
        else:
            await borg.send_message(event.chat_id, f"ι'м gοιиg αƒκ !🚶", file=JARVISpic)
        await asyncio.sleep(0.001)
        await event.delete()
        try:
            await borg.send_message(  # pylint:disable=E0602
                Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
                f"#AFKTRUE \nSet AFK mode to True, and Reason is {reason}",file=JARVISpic
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            logger.warn(str(e))  # pylint:disable=E0602



        
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

CmdHelp("afk").add_command(
  'afk', '<reply to media>/<or type a reson>', 'Marks you AFK(Away from Keyboard) with reason(if given) also shows afk time. Media also supported.'
).add_warning(
   "Official"
).add_type(
   "Official"
).add()
