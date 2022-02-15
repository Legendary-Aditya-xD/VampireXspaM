import asyncio
import os
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, Button
from telethon.tl.custom import button
from .. import Don, Don2, Don3, Don4, Don5, Don6, Don7, Don8, Don9, Don10, ALIVE_PIC

Don_IMG = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/4cc84cabf3ee789d64ce0.jpg"


Don_Button = [
        [
        Button.url("ᴄʀᴇᴀᴛᴏʀ", "https://t.me/Always_Don")
        ]
        ]


@Don.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)
                
@Don2.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don2.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don2.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)      
 
@Don3.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don3.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don3.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)
                
@Don4.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don4.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don4.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)  

@Don5.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don5.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don5.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)

@Don6.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don6.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don6.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)       

@Don7.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don7.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id 
       firstname = replied_user.user.first_name
       Donmsg = f"***Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don7.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)

@Don8.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don8.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don8.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)
                
@Don9.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don9.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don9.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)
                
@Don10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
       DonBot = await Don10.get_me()
       bot_id = DonBot.first_name
       bot_username = DonBot.username
       replied_user = await event.client(GetFullUserRequest(event.sender_id))
       TheAlways = event.chat_id
       firstname = replied_user.user.first_name
       Donmsg = f"**Hello, {firstname} ! This is TeamAlways SpamBot \n\n✗ Pᴏᴡᴇʀᴇᴅ 💕 Bʏ: @Team_Always !**"
       await Don10.send_file(TheAlways,
                Don_IMG,
                caption=Donmsg, 
                buttons=Don_Button)
