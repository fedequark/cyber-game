from flask import Blueprint, session, redirect, url_for, render_template

generate_random_player_bp = Blueprint('generate_random_player', __name__)

@generate_random_player_bp.route('/generate_random_player')
def generate_random_player():
    # Generar datos aleatorios del jugador
    session['player_name'] = 'Jugador Aleatorio'
    session['player_role'] = 'Especialista en seguridad'
    session['experience_level'] = 'Intermedio'
    session['technical_skills'] = ['Redes', 'Seguridad de aplicaciones']
    session['non_technical_skills'] = ['Comunicación', 'Trabajo en equipo']
    return redirect(url_for('generate_random_player.player_profile'))

@generate_random_player_bp.route('/player_profile')
def player_profile():
    company_configured = all(key in session for key in [
        'industry', 'size', 'security_budget', 'maturity_level',
        'critical_assets_data', 'critical_assets_systems', 'compliance_requirements',
        'technologies_used', 'security_policies'
    ])
    return render_template('player_profile.html',
                           player_name=session.get('player_name'),
                           player_role=session.get('player_role'),
                           experience_level=session.get('experience_level'),
                           technical_skills=session.get('technical_skills'),
                           non_technical_skills=session.get('non_technical_skills'),
                           company_configured=company_configured)
