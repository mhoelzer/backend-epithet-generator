#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This is in Python3
"""

__author__ = "mhoelzer"

from flask import Flask
from flask import jsonify
from backend_epithet_generator.helpers import EpithetGenerator, Vocabulary
# ^^^ . does b/c it goes out to parent then back; changed where py looks; 
# not where running but same dir where this is; relative import

import random

app = Flask(__name__)


@app.route("/")
def generate_epithets():
    result = EpithetGenerator().generate_one()
    return jsonify({"epithets": result})


@app.route("/vocabulary")
def vocabulary():
    result = Vocabulary.read_json("resources/data.json")
    return jsonify({"vocabulary": result})


@app.route("/epithets/<int:quantity>")
def generate_multiple_epithets(quantity):
    result = EpithetGenerator().generate_multi(quantity)
    return jsonify({"epithets": result})


@app.route("/randomizeme")
def generate_random_num_epithets():
    random_times = random.randint(1, 333)
    result = EpithetGenerator().generate_multi(random_times)
    return jsonify({"epithets": result})
