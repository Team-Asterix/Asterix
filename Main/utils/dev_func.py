# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


import sys
import shlex
import asyncio
import traceback
from io import StringIO
from Main import Altruix
from pprint import pprint
from pyrogram import Client
from pyrogram.types import Message


p = print
pp = pprint


async def execute_py(c: Client, code: str, m: Message):
    exec(
        "async def __exec_py(c, m):"
        + "\n rm = m.reply_to_message"
        + "\n message = m"
        + "\n client = Client = c"
        + "\n chat = m.chat"
        + "\n user = m.from_user"
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__exec_py"](c, m)


async def eval_py(client: Client, code: str, m: Message):
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await execute_py(client, code, m)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = Altruix.get_string("NO_OUTPUT")
    return evaluation.strip()


async def exec_terminal(command: str):
    success = True
    return_code = 0
    command = shlex.split(command)
    output = ""
    try:
        process = await asyncio.create_subprocess_exec(
            *command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
        )
        return_code = process.returncode
        stdout, stderr = await process.communicate()
        output += stdout.decode("utf-8").strip()
        if stderr:
            output += "\n" + stderr.decode("utf-8").strip()
        success = True
    except Exception:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        errors = traceback.format_exception(etype=exc_type, value=exc_obj, tb=exc_tb)
        success = False
        output += errors[-1]
    return success, output, return_code


Altruix.__setattr__("run_cmd", exec_terminal)
Altruix.__setattr__("eval_py", eval_py)
