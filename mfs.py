import asyncio
from datetime import datetime
import time
import os
import re
import json
import g4f
from vars import *

system_prompt = {
    "role": "system",
    "content": PERSONA
}
messages = []


def AI(input_text):
    messages.append({
        "role": "user",
        "content": input_text
    })
    messages.append(system_prompt)
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            provider=g4f.Provider.DeepAi
        )
    except Exception as e:
        print(f"\n{e}\n")
        response = "Whoops... Something went wrong"
    messages.pop()

    if ALLOW_MEMORY:
        messages.append({
            "role": "assistant",
            "content": response,
        })
    else:
        messages.pop()
    return clean_text(response)


def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'www\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\".*?\"', '', text)
    text = re.sub(r'\*', '', text)
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'user: ', '', text, flags=re.I)
    text = re.sub(r'system: ', '', text, flags=re.I)
    text = re.sub(r'assistant: ', '', text, flags=re.I)
    text = text.replace(" : ", "")
    text = text.replace(f"{BOT_NICK}", "")
    text = text.replace(f"@", "")
    return text


def split_long_gpt(input_string):
    num_substrings = len(input_string) // 440 + \
        (1 if len(input_string) % 440 > 0 else 0)
    substrings = [input_string[i * 440:(i + 1) * 440]
                  for i in range(num_substrings)]
    return substrings


def check_for_letters(text, letters):
    for letter in letters:
        if letter in text:
            return True
    return False


def write_to_log(input_message, author, channel, output_message):
    now = datetime.now()
    file_name = f"{channel}_{now.strftime('%d-%m-%Y')}.json"
    file_path = os.path.join(log_dir, file_name)

    log_data = {
        'PROMPT': input_message,
        'RESPONSE': output_message,
        'USER': author,
        'CHANNEL': channel,
        'TIME': now.strftime("%H:%M:%S"),
        'LOGGING': LOGGING,
        'DELAY': DELAY,
        'ALLOW_MEMORY': ALLOW_MEMORY,
    }

    try:
        with open(file_path, "a", encoding="utf-8") as log_file:
            log_file.write(json.dumps(log_data) + "\n")
    except IOError as e:
        print(f"Could not write to {file_path}: {e}")
