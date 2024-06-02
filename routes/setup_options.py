from flask import Blueprint, render_template, redirect, url_for, session
import random

setup_options_bp = Blueprint('setup_options', __name__)

@setup_options_bp.route('/setup_options')
def setup_options():
    return render_template('setup_options.html')

@setup_options_bp.route('/generate_random_all')
def generate_random_all():
    # Llamar a las funciones de generación aleatoria de empresa y jugador
    generate_random_company()
    generate_random_player()
    return redirect(url_for('confirmation.confirmation'))

def generate_random_company():
    industries = ['Tecnología', 'Finanzas', 'Salud', 'Educación', 'Manufactura']
    sizes = ['Microempresa', 'Pequeña empresa', 'Mediana empresa', 'Gran empresa']
    security_budgets = ['Muy bajo', 'Bajo', 'Medio', 'Alto', 'Muy alto']
    maturity_levels = ['Bajo', 'Medio', 'Alto']
    critical_assets_data_list = [['Datos personales', 'Datos financieros'],
                                 ['Datos de salud', 'Propiedad intelectual'],
                                 ['Datos de clientes', 'Información confidencial']]
    critical_assets_systems_list = [['Aplicaciones web', 'Bases de datos'],
                                    ['Servidores', 'Infraestructura en la nube'],
                                    ['Sistemas SCADA', 'Sistemas de correo electrónico']]
    compliance_requirements_list = [['GDPR', 'ISO 27001'],
                                    ['HIPAA', 'PCI DSS'],
                                    ['SOX', 'NIST']]
    technologies_used_list = [['Aplicaciones web', 'Infraestructura en la nube'],
                              ['Software ERP', 'Redes industriales'],
                              ['Sistemas operativos', 'Aplicaciones móviles']]
    security_policies_list = [['Política de seguridad de la información', 'Política de control de acceso'],
                              ['Política de respuesta a incidentes', 'Política de continuidad del negocio'],
                              ['Política de gestión de riesgos', 'Política de seguridad física']]
    session['industry'] = random.choice(industries)
    session['size'] = random.choice(sizes)
    session['security_budget'] = random.choice(security_budgets)
    session['maturity_level'] = random.choice(maturity_levels)
    session['critical_assets_data'] = random.choice(critical_assets_data_list)
    session['critical_assets_systems'] = random.choice(critical_assets_systems_list)
    session['compliance_requirements'] = random.choice(compliance_requirements_list)
    session['technologies_used'] = random.choice(technologies_used_list)
    session['security_policies'] = random.choice(security_policies_list)

def generate_random_player():
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
    session['player_name'] = random.choice(player_names)
    session['player_role'] = random.choice(player_roles)
    session['experience_level'] = random.choice(experience_levels)
    session['technical_skills'] = random.choice(technical_skills_list)
    session['non_technical_skills'] = random.choice(non_technical_skills_list)
