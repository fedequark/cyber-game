from flask import Blueprint, session, redirect, url_for, render_template

generate_random_company_bp = Blueprint('generate_random_company', __name__)

@generate_random_company_bp.route('/generate_random_company')
def generate_random_company():
    # Generar datos aleatorios de la empresa
    session['industry'] = 'Tecnología'
    session['size'] = 'Mediana empresa'
    session['security_budget'] = 'Medio'
    session['maturity_level'] = 'Intermedio'
    session['critical_assets_data'] = ['Datos personales', 'Datos financieros']
    session['critical_assets_systems'] = ['Aplicaciones web', 'Bases de datos']
    session['compliance_requirements'] = ['GDPR', 'ISO 27001']
    session['technologies_used'] = ['Aplicaciones web', 'Infraestructura en la nube']
    session['security_policies'] = ['Política de seguridad de la información', 'Política de control de acceso']
    return redirect(url_for('generate_random_company.company_profile'))

@generate_random_company_bp.route('/company_profile')
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
