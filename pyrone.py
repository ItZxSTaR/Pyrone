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


ONE_WORDS = ["TERI", "MAA", "KI", "CHUT", "AJA", "TERI", "MAA", "KI", "CHUT", "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP",
           "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA", "AAGYA", "TERI", "MAA ", "CHODNE",
           "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE",
           "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE", "BOOBS",
           "DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA",
           "LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERI", "MAA", "KI", "CHUT", "AJA", "TERI", "MAA", "KI", "CHUT",
           "FAAD", "DUNGA", "HIJDE", "TERA", "BAAP","HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE", "AA BETA",
           "AAGYA", "TERI", "MAA ", "CHODNE","AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA",
           "TERI", "MAA", "KE", "BHOSDE", "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG",
           "SUNUNGA", "PURI","RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "TERI", "MAA", "KE",
           "BOOBS","DABAUNGA","XXX","TERI","MAA","KAA","CHUT","MARU","RANDI","KEE","PILEE","TERI","MAA","KAA","BHOSDAA",
           "MARU","SUAR","KEE","CHODE","TERI","MAAA","KEEE","NUDES","BECHUNGA","RANDI","KEE","PILLE","TERI","MAAA",
           "CHODU","SUAR","KEEE","PILEE","TERIII","MAAA","DAILYY","CHUDTTI","HAII","MADHARCHOD","AUKAT","BANAA",
           "LODE","TERAA","BAAP","HUU","TERI","GFF","KAA","CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI","BHOSDAA","MARUU","MADHARCHOD","TERI ","NANAI","KAA",
           "CHUTT","MARU","TERII","BEHEN","KAAA","BHOSDAA","MARU","RANDII","KEEE","CHODE","TERI","DADI","KAAA","BOOR",
           "GARAM","KARR","TERE","PUREE","KHANDAN","KOOO","CHODUNGAA","BAAP","SEE","BAKCHODI","KAREGAA","SUARR",
           "KEEE","PILLEE","NAAK","MEEE","NETAA","BAAP","KOO","KABHII","NAAH","BOLNAA","BETAA","CHUSS","LEEE",
           "MERAA","LODAA","JAISE","ALUU","KAAA","PAKODAA","TERI","MAAA","BEHEN","GFF","NANI","DIIN","RAAT","SOTEE",
           "JAGTEE","PELTAA","HUUU","LODEE","CHAAR","CHAWNII","GHODEE","PEEE","TUMM","MEREE","LODEE","PEE","TERI",
           "MAA","KAAA","BOOBS","DABATA HU", "TERA", "BAAP", "HU", "KIDXX", "SPEED", "PAKAD", "BHEN KE LAUDE",
           "AA BETA", "AAGYA", "TERI", "MAA ", "CHODNE",
           "AB", "TERI ", "MAA", "CHUDEGI", "KUTTE", "KI", "TARAH", "BETA", "TERI", "MAA", "KE", "BHOSDE",
           "ME", "JBL", "KE", "SPEAKER", "DAAL", "KAR", "BASS", "BOOSTED", "SONG", "SUNUNGA", "PURI",
           "RAAT", "LAGATAR", "TERI", "MAA", "KE", "SATH", "SEX", "KARUNGA🔥", "CHUD", "GAYA", "BACCHA", "BAAP SE",
           "AUKAT ME", "RAHO", "WARNA", "MAA CHOD DENGE TUMARI"]


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
