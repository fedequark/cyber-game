from flask import Blueprint, render_template, session

confirmation_bp = Blueprint('confirmation', __name__)

@confirmation_bp.route('/confirmation')
def confirmation():
    player_configured = all(key in session for key in [
        'player_name', 'player_role', 'experience_level', 'technical_skills', 'non_technical_skills'
    ])
    company_configured = all(key in session for key in [
        'industry', 'size', 'security_budget', 'maturity_level',
        'critical_assets_data', 'critical_assets_systems', 'compliance_requirements',
        'technologies_used', 'security_policies'
    ])
    return render_template('confirmation.html',
                           player_configured=player_configured,
                           company_configured=company_configured,
                           player_name=session.get('player_name'),
                           player_role=session.get('player_role'),
                           experience_level=session.get('experience_level'),
                           technical_skills=session.get('technical_skills'),
                           non_technical_skills=session.get('non_technical_skills'),
                           industry=session.get('industry'),
                           size=session.get('size'),
                           security_budget=session.get('security_budget'),
                           maturity_level=session.get('maturity_level'),
                           critical_assets_data=session.get('critical_assets_data'),
                           critical_assets_systems=session.get('critical_assets_systems'),
                           compliance_requirements=session.get('compliance_requirements'),
                           technologies_used=session.get('technologies_used'),
                           security_policies=session.get('security_policies'))
