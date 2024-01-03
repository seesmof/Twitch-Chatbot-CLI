from rich.console import Console
from rich.traceback import install
from twitchio.ext import commands

install()
console = Console()


class Bot(commands.Bot):
    def __init__(self, token="", prefix="!", channels=[]):
        super().__init__(token=token, prefix=prefix, initial_channels=channels)

    async def start(self):
        await self.start()

    async def restart(self):
        await self.restart()

    async def event_ready(self):
        console.log("[green]Bot connected![/]")

    async def event_message(self, message):
        console.log()
        await self.handle_commands(message)
