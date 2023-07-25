import asyncio
from datetime import datetime
import time
from deep_translator import GoogleTranslator
import os
from langdetect import detect
import re

from vars import *
import g4f
messages = [
    {
        "role": "system",
        "content": PERSONA,
    },
]


#   <GENERATING MESSAGES>   #

def gpt4free(input_text, provider, model="gpt-3.5-turbo"):
    messages.append({
        "role": "user",
        "content": input_text
    })
    response = g4f.ChatCompletion.create(
        model=model,
        messages=messages,
        provider=provider
    )

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
    ]
    fallback_models = [
        "falcon-40b",
        "falcon-7b",
        "llama-13b",
    ]
    fallback_provider = g4f.Provider.H2o
    output_text = None

    for provider in providers:
        try:
            output_text = gpt4free(input_text, provider)
            break
        except Exception as e:
            print(f"Exception occurred for provider {provider}: {e}")
            continue

    if output_text is None:
        for model in fallback_models:
            try:
                output_text = gpt4free(input_text, fallback_provider, model)
                break
            except Exception as e:
                print(f"Exception occurred for fallback model {model}: {e}")
                continue

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nGenerated in {elapsed_time:.2f} seconds")

    if (detect(input_text) == "ua" or detect(input_text) == "ru") and detect(output_text) != "ua":
        output_text = GoogleTranslator(
            source='auto', target='ua').translate(output_text)
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


def write_to_log(message, author, CHANNEL):
    now = datetime.now()
    file_name = CHANNEL + "-log_" + now.strftime("%d-%m-%Y") + ".md"
    file_path = os.path.join(log_dir, file_name)

    try:
        with open(file_path, "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime('%H:%M:%S')
            log_file.write(timestamp)
            log_file.write(f"\n\n{author}: {message}\n")
            log_file.write(f"\n---\n\n")
    except:
        print(f"Could not write to {file_path}")
