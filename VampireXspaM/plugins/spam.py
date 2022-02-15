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
import random
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from resources.data import GROUP, PORMS


SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)



@Don.on(events.NewMessage(pattern=r"\.bspam"))
@Don2.on(events.NewMessage(pattern=r"\.bspam"))
@Don3.on(events.NewMessage(pattern=r"\.bspam"))
@Don4.on(events.NewMessage(pattern=r"\.bspam"))
@Don5.on(events.NewMessage(pattern=r"\.bspam"))
@Don6.on(events.NewMessage(pattern=r"\.bspam"))
@Don7.on(events.NewMessage(pattern=r"\.bspam"))
@Don8.on(events.NewMessage(pattern=r"\.bspam"))
@Don9.on(events.NewMessage(pattern=r"\.bspam"))
@Don10.on(events.NewMessage(pattern=r"\.bspam"))
async def spam(e):
    usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = Sᴘᴀᴍ\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Always) == 2:
            message = str(Always[1])
            counter = int(Always[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Always[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Always[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

@Don.on(events.NewMessage(pattern=r"\.pspam"))
@Don2.on(events.NewMessage(pattern=r"\.pspam"))
@Don3.on(events.NewMessage(pattern=r"\.pspam"))
@Don4.on(events.NewMessage(pattern=r"\.pspam"))
@Don5.on(events.NewMessage(pattern=r"\.pspam"))
@Don6.on(events.NewMessage(pattern=r"\.pspam"))
@Don7.on(events.NewMessage(pattern=r"\.pspam"))
@Don8.on(events.NewMessage(pattern=r"\.pspam"))
@Don9.on(events.NewMessage(pattern=r"\.pspam"))
@Don10.on(events.NewMessage(pattern=r"\.pspam"))
async def pspam(e):
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(Always) == 1:
            counter = int(Always[0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! I can't spam here"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `.pornspam <count>`"
            await e.reply(usage, parse_mode=None, link_preview=None )
