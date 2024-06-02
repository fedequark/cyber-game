from flask import Flask, session, redirect, url_for, render_template
import json
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

# Importar las nuevas rutas y modelos extendidos
from models_extended import db
from routes.scenarios import scenarios_bp
from routes.decision_extended import decision_extended_bp

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

# Registrar los Blueprints comunes
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

# Cargar el archivo JSON
with open('decision_tree.json', encoding='utf-8') as f:
    decision_tree = json.load(f)

# Almacenar el árbol de decisiones en la sesión al inicio de la aplicación
@app.before_request
def initialize_decision_tree():
    if 'decision_tree_initialized' not in session:
        session['decision_tree'] = decision_tree
        session['current_node'] = decision_tree
        session['decision_tree_initialized'] = True

# Registrar los Blueprints y configurar la base de datos si se usa el workflow basado en la base de datos
use_database = app.config['USE_DATABASE']
if use_database:
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI']
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.register_blueprint(scenarios_bp, url_prefix='/scenarios')
    app.register_blueprint(decision_extended_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
