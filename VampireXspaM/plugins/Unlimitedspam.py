import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS

@Don.on(events.NewMessage(pattern=r"\.uspam"))
@Don2.on(events.NewMessage(pattern=r"\.uspam"))
@Don3.on(events.NewMessage(pattern=r"\.uspam"))
@Don4.on(events.NewMessage(pattern=r"\.uspam"))
@Don5.on(events.NewMessage(pattern=r"\.uspam"))
@Don6.on(events.NewMessage(pattern=r"\.uspam"))
@Don7.on(events.NewMessage(pattern=r"\.uspam"))
@Don8.on(events.NewMessage(pattern=r"\.uspam"))
@Don9.on(events.NewMessage(pattern=r"\.uspam"))
@Don10.on(events.NewMessage(pattern=r"\.uspam"))
async def unlimitedspam(event):
  if event.sender_id in SUDO_USERS:
    try:
      op = event.text[7:]
      x = None
      while x == None:
        await event.client.send_message(event.chat, op)
        await asyncio.sleep(0.3)
    except Exception as e:
      await event.reply("Oops!! Something went wrong, Report To @Always_Don\nPowered By @Team_Always\n\n" + str(e))
