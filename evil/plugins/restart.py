import sys
from pyrogram.types import Message
from helpers.command import commandpro
from pyrogram import Client
from os import execle, environ
from helpers.decorators import errors, sudo_users_only


@Client.on_message(commandpro(["xd"]))
@errors
@sudo_users_only
async def stop(_, message: Message):
    args = [sys.executable, "main.py"]
    execle(sys.executable, *args, environ)
    return
