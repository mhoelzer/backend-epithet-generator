#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This is in Python3
"""

__author__ = "mhoelzer"

from flask import Flask
from flask import jsonify
from dotenv import load_dotenv

import os

app = Flask(__name__)

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
# ^^^ links with env file; ^^^if fork, can run based off computer


@app.route("/")
def generate_epithets():
    epithets = {"epithets": []}
    return jsonify(epithets)


@app.route("/vocabulary")
def vocabulary():
    vocabulary = {"vocabulary": {}}
    return jsonify(vocabulary)
