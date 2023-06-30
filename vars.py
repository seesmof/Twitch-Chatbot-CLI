import os

# enter your bot token
GPT_TOKEN = ""

# enter your bot's nickname, without @
GPT_BOT_NICK = ""

# enter a delay between messages. set to 20 seconds by default
DELAY = 20  # in seconds

# enter the channel names you want your bot to work in
WANTED_CHANNELS = [
    # "yourChannelName",
    # "...",
]

# enter your potential log directory file path, below is just an example
log_dir = "C:/TwitchBot/logs/"
# Check if the log folder exists
if not os.path.exists(log_dir):
    # Create the log folder if it doesn't exist
    os.makedirs(log_dir)
