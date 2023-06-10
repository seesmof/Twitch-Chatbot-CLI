import os

# enter your bot token
GPT_TOKEN = ""

# enter your bot's nickname, without @
GPT_BOT_NICK = ""

# enter your potential log directory file path, below is just an example
log_dir = "C:/TwitchBot/logs/"
# Check if the log folder exists
if not os.path.exists(log_dir):
    # Create the log folder if it doesn't exist
    os.makedirs(log_dir)
