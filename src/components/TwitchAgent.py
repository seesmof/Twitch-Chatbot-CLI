from twitchio.ext import commands


class TwitchAgent(commands.Bot):
    def __init__(self, token, prefix, channels):
        super().__init__(
            token=token,
            prefix=prefix,
            initial_channels=channels,
        )

    def start(self):
        pass

    def stop(self):
        pass
