#!/usr/bin/python3
"""add_item function"""
import sys

load = __import__('6-load_from_json_file').load_from_json_file

save = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
try:
        data = load_from_json_file(filename)
except FileNotFoundError:
        data = []
    
        items.extend(sys.argv[1:])
        save_to_json_file(data, filename)
