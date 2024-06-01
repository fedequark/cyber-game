from flask import Blueprint, session, render_template, make_response
from tree_data_loader import load_tree_data

restart_bp = Blueprint('restart', __name__)

@restart_bp.route('/restart')
def restart():
    tree_data = load_tree_data('decision_tree.json')
    session['report'] = []
    session['decisions'] = []
    session['current_node'] = tree_data
    response = make_response(render_template('decision.html', node=tree_data))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response
