from os import path
from typing import List, Tuple
import inquirer
from rich.console import Console
from rich.traceback import install
import json

install()
console = Console()


def openLiveChatWindow(console: object) -> None:
    console.print("Live chatting...")


currentDir = path.dirname(path.abspath(__file__))


def loadConfig() -> dict:
    with open(
        path.join(currentDir, "..", "..", "data", "config.json"), "r", encoding="utf-8"
    ) as f:
        return json.load(f)


def saveConfig(creds: dict) -> None:
    filePath = path.join(currentDir, "..", "..", "data", "config.json")
    with open(filePath, "w", encoding="utf-8") as f:
        json.dump(creds, f, indent=2)


def loadFeatures() -> dict:
    with open(
        path.join(currentDir, "..", "..", "data", "features.json"),
        "r",
        encoding="utf-8",
    ) as f:
        return json.load(f)


def configureFeatures(features: dict) -> None:
    featuresList = [(feat, val) for feat, val in features.items()]
    questions = [
        inquirer.Checkbox(
            "features",
            message="Select features using arrow keys",
            choices=[feat for feat, _ in featuresList],
            default=[feat for feat, val in featuresList if val],
        )
    ]
    answers = inquirer.prompt(questions)

    for feat in featuresList:
        features[feat[0]] = feat[0] in answers["features"]

    filePath = path.join(currentDir, "..", "..", "data", "features.json")
    with open(
        filePath,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(features, f, indent=2)

    console.print("[green]Features configured successfully[/]")

    return features


def changeCredentials(creds: dict) -> dict:
    credentialsList = [(cred, val) for cred, val in creds.items()]

    questions = [
        inquirer.List(
            "choice",
            message="What do you want to change?",
            choices=[cred for cred, _ in credentialsList],
        )
    ]
    answers = inquirer.prompt(questions)
    answer = answers["choice"]
    console.print(f"Old value: {creds[answer]}")

    if answer == "token":
        questions = [
            inquirer.Text(
                "token",
                message="Enter your new Access Token",
                validate=lambda _, x: x != "",
            )
        ]
        answers = inquirer.prompt(questions)
        creds["token"] = answers["token"]
    elif answer == "username":
        questions = [
            inquirer.Text(
                "username",
                message="Enter your new bot's username",
                validate=lambda _, x: x != "",
            )
        ]
        answers = inquirer.prompt(questions)
        creds["username"] = answers["username"]
    elif answer == "channels":
        questions = [
            inquirer.Text(
                "channels",
                message="Enter the channels you want to join separated by comma",
                validate=lambda _, x: x != "" and "," in x,
            )
        ]
        answers = inquirer.prompt(questions)
        creds["channels"] = answers["channels"].split(",")

    saveConfig(creds)
    console.print("[green]Credentials changed successfully[/]")

    return creds


def setupCredentials(creds: dict) -> None:
    credentialsList = [(cred, val) for cred, val in creds.items()]

    questions = [
        inquirer.Text(
            "token",
            message="Enter your Access Token",
            validate=lambda _, x: x != "",
        ),
        inquirer.Text(
            "username",
            message="Enter your bot's username",
            validate=lambda _, x: x != "",
        ),
        inquirer.Text(
            "channels",
            message="Enter the channels you want to join separated by comma",
            validate=lambda _, x: x != "" and "," in x,
        ),
    ]
    answers = inquirer.prompt(questions)
    answers["token"] = answers["token"].strip()
    answers["username"] = answers["username"].strip()
    answers["channels"] = answers["channels"].split(",")

    for key, value in answers.items():
        creds[key] = value

    saveConfig(creds)
    console.print("[green]Credentials configured successfully[/]")

    return creds
