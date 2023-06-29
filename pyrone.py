import sys
import asyncio

from os import execle, getenv, environ

from pyrogram import Client, filters, idle
from pyrogram.types import Message
from pyrogram.handlers import MessageHandler
from pyrogram.errors import FloodWait


# ------------- SESSIONS -------------

SESSION1 = getenv('SESSION1', default=None)
SESSION2 = getenv('SESSION2', default=None)
SESSION3 = getenv('SESSION3', default=None)
SESSION4 = getenv('SESSION4', default=None)
SESSION5 = getenv('SESSION5', default=None)


# ------------- CLIENTS -------------

if SESSION1:
    M1 = Client(SESSION1, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M1 = None

if SESSION2:
    M2 = Client(SESSION2, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M2 = None

if SESSION3:
    M3 = Client(SESSION3, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M3 = None

if SESSION4:
    M4 = Client(SESSION4, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M4 = None

if SESSION5:
    M5 = Client(SESSION5, api_id=25981592, api_hash="709f3c9d34d83873d3c7e76cdd75b866")
else:
    M5 = None


ONE_WORDS = ["𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙄", "𝘾𝙃𝙐𝙏", "𝘼𝙅𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙄", "𝘾𝙃𝙐𝙏", "𝙁𝘼𝘼𝘿", "𝘿𝙐𝙉𝙂𝘼", "𝙃𝙄𝙅𝘿𝙀", "𝙏𝙀𝙍𝘼", "𝘽𝘼𝘼𝙋",
           "𝙃𝙐", "𝙆𝙄𝘿𝙓𝙓", "𝙎𝙋𝙀𝙀𝘿", "𝙋𝘼𝙆𝘼𝘿", "𝘽𝙃𝙀𝙉 𝙆𝙀 𝙇𝘼𝙐𝘿𝙀", "𝘼𝘼 𝘽𝙀𝙏𝘼", "𝘼𝘼𝙂𝙔𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼 ", "𝘾𝙃𝙊𝘿𝙉𝙀",
           "𝘼𝘽", "𝙏𝙀𝙍𝙄 ", "𝙈𝘼𝘼", "𝘾𝙃𝙐𝘿𝙀𝙂𝙄", "𝙆𝙐𝙏𝙏𝙀", "𝙆𝙄", "𝙏𝘼𝙍𝘼𝙃", "𝘽𝙀𝙏𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝘽𝙃𝙊𝙎𝘿𝙀",
           "𝙈𝙀", "𝙅𝘽𝙇", "𝙆𝙀", "𝙎𝙋𝙀𝘼𝙆𝙀𝙍", "𝘿𝘼𝘼𝙇", "𝙆𝘼𝙍", "𝘽𝘼𝙎𝙎", "𝘽𝙊𝙊𝙎𝙏𝙀𝘿", "𝙎𝙊𝙉𝙂", "𝙎𝙐𝙉𝙐𝙉𝙂𝘼", "𝙋𝙐𝙍𝙄",
           "𝙍𝘼𝘼𝙏", "𝙇𝘼𝙂𝘼𝙏𝘼𝙍", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝙎𝘼𝙏𝙃", "𝙎𝙀𝙓", "𝙆𝘼𝙍𝙐𝙉𝙂𝘼🔥", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝘽𝙊𝙊𝘽𝙎",
           "𝘿𝘼𝘽𝘼𝙐𝙉𝙂𝘼","𝙓𝙓𝙓","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼","𝙆𝘼𝘼","𝘾𝙃𝙐𝙏","𝙈𝘼𝙍𝙐","𝙍𝘼𝙉𝘿𝙄","𝙆𝙀𝙀","𝙋𝙄𝙇𝙀𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼","𝙆𝘼𝘼","𝘽𝙃𝙊𝙎𝘿𝘼𝘼",
           "𝙈𝘼𝙍𝙐","𝙎𝙐𝘼𝙍","𝙆𝙀𝙀","𝘾𝙃𝙊𝘿𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼","𝙆𝙀𝙀𝙀","𝙉𝙐𝘿𝙀𝙎","𝘽𝙀𝘾𝙃𝙐𝙉𝙂𝘼","𝙍𝘼𝙉𝘿𝙄","𝙆𝙀𝙀","𝙋𝙄𝙇𝙇𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼",
           "𝘾𝙃𝙊𝘿𝙐","𝙎𝙐𝘼𝙍","𝙆𝙀𝙀𝙀","𝙋𝙄𝙇𝙀𝙀","𝙏𝙀𝙍𝙄𝙄𝙄","𝙈𝘼𝘼𝘼","𝘿𝘼𝙄𝙇𝙔𝙔","𝘾𝙃𝙐𝘿𝙏𝙏𝙄","𝙃𝘼𝙄𝙄","𝙈𝘼𝘿𝙃𝘼𝙍𝘾𝙃𝙊𝘿","𝘼𝙐𝙆𝘼𝙏","𝘽𝘼𝙉𝘼𝘼",
           "𝙇𝙊𝘿𝙀","𝙏𝙀𝙍𝘼𝘼","𝘽𝘼𝘼𝙋","𝙃𝙐𝙐","𝙏𝙀𝙍𝙄","𝙂𝙁𝙁","𝙆𝘼𝘼","𝘽𝙃𝙊𝙎𝘿𝘼𝘼","𝙈𝘼𝙍𝙐𝙐","𝙈𝘼𝘿𝙃𝘼𝙍𝘾𝙃𝙊𝘿","𝙏𝙀𝙍𝙄 ","𝙉𝘼𝙉𝘼𝙄","𝙆𝘼𝘼",
           "𝘾𝙃𝙐𝙏𝙏","𝙈𝘼𝙍𝙐","𝙏𝙀𝙍𝙄𝙄","𝘽𝙀𝙃𝙀𝙉","𝙆𝘼𝘼𝘼","𝘽𝙃𝙊𝙎𝘿𝘼𝘼","𝙈𝘼𝙍𝙐","𝙍𝘼𝙉𝘿𝙄𝙄","𝙆𝙀𝙀𝙀","𝘾𝙃𝙊𝘿𝙀","𝙏𝙀𝙍𝙄","𝘿𝘼𝘿𝙄","𝙆𝘼𝘼𝘼","𝘽𝙊𝙊𝙍",
           "𝙂𝘼𝙍𝘼𝙈","𝙆𝘼𝙍𝙍","𝙏𝙀𝙍𝙀","𝙋𝙐𝙍𝙀𝙀","𝙆𝙃𝘼𝙉𝘿𝘼𝙉","𝙆𝙊𝙊𝙊","𝘾𝙃𝙊𝘿𝙐𝙉𝙂𝘼𝘼","𝘽𝘼𝘼𝙋","𝙎𝙀𝙀","𝘽𝘼𝙆𝘾𝙃𝙊𝘿𝙄","𝙆𝘼𝙍𝙀𝙂𝘼𝘼","𝙎𝙐𝘼𝙍𝙍",
           "𝙆𝙀𝙀𝙀","𝙋𝙄𝙇𝙇𝙀𝙀","𝙉𝘼𝘼𝙆","𝙈𝙀𝙀𝙀","𝙉𝙀𝙏𝘼𝘼","𝘽𝘼𝘼𝙋","𝙆𝙊𝙊","𝙆𝘼𝘽𝙃𝙄𝙄","𝙉𝘼𝘼𝙃","𝘽𝙊𝙇𝙉𝘼𝘼","𝘽𝙀𝙏𝘼𝘼","𝘾𝙃𝙐𝙎𝙎","𝙇𝙀𝙀𝙀",
           "𝙈𝙀𝙍𝘼𝘼","𝙇𝙊𝘿𝘼𝘼","𝙅𝘼𝙄𝙎𝙀","𝘼𝙇𝙐𝙐","𝙆𝘼𝘼𝘼","𝙋𝘼𝙆𝙊𝘿𝘼𝘼","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼","𝘽𝙀𝙃𝙀𝙉","𝙂𝙁𝙁","𝙉𝘼𝙉𝙄","𝘿𝙄𝙄𝙉","𝙍𝘼𝘼𝙏","𝙎𝙊𝙏𝙀𝙀",
           "𝙅𝘼𝙂𝙏𝙀𝙀","𝙋𝙀𝙇𝙏𝘼𝘼","𝙃𝙐𝙐𝙐","𝙇𝙊𝘿𝙀𝙀","𝘾𝙃𝘼𝘼𝙍","𝘾𝙃𝘼𝙒𝙉𝙄𝙄","𝙂𝙃𝙊𝘿𝙀𝙀","𝙋𝙀𝙀𝙀","𝙏𝙐𝙈𝙈","𝙈𝙀𝙍𝙀𝙀","𝙇𝙊𝘿𝙀𝙀","𝙋𝙀𝙀","𝙏𝙀𝙍𝙄",
           "𝙈𝘼𝘼","𝙆𝘼𝘼𝘼","𝘽𝙊𝙊𝘽𝙎","𝘿𝘼𝘽𝘼𝙏𝘼 𝙃𝙐", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙄", "𝘾𝙃𝙐𝙏", "𝘼𝙅𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙄", "𝘾𝙃𝙐𝙏",
           "𝙁𝘼𝘼𝘿", "𝘿𝙐𝙉𝙂𝘼", "𝙃𝙄𝙅𝘿𝙀", "𝙏𝙀𝙍𝘼", "𝘽𝘼𝘼𝙋","𝙃𝙐", "𝙆𝙄𝘿𝙓𝙓", "𝙎𝙋𝙀𝙀𝘿", "𝙋𝘼𝙆𝘼𝘿", "𝘽𝙃𝙀𝙉 𝙆𝙀 𝙇𝘼𝙐𝘿𝙀", "𝘼𝘼 𝘽𝙀𝙏𝘼",
           "𝘼𝘼𝙂𝙔𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼 ", "𝘾𝙃𝙊𝘿𝙉𝙀","𝘼𝘽", "𝙏𝙀𝙍𝙄 ", "𝙈𝘼𝘼", "𝘾𝙃𝙐𝘿𝙀𝙂𝙄", "𝙆𝙐𝙏𝙏𝙀", "𝙆𝙄", "𝙏𝘼𝙍𝘼𝙃", "𝘽𝙀𝙏𝘼",
           "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝘽𝙃𝙊𝙎𝘿𝙀", "𝙈𝙀", "𝙅𝘽𝙇", "𝙆𝙀", "𝙎𝙋𝙀𝘼𝙆𝙀𝙍", "𝘿𝘼𝘼𝙇", "𝙆𝘼𝙍", "𝘽𝘼𝙎𝙎", "𝘽𝙊𝙊𝙎𝙏𝙀𝘿", "𝙎𝙊𝙉𝙂",
           "𝙎𝙐𝙉𝙐𝙉𝙂𝘼", "𝙋𝙐𝙍𝙄","𝙍𝘼𝘼𝙏", "𝙇𝘼𝙂𝘼𝙏𝘼𝙍", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝙎𝘼𝙏𝙃", "𝙎𝙀𝙓", "𝙆𝘼𝙍𝙐𝙉𝙂𝘼🔥", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀",
           "𝘽𝙊𝙊𝘽𝙎","𝘿𝘼𝘽𝘼𝙐𝙉𝙂𝘼","𝙓𝙓𝙓","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼","𝙆𝘼𝘼","𝘾𝙃𝙐𝙏","𝙈𝘼𝙍𝙐","𝙍𝘼𝙉𝘿𝙄","𝙆𝙀𝙀","𝙋𝙄𝙇𝙀𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼","𝙆𝘼𝘼","𝘽𝙃𝙊𝙎𝘿𝘼𝘼",
           "𝙈𝘼𝙍𝙐","𝙎𝙐𝘼𝙍","𝙆𝙀𝙀","𝘾𝙃𝙊𝘿𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼","𝙆𝙀𝙀𝙀","𝙉𝙐𝘿𝙀𝙎","𝘽𝙀𝘾𝙃𝙐𝙉𝙂𝘼","𝙍𝘼𝙉𝘿𝙄","𝙆𝙀𝙀","𝙋𝙄𝙇𝙇𝙀","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼",
           "𝘾𝙃𝙊𝘿𝙐","𝙎𝙐𝘼𝙍","𝙆𝙀𝙀𝙀","𝙋𝙄𝙇𝙀𝙀","𝙏𝙀𝙍𝙄𝙄𝙄","𝙈𝘼𝘼𝘼","𝘿𝘼𝙄𝙇𝙔𝙔","𝘾𝙃𝙐𝘿𝙏𝙏𝙄","𝙃𝘼𝙄𝙄","𝙈𝘼𝘿𝙃𝘼𝙍𝘾𝙃𝙊𝘿","𝘼𝙐𝙆𝘼𝙏","𝘽𝘼𝙉𝘼𝘼",
           "𝙇𝙊𝘿𝙀","𝙏𝙀𝙍𝘼𝘼","𝘽𝘼𝘼𝙋","𝙃𝙐𝙐","𝙏𝙀𝙍𝙄","𝙂𝙁𝙁","𝙆𝘼𝘼","𝘾𝙃𝙐𝘿", "𝙂𝘼𝙔𝘼", "𝘽𝘼𝘾𝘾𝙃𝘼", "𝘽𝘼𝘼𝙋 𝙎𝙀",
           "𝘼𝙐𝙆𝘼𝙏 𝙈𝙀", "𝙍𝘼𝙃𝙊", "𝙒𝘼𝙍𝙉𝘼", "𝙈𝘼𝘼 𝘾𝙃𝙊𝘿 𝘿𝙀𝙉𝙂𝙀 𝙏𝙐𝙈𝘼𝙍𝙄","𝘽𝙃𝙊𝙎𝘿𝘼𝘼","𝙈𝘼𝙍𝙐𝙐","𝙈𝘼𝘿𝙃𝘼𝙍𝘾𝙃𝙊𝘿","𝙏𝙀𝙍𝙄 ","𝙉𝘼𝙉𝘼𝙄","𝙆𝘼𝘼",
           "𝘾𝙃𝙐𝙏𝙏","𝙈𝘼𝙍𝙐","𝙏𝙀𝙍𝙄𝙄","𝘽𝙀𝙃𝙀𝙉","𝙆𝘼𝘼𝘼","𝘽𝙃𝙊𝙎𝘿𝘼𝘼","𝙈𝘼𝙍𝙐","𝙍𝘼𝙉𝘿𝙄𝙄","𝙆𝙀𝙀𝙀","𝘾𝙃𝙊𝘿𝙀","𝙏𝙀𝙍𝙄","𝘿𝘼𝘿𝙄","𝙆𝘼𝘼𝘼","𝘽𝙊𝙊𝙍",
           "𝙂𝘼𝙍𝘼𝙈","𝙆𝘼𝙍𝙍","𝙏𝙀𝙍𝙀","𝙋𝙐𝙍𝙀𝙀","𝙆𝙃𝘼𝙉𝘿𝘼𝙉","𝙆𝙊𝙊𝙊","𝘾𝙃𝙊𝘿𝙐𝙉𝙂𝘼𝘼","𝘽𝘼𝘼𝙋","𝙎𝙀𝙀","𝘽𝘼𝙆𝘾𝙃𝙊𝘿𝙄","𝙆𝘼𝙍𝙀𝙂𝘼𝘼","𝙎𝙐𝘼𝙍𝙍",
           "𝙆𝙀𝙀𝙀","𝙋𝙄𝙇𝙇𝙀𝙀","𝙉𝘼𝘼𝙆","𝙈𝙀𝙀𝙀","𝙉𝙀𝙏𝘼𝘼","𝘽𝘼𝘼𝙋","𝙆𝙊𝙊","𝙆𝘼𝘽𝙃𝙄𝙄","𝙉𝘼𝘼𝙃","𝘽𝙊𝙇𝙉𝘼𝘼","𝘽𝙀𝙏𝘼𝘼","𝘾𝙃𝙐𝙎𝙎","𝙇𝙀𝙀𝙀",
           "𝙈𝙀𝙍𝘼𝘼","𝙇𝙊𝘿𝘼𝘼","𝙅𝘼𝙄𝙎𝙀","𝘼𝙇𝙐𝙐","𝙆𝘼𝘼𝘼","𝙋𝘼𝙆𝙊𝘿𝘼𝘼","𝙏𝙀𝙍𝙄","𝙈𝘼𝘼𝘼","𝘽𝙀𝙃𝙀𝙉","𝙂𝙁𝙁","𝙉𝘼𝙉𝙄","𝘿𝙄𝙄𝙉","𝙍𝘼𝘼𝙏","𝙎𝙊𝙏𝙀𝙀",
           "𝙅𝘼𝙂𝙏𝙀𝙀","𝙋𝙀𝙇𝙏𝘼𝘼","𝙃𝙐𝙐𝙐","𝙇𝙊𝘿𝙀𝙀","𝘾𝙃𝘼𝘼𝙍","𝘾𝙃𝘼𝙒𝙉𝙄𝙄","𝙂𝙃𝙊𝘿𝙀𝙀","𝙋𝙀𝙀𝙀","𝙏𝙐𝙈𝙈","𝙈𝙀𝙍𝙀𝙀","𝙇𝙊𝘿𝙀𝙀","𝙋𝙀𝙀","𝙏𝙀𝙍𝙄",
           "𝙈𝘼𝘼","𝙆𝘼𝘼𝘼","𝘽𝙊𝙊𝘽𝙎","𝘿𝘼𝘽𝘼𝙏𝘼 𝙃𝙐", "𝙏𝙀𝙍𝘼", "𝘽𝘼𝘼𝙋", "𝙃𝙐", "𝙆𝙄𝘿𝙓𝙓", "𝙎𝙋𝙀𝙀𝘿", "𝙋𝘼𝙆𝘼𝘿", "𝘽𝙃𝙀𝙉 𝙆𝙀 𝙇𝘼𝙐𝘿𝙀",
           "𝘼𝘼 𝘽𝙀𝙏𝘼", "𝘼𝘼𝙂𝙔𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼 ", "𝘾𝙃𝙊𝘿𝙉𝙀",
           "𝘼𝘽", "𝙏𝙀𝙍𝙄 ", "𝙈𝘼𝘼", "𝘾𝙃𝙐𝘿𝙀𝙂𝙄", "𝙆𝙐𝙏𝙏𝙀", "𝙆𝙄", "𝙏𝘼𝙍𝘼𝙃", "𝘽𝙀𝙏𝘼", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝘽𝙃𝙊𝙎𝘿𝙀",
           "𝙈𝙀", "𝙅𝘽𝙇", "𝙆𝙀", "𝙎𝙋𝙀𝘼𝙆𝙀𝙍", "𝘿𝘼𝘼𝙇", "𝙆𝘼𝙍", "𝘽𝘼𝙎𝙎", "𝘽𝙊𝙊𝙎𝙏𝙀𝘿", "𝙎𝙊𝙉𝙂", "𝙎𝙐𝙉𝙐𝙉𝙂𝘼", "𝙋𝙐𝙍𝙄",
           "𝙍𝘼𝘼𝙏", "𝙇𝘼𝙂𝘼𝙏𝘼𝙍", "𝙏𝙀𝙍𝙄", "𝙈𝘼𝘼", "𝙆𝙀", "𝙎𝘼𝙏𝙃", "𝙎𝙀𝙓", "𝙆𝘼𝙍𝙐𝙉𝙂𝘼🔥", "𝘾𝙃𝙐𝘿", "𝙂𝘼𝙔𝘼", "𝘽𝘼𝘾𝘾𝙃𝘼", "𝘽𝘼𝘼𝙋 𝙎𝙀",
           "𝘼𝙐𝙆𝘼𝙏 𝙈𝙀", "𝙍𝘼𝙃𝙊", "𝙒𝘼𝙍𝙉𝘼", "𝙈𝘼𝘼 𝘾𝙃𝙊𝘿 𝘿𝙀𝙉𝙂𝙀 𝙏𝙐𝙈𝘼𝙍𝙄"]


async def pyrone(client: Client, message: Message):
    chat_id = message.chat.id
    ruser = None

    if message.reply_to_message:
        ruser = message.reply_to_message.message_id
    
    try:
        for word in ONE_WORDS:
            await client.send_chat_action(chat_id, "typing")
            await client.send_message(chat_id, word, reply_to_message_id=ruser)
            await asyncio.sleep(0.3)
    except FloodWait:
        pass


async def restart(_, __):
    args = [sys.executable, "pyrone.py"]
    execle(sys.executable, *args, environ)


# ADDING HANDLERS

if M1:
    M1.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M1.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M2:
    M2.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M2.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M3:
    M3.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M3.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M4:
    M4.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M4.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))

if M5:
    M5.add_handler(MessageHandler(pyrone, filters.command(["T3RI", "L0L", "AJA", "AAJA", "START"], prefixes=None) & filters.me))
    M5.add_handler(MessageHandler(restart, filters.command(["XD", "FARAR", "STOP", "FUCKED"], prefixes=None) & filters.me))


# STARTING CLIENTS

if M1:
    M1.start()
    M1.join_chat("TheAltron")

if M2:
    M2.start()
    M2.join_chat("TheAltron")

if M3:
    M3.start()
    M3.join_chat("TheAltron")

if M4:
    M4.start()
    M4.join_chat("TheAltron")

if M5:
    M5.start()
    M5.join_chat("TheAltron")

print("Pyrone Started Successfully")

idle()


# STOPPING CLIENTS

if M1:
    M1.stop()

if M2:
    M2.stop()

if M3:
    M3.stop()

if M4:
    M4.stop()

if M5:
    M5.stop()
