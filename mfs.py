import openai
import os
import asyncio
import gpt4free
from gpt4free import Provider
from deep_translator import GoogleTranslator
from vars import *
from datetime import datetime


#   <GENERATING MESSAGES>   #

# if you want to generate messages using OpenAI API, feel free to provide your API key below
openai.api_key = ""

# if you do end up providing an API key, here is a default AI model - quite powerful, yet cheap one
model_engine = "gpt-3.5-turbo"


def openai_generate(input_text, context):
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": context},
            {"role": "user", "content": input_text}
        ],
        max_tokens=280,
        temperature=0.7,
    )
    output_text = response['choices'][0]['message']['content']
    return output_text


# If you either don't have an OpenAI API key or simply don't want to use it, you can just use the functions below, which I recommend
# But if you do end up using the OpenAI API, make sure to change the corresponding function in main file


def generate_ua(input_text):
    input_prompt = GoogleTranslator(
        source='auto', target='en').translate(input_text)
    response = gpt4free.Completion.create(
        Provider.You, prompt=input_prompt)
    response = GoogleTranslator(
        source='en', target='uk').translate(response)
    return response


def generate_en(input_text):
    input_prompt = GoogleTranslator(
        source='auto', target='en').translate(input_text)
    response = gpt4free.Completion.create(
        Provider.You, prompt=input_prompt)
    return response


def split_long_gpt(input_string):
    num_substrings = len(input_string) // 475 + \
        (1 if len(input_string) % 475 > 0 else 0)
    substrings = [input_string[i * 475:(i + 1) * 475]
                  for i in range(num_substrings)]
    return substrings


# Below are supplementary functions, just leave them as they are, unless you know what you're doing


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
        await asyncio.sleep(2)


def check_for_letters(text, letters):
    for letter in letters:
        if letter in text:
            return True
    return False


def write_to_log(message, author, CHANNEL):
    # for handling current time
    now = datetime.now()
    # for handling the file name
    file_name = CHANNEL + "-log_" + now.strftime("%d-%m-%Y") + ".md"
    # for handling the file path
    file_path = os.path.join(log_dir, file_name)

    # open file with appropriate decoding
    with open(file_path, "a", encoding="utf-8") as log_file:
        # declare and output timestamp before message
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_file.write(timestamp)
        # output message with author name to log
        log_file.write(f"\n\n{author}: {message}\n")
        log_file.write(f"\n---\n\n")
