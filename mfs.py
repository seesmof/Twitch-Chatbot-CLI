import re
import g4f


def generateResponse(prompt: str, memory: [dict]) -> str:
    currentQuery = {"role": "user", "content": prompt}
    memory.append(currentQuery)

    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=memory,
        stream=False,
        timeout=5,
    )
    responseDict = {"role": "assistant", "content": response}
    memory.append(responseDict)

    return cleanText(response)


def cleanText(text: str, nickname: str) -> str:
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"\[.*?\]", "", text)
    text = re.sub(r"\".*?\"", "", text)
    text = re.sub(r"\*", "", text)
    text = text.replace("\n", " ")
    text = text.replace("user: ", "", flags=re.I)
    text = text.replace("system: ", "", flags=re.I)
    text = text.replace("assistant: ", "", flags=re.I)
    text = text.replace(" : ", "")
    text = text.replace(nickname, "")
    text = text.replace("@", "")
    return text


def splitMessage(response: str) -> [str]:
    messageLimit = 440
    partsCount = len(response) // messageLimit + (
        1 if len(response) % messageLimit > 0 else 0
    )
    substrings = [
        response[i * messageLimit : (i + 1) * messageLimit] for i in range(partsCount)
    ]

    return substrings
