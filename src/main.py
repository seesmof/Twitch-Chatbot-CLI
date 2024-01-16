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

from os import path
from rich.console import Console
from rich.traceback import install

install()
console = Console()

from components.validators import Config, Features
from components.Bot import Bot
from utils.misc import readJson


currentDir = path.dirname(path.abspath(__file__))
logsPath = path.join(currentDir, "..", "data", "logs.db")

configPath = path.join(currentDir, "..", "data", "config.json")
featuresPath = path.join(currentDir, "..", "data", "features.json")
personasPath = path.join(currentDir, "..", "data", "personas.json")

configData = readJson(configPath)
featuresData = readJson(featuresPath)
personas = readJson(personasPath)["personas"]


def main():
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
