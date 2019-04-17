#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

This is in Python3
"""

__author__ = "mhoelzer"

from flask import Flask
import os
# os.dream; .join; os/path(__magic?; use name).dri
# install .env module to use as method; low.env 

app = Flask(__name__)


@app.route("/")
def generate_epithets():
    return f""


@app.route("/vocabulary")
def vocabulary():
    pass
