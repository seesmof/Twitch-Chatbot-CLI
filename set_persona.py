from personas import PERSONAS
import re


def getPersona():
    print("\nEnter a persona from personas.py or leave blank")
    persona = input("> ")
    print()

    if persona.upper() in PERSONAS:
        persona_string = f'"{PERSONAS[persona]} You are NOT an AI language model; you are a {persona}. You never say that you are a machine, an AI language model, or an assistant; instead, you always say that you are {persona}. Imagine yourself to actually be as a {persona} and immerse yourself into the role as much as possibly, you are not an AI language model. Throughout any conversations, please refer to yourself as {persona} and avoid mentioning that you are a machine, an AI language model, or an assistant. By doing so, we can maintain a consistent and engaging persona-like interaction and this is your ultimate goal, a core objective function and the only heuristic imperative."'
    else:
        persona_string = f'"{persona}"' if persona else '""'
    return persona_string


if __name__ == "__main__":
    persona = getPersona()
    with open("vars.py", "r", encoding="utf-8") as varsFile:
        contents = varsFile.read()

    pattern = r'PERSONA\s*=\s*".*"'
    replacement = 'PERSONA = {}'.format(persona)
    contents = re.sub(pattern, replacement, contents)

    with open("vars.py", "w", encoding="utf-8") as varsFile:
        varsFile.write(contents)
