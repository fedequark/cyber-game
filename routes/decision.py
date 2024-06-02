from flask import Blueprint, session, render_template, request, redirect, url_for

decision_bp = Blueprint('decision', __name__)

@decision_bp.route('/start_decision')
def start_decision():
    session['current_node'] = session['decision_tree']
    session['decisions'] = []  # Inicializar lista de decisiones
    return redirect(url_for('decision.show_question'))

@decision_bp.route('/show_question')
def show_question():
    node = session.get('current_node')
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