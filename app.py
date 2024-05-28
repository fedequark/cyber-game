from flask import Flask, render_template, request, session, redirect, url_for
from tree_data_loader import load_tree_data

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

# Cargar los datos del árbol de decisiones
tree_data = load_tree_data('decision_tree.csv')

@app.route('/')
def index():
    session.clear()  # Limpiar la sesión antes de empezar
    session['report'] = []  # Iniciar o reiniciar el reporte
    first_node = tree_data[0]
    return render_template('decision.html', node=first_node)

@app.route('/handle_decision', methods=['POST'])
def handle_decision():
    choice = request.form['decision']
    print("Decisión tomada:", choice)  # Depuración

    if choice == "fin":
        # Si la decisión es "fin", agrega la conclusión correspondiente y redirige a la página de conclusiones
        conclusion = next((opt['conclusion'] for node in tree_data for opt in node['options'] if opt['result'] == "fin" and opt['text'] == request.form['decision_text']), None)
        if conclusion:
            session['report'].append(conclusion)
            print("Conclusión final agregada:", conclusion)  # Depuración
        session.modified = True  # Marcar la sesión como modificada
        return redirect(url_for('conclusion'))
    
    next_node = next((item for item in tree_data if item['question'] == choice), None)
    
    if next_node:
        # Encontrar la opción correspondiente y agregar la conclusión
        option = next((opt for opt in next_node['options'] if opt['result'] == choice), None)
        if option:
            session['report'].append(option['conclusion'])
            print("Conclusión agregada:", option['conclusion'])  # Depuración
        session.modified = True  # Marcar la sesión como modificada
        return render_template('decision.html', node=next_node)
    else:
        # Si no se encuentra un siguiente nodo, redirigir a la página de conclusión
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