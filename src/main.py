"""
We can have one window be opened as a menu for user to toggle all the features on/off, enter their credentials, see the logs and so on. And when the user chooses an option to start the bot, a new terminal window will be opened to start the bot.
"""

import inquirer
from click_shell import shell
from rich.markdown import Markdown as md
from rich.console import Console
from rich.traceback import install

install()
console = Console()


@shell(prompt="> ")
def the_shell() -> None:
    console.print(
        "Welcome to Twitch AI Chatbot app! Enter 'help' for a list of commands."
    )


@the_shell.command()
def start() -> None:
    """
    Starts the bot in a new terminal window, but also checks for valid credentials
    """
    pass


@the_shell.command()
def creds() -> None:
    """
    Allows user to configure the bot's credentials
    """
    console.print(
        md(
            "You can get your token [here](https://twitchtokengenerator.com/). Select `Bot Chat Token` and then copy `Access Token` value"
        )
    )


@the_shell.command()
def feats() -> None:
    """
    Allows user to toggle the bot's features on/off
    """
    pass


@the_shell.command()
def logs() -> None:
    """
    View the bot's logs
    """
    pass


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
Here is a list of available commands:

- start: Start the bot
- creds: Configure the bot
- feats: Toggle bot's features
- logs: View the bot's logs
- help: Show this help message
- quit: Exit the shell
"""
        )
    )


if __name__ == "__main__":
    the_shell()
