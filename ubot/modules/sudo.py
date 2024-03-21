from ubot import *
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
 
 
@PY.UBOT("addsudo")
async def _(client, message):
     await addsudo_cmd(client, message)
     
     
@PY.UBOT("delsudo")
async def _(client, message):
     await delsudo_cmd(client, message)
     
@PY.UBOT("getsudo")
async def _(client, message):
     await getsudo_cmd(client, message)  
