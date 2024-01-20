import g4f

from rich.console import Console
from rich.traceback import install

install()
console = Console()


def generateResponse(prompt: str, memory: [dict]) -> str:
    currentQuery = {"role": "user", "content": prompt}
    memory.append(currentQuery)

    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_35_turbo,
        messages=memory,
        stream=False,
    )
    responseDict = {"role": "assistant", "content": response}
    memory.append(responseDict)

    return response


def splitMessage(response: str) -> [str]:
    messageLimit = 440
    partsCount = len(response) // messageLimit + (
        1 if len(response) % messageLimit > 0 else 0
    )
    substrings = [
        response[i * messageLimit : (i + 1) * messageLimit] for i in range(partsCount)
    ]

    return substrings
