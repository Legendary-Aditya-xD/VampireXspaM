import asyncio
from .. import Don, Don2, Don3, Don4, Don5, Don6, Don7, Don8, Don9, Don10, SUDO_USERS
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon import events
import os
import random
import sys
    

@Don.on(events.NewMessage(pattern=r"\.leave"))
@Don2.on(events.NewMessage(pattern=r"\.leave"))
@Don3.on(events.NewMessage(pattern=r"\.leave"))
@Don4.on(events.NewMessage(pattern=r"\.leave"))
@Don5.on(events.NewMessage(pattern=r"\.leave"))
@Don6.on(events.NewMessage(pattern=r"\.leave"))
@Don7.on(events.NewMessage(pattern=r"\.leave"))
@Don8.on(events.NewMessage(pattern=r"\.leave"))
@Don9.on(events.NewMessage(pattern=r"\.leave"))
@Don10.on(events.NewMessage(pattern=r"\.leave"))
async def _(e):
    usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = Lᴇᴀᴠᴇ\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SUDO_USERS:
        always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = always[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )   
