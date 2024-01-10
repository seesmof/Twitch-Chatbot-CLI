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


"""
We can have just one window, as I haven't figured out how to open and then close a given terminal window, and plus its not too sustainable for different platforms anyway, so we will have just one. But, in it we will first load our credentials and check if they are not empty. If they're not, just set them to the bot and ask user if they want to toggle any features on and off. The features will include:

- delay
- memory
- persona
- logging
- AI model

And if user answers yes we show the menu with ability to change those features and then start the bot. How exactly do we do it is the question though. Do we just ask the user if they would like to edit anything else after they edited some feature and then show the menu again? Probably thats the way. Okay, we'll figure it out later when we get there. So for right now to finally make an MVP we need to just load the credentials, set them to whichever ones work just for testing, and then we start the bot. Here's a brief schematic outline of what i just laid out:

- Load credentials
    - If not empty, set them to the bot
    - If empty, prompt user to enter credentials
- Load features
- Prompt user to toggle features
    - If agree, list the features and prompt to choose which one to edit
    - If not, just start the bot
- Start the bot in any case after the features are manipulated

personaQuestion = [
    inquirer.List(
        "persona",
        message="Pick a persona for the bot",
        choices=["None"] + list(personas.keys()),
        default="None",
    )
]
personaAnswer = inquirer.prompt(personaQuestion)
persona = personas[personaAnswer["persona"]]
console.print(persona)
"""
