from twitchio.ext import commands
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from mfs import *


class Bot(commands.Bot):
    def __init__(self, token: str = None, prefix: str = "!", channels: [str] = []):
        super().__init__(
            token=token,
            prefix=prefix,
            initial_channels=channels,
        )
        self.prompt: str = None
        self.messages: [dict] = [
            {"role": "system", "content": "Answer as briefly as possible."}
        ]

    async def event_ready(self):
        console.log(f"Bot started as '{self.nick}'")

    async def event_message(self, message):
        if message.echo:
            return

        if message.content.startswith("!ai"):
            givenPrompt: str = (
                message.content.split(" ", 1)[1] if " " in message.content else None
            )
            self.prompt = givenPrompt if givenPrompt else None
            console.log(f"{message.author.name} asked: {self.prompt}")

        try:
            await self.handle_commands(message)
        except AttributeError:
            pass

    @commands.cooldown(rate=1, per=5, bucket=commands.Bucket.user)
    @commands.command(aliases=["ai"])
    async def processPrompt(self, ctx: commands.Context):
        if self.prompt:
            with console.status("Generating response..."):
                response = generateResponse(self.prompt, self.messages)

            """
            if logging:
                write to logs
            """

            partitionedText = (
                splitMessage(response) if len(response) > 440 else [response]
            )
            for text in partitionedText:
                await ctx.channel.send(f"{text} @{ctx.author.name}")

        else:
            console.log(
                f"[red]Failed to generate message from {ctx.author.name} in {ctx.channel.name}[/]"
            )

    async def event_command_error(
        self, context: commands.Context, error: Exception
    ) -> None:
        pass


# TODO load config and features from files, check if config is empty and if so prompt to enter values that are missing
bot = Bot()
bot.run()
