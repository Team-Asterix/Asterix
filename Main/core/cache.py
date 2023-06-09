# Copyright (C) 2023-present by Team-Asterix@Github, < https://github.com/Team-Asterix >.
#
# This file is part of < https://github.com/Team-Asterix/Asterix > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/Team-Asterix/Asterix/blob/main/LICENSE >
#
# All rights reserved.


import logging


logger = logging.getLogger(__name__)


class Cache:
    def __init__(self, config, db, clients) -> None:
        self.config = config
        self.db = db
        self.clients = clients

    # async def init_all_custom_files(self):
    #     path_ = "./cache/"
    #     if not os.path.exists(path_):
    #         os.makedirs(path_)
    #         logger.info("Created cache directory")
    #     if alive_media := await self.config.get_env("ALIVE_MEDIA"):
    #         await custom_init(alive_media, suffix_file="alive", to_path=path_)
    #     if pm_media := await self.config.get_env("PM_MEDIA"):
    #         await custom_init(pm_media, suffix_file="pmpermit", to_path=path_)
    #     if bot_st_media := await self.config.get_env("CUSTOM_BOT_MEDIA"):
    # await custom_init(bot_st_media, suffix_file="bot_st_media",
    # to_path=path_)

    async def update_auto_post_cache(self):
        auto_post_db = self.db.make_collection("auto_post_s")
        for client in self.clients:
            if not self.config.AUTOPOST_CACHE.get(client.myself.id):
                self.config.AUTOPOST_CACHE[client.myself.id] = {}
            async for adb in auto_post_db.find({"client_id": client.myself.id}):
                if adb and adb.get("from_chat") and adb.get("to_chat"):
                    if not self.config.AUTOPOST_CACHE[client.myself.id].get(
                        int(adb["from_chat"])
                    ):
                        self.config.AUTOPOST_CACHE[client.myself.id] = {
                            int(adb.get("from_chat")): [int(adb.get("to_chat"))]
                        }
                    else:
                        self.config.AUTOPOST_CACHE[client.myself.id][
                            int(adb["from_chat"])
                        ].append(int(adb["to_chat"]))
