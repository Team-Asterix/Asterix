# Copyright (C) 2023-present by Altruix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


class NoDatabaseConnected(Exception):
    def __init__(self, message):
        super().__init__(message)


class Package404(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class AlreadyInstalled(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class InvalidPackageToUpdate(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EnvVariableTypeError(Exception):
    def __init__(self, message):
        super().__init__(message)


class InvalidInputTime(Exception):
    def __init__(self, message):
        super().__init__(message)
