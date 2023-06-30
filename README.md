<a name="readme-top"></a>

<a href="./instruction_Ukraine.md"><strong>Інструкція Українською <img height="16" src="./interference/Ukraine.png" alt="external-national-flags-others-iconmarket-5" /></strong></a>

<div align="center">
<h1 align="center">Twitch AI Chathatbot</h1>
</div>

## Table of contents

- [Table of contents](#table-of-contents)
- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## About

This is a simple Twitch chatbot that generates messages using AI. The bot listens to messages in a specified channel and generates a response based on the input text.

## Prerequisites

- Make sure you have **Python** of version 3.10+ installed on your system
- Make sure you know how to work with and run commands in console

## Installation

1. Clone the repository by running

```
git clone https://github.com/seesmof/twitch-ai-chatbot.git
```

Or click this [link](https://github.com/seesmof/twitch-ai-chatbot/archive/refs/tags/0.1.1.zip), then unzip the archive onto your system.

2. Install the required dependencies by running

```
pip install -r requirements.txt
```

3. Visit the [link](https://twitchtokengenerator.com/), select the `Bot Chat Token` option when prompted, and copy the `Access Token` value.

4. Go to `vars.py` file and add change the following variables:

```py
# enter your bot token
GPT_TOKEN = ""

# enter your bot's nickname, without @
GPT_BOT_NICK = ""

# OPTIONAL: enter a delay between messages, if needed. set to 20 seconds by default
DELAY = 20  # in seconds

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

You can add as many channels as you want. Also make sure that there is no `#` sign in square brackets before the name of your channel. In Python, it denotes a comment, so all lines with this sign in front will be ignored by the program.

Regarding the delay between messages, keep in mind that it is optinal to change it. If you want your bot to send and process messages faster, feel free to change it. But do keep in mind that setting it too low might result in a temporary suspension of your bot's account, so I would not recommend setting it below **5 seconds**.

5. Run the bot using the following command:

```
python main.py
```

Or by just starting the `main.py` executable file on your computer. And you're all set! The bot will work as long as the file is running.

## Usage

Once the bot is up and running, it will listen to messages in the specified channel (or channels) and generate a response based on the input prompt.

To generate a message, mention the bot in your message by using `@<yourBotName>`. The bot will then generate a response based on the input text and send it to the chat.

The bot has a delay between each message of 20 seconds. If you want to change that, go to `main.py` file and change the number in brackets on line 25.

## License

This project is licensed under the [MIT License](./LICENSE).

<p align="right"><a href="#readme-top"><strong>Back to top</strong></a></p>
