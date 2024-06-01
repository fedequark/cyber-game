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
    return redirect(url_for('company_setup.company_profile'))
