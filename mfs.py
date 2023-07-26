import asyncio
from datetime import datetime
import time
from deep_translator import GoogleTranslator
import os
from langdetect import detect
import re
import json

from vars import *
import g4f
system_prompt = {
    "role": "system",
    "content": PERSONA
}
messages = []


#   <GENERATING MESSAGES>   #

def gpt4free(input_text, provider, model="gpt-3.5-turbo"):
    messages.append({
        "role": "user",
        "content": input_text
    })
    messages.append(system_prompt)
    response = g4f.ChatCompletion.create(
        model=model,
        messages=messages,
        provider=provider
    )
    messages.pop()

    if ALLOW_MEMORY:
        messages.append({
            "role": "assistant",
            "content": response,
        })
    else:
        messages.pop()

    return clean_text(response)


def generate_ai_message(message):
    start_time = time.time()
    input_text = message.replace(f"{BOT_NICK}", "")
    input_text = input_text.replace("@", "")

    providers = [
        g4f.Provider.DeepAi,
        g4f.Provider.AItianhu,
        g4f.Provider.Aichat,
        g4f.Provider.GetGpt,
        g4f.Provider.EasyChat,
        g4f.Provider.Acytoo,
        g4f.Provider.DfeHub,
        g4f.Provider.AiService,
        g4f.Provider.BingHuan,
        g4f.Provider.Wewordle,
        g4f.Provider.ChatgptAi,
        g4f.Provider.H2o,
    ]

    for provider in providers:
        try:
            output_text = gpt4free(input_text, provider)
            if output_text is None or " is not working" in output_text or output_text == "":
                continue
            else:
                break
        except Exception as e:
            continue

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nGenerated in {elapsed_time:.2f} seconds")

    if (detect(input_text) == "uk" or detect(input_text) == "ru") and detect(output_text) != "uk":
        output_text = GoogleTranslator(
            source='auto', target='uk').translate(output_text)
    return output_text


# Below are supplementary functions, just leave them as they are, unless you know what you're doing

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
    return text


def split_long_gpt(input_string):
    num_substrings = len(input_string) // 440 + \
        (1 if len(input_string) % 440 > 0 else 0)
    substrings = [input_string[i * 440:(i + 1) * 440]
                  for i in range(num_substrings)]
    return substrings


async def send_split_gpt(ctx, message):
    substrings_list = split_long_gpt(message)
    for substring in substrings_list:
        await ctx.channel.send(substring)
        await asyncio.sleep(2)


def split_long_message(input_string):
    words = input_string.split()
    result = []
    for i in range(0, len(words), 10):
        result.append(" ".join(words[i:i+10]))
    return result


async def send_split_message(ctx, message):
    substrings_list = split_long_message(message)
    for substring in substrings_list:
        await ctx.channel.send(substring)
        await asyncio.sleep(6)


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
