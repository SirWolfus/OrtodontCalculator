import json

def json_converter(n):
    with open('ortocalc.json', 'w') as file:
        json.dump(n, file)