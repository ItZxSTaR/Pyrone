from pyrogram.types import Message
import asyncio
from pyrogram import Client, filters
from helpers.data import OneWord
from config import *

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["l0l"], [""]))
async def oneword(onew: Client, e: Message):
      if e.reply_to_message:
          id = e.reply_to_message_id
          if int(id) in SUDO_USERS:
                await e.reply_text("BAAP KO GAALI MT DO")
          else:
              for msg in OneWord:
                await e.reply_text(msg, reply_to_message_id=id)
                await asyncio.sleep(0.2)
      else:
          for msg in OneWord:
            await onew.send_message(e.chat.id, msg)
            await asyncio.sleep(0.2)
