from os import path
from components.Bot import Bot

from components.Interface import the_shell as startCli


def main():
    currentDir = path.dirname(path.abspath(__file__))
    dataDir = path.join(currentDir, "..", "data")
    userConfigPath = path.join(dataDir, "config.json")
    featuresConfigPath = path.join(dataDir, "features.json")
    logsDatabasePath = path.join(dataDir, "logs.db")

    startCli()


if __name__ == "__main__":
    main()
