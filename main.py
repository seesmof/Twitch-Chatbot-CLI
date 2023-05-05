from twitchio.ext import commands
import asyncio
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
    # print message to console
    print(f"{GPT_BOT_NICK} is online at {CHANNEL}!")
    # write log message using mfs module
    mfs.write_to_log(f"is online at {CHANNEL}!", GPT_BOT_NICK, CHANNEL)


@ bot.event
async def event_message(ctx):
    # Check if the message is from the GPT bot, and if so, log the message and return
    if ctx.author.name.lower() == GPT_BOT_NICK.lower():
        print(f"\nBOT: {ctx.content}")
        mfs.write_to_log(ctx.content, GPT_BOT_NICK, CHANNEL)
        return

    # Check if the message contains a bot nickname in it
    letters = [f"@{GPT_BOT_NICK}"]
    if mfs.check_for_letters(ctx.content.lower(), letters):
        # Preprocess the input text
        input_text = ctx.content.replace(f"@{GPT_BOT_NICK}", "")
        input_text = " ".join(input_text.split())
        output_text = "@" + ctx.author.name + ", "

        # ATTENTION: If you want your messages to be generated in Ukrainian - change the line below to this:
        # output_text += mfs.generate_ua(input_text)
        # So, pretty much, just change the function to generate_ua
        output_text += mfs.generate_en(input_text)

        # Send the generated message in chunks
        await mfs.send_split_gpt(ctx, output_text)

    # Wait for 1 second before continuing
    await asyncio.sleep(1)

if __name__ == "__main__":
    bot.run()
