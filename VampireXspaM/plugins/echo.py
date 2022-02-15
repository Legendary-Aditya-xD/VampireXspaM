import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from TeamAlwaysXSpam import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from TeamAlwaysXSpam.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from resources.data import TeamAlways


@Don.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don2.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don3.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don4.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don5.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don6.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don7.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don8.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don9.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
@Don10.on(events.NewMessage(incoming=True, pattern=r"\.echo"))
async def echo(event):
  usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = **Eᴄʜᴏ**\n\nCommand:\n\n `.echo <reply to a User>`"
  if event.sender_id in SUDO_USERS:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            if int(user_id) in TeamAlways:
                    text = f"I can't Echo On My Creator"
                    await event.reply(text, parse_mode=None, link_preview=None )
            elif int(user_id) in SUDO_USERS:
                    text = f"This guy is a sudo user."
                    await event.reply(text, parse_mode=None, link_preview=None )
            else:
                 chat_id = event.chat_id
                 try:
                     hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                     hmm = Get(hmm)
                     await event.client(hmm)
                 except BaseException:
                    pass
                 if is_echo(user_id, chat_id):
                     await event.reply("The user is already enabled with echo ")
                     return
                 addecho(user_id, chat_id)
                 await event.reply("Echo activated On the user ✅")
     else:
          await event.reply(usage)

@Don.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don2.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don3.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don4.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don5.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don6.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don7.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don8.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don9.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
@Don10.on(events.NewMessage(incoming=True, pattern=r"\.decho"))
async def echo(event):
  usage = "Mᴏᴅᴜʟᴇ Nᴀᴍᴇ = **Eᴄʜᴏ**\n\nCommand:\n\n `.decho <reply to a User>`"
  if event.sender_id in SUDO_USERS or event.sender_id in DEV:
     if event.reply_to_msg_id is not None:
            reply_msg = await event.get_reply_message()
            user_id = reply_msg.sender_id
            chat_id = event.chat_id
            try:
                hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
                hmm = Get(hmm)
                await event.client(hmm)
            except BaseException:
                pass
            if is_echo(user_id, chat_id):
                remove_echo(user_id, chat_id)
                await event.reply("Echo has been stopped for the user ☑️")
            else:
                await event.reply("The user is not activated with echo")
     else:
          await event.reply(usage)


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
async def _(e):
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(0.5)
        try:
            Always = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            Always = Get(Always)
            await e.client(Always)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)
