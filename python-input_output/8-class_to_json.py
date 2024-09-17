#!/usr/bin/python3
"""class_to_json class"""
import json


def class_to_json(obj):
    """returns a json representation of obj"""

    return (obj.__dict__)
