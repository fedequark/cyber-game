from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aleatoria'

@app.route('/', methods=['GET'])
def index():
    session['report'] = []  # Iniciar o reiniciar el reporte
    first_node = tree_data[0]
    return render_template('decision.html', question=first_node['question'], options=first_node['options'])

@app.route('/handle_decision', methods=['POST'])
def handle_decision():
    choice = request.form['decision']
    for node in tree_data:
        if node['result'] == choice:
            session['report'].append(node['conclusion'])  # Agregar conclusión al reporte
            return render_template('decision.html', question=node['question'], options=node['options'])
    return redirect(url_for('conclusion'))

@app.route('/conclusion', methods=['GET'])
def conclusion():
    report = " ".join(session['report'])  # Combinar todas las conclusiones
    return render_template('conclusion.html', message=report)

if __name__ == '__main__':
    app.run(debug=True)