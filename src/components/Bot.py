from rich.console import Console
from rich.traceback import install
from twitchio.ext import commands

install()
console = Console()


class Bot(commands.Bot):
    def __init__(
        self,
        token="",
        prefix="!",
        channels=[],
        haveMemory: bool = False,
        haveLogging: bool = False,
    ):
        super().__init__(token=token, prefix=prefix, initial_channels=channels)
        self.haveMemory = haveMemory
        self.haveLogging = haveLogging

    async def restart(self):
        await self.restart()

    async def event_ready(self):
        console.log(f"[green]Bot connected![/]")

    async def event_message(self, message):
        console.print(message.content)
        await self.handle_commands(message)
