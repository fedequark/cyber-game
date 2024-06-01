from flask import Blueprint, session, render_template, make_response

conclusion_bp = Blueprint('conclusion', __name__)

@conclusion_bp.route('/conclusion', methods=['GET'])
def conclusion():
    report = " ".join(session.get('report', []))
    decisions = session.get('decisions', [])
    response = make_response(render_template('conclusion.html', message=report, decisions=decisions))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response