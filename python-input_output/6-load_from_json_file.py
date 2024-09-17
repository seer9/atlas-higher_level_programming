#!/usr/bin/python3
"""load_from_json_file function"""


def load_from_json_file(filename):
    """loads a json file and returns its content"""
    import json

    with open(filename) as f:
        return json.load(f)