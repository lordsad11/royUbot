from ubot import *


__MODULE__ = "Joinvc"
__HELP__ = """
Bantuan Untuk Joinvc

• Perintah: <code>{0}leavevc</code>
• Penjelasan: Untuk meninggalkan voice chat grup.

• Perintah: <code>{0}joinvc</code>
• Penjelasan: Untuk bergabung voice chat grup.
"""


list_data = []


def remove_list(user_id):
    list_data[:] = [item for item in list_data if item.get("id") != user_id]


def add_list(user_id, text):
    data = {"id": user_id, "nama": text}
    list_data.append(data)


def get_list():
    if not list_data:
        return "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜsᴇʀ ᴅɪ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴍᴀɴᴀᴘᴜɴ</b>"

    msg = "\n".join(item["nama"] for item in list_data)
    return msg


@PY.UBOT("joinvc")
async def _(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    text = f"• <b>[{client.me.first_name} {client.me.last_name or ''}](tg://user?id={client.me.id})</b> | <code>{chat_id}</code>"
    try:
        await client.group_call.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    await message.reply("<b>Si Jamet Naek Ke Pohon</b>")
    await asyncio.sleep(5)
    await client.group_call.set_is_mute(True)
    add_list(client.me.id, text)


@PY.UBOT("leavevc")
async def _(client, message):
    try:
        await client.group_call.stop()
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    remove_list(client.me.id)
    return await message.reply("<b>Si Jamet Turun Dari Pohon</b>")


@PY.UBOT("listos")
async def _(client, message):
    await message.reply(get_list())

           
