import os
from personas import PERSONAS

# enter your bot token
TOKEN = ""

# enter your bot's nickname, without @
BOT_NICK = ""

# enter a delay between messages. set to 20 seconds by default
DELAY = 20  # in seconds

# enter the channel names you want your bot to work in
WANTED_CHANNELS = [
    "replaceWithYourChannelName",
    "addMoreIfNeeded",
]

# CAUTION: enter the users you don't want your bot to answer to. useful for preventing answering to other bots or just unwanted individuals using your bot.
BLOCKED_USERS = [
    "dontReplyToThisUser",
    "andThisOneToo",
]

# whether to allow the bot to have a memory of the previous chat messages. possible values are either True or False. set to True by default
ALLOW_MEMORY = True

# whether to log the chat messages to a file. possible values are either True or False
LOGGING = True

# replace with persona name you want to set, or type in the persona description you want, or simply leave empty if you don't want any persona
PERSONA = ""
# list of personas can be found in `personas.py` file, further information on setup specifics can be found in `more_on_vars.md` file

if LOGGING:
    # the path to a folder where the logs will be saved. feel free to change it to whichever one you want
    log_dir = "./logs/"
    # Check if the log folder exists
    if not os.path.exists(log_dir):
        # Create the log folder if it doesn't exist
        os.makedirs(log_dir)

if PERSONA in PERSONAS:
    PERSONA = PERSONAS[PERSONA]
