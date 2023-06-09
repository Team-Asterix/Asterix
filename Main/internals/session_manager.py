# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


from Main import Altruix
from pyrogram import filters
from Main.core.decorators import log_errors
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup


@Altruix.bot.on_message(filters.command("add", "/") & filters.user(Altruix.auth_users))
@log_errors
async def add_session_command_handler(_, m: Message):
    if m.from_user.id not in Altruix.auth_users:
        return await m.reply_text("Hey, I'm just a bot. Powered by @AltruixUB.")
    await m.reply(
        "Do you have the string session already generated?.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Yes", callback_data="session_yes"),
                    InlineKeyboardButton("No", callback_data="session_no"),
                ]
            ]
        ),
    )
