

from ubot import *

__MODULE__ = "Afk"
__HELP__ = """
Bantuan Untuk Afk

• Perintah: <code>{0}afk</code> [alasan]
• Penjelasan: Untuk mengaktifkan mode afk.
"""


@PY.UBOT("afk"mo)
async def _(client, message):
    await set_afk(client, message)
    
    
async def _(client, message):
    await afk_er(client, message)
    
    
@ubot.on_message(filters.outgoing & filters.me & is_afk)
async def _(client, message):
    await no_afke(client, message)
