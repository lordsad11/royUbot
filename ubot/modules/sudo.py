from ubot import *
 
@PY.UBOT("addsudo")
async def _(client, message):
     await addsudo_cmds(client, message)
     
     
@PY.UBOT("delsudo")
async def _(client, message):
     await delsudo_cmds(client, message)
     
@PY.UBOT("getsudo")
async def _(client, message):
     await getsudo_cmds(client, message)  
