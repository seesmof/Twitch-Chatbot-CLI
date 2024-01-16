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
        self.prompt: str = None
        self.prevUser: str = None

    async def event_ready(self):
        console.log(f"Bot started as '{self.nick}'")

    async def event_message(self, message):
        if message.author.name == self.nick:
            return

        if (
            message.content.startswith("!ai")
            or message.content.startswith("!generateMessage")
            or message.content.startswith(f"@{self.nick}")
        ):
            givenPrompt: str = (
                message.content.split(" ", 1)[1] if " " in message.content else None
            )
            self.prompt = givenPrompt if givenPrompt else None
            self.prevUser = message.author.name if self.prompt else None

            console.log(f"{message.author.name} asked: {self.prompt}")

        try:
            await self.handle_commands(message)
        except AttributeError:
            pass

    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(aliases=["ai"])
    async def generateMessage(self, ctx: commands.Context):
        if self.prompt:
            pass
        else:
            console.log(
                f"[red]Failed to generate message from {ctx.author.name} in {ctx.channel.name}[/]"
            )

    async def event_command_error(
        self, context: commands.Context, error: Exception
    ) -> None:
        pass
