#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This is in Python3
"""

__author__ = "mhoelzer"

from flask import Flask
from flask import jsonify
# from dotenv import load_dotenv
from .helpers import EpithetGenerator, Vocabulary
# . does b/c it goes out to parent then back; changed where py looks; not where running but same dir where this is; relative import

app = Flask(__name__)

# tells flask what name of file is but flask needs to find it; will need .env later but not right now
# load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
# ^^^ links with env file; ^^^if fork, can run based off computer
# FLASK_APP = os.environ.get("FLASK_APP")
# FLASK_ENV = os.environ.get("FLASK_ENV")


@app.route("/")
def generate_epithets():
    result = EpithetGenerator().generate()
    # epithets = {"epithets": result}
    return jsonify({"epithets": result})


@app.route("/vocabulary")
def vocabulary():
    # vocabulary = {"vocabulary": {}}
    # return jsonify(vocabulary)
    result = Vocabulary().read_json()
    return jsonify({"vocabulary": result})
