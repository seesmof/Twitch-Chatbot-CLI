from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install
import inquirer
from click_shell import shell

from utils import openLiveChatWindow

install()
console = Console()


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


@the_shell.command()
def stop() -> None:
    # stop the bot and close all live chats
    console.print("Stopping the bot...")


@the_shell.command()
def config() -> None:
    # allow user to configure the bot
    console.print("Configuring the bot...")


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
Here is a list of available commands:

- help: Show this help message
- start: Start the bot
- stop: Stop the bot
- config: Configure the bot
- quit: Exit the shell
"""
        )
    )


if __name__ == "__main__":
    the_shell()
