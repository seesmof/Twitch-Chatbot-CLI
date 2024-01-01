messages = [
    "dirty brick roof poem dot above however leather we work pupil dug tube success afraid log according engine you steep neck verb light short",
    "instance characteristic magic stove tool clearly income happily other biggest book bright pine engine progress author day hidden unhappy trace heading log lamp whatever",
    "hole control separate managed eat else bound creature describe soon activity develop even arrow feed plane diagram lost congress doing native sell driver fun",
    "sell sight plan road gradually neck ground her occasionally lower upon bound start huge available particles sad caught difference due burn time exclaimed pile",
    "leather warm troops smile large here ought correctly known stock bright did discuss see air slow blood exciting pair wonder then beat ten paid",
    "ill safe major try air automobile week summer village substance putting fun sun count experience listen everywhere naturally gentle roof unusual travel longer visitor",
    "bend color electric among breathe hope control least curve pink honor mice smooth type blue land number relationship news guard function center hello city",
    "recall buried roof twelve happen outline average doing likely strange naturally forgot captain throat pale watch fairly rain meal angry education trace else box",
    "managed deep including tall met field seven cotton forgot moving flies saw spend eager chapter death movie ordinary special improve avoid more aside missing",
    "dust muscle edge development naturally worry birds ordinary review softly goes refused couple tower living real owner event little temperature money view poetry exchange",
    "offer row courage coming new donkey use sunlight up when mind dinner active soldier would rising present atmosphere neck band natural musical money rich",
    "sheep solution forest faster course cool shall earlier prevent command toy claws whom knife remove cream rising we metal solar nature three drew creature",
    "learn sitting science as tool cold smoke pure fifty possibly book there excitement either behavior one single exclaimed clothes fairly shoe score design surrounded",
    "grass tree future fort citizen factory got distance visit noon hold standard pet cost wing shake crowd themselves waste exercise extra realize country rose",
    "which single dig me invented darkness agree color coal rich nearest shoe physical gather aside not opposite tank introduced mark log feature crop herself",
    "pay dollar shop wheel mirror against lead sun bow moving furniture stood together cold clothes built consider turn solution upward point location shoot try",
]

from time import sleep
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install
import inquirer
from click_shell import shell

install()
console = Console()


@shell(prompt="> ")
def the_shell() -> None:
    console.print(
        "Welcome to my CLI project template.\nEnter 'help' for a list of commands."
    )


@the_shell.command()
def help() -> None:
    console.print(
        md(
            """
This is just a template for a CLI project.

Here is a list of available commands:

- help: Show this help message
- quit: Exit the shell
"""
        )
    )


def liveChat() -> None:
    for message in messages:
        console.print(message)
        sleep(2)


@the_shell.command()
def meow() -> None:
    catQuestions = [
        inquirer.List(
            "type",
            message="What type of meow do you want?",
            choices=["meow", "purr", "woof", "furr"],
        ),
        inquirer.Text(
            "name",
            message="What is your name?",
            default="Stranger",
            validate=lambda _, x: x != "",
        ),
    ]
    catAnswers = inquirer.prompt(catQuestions)
    console.print(f"Meow, {catAnswers['name']} is a {catAnswers['type']}!")


if __name__ == "__main__":
    liveChat()
