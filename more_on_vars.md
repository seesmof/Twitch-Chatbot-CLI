## Variables

The given `vars.py` file, which is the only file you have to touch if you just want to get your bot to work out of the box, contains the following variables:

```py
TOKEN = ""

BOT_NICK = ""

DELAY = 20

WANTED_CHANNELS = [
    "replaceWithYourChannelName",
    "addMoreIfNeeded",
]

BLOCKED_USERS = [
    "dontReplyToThisUser",
    "andThisOneToo",
]

ALLOW_MEMORY = True

LOGGING = True

PERSONA = ""
```

> **Quick Note**: The specified values of _"replaceWithYourChannelName"_, _"addMoreIfNeeded"_, _"dontReplyToThisUser"_, and _"andThisOneToo"_ are merely placeholders, please understand that. Make sure to change them or remove completely.

Lets quickly run through each of those.

- `TOKEN` - here you enter your bot's `Access Token` that you've gotten from the earlier steps of setting it up;
- `BOT_NICK` - here you simply enter your bot's account name or nickname. You don't have to add any other characters to it, like `@` or something else, just enter the name of the account you created for your bot;
- `DELAY` - _**optional**_ variable, you can leave it as it is. Pretty self-explanatory though, just a delay between each message of your bot. Although, do keep in mind that setting the value too low might result in a temporary suspension of your bot's account, so I would not recommend setting it below **5 seconds**;
- `WANTED_CHANNELS` - a list of channels where you want your bot to work. It can be just one channel, or it can be many channels, up to you. There is no limit on the amount of channels you can specify there, as far as I'm concerned. Same deal as with the bot nickname, make sure to enter the names of Twitch channels just as they are displayed on their pages, no extra characters;
- `BLOCKED_USERS` - _**optional**_ varaible. A list of users you don't want to interract with your bot. The bot will ignore all the messages from the specified users. It can be useful for preventing it from answering to other bots in your chat. But use with **caution**, make sure not to put the names of wanted channels in this list, this will result in streamers not being able to use the bot in their own chat;
- `ALLOW_MEMORY` - a variable that can be either `True` or `False`, meant for switching on and off short-term memory for the bot. If set to `True`, the bot will preserve the context of the conversation. If set to `False`, it will answer to each query independently. Set to `True` by default;
- `LOGGING` - a variable that can be either `True` or `False`, meant for switching on and off the logging of chat messages. The logs are in `.md` format and are, by default, sent to the `logs` folder in root directory. Feel free to change the path for the logging folder to whichever one you like, just make sure its valid. The list is not exhaustive and will be updated with new names over time.
- `PERSONA` - a variable for enabling personification of the model by defining a persona for it either by selecting from the existing list in `personas.py` or typing in your own prompt, or just leaving it empty to disable the feature. **KEEP IN MIND**: to select a model from the list, just type in the exact name of it, all in caps, into the `PERSONA` variable like so: `PERSONA = "GERALT"`, this will set the persona to the desired one. The list of all available predefined personas can be found in `personas.py` file. A guide on how to write your own personas can be found [here](./add_own_persona.md)
