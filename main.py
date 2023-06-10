from twitchio.ext import commands
from vars import *
from mfs import *


class Bot(commands.Bot):
    def __init__(self):
        # ! Replace CHANNEL with your wanted channel name. You can also add multiple channels, just separate them with a comma
        super().__init__(token=GPT_TOKEN,
                         prefix='!', initial_channels=[f'{CHANNEL}'])
        self.lock = asyncio.Lock()

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        async with self.lock:
            letters = [f"@{GPT_BOT_NICK}"]
            if check_for_letters(message.content.lower(), letters) and message.author.name != f"{GPT_BOT_NICK}":
                output_text = generate_ai_message(
                    message.content, message.author.name)
                output_text = split_long_gpt(output_text)
                for substr in output_text:
                    await message.channel.send(f"{substr}, @{message.author.name}")
                    await asyncio.sleep(20)
            write_to_log(message.content, message.author.name,
                         message.channel.name)


bot = Bot()
bot.run()
