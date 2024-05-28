from flask import Flask, render_template, request, redirect, url_for, session
from tree_data_loader import load_tree_data

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aleatoria'

# Carga los datos del árbol de decisiones
tree_data = load_tree_data('decision_tree.csv')

# Las rutas de Flask utilizan 'tree_data'
# ...

import pandas as pd

def load_tree_data(filepath):
    data = pd.read_csv(filepath)
    tree_data = {}
    for index, row in data.iterrows():
        if row['question'] not in tree_data:
            tree_data[row['question']] = {'question': row['question'], 'options': []}
        tree_data[row['question']]['options'].append({'text': row['text'], 'result': row['result']})
    return tree_data.values()  # Devuelve una lista de diccionarios
