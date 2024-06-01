from flask import Blueprint, request, redirect, url_for, session, render_template

player_setup_bp = Blueprint('player_setup', __name__)

@player_setup_bp.route('/player_setup')
def player_setup():
    return render_template('player_setup.html')

@player_setup_bp.route('/handle_player_setup', methods=['POST'])
def handle_player_setup():
    session['player_name'] = request.form.get('player_name')
    session['player_role'] = request.form.get('player_role')
    session['experience_level'] = request.form.get('experience_level')
    session['technical_skills'] = request.form.getlist('technical_skills')
    session['non_technical_skills'] = request.form.getlist('non_technical_skills')
    return redirect(url_for('player_setup.player_profile'))

@player_setup_bp.route('/player_profile')
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
