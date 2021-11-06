import random
from JARVIS.utlis import admin_command,sudo_command,edit_or_reply

hello_message = ["Hello","Hi","Hello there","I am here , hello!","Hey"]
hello_message_random = random.choice(hello_message)

@bot.on(admin_command(pattern = "hi$"))
@bot.on(sudo_command(patten = "hi$"))
async def hi(event):
  id = event.chat_id
  await bot.send_message(id,hello_message_random)
