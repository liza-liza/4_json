import json
import sys


def load_data(file_path):
    try:
        with open(file_path, 'r') as data:
            return json.load(data)
    except FileNotFoundError:
        return None


def pretty_print_json(json_data):
    print(json.dumps(json_data, indent=4,ensure_ascii=False, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_data = load_data(sys.argv[1])
        if json_data:
            pretty_print_json(json_data)
        else:
            print("File or directory {} not found".format(sys.argv[1]))
    else:
        print("Using: python3 pprint_json.py <path to file>")

