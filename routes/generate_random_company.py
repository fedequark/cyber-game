from flask import Blueprint, session, redirect, url_for
import random

generate_random_company_bp = Blueprint('generate_random_company', __name__)

@generate_random_company_bp.route('/generate_random_company')
def generate_random_company():
    # Opciones para los atributos de la empresa
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

    # Seleccionar aleatoriamente los atributos de la empresa
    session['industry'] = random.choice(industries)
    session['size'] = random.choice(sizes)
    session['security_budget'] = random.choice(security_budgets)
    session['maturity_level'] = random.choice(maturity_levels)
    session['critical_assets_data'] = random.choice(critical_assets_data_list)
    session['critical_assets_systems'] = random.choice(critical_assets_systems_list)
    session['compliance_requirements'] = random.choice(compliance_requirements_list)
    session['technologies_used'] = random.choice(technologies_used_list)
    session['security_policies'] = random.choice(security_policies_list)

    return redirect(url_for('company_setup.company_profile'))
