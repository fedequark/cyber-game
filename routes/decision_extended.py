from flask import Blueprint, session, render_template, request, redirect, url_for
from models_extended import Scenario, Situation, Option

decision_extended_bp = Blueprint('decision_extended', __name__)

@decision_extended_bp.route('/start_decision/<int:scenario_id>')
def start_decision(scenario_id):
    scenario = Scenario.query.get(scenario_id)
    if not scenario:
        return redirect(url_for('home.home'))
    session['scenario_id'] = scenario_id
    session['current_situation'] = scenario.situations[0].id
    session['decisions'] = []
    return redirect(url_for('decision_extended.show_situation'))

@decision_extended_bp.route('/show_situation')
def show_situation():
    situation_id = session.get('current_situation')
    situation = Situation.query.get(situation_id)
    if not situation:
        return redirect(url_for('home.home'))
    if 'conclusion' in session:
        return render_template('conclusion_extended.html', conclusion=session['conclusion'], decisions=session['decisions'])
    return render_template('question_extended.html', question=situation.question, options=situation.options)

@decision_extended_bp.route('/make_decision', methods=['POST'])
def make_decision():
    choice_id = int(request.form['choice'])
    option = Option.query.get(choice_id)
    decision_text = option.text
    session['decisions'].append(decision_text)
    if option.next_situation_id:
        session['current_situation'] = option.next_situation_id
    else:
        session['conclusion'] = option.conclusion
    return redirect(url_for('decision_extended.show_situation'))
