<a name="readme-top"></a>

<a href="./README_Ukrainian.md"><strong>Інструкція Українською</strong></a>

<div align="center">
<h1 align="center">Twitch AI Chathatbot</h1>
</div>

## Table of contents

- [Table of contents](#table-of-contents)
- [About](#about)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Automatic](#automatic)
  - [Manual](#manual)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

This is a simple Twitch chatbot that generates messages using AI. The bot listens to messages in a specified channel and generates a response based on the input text.

## Prerequisites

- Make sure you have **Python** of version 3.10+ installed on your system
- Make sure you know how to work with and run commands in console

## Installation

### Automatic

1. Download [package](https://github.com/seesmof/twitch-ai-chatbot/archive/refs/tags/1.3.2.zip), then unzip the archive onto your system.

2. Visit the [link](https://twitchtokengenerator.com/), select the `Bot Chat Token` option when prompted, and copy the `Access Token` value.

3. Run `setup.py` file. This will set all the necessary variables, dependencies, etc. for you. After that you can either choose to add the script to autorun on every system start or manually run `main.py` whenever you want your bot to start working.

### Manual

1. Clone the repository by running

```
git clone https://github.com/seesmof/twitch-ai-chatbot.git
```

Or click this [link](https://github.com/seesmof/twitch-ai-chatbot/archive/refs/tags/1.3.2.zip), then unzip the archive onto your system.

2. Install the required dependencies by running

```
pip install -r requirements.txt
```

3. Visit the [link](https://twitchtokengenerator.com/), select the `Bot Chat Token` option when prompted, and copy the `Access Token` value.

4. Follow [these instructions](./more_on_vars.md) to set up the necessary variables.

5. Run the bot using the following command:

```
python main.py
```

Or by just starting the `main.py` executable file on your computer. And you're all set! The bot will work as long as the file is running.

## Usage

Once the bot is up and running, it will listen to messages in the specified channel (or channels) and generate a response based on the input prompt.

To generate a message, mention the bot in your message by using `@<yourBotName>`. The bot will then generate a response based on the input text and send it to the chat.

The bot has a delay between each message of 20 seconds. If you want to change that, go to `main.py` file and change the number in brackets on line 25.

## Contributing

Contributions of any kind are welcome! Please check out the [contributing guide](CONTRIBUTING.md) for more info on how to get started.

## License

This project is licensed under the [MIT License](./LICENSE).

<p align="right"><a href="#readme-top"><strong>Back to top</strong></a></p>
