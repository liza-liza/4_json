import json
import sys
from pprint import pprint

def load_data(filepath):
    try:
       with open(filepath,'r') as f:
	       MyData = json.load(f)
    except FileNotFoundError as err:
        print(err)
        return None
    else:
        return MyData

def pretty_print_json(data):
    pprint(data)


if __name__ == '__main__':
    if len(sys.argv) > 1:
       data = load_data(sys.argv[1])
       if data:
           pretty_print_json(data)
    else:
        print("Using: python3 pprint_json.py <path to file>")
