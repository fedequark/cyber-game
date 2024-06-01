from flask import Blueprint, session, redirect, url_for, render_template
import random

generate_random_player_bp = Blueprint('generate_random_player', __name__)

@generate_random_player_bp.route('/generate_random_player')
def generate_random_player():
    # Opciones para los atributos del jugador
    player_names = ['Juan', 'María', 'Carlos', 'Laura', 'Pedro']
    player_roles = ['Analista de Seguridad', 'Ingeniero de Seguridad', 'Gerente de Seguridad', 'Arquitecto de Seguridad', 'Consultor de Seguridad']
    experience_levels = ['Junior', 'Intermedio', 'Senior', 'Experto']
    technical_skills_list = [['Redes', 'Seguridad de aplicaciones', 'Criptografía'], 
                             ['Administración de sistemas', 'Análisis forense'], 
                             ['Redes', 'Administración de sistemas'],
                             ['Seguridad de aplicaciones', 'Análisis forense'],
                             ['Criptografía', 'Análisis forense']]
    non_technical_skills_list = [['Comunicación', 'Trabajo en equipo'], 
                                 ['Liderazgo', 'Gestión de proyectos'], 
                                 ['Pensamiento crítico', 'Comunicación'],
                                 ['Trabajo en equipo', 'Gestión de proyectos'],
                                 ['Pensamiento crítico', 'Liderazgo']]

    # Seleccionar aleatoriamente los atributos del jugador
    session['player_name'] = random.choice(player_names)
    session['player_role'] = random.choice(player_roles)
    session['experience_level'] = random.choice(experience_levels)
    session['technical_skills'] = random.choice(technical_skills_list)
    session['non_technical_skills'] = random.choice(non_technical_skills_list)

    return redirect(url_for('player_setup.player_profile'))

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
