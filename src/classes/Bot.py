from rich.console import Console
from rich.traceback import install

from classes.TwitchAgent import TwitchAgent

install()
console = Console()


class Bot:
    def __init__(self, token, prefix, channels):
        self.bot: object = TwitchAgent(token, prefix, channels)
        self.isAuthorized: bool = False

    def start(self, muteConsole=False):
        try:
            if self.bot.token and self.bot.prefix and self.bot.channels:
                self.isAuthorized = True
            self.bot.start() if self.isAuthorized else console.print(
                "[red]Not authorized![/]"
            )
        except Exception as e:
            console.log(f"[red]Failed to start bot: {e}[/]")

        console.print("[green]Bot started![/]") if not muteConsole else None

    def stop(self, muteConsole=False):
        try:
            self.bot.stop()
        except Exception as e:
            console.log(f"[red]Failed to stop bot: {e}[/]")

        console.print("[green]Bot stopped![/]") if not muteConsole else None

    def _restart(self, muteConsole=False):
        try:
            self.stop(muteConsole=True)
            self.start(muteConsole=True)
        except Exception as e:
            console.log(f"[red]Failed to restart bot: {e}[/]")

        console.print("[green]Bot restarted![/]") if not muteConsole else None

    def config(self, newToken, newPrefix, newChannels):
        self.bot.token = newToken
        self.bot.prefix = newPrefix
        self.bot.channels = newChannels
        self._restart(muteConsole=True)
        console.print("[green]Bot config updated![/]")
