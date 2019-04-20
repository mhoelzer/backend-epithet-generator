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
    """
    Handle creating and returning an epithet or multiple

    Usage:
        result = EpithetGenerator().generate_one()
        OR
        result = EpithetGenerator().generate_multi(quantity)
    """

    def generate_one(self):
        """Creates and delivers a single epithet to use against your enemy"""
        data = Vocabulary.read_json("resources/data.json")
        return "{} {} {}!".format(random.choice(data["Column 1"]),
                                  random.choice(data["Column 2"]),
                                  random.choice(data["Column 3"]))

    def generate_multi(self, quantity):
        """Creates and delivers many epithets to use against your enemies"""
        multi_epithets_list = []
        for _ in range(quantity):
            multi_epithets_list.append(self.generate_one() + "!")
        return multi_epithets_list