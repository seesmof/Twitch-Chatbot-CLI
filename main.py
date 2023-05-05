from twitchio.ext import commands
from datetime import datetime
import asyncio
import time
import mfs
from vars import *

# provide a channel, where you wanna run your bot, below
CHANNEL = ""
bot = commands.Bot(
    irc_token=GPT_TMI_TOKEN,
    client_id=GPT_CLIENT_ID,
    nick=GPT_BOT_NICK,
    prefix=BOT_PREFIX,
    initial_channels=[CHANNEL]
)


@ bot.event
async def event_ready():
    print(f"{GPT_BOT_NICK} is online at {CHANNEL}!")
    mfs.write_to_log(f"is online at {CHANNEL}!", GPT_BOT_NICK, CHANNEL)


@ bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == GPT_BOT_NICK.lower():
        print(f"\nBOT: {ctx.content}")
        mfs.write_to_log(ctx.content, GPT_BOT_NICK, CHANNEL)
        return

    letters = [f"@{CHANNEL}"]
    if mfs.check_for_letters(ctx.content.lower(), letters):
        print("\nGenerating a message...")
        start_time = time.time()

        input_text = ctx.content.replace(f"@{CHANNEL}", "")
        input_text = " ".join(input_text.split())
        output_text = "@" + ctx.author.name + ", "

        # ATTENTION: If you want your messages to be generated in Ukrainian - change the line below to this:
        # output_text += mfs.generate_ua(input_text)
        # So, pretty much, just change the function to generate_ua
        output_text += mfs.generate_en(input_text)

        end_time = time.time()
        elapsed_time = end_time - start_time
        await mfs.send_split_gpt(ctx, output_text)
        print(f"\nGenerated in {elapsed_time:.2f} seconds")
    await asyncio.sleep(1)


if __name__ == "__main__":
    bot.run()
