from flask import Blueprint, render_template

setup_options_bp = Blueprint('setup_options', __name__)

@setup_options_bp.route('/setup_options')
def setup_options():
    return render_template('setup_options.html')
