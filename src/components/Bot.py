from typing import List
from twitchio.ext import commands
from rich.console import Console
from rich.traceback import install

install()
console = Console()


class Bot(commands.Bot):
    def __init__(self, token: str = None, prefix: str = "!", channels: List[str] = []):
        super().__init__(
            token=token,
            prefix=prefix,
            initial_channels=channels,
        )

    async def event_ready(self):
        console.log(f"Bot started as '{self.nick}'")

    async def event_message(self, message):
        console.print(message.content)
        try:
            await self.handle_commands(message)
        except AttributeError:
            pass

    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(aliases=["ai"])
    async def generateMessage(self, ctx: commands.Context):
        pass

    async def event_command_error(
        self, context: commands.Context, error: Exception
    ) -> None:
        pass


bot = Bot()
bot.run()
