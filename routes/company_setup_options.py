from flask import Blueprint, render_template

company_setup_options_bp = Blueprint('company_setup_options', __name__)

@company_setup_options_bp.route('/company_setup_options')
def company_setup_options():
    return render_template('company_setup_options.html')
