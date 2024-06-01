from flask import Blueprint, session, redirect, url_for

handle_decision_bp = Blueprint('handle_decision', __name__)

@handle_decision_bp.route('/handle_decision')
def handle_decision():
    # Aquí iría la lógica para manejar las decisiones del juego
    return redirect(url_for('conclusion.conclusion'))
