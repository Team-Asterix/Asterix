# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


# ====================================
# **REQUIRES MULTICLIENT FORMATTING **
# ====================================

import asyncio
from Main import Altruix
from pyrogram import Client as client


async def set_inline_in_botfather(Client: client):
    await Client.send_message("botfather", "/cancel")
    await asyncio.sleep(1)
    message = await Client.send_message("botfather", "/setinline")
    await asyncio.sleep(1)
    await message.reply(f"@{Altruix.bot_info.username}")
    await asyncio.sleep(1)
    await message.reply("Powered by Altruix")
    await asyncio.sleep(1)
