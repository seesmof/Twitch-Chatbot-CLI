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

3. Set up a Twitch account and create a new application [here](https://dev.twitch.tv/console/apps/create) to get your `irc_token` and `client_id`.

For more information on that, read [this file](./setup_bot.md)

4. Go to `vars.py` file and add change the following variables:

```
GPT_TMI_TOKEN = '<your_irc_token>'
GPT_CLIENT_ID = '<your_client_id>'
GPT_BOT_NICK = '<your_bot_nickname>'
BOT_PREFIX = '<your_bot_prefix>'
```

5. Provide a channel where you want to run your bot by modifying the `CHANNEL` variable in the `main.py` file.

6. Run the bot using the following command:

```
python main.py
```

## Usage

Once the bot is up and running, it will listen to messages in the specified channel and generate a response based on the input text.

To generate a message, mention the bot in your message by using `@<bot_nickname>`. The bot will then generate a response based on the input text and send it to the chat.

Note: The bot is currently set up to generate messages in English. If you want to generate messages in Ukrainian, follow the instructions given in a `main.py` file
