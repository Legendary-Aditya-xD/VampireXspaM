import asyncio
import base64
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from resources.data import RAID, REPLYRAID, TeamAlways, HBD

que = {}

@Don.on(events.NewMessage(pattern=r"\.fuk"))
@Don2.on(events.NewMessage(pattern=r"\.fuk"))
@Don3.on(events.NewMessage(pattern=r"\.fuk"))
@Don4.on(events.NewMessage(pattern=r"\.fuk"))
@Don5.on(events.NewMessage(pattern=r"\.fuk"))
@Don6.on(events.NewMessage(pattern=r"\.fuk"))
@Don7.on(events.NewMessage(pattern=r"\.fuk"))
@Don8.on(events.NewMessage(pattern=r"\.fuk"))
@Don9.on(events.NewMessage(pattern=r"\.fuk"))
@Don10.on(events.NewMessage(pattern=r"\.fuk"))
async def spam(e):
    usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = Rᴀɪᴅ\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Always) == 2:
            user = str(Always[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in TeamAlways:
                text = f"I can't raid on My Creator"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Always[0])
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.5)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            if int(g) in TeamAlways:
                text = f"I can't raid on My Creator"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = b.first_name
                counter = int(Always[0])
                username = f"[{c}](tg://user?id={g})"
                for _ in range(counter):
                    reply = random.choice(RAID)
                    caption = f"{username} {reply}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage)



@Don.on(events.NewMessage(incoming=True))
@Don2.on(events.NewMessage(incoming=True))
@Don3.on(events.NewMessage(incoming=True))
@Don4.on(events.NewMessage(incoming=True))
@Don5.on(events.NewMessage(incoming=True))
@Don6.on(events.NewMessage(incoming=True))
@Don7.on(events.NewMessage(incoming=True))
@Don8.on(events.NewMessage(incoming=True))
@Don9.on(events.NewMessage(incoming=True))
@Don10.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(REPLYRAID)),
            reply_to=event.message.id,
        )


@Don.on(events.NewMessage(pattern=r"\.hardcore"))
@Don2.on(events.NewMessage(pattern=r"\.hardcore"))
@Don3.on(events.NewMessage(pattern=r"\.hardcore"))
@Don4.on(events.NewMessage(pattern=r"\.hardcore"))
@Don5.on(events.NewMessage(pattern=r"\.hardcore"))
@Don6.on(events.NewMessage(pattern=r"\.hardcore"))
@Don7.on(events.NewMessage(pattern=r"\.hardcore"))
@Don8.on(events.NewMessage(pattern=r"\.hardcore"))
@Don9.on(events.NewMessage(pattern=r"\.hardcore"))
@Don10.on(events.NewMessage(pattern=r"\.hardcore"))
async def _(e):
    global que
    usage = f"Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = RᴇᴘʟʏRᴀɪᴅ\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>."
    if e.sender_id in SUDO_USERS:
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        Donx = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(Always[0])
            a = await e.client.get_entity(message)
            user_idd = a.id
            user_id = int(user_idd)
            if int(user_id) in TeamAlways:
                text = f" can't raid on My Creator"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            umser = await e.client.get_entity(a.sender_id)
            user_idd = umser.id
            user_id = int(user_idd)
            if int(user_id) in TeamAlways:
                text = f"  can't raid on My Creator."
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                text = f"This guy is a sudo user."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                que[user_id] = []
                gey = que.get(user_id)
                phucker = [user_id]
                gey.append(phucker)
                text = f"Activated Replyraid"
                await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage)


@Don.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don2.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don3.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don4.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don5.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don6.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don7.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don8.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don9.on(events.NewMessage(pattern=r"\.dhardcore"))
@Don10.on(events.NewMessage(pattern=r"\.dhardcore"))
async def _(e):
    usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = Dᴇᴀᴄᴛɪᴠᴀᴛᴇ RᴇᴘʟʏRᴀɪᴅ\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    global que    
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(Always[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@Don.on(events.NewMessage(pattern=r"\.hbd"))
@Don2.on(events.NewMessage(pattern=r"\.hbd"))
@Don3.on(events.NewMessage(pattern=r"\.hbd"))
@Don4.on(events.NewMessage(pattern=r"\.hbd"))
@Don5.on(events.NewMessage(pattern=r"\.hbd"))
@Don6.on(events.NewMessage(pattern=r"\.hbd"))
@Don7.on(events.NewMessage(pattern=r"\.hbd"))
@Don8.on(events.NewMessage(pattern=r"\.hbd"))
@Don9.on(events.NewMessage(pattern=r"\.hbd"))
@Don10.on(events.NewMessage(pattern=r"\.hbd"))
async def spam(e):
    usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = **HAPPY BIRTHDAY**\n\nCommand:\n\n.hbd <count> <Username of User>\n\n.hbd <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Always = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Always) == 2:
            user = str(Always[1])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) == 2007685881:
                text = f"Noob"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                username = f"[{c}](tg://user?id={g})"
                counter = int(Always[0])
                for _ in range(counter):
                    msg = random.choice(HBD)
                    caption = f"{username} \n\n {msg}"
                    async with e.client.action(e.chat_id, "typing"):
                        await e.client.send_message(e.chat_id, caption)
                        await asyncio.sleep(0.3)
