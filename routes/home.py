from flask import Blueprint, render_template, session

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def home():
    # Resetea la configuración de la Empresa y Jugador
    keys_to_reset = [
        'industry', 'size', 'security_budget', 'maturity_level',
        'critical_assets_data', 'critical_assets_systems', 'compliance_requirements',
        'technologies_used', 'security_policies',
        'player_name', 'player_role', 'experience_level', 'technical_skills', 'non_technical_skills'
    ]
    for key in keys_to_reset:
        session.pop(key, None)
    return render_template('index.html')
