import os

# enter your bot token in format "oauth:..."
GPT_TMI_TOKEN = ""

# enter your client id
GPT_CLIENT_ID = ""

# enter your bot's nickname, without @
GPT_BOT_NICK = ""

# leave this as it is, unless you know what you're doing
BOT_PREFIX = "!"

# enter your potential log directory file path, below is just an example
log_dir = "C:/TwitchBot/logs/"
# Check if the log folder exists
if not os.path.exists(log_dir):
    # Create the log folder if it doesn't exist
    os.makedirs(log_dir)
