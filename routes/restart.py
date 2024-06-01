from flask import Blueprint, session, redirect, url_for
from tree_data_loader import load_tree_data

restart_bp = Blueprint('restart', __name__)

@restart_bp.route('/restart')
def restart():
    session.clear()
    decision_tree = load_tree_data('decision_tree.json')
    session['decision_tree'] = decision_tree
    session['current_node'] = decision_tree
    session['decisions'] = []
    return redirect(url_for('index'))
