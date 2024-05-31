from flask import Flask, render_template, request, session, redirect, url_for, make_response
from tree_data_loader import load_tree_data

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

# Cargar los datos del árbol de decisiones
tree_data = load_tree_data('decision_tree.json')

# Ruta para la nueva pantalla inicial
@app.route('/')
def home():
    return render_template('index.html')

# Ruta original para la configuración del juego
@app.route('/setup')
def index():
    return render_template('setup.html')

@app.route('/handle_setup', methods=['POST'])
def handle_setup():
    # Guardar los datos de configuración de la empresa en la sesión
    session['company'] = {
        'name': request.form['name'],
        'industry': request.form['industry'],
        'size': request.form['size'],
        'security_budget': request.form['security_budget'],
        'maturity_level': request.form['maturity_level'],
        'critical_assets': {
            'data': request.form.getlist('critical_assets_data'),
            'systems': request.form.getlist('critical_assets_systems')
        },
        'compliance_requirements': request.form.getlist('compliance_requirements'),
        'technologies_used': request.form.getlist('technologies_used'),
        'security_policies': request.form.getlist('security_policies')
    }
    return redirect(url_for('player_setup'))

@app.route('/player_setup')
def player_setup():
    return render_template('player_setup.html')

@app.route('/handle_player_setup', methods=['POST'])
def handle_player_setup():
    # Guardar los datos de configuración del jugador en la sesión
    session['player'] = {
        'name': request.form['player_name'],
        'role': request.form['player_role'],
        'experience_level': request.form['experience_level'],
        'technical_skills': request.form.getlist('technical_skills'),
        'non_technical_skills': request.form.getlist('non_technical_skills')
    }
    return redirect(url_for('start_game'))

@app.route('/start_game')
def start_game():
    session['report'] = [] # Iniciar o reiniciar el reporte
    session['decisions'] = [] # Guardar las decisiones tomadas
    session['current_node'] = tree_data
    response = make_response(render_template('decision.html', node=tree_data))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/handle_decision', methods=['POST'])
def handle_decision():
    decision_text = request.form['decision_text']
    current_node = session.get('current_node', tree_data)
    next_node = None
    for option in current_node['options']:
        if option['text'] == decision_text:
            session['decisions'].append(decision_text)
            if 'next' in option:
                next_node = option['next']
            else:
                conclusion = option['conclusion']
                session['report'].append(conclusion)
                session.modified = True # Marcar la sesión como modificada
                return redirect(url_for('conclusion'))
            break
    if next_node:
        session['current_node'] = next_node
        session.modified = True # Marcar la sesión como modificada
        response = make_response(render_template('decision.html', node=next_node))
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    else:
        return redirect(url_for('conclusion'))

@app.route('/conclusion', methods=['GET'])
def conclusion():
    report = " ".join(session.get('report', [])) # Combinar todas las conclusiones
    decisions = session.get('decisions', [])
    response = make_response(render_template('conclusion.html', message=report, decisions=decisions))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)
