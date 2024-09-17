#!/usr/bin/python3
"""add_item function"""
from sys import argv

if __name__ == "__main__":

load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    data = load_from_json_file(filename)
except FileNotFoundError:
    data = []

for _ in range(1, len(argv)):
    data.append(argv[_])
save_to_json_file(data, filename)