from os import path

from components.Interface import the_shell as startCli


def main():
    currentDir = path.dirname(path.abspath(__file__))
    dataDir = path.join(currentDir, "..", "data")

    startCli()


if __name__ == "__main__":
    main()
