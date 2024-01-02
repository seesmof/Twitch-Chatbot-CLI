from click_shell import shell
import inquirer
from rich.markdown import Markdown as md
from rich.console import Console
from rich.traceback import install
from components.Bot import Bot

from utils.misc import openLiveChatWindow

install()
console = Console()
bot = Bot()


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
def stop() -> None:
    # stop the bot and close all live chats
    bot.stop()
    console.print("Stopping the bot...")


@the_shell.command()
def features() -> None:
    # allow user to configure the bot
    console.print("Configuring the bot...")


@the_shell.command()
def credentials() -> None:
    # allow user to toggle different features like Memory, Logging, Live Chat, and more
    console.print("Toggling bot's features...")


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
Here is a list of available commands:

- help: Show this help message
- start: Start the bot
- stop: Stop the bot
- credentials: Configure the bot
- features: Toggle bot's features
- quit: Exit the shell
"""
        )
    )
