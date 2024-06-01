from flask import Blueprint, render_template

player_setup_options_bp = Blueprint('player_setup_options', __name__)

@player_setup_options_bp.route('/player_setup_options')
def player_setup_options():
    return render_template('player_setup_options.html')
