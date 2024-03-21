from ubot import *
from pyrogram import Client, errors, filters
from pyrogram.types import ChatPermissions, Message
 
 
 __MODULE__ = "Sudo"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴜᴅᴏ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>addsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴜsᴇʀ ᴋᴇ ᴅᴀʟᴀᴍ ᴅᴀғᴛᴀʀ sᴜᴅᴏ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>delsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ᴜsᴇʀ ᴅᴀʀɪ ᴅᴀғᴛᴀʀ sᴜᴅᴏ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>getsudo</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ᴅᴀғᴛᴀʀ sᴜᴅᴏ
"""
 
@PY.UBOT("addsudo")
async def _(client, message):
     await addsudo_cmd(client, message)
     
     
@PY.UBOT("delsudo")
async def _(client, message):
     await delsudo_cmd(client, message)
     
@PY.UBOT("getsudo")
async def _(client, message):
     await getsudo_cmd(client, message)  
