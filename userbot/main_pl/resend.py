from JARVISBOT.utils import admin_cmd, sudo_cmd
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="resend"))
@bot.on(sudo_cmd(pattern="resend", allow_sudo=True))
async def _(event):
    await event.delete()
    m = await event.get_reply_message()
    if not m:
        return
    await event.respond(m)

CmdHelp("resend").add_command(
  "resend", "<reply>", "Resends the replied message in current chat"
).add()
