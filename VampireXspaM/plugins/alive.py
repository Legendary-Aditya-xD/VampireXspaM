from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS, alwaysversion
from .. import ALIVE_PIC
from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime

DON_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/4cc84cabf3ee789d64ce0.jpg"
  

          
always = "**Tᴇᴀᴍ Aʟᴡᴀʏꜱ Sᴘᴀᴍ Bᴏᴛ Iꜱ Wᴏʀᴋɪɴɢ Pᴇʀꜰᴇᴄᴛʟʏ♠️♠️**\n\n"

always += f"🔥**TᴇᴀᴍAʟᴡᴀʏꜱ Sᴘᴀᴍ Sʏꜱᴛᴇᴍ**🔥\n\n"

always += f" **•⭕️• Pʏᴛʜᴏɴ Vᴇʀsɪᴏɴ** : `3.9.6`\n"

always += f" **•⭕️• Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ** : `{version.__version__}`\n"

always += f" **•⭕️• Bot Vᴇʀsɪᴏɴ**  : `{alwaysversion}`\n"

always += f" **•⭕️• Cʀᴇᴀᴛᴏʀ**  : [Dᴏɴ](t.me/Always_Don)\n\n"
         
                                    
@Don.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don2.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don2.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )

@Don3.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don3.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don4.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don4.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don5.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don5.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
   
@Don6.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don6.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don7.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don7.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don8.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don8.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
    
@Don9.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don9.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
@Don10.on(events.NewMessage(pattern=".alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Don10.send_file(event.chat_id,
                                  DON_PIC,
                                  caption=always,
                                  buttons=[
        [
        Button.url("Cᴏᴍᴍᴜɴɪᴛʏ", "https://t.me/Team_Always")
        ]
        ]
        )
    
