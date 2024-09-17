#!/usr/bin/python3
"""save_to_json_file function"""


def save_to_json_file(my_obj, filename):
    """saves my_obj to a json file"""
    import json
    with open(filename, "w") as f:
        return json.dump(my_obj, f)
