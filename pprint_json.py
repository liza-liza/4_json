import json
import sys
from pprint import pprint

def load_data(file_path):
    try:
        with open(file_path,'r') as f:
	        json_data = json.load(f)
    except FileNotFoundError as err:
        print(err)
        return None
    else:
        return json_data

def pretty_print_json(json_data):
    pprint(json_data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_data = load_data(sys.argv[1])
        if json_data:
            pretty_print_json(json_data)
    else:
        print("Using: python3 pprint_json.py <path to file>")
