from datetime import datetime
import os
import asyncio
import time
import re
from vars import *
import g4f
from deep_translator import GoogleTranslator
from langdetect import detect
from g4f.Provider import (
    Yqcloud,
    Aichat,
    Lockchat,
    ChatgptLogin,
    DeepAi,
    GetGpt,
)

providers_list = [
    DeepAi,
    GetGpt,
    Aichat,
    Yqcloud,
    Lockchat,
    ChatgptLogin,
]
messages = []
# TODO: Add an option to turn off memory for the bot using a separate variable in vars.py


#   <GENERATING MESSAGES>   #

def gpt4free_ua(input_text, input_provider):
    response = gpt4free(input_text, input_provider)
    response = GoogleTranslator(
        source='auto', target='uk').translate(response)
    return response


def gpt4free_en(input_text, input_provider):
    input_prompt = GoogleTranslator(
        source='auto', target='en').translate(input_text)
    response = gpt4free(input_prompt, input_provider)
    return response


def gpt4free(input_text, input_provider):
    messages.append({
        "role": "user",
        "content": input_text
    })
    response = g4f.ChatCompletion.create(
        model=g4f.Model.gpt_35_turbo,
        messages=messages,
        provider=input_provider
    )
    messages.append({
        "role": "assistant",
        "content": response,
    })
    return clean_text(response)


def clean_text(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'www\S+', '', text)
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\".*?\"', '', text)
    text = re.sub(r'\*', '', text)
    text = re.sub(r'\n', ' ', text)
    text = text.replace(" : ", "")

    return text


def generate_ai_message(message):
    print("\nGenerating a message...\n")
    start_time = time.time()

    input_text = message.replace(f"{GPT_BOT_NICK}", "")
    input_text = input_text.replace("@", "")
    output_text = ""
    lang = detect(input_text)

    if lang == "uk" or lang == "ru":
        print("Language is Ukrainian")
        try:
            output_text = gpt4free_ua(input_text, providers_list[0])
        except:
            providers_list.remove(providers_list[0])
        if output_text == "" or output_text == None or output_text == "None":
            print(f"Response not generated")
            providers_list.remove(providers_list[0])
            for provider in providers_list:
                try:
                    output_text = gpt4free_ua(input_text, provider)
                    if output_text != "" or output_text != None or output_text != "None":
                        break
                    else:
                        continue
                except:
                    print(f"Response not generated")
                    providers_list.remove(provider)
    else:
        print("Language is NOT Ukrainian")
        try:
            output_text = gpt4free_en(input_text, providers_list[0])
        except:
            providers_list.remove(providers_list[0])
        if output_text == "" or output_text == None or output_text == "None":
            print(f"Response not generated")
            providers_list.remove(providers_list[0])
            for provider in providers_list:
                try:
                    output_text = gpt4free_en(input_text, provider)
                    if output_text != "" or output_text != None or output_text != "None":
                        break
                    else:
                        continue
                except:
                    print(f"Response not generated")
                    providers_list.remove(provider)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"\nGenerated in {elapsed_time:.2f} seconds")
    return output_text


# Below are supplementary functions, just leave them as they are, unless you know what you're doing


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

    with open(file_path, "a", encoding="utf-8") as log_file:
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_file.write(timestamp)
        log_file.write(f"\n\n{author}: {message}\n")
        log_file.write(f"\n---\n\n")
