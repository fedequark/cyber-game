import json

def load_tree_data(file_path):
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)
