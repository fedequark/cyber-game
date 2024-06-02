from app import app, db
from models import Scenario, Option

with app.app_context():
    db.create_all()
    
    # Crear escenario inicial
    scenario1 = Scenario(question="¿Has detectado un posible incidente de seguridad?")
    db.session.add(scenario1)
    db.session.commit()

    # Opciones para el escenario inicial
    option1 = Option(text="Sí, ha ocurrido un incidente", scenario_id=scenario1.id, next_scenario_id=2)
    option2 = Option(text="No, es una falsa alarma", scenario_id=scenario1.id, conclusion="No se detectó ningún incidente real. No se requieren acciones adicionales.")
    db.session.add_all([option1, option2])
    db.session.commit()

    # Crear segundo escenario
    scenario2 = Scenario(question="Evalúa la gravedad del incidente")
    db.session.add(scenario2)
    db.session.commit()

    # Opciones para el segundo escenario
    option3 = Option(text="Alto riesgo (ataque ransomware activo)", scenario_id=scenario2.id, next_scenario_id=3)
    option4 = Option(text="Riesgo medio (intento de phishing sin éxito)", scenario_id=scenario2.id, next_scenario_id=4)
    option5 = Option(text="Bajo riesgo (malware detectado y contenido)", scenario_id=scenario2.id, next_scenario_id=5)
    db.session.add_all([option3, option4, option5])
    db.session.commit()

    # Crear más escenarios y opciones según sea necesario

    # Escenario de alto riesgo
    scenario3 = Scenario(question="Elige una acción inicial adecuada")
    db.session.add(scenario3)
    db.session.commit()

    # Opciones para el escenario de alto riesgo
    option6 = Option(text="Aislar la red afectada (Perfil Técnico)", scenario_id=scenario3.id, next_scenario_id=6)
    option7 = Option(text="Notificar al equipo de TI (Perfil No Técnico)", scenario_id=scenario3.id, next_scenario_id=7)
    db.session.add_all([option6, option7])
    db.session.commit()

    # Continúa agregando más escenarios y opciones según sea necesario
