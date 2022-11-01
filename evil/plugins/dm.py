from pyrogram import filters, Client
from pyrogram.types import Message
import asyncio
from helpers.data import *
from config import *


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmfuck"], ["."]))
async def dmfuck(xspam: Client, e: Message):
    dmpy = e.text.split(" ", 1)
    if e.reply_to_message and len(dmpy) != 2:
        id = e.reply_to_message_id
        if int(id) in SUDO_USERS:
            await e.reply_text("BAAP KO GAALI MT DO")
        else:
            for msg in OneWord:
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.1)
    else:
        ok = await xspam.get_users(dmpy[1])
        id = ok.id
        if int(id) in SUDO_USERS:
            await e.reply_text("BAAP KO GAALI MT DO")
        else:
            for msg in OneWord:
                await xspam.send_message(id, msg)
                await asyncio.sleep(0.1)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["dmspam"], ["."]))
async def dmspam(xspam: Client, e: Message):
    usage = ""
    try:
        dmpy = e.text.split(" ", 3)
    except:
        dmpy = e.text.split(" ", 2)

    if e.reply_to_message and len(dmpy) != 4:
        id = e.reply_to_message_id
        if int(id) in SUDO_USERS:
            await e.reply_text("BAAP KO GAALI MT DO")
        else:
            for _ in range(int(dmpy[1])):
                await xspam.send_message(id, dmpy[2])
                await asyncio.sleep(0.2)
    elif len(dmpy) == 4:
        ok = await xspam.get_users(dmpy[1])
        id = ok.id
        if int(id) in SUDO_USERS:
            await e.reply_text("BAAP KO GAALI MT DO")
        else:
            for _ in range(int(dmpy[2])):
                await xspam.send_message(id, dmpy[3])
                await asyncio.sleep(0.1)
    else:
        await e.reply_text(usage)
