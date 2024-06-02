from flask import Blueprint, request, jsonify
from models import db, Scenario, Option

api_bp = Blueprint('api', __name__)

@api_bp.route('/scenarios', methods=['POST'])
def add_scenario():
    data = request.get_json()
    scenario = Scenario(question=data['question'])
    db.session.add(scenario)
    db.session.commit()
    for option_data in data['options']:
        option = Option(
            text=option_data['text'],
            scenario_id=scenario.id,
            next_scenario_id=option_data.get('next_scenario_id'),
            conclusion=option_data.get('conclusion')
        )
        db.session.add(option)
    db.session.commit()
    return jsonify({'message': 'Scenario created'}), 201

@api_bp.route('/scenarios', methods=['GET'])
def get_scenarios():
    scenarios = Scenario.query.all()
    result = []
    for scenario in scenarios:
        options = Option.query.filter_by(scenario_id=scenario.id).all()
        options_list = [{'text': option.text, 'next_scenario_id': option.next_scenario_id, 'conclusion': option.conclusion} for option in options]
        result.append({'id': scenario.id, 'question': scenario.question, 'options': options_list})
    return jsonify(result)

# Similar endpoints for updating and deleting scenarios
