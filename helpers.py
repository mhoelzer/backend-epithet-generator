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

    def generate_one(self):
        """"""
        data = Vocabulary.read_json("resources/data.json")
        return "{} {} {}".format(random.choice(data["Column 1"]), random.choice(data["Column 2"]), random.choice(data["Column 3"]))

    def generate_multi(self, quantity):
        """"""
        multi_epithets_list = []
        for num in range(quantity):
            multi_epithets_list.append(self.generate_one())
        return multi_epithets_list

        multi_epithets_dict = {}
        for num in range(quantity):
            multi_epithets_dict[num + 1] = self.generate_one()
        return multi_epithets_dict