import random
from models import Incident

def present_incident(incidents):
    if not incidents:
        return None
    incident_data = random.choice(incidents)
    steps = [step for step in incidents if step['Name'] == incident_data['Name']]
    print(f"Incident: {incident_data['Name']}\nDescription: {incident_data['Description']}\nImpact: {incident_data['Impact']}\n")
    return Incident(incident_data['Name'], incident_data['Description'], incident_data['Impact'], steps)
