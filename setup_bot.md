## How to configure your Twitch bot account

To get the bot working you need to have a Twitch account registered. Once you do, follow the instructions below and get all the necessary information to proceed and run the bot

### 1. Get TMI token

First, you need a TMI token. Considering you already have a Twitch account registered, just follow the link below, copy the token and paste it into a corresponding variable in `vars.py` file

https://twitchapps.com/tmi/

### 2. Get client ID

Now that we have a token, let's create a client ID. You will need to follow the steps below to accoplish that

1. Got to [Twitch Developer Console](https://dev.twitch.tv/console/apps/create)
2. Create an application and provide the following data
   - Name: can be any name you want
   - OAuth Redirect URLs: if you are running the bot on your own computer, just enter `https://localhost`
   - Category: select Chat Bot
3. Once the application is created, you will have your client ID right in there, if you click `Manage` button

Okay, now just paste it into a variable in `vars.py` file

---

And, we're pretty much done here! It is that easy, now you just have to specify the name of your Twitch account in a corresponding variable in `vars.py` file and you're good to go. Now you just have to run the script and the bot will be live
