# Twitch Chatbot with AI Integration

This is a simple Twitch chatbot that generates messages using AI. The bot listens to messages in a specified channel and generates a response based on the input text.

## Installation

1. Clone the repository

```
git clone https://github.com/seesmof/twitch-ai-chatbot.git
```

2. Install the required dependencies

```
pip install -r requirements.txt
```

3. Visit the [link](https://twitchtokengenerator.com/), select the `Bot Chat Token` option when prompted, and copy the token.

4. Go to `vars.py` file and add change the following variables:

```py
# enter your bot token
GPT_TOKEN = ""

# enter your bot's nickname, without @
GPT_BOT_NICK = ""

# enter the channel names you want your bot to work in
WANTED_CHANNELS = [
    # "yourChannelName",
    # "...",
]
```

Example of a working channels list:

```py
WANTED_CHANNELS = [
    "yourChannelName",
    "anotherChannelName",
    "yetAnotherChannelName",
]
```

You can add as many channels as you want.

5. Run the bot using the following command:

```
python main.py
```

## Usage

Once the bot is up and running, it will listen to messages in the specified channel (or channels) and generate a response based on the input prompt.

To generate a message, mention the bot in your message by using `@<yourBotName>`. The bot will then generate a response based on the input text and send it to the chat.

The bot has a delay between each message of 20 seconds. If you want to change that, go to `main.py` file and change the number in brackets on line 25.
