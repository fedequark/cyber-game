from flask import Blueprint, session, render_template, request, redirect, url_for
import json
import os
import random

decision_bp = Blueprint('decision', __name__)

def seleccionar_escenario():
    scenarios = session.get('scenarios')
    if not scenarios:
        print("Error: No hay escenarios disponibles en la sesión.")
        return None

    # Obtener nivel de experiencia del jugador desde la sesión
    player_profile = session.get('player_profile', {})
    print(f"Perfil del jugador: {player_profile}")
    experience_level = player_profile.get('experience_level', '').lower()
    print(f"Nivel de experiencia del jugador: {experience_level}")

    # Filtrar escenarios por nivel de experiencia
    filtered_scenarios = {key: value for key, value in scenarios.items() if experience_level in key}
    print(f"Escenarios filtrados: {filtered_scenarios}")

    if not filtered_scenarios:
        print("Error: No se encontraron escenarios para el nivel de experiencia dado.")
        return None

    # Seleccionar aleatoriamente un escenario de los filtrados
    scenario_key = random.choice(list(filtered_scenarios.keys()))
    scenario_path = filtered_scenarios[scenario_key]
    if os.path.exists(scenario_path):
        with open(scenario_path, encoding='utf-8') as f:
            scenario = json.load(f)
            print(f"Escenario seleccionado: {scenario_key}, ruta: {scenario_path}")
            return scenario
    else:
        raise FileNotFoundError(f"El archivo de escenario {scenario_path} no existe.")

@decision_bp.route('/start_decision')
def start_decision():
    print("Iniciando juego de decisiones...")
    scenario = seleccionar_escenario()
    if scenario:
        session['decision_tree'] = scenario
        session['current_node'] = scenario
        session['decisions'] = []  # Inicializar lista de decisiones
        return redirect(url_for('decision.show_question'))
    else:
        print("Error: No se pudo seleccionar un escenario.")
        return "Error: No se pudo seleccionar un escenario.", 500

@decision_bp.route('/show_question')
def show_question():
    node = session.get('current_node')
    # print(f"Mostrando pregunta para nodo: {node}")
    if not node:
        print("Error: Nodo actual es None")
        return "Error: Nodo actual es None", 500
    elif 'question' not in node and 'conclusion' not in node:
        print(f"Error: Nodo actual no contiene 'question' ni 'conclusion'. Nodo actual: {node}")
        return "Error: Nodo actual no contiene 'question' ni 'conclusion'", 500
    if 'conclusion' in node:
        return render_template('conclusion.html', conclusion=node['conclusion'], decisions=session['decisions'])
    return render_template('question.html', question=node['question'], options=node['options'])

@decision_bp.route('/make_decision', methods=['POST'])
def make_decision():
    choice = int(request.form['choice'])
    node = session.get('current_node')
    decision_text = node['options'][choice]['text']
    session['decisions'].append(decision_text)  # Almacenar la decisión tomada
    next_node = node['options'][choice].get('next')
    if next_node:
        session['current_node'] = next_node
    else:
        session['current_node'] = node['options'][choice]
    return redirect(url_for('decision.show_question'))
