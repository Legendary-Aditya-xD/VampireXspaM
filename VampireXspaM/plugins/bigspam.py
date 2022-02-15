async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS

@Don.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don2.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don3.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don4.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don5.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don6.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don7.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don8.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don9.on(events.NewMessage(pattern=r"\.bigbspam"))
@Don10.on(events.NewMessage(pattern=r"\.bigbspam"))
async def spam(e):
    usage = "**Mᴏᴅᴜʟᴇ Nᴀᴍᴇ** = Bɪɢsᴘᴀᴍ\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        rizoel = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(always) == 2:
            message = str(always[1])
            counter = int(always[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(always[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(always[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
