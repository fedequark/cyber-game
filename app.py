from flask import Flask, session, redirect, url_for, render_template
import json
import os
import random
from routes.home import home_bp
from routes.company_setup import company_setup_bp
from routes.generate_random_company import generate_random_company_bp
from routes.generate_random_player import generate_random_player_bp
from routes.restart import restart_bp
from routes.handle_decision import handle_decision_bp
from routes.conclusion import conclusion_bp
from routes.profile import profile_bp
from routes.setup_options import setup_options_bp
from routes.company_setup_options import company_setup_options_bp
from routes.player_setup_options import player_setup_options_bp
from routes.player_setup import player_setup_bp
from routes.confirmation import confirmation_bp
from routes.decision import decision_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Cargar el archivo de escenarios
try:
    with open('scenarios.json', encoding='utf-8') as f:
        scenarios = json.load(f)
        # print("Escenarios cargados correctamente:", scenarios)
except json.JSONDecodeError as e:
    print(f"Error al cargar scenarios.json: {e}")
    scenarios = {}

@app.before_first_request
def initialize_scenarios():
    print("Ejecutando initialize_scenarios")
    if scenarios:
        session['scenarios'] = scenarios
        print("Escenarios guardados en la sesión:", session['scenarios'])
    else:
        print("No se pudieron cargar los escenarios.")

# Registrar los Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(company_setup_bp)
app.register_blueprint(generate_random_company_bp)
app.register_blueprint(generate_random_player_bp)
app.register_blueprint(restart_bp)
app.register_blueprint(handle_decision_bp)
app.register_blueprint(conclusion_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(setup_options_bp)
app.register_blueprint(company_setup_options_bp)
app.register_blueprint(player_setup_options_bp)
app.register_blueprint(player_setup_bp)
app.register_blueprint(confirmation_bp)
app.register_blueprint(decision_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
