from flask import Blueprint, render_template, session

profile_bp = Blueprint('profile', __name__, url_prefix='/profile')

@profile_bp.route('/')
def profile():
    industry = session.get('industry')
    size = session.get('size')
    security_budget = session.get('security_budget')
    maturity_level = session.get('maturity_level')
    critical_assets_data = session.get('critical_assets_data', [])
    critical_assets_systems = session.get('critical_assets_systems', [])
    compliance_requirements = session.get('compliance_requirements', [])
    technologies_used = session.get('technologies_used', [])
    security_policies = session.get('security_policies', [])
    
    return render_template('profile.html', 
                           industry=industry, size=size, 
                           security_budget=security_budget, 
                           maturity_level=maturity_level, 
                           critical_assets_data=critical_assets_data, 
                           critical_assets_systems=critical_assets_systems, 
                           compliance_requirements=compliance_requirements, 
                           technologies_used=technologies_used, 
                           security_policies=security_policies)
