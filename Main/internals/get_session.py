# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


import re
import glob
import asyncio
import contextlib
from Main import Altruix
from pyrogram import filters
from Main.core.decorators import log_errors
from pyrogram.types import (
    Message, ForceReply, CallbackQuery, KeyboardButton, ReplyKeyboardMarkup,
    ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup)


@Altruix.bot.on_message(filters.command("start", "/") & filters.private)
@log_errors
async def start_command_handler(_, m: Message):
    payload = m.text.replace("/start", "").strip()
    if not payload:
        path_ = "./cache/bot_st_media.*"
        file = (
            glob.glob(path_)[0] if glob.glob(path_) else "./Main/assets/images/logo.jpg"
        )
        await m.reply_file(
            file,
            caption=Altruix.get_string("BOT_ST_MSG").format(
                m.from_user.mention, Altruix.config.CUSTOM_BT_START_MSG or ""
            ),
            reply_markup=ReplyKeyboardRemove(),
            send_msg_if_file_invalid=True,
        )
        if Altruix.training_wheels_protocol and m.from_user.id in Altruix.auth_users:
            await m.reply(
                "You'll have to add a user session to disable TWP, would you like to proceed?",
                reply_markup=ReplyKeyboardMarkup(
                    [[KeyboardButton("Yeah sure")]],
                    resize_keyboard=True,
                    one_time_keyboard=True,
                ),
            )
            _ = await m.from_user.listen()
            await m.reply(
                "Alright, let's get started.", reply_markup=ReplyKeyboardRemove()
            )
            await asyncio.sleep(1)
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
    elif payload == "add_session":
        await m.reply("Alright, let's get started.", reply_markup=ReplyKeyboardRemove())
        await asyncio.sleep(1)
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


@Altruix.bot.on_callback_query(filters.regex("^add_session"))
@log_errors
async def add_session_menu_cb_handler(_, cb: CallbackQuery):
    await cb.message.edit(
        "Alright, let's get started.", reply_markup=ReplyKeyboardRemove()
    )
    await asyncio.sleep(1)
    await cb.message.reply(
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


@Altruix.bot.on_callback_query(filters.regex("^session_yes"))
@log_errors
async def add_session_cb_handler(_, cb: CallbackQuery):
    with contextlib.suppress(Exception):
        await cb.message.delete()
    await cb.message.reply(
        "Alright... send me your string session.\nUse /cancel to cancel the current operation.",
        reply_markup=ForceReply(),
    )
    # session = await cb.from_user.listen(filters.regex(r"(\S{300,400})",
    # timeout=600))
    while True:
        session: Message = await cb.from_user.listen(filters.text, timeout=600)
        if session.text.startswith("/"):
            await cb.message.reply("The current process was cancelled.")
            return
        if match := re.search(r"(\S{300,400})", session.text):
            session = match[1]
            break
        else:
            await session.reply("Please send me a valid string session.", quote=True)
    status = await cb.message.reply(
        "<code>Processing the given string session...</code>"
    )
    new_session = await Altruix.add_session(session, status)
    await new_session.send_message(
        Altruix.bot.info.id,
        "<b>Asterix have been successfully connected with your account!</b> \nPlease visit @AltruixUB for any support or help!",
    )
