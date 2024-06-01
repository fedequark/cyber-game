from flask import Blueprint, session, request, redirect, url_for, render_template

handle_player_setup_bp = Blueprint('handle_player_setup', __name__)

@handle_player_setup_bp.route('/handle_player_setup', methods=['POST'])
def handle_player_setup():
    player_profile = {
        'player_name': request.form.get('player_name'),
        'role': request.form.get('player_role'),
        'experience_level': request.form.get('experience_level'),
        'technical_skills': request.form.getlist('technical_skills'),
        'non_technical_skills': request.form.getlist('non_technical_skills')
    }
    session['player_profile'] = player_profile
    print("Perfil del jugador guardado en la sesión:", session['player_profile'])
    return redirect(url_for('confirmation.show_confirmation'))

@handle_player_setup_bp.route('/player_setup')
def player_setup():
    return render_template('player_setup.html')
