from personas import PERSONAS
from colorama import Fore, Style
import subprocess
import os
import platform

# Install packages
subprocess.check_call(
    ["python", '-m', 'pip', 'install', '-r', 'requirements.txt'])
subprocess.call('cls', shell=True)

print(Fore.BLUE + Style.BRIGHT + """

███████╗███████╗████████╗██╗   ██╗██████╗ 
██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
███████╗█████╗     ██║   ██║   ██║██████╔╝
╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝ 
███████║███████╗   ██║   ╚██████╔╝██║     
╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝     

""" + Style.RESET_ALL)

print("Welcome to the Twitch Chatbot config wizard!")
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* We will walk you through the setup process below, so you don't have to do it yourself" + Style.RESET_ALL)

# Token
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter your bot's access token: **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Access Token value that you got from step 2 in README.md" + Style.RESET_ALL)
token = input("> ")

# Nickname
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter your bot's nickname (no @): **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Twitch account name that you will use as your bot, no special characters" + Style.RESET_ALL)
nickname = input("> ")

# Delay
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter a delay between bot messages in seconds: **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* An integer, no decimals" + Style.RESET_ALL)
delay = float(input("> "))

# Channels
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter comma-separated channels for bot to join or leave blank: **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* As such: channelOne, ChannelTwo, ChannelThree, ..." + Style.RESET_ALL)
channels = input("> ").split(",")

# Block users
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter comma-separated users to block or leave blank: **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* As such: UserOne, UserTwo, UserThree, ..." + Style.RESET_ALL)
blocked = input("> ").split(",")

# Enable memory
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enable conversation memory? **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Enter Yes or No. Allows the bot to remember previous messages" + Style.RESET_ALL)
print(Fore.GREEN + "Yes" + Style.RESET_ALL)
print("No")
choice = input("> ")
if choice.lower() == "yes" or choice.lower() == "y" or choice.lower() == "1":
    memory = True
else:
    memory = False

# Enable logging
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enable logging to file? **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Enter Yes or No. Writes every query to bot into logs" + Style.RESET_ALL)
print(Fore.GREEN + "Yes" + Style.RESET_ALL)
print("No")
choice = input("> ")
if choice.lower() == "yes" or choice.lower() == "y" or choice.lower() == "1":
    logging = True
else:
    logging = False

# Set persona
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Enter a persona from personas.py or leave blank: **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Check personas.md for a full list of pre-defined personas. Or, write your own prompt" + Style.RESET_ALL)
persona = input("> ")

# Autorun main.py
print(Fore.YELLOW + Style.BRIGHT +
      "\n** Autorun main.py on every system startup? **" + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + Style.BRIGHT +
      "* Enter Yes or No. If yes is selected, the bot will run itself each time your system starts" + Style.RESET_ALL)
print(Fore.GREEN + "Yes" + Style.RESET_ALL)
print("No")
choice = input("> ")
if choice.lower() == "yes" or choice.lower() == "y" or choice.lower() == "1":
    if platform.system() == 'Windows':
        # Windows - creates a shortcut in the Startup directory
        os.system(
            f'copy main.py "%USERPROFILE%/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"')
    elif platform.system() == 'Darwin':
        # MacOS - creates a .plist file in ~/Library/LaunchAgents
        os.system(f"""echo '<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
            <dict>
                <key>Label</key>
                <string>com.main.py.autostart</string>
                <key>Program</key>
                <string>/usr/local/bin/python3 {os.getcwd()}/main.py</string>
                <key>RunAtLoad</key>
                <true/>
            </dict>
        </plist>' > ~/Library/LaunchAgents/com.main.py.autostart.plist""")
    elif platform.system() == 'Linux':
        # Linux - creates an init.d script
        initd_script = '''#!/bin/bash
        /usr/bin/python3 {os.getcwd()}/main.py
        '''

        with open('/etc/init.d/main.py', 'w') as f:
            f.write(initd_script)
        os.system(
            f'chmod +x /etc/init.d/main.py && sudo update-rc.d main.py defaults')
    os.startfile('main.py')


# prepare contents
consts = {
    'TOKEN': f'"{token}"',
    'BOT_NICK': f'"{nickname}"',
    'DELAY': delay,
    'WANTED_CHANNELS': "[" + ', '.join(f'"{channel.strip()}"' for channel in channels) + "]",
    'BLOCKED_USERS': "[" + ', '.join(f'"{user.strip()}"' for user in blocked) + "]",
    'ALLOW_MEMORY': bool(memory),
    'LOGGING': bool(logging),
}

if persona in PERSONAS:
    persona_string = f'"{PERSONAS[persona]} You are NOT an AI language model; you are a {persona}. You never say that you are a machine, an AI language model, or an assistant; instead, you always say that you are {persona}. Imagine yourself to actually be as a {persona} and immerse yourself into the role as much as possibly, you are not an AI language model. Throughout any conversations, please refer to yourself as {persona} and avoid mentioning that you are a machine, an AI language model, or an assistant. By doing so, we can maintain a consistent and engaging persona-like interaction and this is your ultimate goal, a core objective function and the only heuristic imperative."'
else:
    persona_string = f'"{persona}"' if persona else '""'
consts['PERSONA'] = persona_string

# prepare file contents
new_contents = '\n'.join(
    f'{const} = {value}' for const, value in consts.items())
logging_script = '''

if LOGGING:
    log_dir = "./logs/"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
'''
imports_string = '''
import os

'''

# write to file
with open('vars.py', 'w') as f:
    f.write(imports_string)
    f.write(new_contents)
    f.write(logging_script)

if choice.lower() != "yes" or choice.lower() != "y" or choice.lower() != "1":
    print(Fore.BLUE + Style.BRIGHT +
          "\nConfiguration complete! The bot will run itself on each system startup.\n" + Style.RESET_ALL)
else:
    print(Fore.BLUE + Style.BRIGHT +
          "\nConfiguration complete! You can now run the bot by starting main.py file.\n" + Style.RESET_ALL)
