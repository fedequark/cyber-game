import json

def load_tree_data(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)