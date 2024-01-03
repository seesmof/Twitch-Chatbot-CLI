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
        json.dump(features, f, indent=4)

    console.print("[green]Features configured successfully[/]")

    return features
