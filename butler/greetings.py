import json
import random
from pathlib import Path

# Locate the data folder relative to this file
DATA_FOLDER = Path(__file__).parent.parent / "data"


def load_json(filename: str):
    """Load a JSON file from the data folder."""
    with open(DATA_FOLDER / filename, "r", encoding="utf-8") as file:
        return json.load(file)


GREETINGS = load_json("greetings.json")
DRINKS = load_json("drinks.json")


def greeting_for(name: str) -> str:
    """Return a random greeting."""

    template = random.choice(GREETINGS)
    drink = random.choice(DRINKS)

    return template.format(
        name=name,
        drink=drink["name"],
        temperature=drink["temperature"],
    )