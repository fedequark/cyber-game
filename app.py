from flask import Flask
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

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

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

if __name__ == '__main__':
    app.run(debug=True)
