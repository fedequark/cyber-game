from flask import Blueprint, render_template, request, redirect, url_for

handle_decision_bp = Blueprint('handle_decision', __name__)

@handle_decision_bp.route('/handle_decision', methods=['GET', 'POST'])
def handle_decision():
    if request.method == 'POST':
        decision_text = request.form.get('decision_text')
        # Lógica para manejar la decisión tomada
        return redirect(url_for('conclusion.conclusion'))  # Redirigir a la conclusión después de la decisión
    node = {
        'options': [
            {'text': 'Opción 1'},
            {'text': 'Opción 2'},
            {'text': 'Opción 3'}
        ]
    }
    return render_template('decision.html', node=node)
