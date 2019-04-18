import json
import random


class Vocabulary:
    """
    Handle loading in a JSON file with proper unfinished swears in it!

    Usage:
        data = Vocabulary.read_json("/path/to/data.json")
    """

    def read_json(path, mode='r'):
        # resources/data.json
        with open(path, mode=mode) as handle:
            return json.load(handle)


class EpithetGenerator:
    """"""

    def generate(self):
        data = Vocabulary.read_json("resources/data.json")
        return "{} {} {}".format(random.choice(data["Column 1"]), random.choice(data["Column 2"]), random.choice(data["Column 3"]))
