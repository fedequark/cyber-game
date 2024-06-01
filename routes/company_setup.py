from flask import Blueprint, render_template, request, redirect, url_for, session

company_setup_bp = Blueprint('company_setup', __name__, url_prefix='/company_setup')

@company_setup_bp.route('/', methods=['GET', 'POST'])
def setup():
    if request.method == 'POST':
        session['industry'] = request.form.get('industry')
        session['size'] = request.form.get('size')
        session['security_budget'] = request.form.get('security_budget')
        session['maturity_level'] = request.form.get('maturity_level')
        session['critical_assets_data'] = request.form.getlist('critical_assets_data')
        session['critical_assets_systems'] = request.form.getlist('critical_assets_systems')
        session['compliance_requirements'] = request.form.getlist('compliance_requirements')
        session['technologies_used'] = request.form.getlist('technologies_used')
        session['security_policies'] = request.form.getlist('security_policies')
        return redirect(url_for('company_setup.company_profile'))
    return render_template('company_setup.html')

@company_setup_bp.route('/company_profile')
def company_profile():
    player_configured = all(key in session for key in [
        'player_name', 'player_role', 'experience_level', 'technical_skills', 'non_technical_skills'
    ])
    return render_template('company_profile.html',
                           industry=session.get('industry'),
                           size=session.get('size'),
                           security_budget=session.get('security_budget'),
                           maturity_level=session.get('maturity_level'),
                           critical_assets_data=session.get('critical_assets_data'),
                           critical_assets_systems=session.get('critical_assets_systems'),
                           compliance_requirements=session.get('compliance_requirements'),
                           technologies_used=session.get('technologies_used'),
                           security_policies=session.get('security_policies'),
                           player_configured=player_configured)
