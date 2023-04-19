# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


import pathlib


def get_all_files_in_path(path):
    path = pathlib.Path(path)
    return [i.absolute() for i in path.glob("**/*")]
