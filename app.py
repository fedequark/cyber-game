from flask import Flask, render_template, request, session, redirect, url_for
from tree_data_loader import load_tree_data

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

# Cargar los datos del árbol de decisiones
tree_data = load_tree_data('decision_tree.json')

@app.route('/')
def index():
    session.clear()  # Limpiar la sesión antes de empezar
    session['report'] = []  # Iniciar o reiniciar el reporte
    session['current_node'] = tree_data
    return render_template('decision.html', node=tree_data)

@app.route('/handle_decision', methods=['POST'])
def handle_decision():
    decision_text = request.form['decision_text']
    current_node = session.get('current_node', tree_data)
    
    next_node = None
    for option in current_node['options']:
        if option['text'] == decision_text:
            if 'next' in option:
                next_node = option['next']
            else:
                session['report'].append(option['conclusion'])
                return redirect(url_for('conclusion'))
            break
    
    if next_node:
        session['current_node'] = next_node
        session.modified = True  # Marcar la sesión como modificada
        return render_template('decision.html', node=next_node)
    else:
        print("No se encontró el siguiente nodo, redirigiendo a conclusión")
        return redirect(url_for('conclusion'))

@app.route('/conclusion', methods=['GET'])
def conclusion():
    print("Sesión actual:", dict(session))  # Depuración completa de la sesión
    report = " ".join(session.get('report', []))  # Combinar todas las conclusiones
    print("Reporte final:", report)  # Depuración
    return render_template('conclusion.html', message=report)

if __name__ == '__main__':
    app.run(debug=True)