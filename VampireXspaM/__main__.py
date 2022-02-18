#TeamAlwaysXSpam By @Team_Always

import asyncio
import sys
from sys import argv
import glob
from pathlib import Path
from TeamAlwaysXSpam.utils import load_plugins
import logging
from telethon import events
from . import Don, Don2, Don3, Don4, Don5, Don6, Don7, Don8, Don9, Don10

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


path = "VampireXspam/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Team Always Bot Spam Successfully deployed -!")
print("Enjoy! Do visit @Team_Always")

if __name__ == "__main__":
    Don.run_until_disconnected()
    
if __name__ == "__main__":
    Don2.run_until_disconnected()

if __name__ == "__main__":
    Don3.run_until_disconnected()
    
if __name__ == "__main__":
    Don4.run_until_disconnected()

if __name__ == "__main__":
    Don5.run_until_disconnected()
    
if __name__ == "__main__":
    Don6.run_until_disconnected()
    
if __name__ == "__main__":
    Don7.run_until_disconnected()

if __name__ == "__main__":
    Don8.run_until_disconnected()
    
if __name__ == "__main__":
    Don9.run_until_disconnected()

if __name__ == "__main__":
    Don10.run_until_disconnected()
