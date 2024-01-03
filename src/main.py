from click_shell import shell
import inquirer
from rich.markdown import Markdown as md
from rich.console import Console
from rich.traceback import install

from utils.misc import (
    changeCredentials,
    setupCredentials,
    configureFeatures,
    loadConfig,
    loadFeatures,
    openLiveChatWindow,
)
from components.Bot import Bot

install()
console = Console()
bot = None


@shell(prompt="> ")
def the_shell() -> None:
    console.print(
        "Welcome to Twitch AI Chatbot app! Enter 'help' for a list of commands."
    )

    features = loadFeatures()
    if features["autostart"]:
        start()


@the_shell.command()
def start() -> None:
    global bot
    credentials = loadConfig()
    if (
        credentials["token"] == ""
        or credentials["username"] == ""
        or credentials["channels"] == []
    ):
        setupCredentials(creds=credentials)

    features = loadFeatures()
    bot = Bot(
        token=credentials["token"],
        channels=credentials["channels"],
        haveLogging=features["logging"],
        haveMemory=features["memory"],
    )

    showChatQuestion = [
        inquirer.Confirm(
            "showChat",
            message="Do you want to see live chat?",
            default=False,
        )
    ]
    showChatAnswer = inquirer.prompt(showChatQuestion)
    openLiveChatWindow(console=console) if showChatAnswer["showChat"] else None

    try:
        bot.run()
    except Exception as e:
        return


@the_shell.command()
def stop() -> None:
    bot.close() if bot else console.print("Bot is not running")


@the_shell.command()
def feats() -> None:
    features = loadFeatures()
    features = configureFeatures(features=features)


@the_shell.command()
def creds() -> None:
    console.print(
        md(
            "You can get your token [here](https://twitchtokengenerator.com/). Select `Bot Chat Token` and then copy `Access Token` value"
        )
    )
    credentials = loadConfig()

    if (
        credentials["token"] != ""
        and credentials["username"] != ""
        and credentials["channels"] != []
    ):
        credentials = changeCredentials(creds=credentials)
    else:
        credentials = setupCredentials(creds=credentials)

    global bot
    bot = Bot(token=credentials["token"], channels=credentials["channels"])


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
Here is a list of available commands:

- start: Start the bot
- stop: Stop the bot
- creds: Configure the bot
- feats: Toggle bot's features
- help: Show this help message
- quit: Exit the shell
"""
        )
    )


if __name__ == "__main__":
    the_shell()
