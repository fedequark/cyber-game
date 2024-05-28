import pandas as pd

def load_tree_data(filepath):
    data = pd.read_csv(filepath)
    tree = {}
    for index, row in data.iterrows():
        if row['question'] not in tree:
            tree[row['question']] = []
        tree[row['question']].append({'text': row['text'], 'result': row['result']})
    return tree
