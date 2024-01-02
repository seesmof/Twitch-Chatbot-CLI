from twitchio.ext import commands
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class TwitchAgent(commands.Bot):
    def __init__(self, token, prefix, channels):
        super().__init__(
            token=token,
            prefix=prefix,
            initial_channels=channels,
        )

    async def event_ready(self):
        console.log("[green]Bot connected![/]")

    async def event_message(self, message):
        console.log()
        await self.handle_commands(message)

    async def start(self):
        await self.start()

    async def stop(self):
        await self.close()
