from .. import Don, Don2, Don3, Don4, Don5 , Don6, Don7, Don8, Don9, Don10, SUDO_USERS
from telethon import events
import os
import random
import sys


@Don.on(events.NewMessage(pattern=r"\.reboot"))
@Don2.on(events.NewMessage(pattern=r"\.reboot"))
@Don3.on(events.NewMessage(pattern=r"\.reboot"))
@Don4.on(events.NewMessage(pattern=r"\.reboot"))
@Don5.on(events.NewMessage(pattern=r"\.reboot"))
@Don6.on(events.NewMessage(pattern=r"\.reboot"))
@Don7.on(events.NewMessage(pattern=r"\.reboot"))
@Don8.on(events.NewMessage(pattern=r"\.reboot"))
@Don9.on(events.NewMessage(pattern=r"\.reboot"))
@Don10.on(events.NewMessage(pattern=r"\.reboot"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "**Rebooting Your SEXYYY Spam Bots**.. Please Wait Until It Starts Again"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Don.disconnect()
        except Exception:
            pass
        try:
            await Don2.disconnect()
        except Exception:
            pass
        try:
            await Don3.disconnect()
        except Exception:
            pass
        try:
            await Don4.disconnect()
        except Exception:
            pass
        try:
            await Don5.disconnect()
        except Exception:
            pass
        try:
            await Don6.disconnect()
        except Exception:
            pass
        try:
            await Don7.disconnect()
        except Exception:
            pass
        try:
            await Don8.disconnect()
        except Exception:
            pass
        try:
            await Don9.disconnect()
        except Exception:
            pass
        try:
            await Don10.disconnect()
        except Exception:
            pass


        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
