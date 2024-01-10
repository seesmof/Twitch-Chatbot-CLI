import json


def readJson(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def saveJson(path: str, data: dict | list) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
