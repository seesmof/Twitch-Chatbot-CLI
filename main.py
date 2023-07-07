from twitchio.ext import commands
from vars import *
from mfs import *


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(token=TOKEN,
                         prefix='!', initial_channels=WANTED_CHANNELS)
        self.lock = asyncio.Lock()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        async with self.lock:
            letters = [f"@{BOT_NICK}"]
            output_text = ""
            print(
                f'Message from {message.author.name}: {message.content}. Channel: {message.channel.name}')

            if check_for_letters(message.content.lower(), letters) and message.author.name != BOT_NICK and message.author.name not in BLOCKED_USERS:
                output_text = generate_ai_message(message.content)
                split_text = split_long_gpt(output_text)
                for substr in split_text:
                    await message.channel.send(f"{substr} @{message.author.name}")
                    await asyncio.sleep(DELAY)

            if LOGGING:
                if message.author is not None:
                    write_to_log(message.content, message.author.name,
                                 message.channel.name)
                    write_to_log(output_text, BOT_NICK.upper(),
                                 message.channel.name)
                    print(
                        f"Query from {message.author.name} in {message.channel.name} as well as the response to it by {BOT_NICK} were successfully logged.")
                else:
                    write_to_log(message.content, "UNKNOWN",
                                 message.channel.name)
                    write_to_log(output_text, BOT_NICK.upper(),
                                 message.channel.name)
                    print(
                        f"Query from UNKNOWN in {message.channel.name} as well as the response to it by {BOT_NICK} were successfully logged.")


bot = Bot()
bot.run()
