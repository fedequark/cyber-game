import random
from flask import Flask, render_template, request, session, redirect, url_for, make_response
from tree_data_loader import load_tree_data

app = Flask(__name__)
app.secret_key = 'your_random_secret_key'

# Cargar los datos del árbol de decisiones
tree_data = load_tree_data('decision_tree.json')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/setup')
def setup():
    return render_template('setup.html')

@app.route('/generate_random')
def generate_random():
    # Generar datos aleatorios para la empresa
    industries = ["Tecnología", "Finanzas", "Salud", "Gobierno", "Educación", "Energía", "Manufactura", "Retail", "Transporte", "Telecomunicaciones", "Entretenimiento", "Otra"]
    sizes = ["Microempresa", "Pequeña empresa", "Mediana empresa", "Gran empresa", "Corporación"]
    budgets = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]
    maturities = ["Muy bajo", "Bajo", "Medio", "Alto", "Muy alto"]
    assets_data = ["Personales", "Financieros", "De salud", "Propiedad intelectual", "Secretos comerciales", "Otros"]
    assets_systems = ["Aplicaciones web", "Bases de datos", "Sistemas de producción", "Infraestructura de red", "Otros"]
    compliance = ["GDPR", "HIPAA", "PCI DSS", "SOX", "GLBA", "ISO 27001", "DORA", "NIS2", "Otra"]
    technologies = ["Aplicaciones web", "Bases de datos", "Aplicaciones móviles", "Infraestructura en la nube", "Sistemas de correo electrónico", "Sistemas de gestión de relaciones con los clientes (CRM)", "Sistemas de planificación de recursos empresariales (ERP)", "Sistemas de control industrial (ICS/SCADA)", "Otros"]
    policies = ["Política de seguridad de la información", "Política de control de acceso", "Política de gestión de activos", "Política de seguridad de recursos humanos", "Política de seguridad física y del entorno", "Política de gestión de las comunicaciones y operaciones", "Política de adquisición, desarrollo y mantenimiento de sistemas de información", "Política de gestión de incidentes de seguridad de la información", "Política de continuidad del negocio", "Política de cumplimiento"]

    session['company'] = {
        'name': "Empresa Random",
        'industry': random.choice(industries),
        'size': random.choice(sizes),
        'security_budget': random.choice(budgets),
        'maturity_level': random.choice(maturities),
        'critical_assets': {
            'data': random.sample(assets_data, k=2),
            'systems': random.sample(assets_systems, k=2)
        },
        'compliance_requirements': random.sample(compliance, k=2),
        'technologies_used': random.sample(technologies, k=2),
        'security_policies': random.sample(policies, k=2)
    }

    # Generar datos aleatorios para el jugador
    roles = ["Administrador de sistemas", "Especialista en seguridad", "Gerente de TI", "Consultor de seguridad", "Ingeniero de red", "Desarrollador de software", "Arquitecto de seguridad", "Auditor de seguridad", "Analista de seguridad", "Especialista en cumplimiento", "Otros"]
    experience_levels = ["Principiante", "Intermedio", "Avanzado", "Experto"]
    technical_skills = ["Redes", "Seguridad de aplicaciones", "Criptografía", "Análisis forense", "Respuesta a incidentes", "Gestión de identidades y accesos", "Monitoreo y análisis de seguridad", "Desarrollo seguro", "Penetration testing"]
    non_technical_skills = ["Comunicación", "Liderazgo", "Gestión de proyectos", "Pensamiento crítico", "Resolución de problemas", "Trabajo en equipo"]

    session['player'] = {
        'name': "Jugador Random",
        'role': random.choice(roles),
        'experience_level': random.choice(experience_levels),
        'technical_skills': random.sample(technical_skills, k=3),
        'non_technical_skills': random.sample(non_technical_skills, k=2)
    }

    return redirect(url_for('summary'))

@app.route('/handle_setup', methods=['POST'])
def handle_setup():
    session['company'] = {
        'name': request.form['name'],
        'industry': request.form['industry'],
        'size': request.form['size'],
        'security_budget': request.form['security_budget'],
        'maturity_level': request.form['maturity_level'],
        'critical_assets': {
            'data': request.form.getlist('critical_assets_data'),
            'systems': request.form.getlist('critical_assets_systems')
        },
        'compliance_requirements': request.form.getlist('compliance_requirements'),
        'technologies_used': request.form.getlist('technologies_used'),
        'security_policies': request.form.getlist('security_policies')
    }
    return redirect(url_for('player_setup'))

@app.route('/player_setup')
def player_setup():
    return render_template('player_setup.html')

@app.route('/handle_player_setup', methods=['POST'])
def handle_player_setup():
    session['player'] = {
        'name': request.form['player_name'],
        'role': request.form['player_role'],
        'experience_level': request.form['experience_level'],
        'technical_skills': request.form.getlist('technical_skills'),
        'non_technical_skills': request.form.getlist('non_technical_skills')
    }
    return redirect(url_for('summary'))

@app.route('/summary')
def summary():
    company = session.get('company', {})
    player = session.get('player', {})
    return render_template('summary.html', company=company, player=player)

@app.route('/start_game')
def start_game():
    session['report'] = []  # Iniciar o reiniciar el reporte
    session['decisions'] = []  # Guardar las decisiones tomadas
    session['current_node'] = tree_data
    response = make_response(render_template('decision.html', node=tree_data))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route('/handle_decision', methods=['POST'])
def handle_decision():
    decision_text = request.form['decision_text']
    current_node = session.get('current_node', tree_data)
    next_node = None
    for option in current_node['options']:
        if option['text'] == decision_text:
            session['decisions'].append(decision_text)
            if 'next' in option:
                next_node = option['next']
            else:
                conclusion = option['conclusion']
                session['report'].append(conclusion)
                session.modified = True  # Marcar la sesión como modificada
                return redirect(url_for('conclusion'))
            break
    if next_node:
        session['current_node'] = next_node
        session.modified = True  # Marcar la sesión como modificada
        response = make_response(render_template('decision.html', node=next_node))
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    else:
        return redirect(url_for('conclusion'))

@app.route('/conclusion', methods=['GET'])
def conclusion():
    report = " ".join(session.get('report', []))  # Combinar todas las conclusiones
    decisions = session.get('decisions', [])
    response = make_response(render_template('conclusion.html', message=report, decisions=decisions))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

if __name__ == '__main__':
    app.run(debug=True)
