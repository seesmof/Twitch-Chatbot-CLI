from os import path
import json
from src.archive.personas import PERSONAS
import inquirer
from rich.markdown import Markdown as md
from rich.table import Table
from rich.console import Console
from rich.traceback import install

install()
console = Console()

currentDir = path.dirname(path.abspath(__file__))
personasFile = path.join(currentDir, "data", "personas.json")
personas = {name.title(): description for name, description in PERSONAS.items()}
console.print(personas)
with open(personasFile, "w", encoding="utf-8") as f:
    json.dump(personas, f, indent=2)

"""
We can have just one window, as I haven't figured out how to open and then close a given terminal window, and plus its not too sustainable for different platforms anyway, so we will have just one. But, in it we will first load our credentials and check if they are not empty. If they're not, just set them to the bot and ask user if they want to toggle any features on and off. The features will include:

- delay
- memory
- persona
- logging

And if user answers yes we show the menu with ability to change those features and then start the bot. How exactly do we do it is the question though. Do we just ask the user if they would like to edit anything else after they edited some feature and then show the menu again? Probably thats the way. Okay, we'll figure it out later when we get there. So for right now to finally make an MVP we need to just load the credentials, set them to whichever ones work just for testing, and then we start the bot. Here's a brief schematic outline of what i just laid out:

- Load credentials
    - If not empty, set them to the bot
    - If empty, prompt user to enter credentials
- Load features
- Prompt user to toggle features
    - If agree, list the features and prompt to choose which one to edit
    - If not, just start the bot
- Start the bot in any case after the features are manipulated
"""
