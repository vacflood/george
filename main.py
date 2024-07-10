from   misc.bot      import Bot
from   misc.config   import Config

import asyncio

class George():
    def __init__(self) -> None:
        self.token = Config.get(value='token')

    @staticmethod
    def start(token: str) -> None:
        Bot.start(token=token)

asyncio.run(main=George().start(token=George().token))