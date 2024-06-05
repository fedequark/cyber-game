from flask import Blueprint, request, session, redirect, url_for, render_template, make_response

handle_decision_bp = Blueprint('handle_decision', __name__)

@handle_decision_bp.route('/handle_decision', methods=['POST'])
def handle_decision():
    decision_text = request.form['decision_text']
    current_node = session.get('current_node', None)
    next_node = None
    if current_node:
        for option in current_node.get('options', []):
            if option['text'] == decision_text:
                session['decisions'].append(decision_text)
                if 'next' in option:
                    next_node = option['next']
                else:
                    conclusion = option['conclusion']
                    session['report'].append(conclusion)
                    session.modified = True
                    return redirect(url_for('conclusion.conclusion'))
                break
    if next_node:
        session['current_node'] = next_node
        session.modified = True
        response = make_response(render_template('decision.html', node=next_node))
        response.headers['Content-Type'] = 'text/html; charset=utf-8'
        return response
    else:
        return redirect(url_for('conclusion.conclusion'))
