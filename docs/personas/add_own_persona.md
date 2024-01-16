## Guide for Adding Personas

Here is a simple guide for adding your own persona prompts to the `personas.py` file:

1. Come up with a fictional character to use as a persona. Think of their name, story, abilities, personality traits.

2. Add the persona to the `PERSONAS` dictionary object in this format:

```
"PERSONA_NAME": "Persona prompt text",
```

- Replace `PERSONA_NAME` with the name of your persona in ALL_CAPS separated by underscores.

- The persona prompt text should be written in second person, asking the model to "imagine yourself as" the persona, describe them, and encourage taking on their persona.

3. Make sure to put a comma after the persona, except for the last one.

4. That's it! You've added a new persona prompt to the list. Now you can use it just as you would any other persona from the `personas.py` file in your `vars.py` _PERSONA_ variable.

5. You can add as many personas as you want by following steps 1-4. Get creative and have fun!
