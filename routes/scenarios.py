from flask import Blueprint, request, jsonify
from models_extended import db, Scenario, Situation, Option

scenarios_bp = Blueprint('scenarios', __name__)

@scenarios_bp.route('/scenarios', methods=['POST'])
def add_scenario():
    data = request.get_json()
    scenario = Scenario(title=data['title'])
    db.session.add(scenario)
    db.session.commit()
    for situation_data in data['situations']:
        situation = Situation(
            question=situation_data['question'],
            scenario_id=scenario.id
        )
        db.session.add(situation)
        db.session.commit()
        for option_data in situation_data['options']:
            option = Option(
                text=option_data['text'],
                situation_id=situation.id,
                next_situation_id=option_data.get('next_situation_id'),
                conclusion=option_data.get('conclusion')
            )
            db.session.add(option)
        db.session.commit()
    return jsonify({'message': 'Scenario created'}), 201

@scenarios_bp.route('/scenarios', methods=['GET'])
def get_scenarios():
    scenarios = Scenario.query.all()
    result = []
    for scenario in scenarios:
        situations = Situation.query.filter_by(scenario_id=scenario.id).all()
        situations_list = []
        for situation in situations:
            options = Option.query.filter_by(situation_id=situation.id).all()
            options_list = [{'text': option.text, 'next_situation_id': option.next_situation_id, 'conclusion': option.conclusion} for option in options]
            situations_list.append({'id': situation.id, 'question': situation.question, 'options': options_list})
        result.append({'id': scenario.id, 'title': scenario.title, 'situations': situations_list})
    return jsonify(result)
