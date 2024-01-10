from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from components.validators import Config, Features
from components.Bot import Bot
from utils.misc import readJson


currentDir = path.dirname(path.abspath(__file__))
configFile = path.join(currentDir, "..", "data", "config.json")
featuresFile = path.join(currentDir, "..", "data", "features.json")
logsFile = path.join(currentDir, "..", "data", "logs.db")
personasFile = path.join(currentDir, "..", "data", "personas.json")


def main():
    configData = readJson(configFile)
    featuresData = readJson(featuresFile)
    personas = readJson(personasFile)["personas"]

    config = Config(**configData)
    console.print(
        f"Token: {config.token if config.token else 'None'}, Username: {config.username if config.username else 'None'}, Channels: {config.channels if config.channels else 'None'}",
    )

    features = Features(**featuresData)
    console.print(
        f"Delay: {features.delay if features.delay else 'None'}, Memory: {'Yes' if features.memory else 'No'}, Persona: {features.persona if features.persona else 'None'}, Logging: {'Yes' if features.logging else 'No'}, Model: {features.model.upper() if features.model else 'None'}",
    )

    console.print(personas["Darth Vader"])


if __name__ == "__main__":
    main()
