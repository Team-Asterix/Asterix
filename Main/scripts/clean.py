# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.

import pathlib


work_dir = pathlib.Path(__file__).parent.absolute()

for path in work_dir.rglob("*.py[co]"):
    print(f"Removed '{path}'")
    path.unlink()

for dir in work_dir.rglob("__pycache__"):
    print(f"Removed '{dir}'")
    dir.rmdir()

print("\nAll Clean")
