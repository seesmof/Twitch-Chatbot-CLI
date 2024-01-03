from click_shell import shell
import inquirer
from rich.markdown import Markdown as md
from rich.console import Console
from rich.traceback import install
from components.Bot import Bot

from utils.misc import configureFeatures, loadFeatures, openLiveChatWindow
from components.Bot import Bot

install()
console = Console()
TOKEN = ""
CHANNELS = []

bot = Bot(token=TOKEN, channels=CHANNELS)


@shell(prompt="> ")
def the_shell() -> None:
    console.print(
        "Welcome to Twitch AI Chatbot app! Enter 'help' for a list of commands."
    )


@the_shell.command()
def start() -> None:
    # start the bot, ask if they want to see live chat
    # before starting, check if all the variables are in place. if not, prompt to enter all the data first
    # if yes, start a new terminal window with the live twitch chat
    console.print("Starting the bot...")
    showChatQuestion = [
        inquirer.Confirm(
            "showChat",
            message="Do you want to see live chat?",
            default=False,
        )
    ]
    showChatAnswer = inquirer.prompt(showChatQuestion)

    openLiveChatWindow(console=console) if showChatAnswer["showChat"] else None
    bot.start(muteConsole=True)


@the_shell.command()
def feats() -> None:
    # allow user to toggle different features like Memory, Logging, Live Chat, and more
    """
    - Logging
    - Memory
    - Auto-Start
    """
    features = loadFeatures()
    features = configureFeatures(features=features)
    console.print("Restarting the bot...")


@the_shell.command()
def creds() -> None:
    # allow user to configure the bot
    console.print(
        md(
            "You can get your token [here](https://twitchtokengenerator.com/). Select `Bot Chat Token` and then copy `Access Token` value"
        )
    )
    console.print("Configuring the bot...")


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
Here is a list of available commands:

- start: Start the bot
- creds: Configure the bot
- feats: Toggle bot's features
- help: Show this help message
- quit: Exit the shell
"""
        )
    )


if __name__ == "__main__":
    the_shell()
