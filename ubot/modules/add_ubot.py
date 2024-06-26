from ubot import *


@PY.CALLBACK("crot")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("bayar")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@PY.CALLBACK("addubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@PY.CALLBACK("cek")
@PY.BOT("getubot", FILTERS.SUDO)
async def _(client, message):
    await cek_ubot(client, message)


@PY.CALLBACK("cekmasa")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@PY.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def _(client, callback_query):
    await tools_userbot(client, callback_query)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)

    
@PY.CALLBACK("^(prev_ub|next_ub)")
async def _(client, callback_query):
    await next_prev_ubot(client, callback_query)
