import pandas as pd

def load_tree_data(filepath):
    data = pd.read_csv(filepath)
    tree_data = {}
    for index, row in data.iterrows():
        if row['question'] not in tree_data:
            tree_data[row['question']] = {'question': row['question'], 'options': []}
        tree_data[row['question']]['options'].append({
            'text': row['text'],
            'result': row['result'],
            'conclusion': row['conclusion'] if 'conclusion' in row and not pd.isna(row['conclusion']) else ''
        })
    return list(tree_data.values())