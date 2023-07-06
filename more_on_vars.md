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
```

> **Quick Note**: The specified values of _"replaceWithYourChannelName"_, _"addMoreIfNeeded"_, _"dontReplyToThisUser"_, and _"andThisOneToo"_ are merely placeholders, please understand that. Make sure to change them or remove completely.

Lets quickly run through each of those.

- `TOKEN` - here you enter your bot's `Access Token` that you've gotten from the earlier steps of setting it up;
- `BOT_NICK` - here you simply enter your bot's account name or nickname. You don't have to add any other characters to it, like `@` or something else, just enter the name of the account you created for your bot;
- `DELAY` - _**optional**_ variable, you can leave it as it is. Pretty self-explanatory though, just a delay between each message of your bot. Although, do keep in mind that setting the value too low might result in a temporary suspension of your bot's account, so I would not recommend setting it below **5 seconds**;
- `WANTED_CHANNELS` - a list of channels where you want your bot to work. It can be just one channel, or it can be many channels, up to you. There is no limit on the amount of channels you can specify there, as far as I'm concerned. Same deal as with the bot nickname, make sure to enter the names of Twitch channels just as they are displayed on their pages, no extra characters;
- `BLOCKED_USERS` - _**optional**_ varaible. A list of users you don't want to interract with your bot. The bot will ignore all the messages from the specified users. It can be useful for preventing it from answering to other bots in your chat. But use with **caution**, make sure not to put the names of wanted channels in this list, this will result in streamers not being able to use the bot in their own chat.
