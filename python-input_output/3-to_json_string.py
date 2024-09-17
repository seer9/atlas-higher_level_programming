#!/usr/bin/python3
"""to_json_string function"""


def to_json_string(my_obj):
    """returns a json string representation of my_obj"""
    import json
    return json.dumps(my_obj)