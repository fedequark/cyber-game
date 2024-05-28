from read_csv import read_csv

def load_valid_actions(mapping_file):
    valid_actions = {}
    mapping_data = read_csv(mapping_file)

    for row in mapping_data:
        try:
            incident = row['Incident']
            step = row['Step']
            substep = row['Substep']
            action = row['Action']
            consequence = row['Consequence']
            time = row['Time']
            resource_cost = row['Resource Cost']
            
            if incident not in valid_actions:
                valid_actions[incident] = {}
            if step not in valid_actions[incident]:
                valid_actions[incident][step] = []
            try:
                resource_cost = eval(str(resource_cost))  # Convertir la cadena a diccionario
            except (SyntaxError, NameError):
                print(f"Error evaluating resource cost: {resource_cost}")
                resource_cost = {'financial': 0, 'human': 0, 'technological': 0}  # Valor por defecto en caso de error
            valid_actions[incident][step].append({
                'Action': action,
                'Substep': substep,
                'Consequence': consequence,
                'Time': time,
                'Resource Cost': resource_cost
            })
        except KeyError as e:
            print(f"Skipping invalid row: {row} (missing key {e})")
    return valid_actions

def take_action(incident, step, team, actions, valid_actions, taken_actions, remaining_resources):
    print(f"Step {step} of {incident.name}")
    print("Available Actions:")
    actions_options = [item['Action'] for item in actions]
    for i, action in enumerate(actions_options, 1):
        print(f"{i}. {action}")
    
    while True:
        try:
            selected_actions = input("Select actions (1, 2, 3, ...): ").split(",")
            selected_actions = [int(action.strip()) - 1 for action in selected_actions]
            actions_taken = [actions_options[action] for action in selected_actions]
            break
        except (IndexError, ValueError):
            print("Invalid input. Please select valid options.")
    
    action_successes = []
    scores = []
    total_time = 0
    total_cost = {'financial': 0, 'human': 0, 'technological': 0}
    consequences = []

    for action in actions_taken:
        action_data = next((item for item in valid_actions[incident.name][str(step)] if item['Action'] == action), None)
        
        if not action_data:
            print(f"The action '{action}' is not effective for the incident '{incident.name}', step {step}.")
            action_successes.append(False)
            scores.append(-5)  # Asignar una puntuación negativa para una acción inválida
            continue

        action_time = int(action_data['Time'])
        resource_cost = action_data['Resource Cost']  # Ya está convertido a diccionario
        consequence = action_data['Consequence']
        
        if any(remaining_resources[res] < cost for res, cost in resource_cost.items()):
            print(f"Not enough resources for the action '{action}'")
            action_successes.append(False)
            scores.append(0)  # No score if not enough resources
            break

        total_time += action_time
        for res, cost in resource_cost.items():
            total_cost[res] += cost
        consequences.append(consequence)
        
        if action not in taken_actions:
            print(f"The action '{action}' is valid for the incident '{incident.name}', step {step}.")
            action_successes.append(True)
            scores.append(10)  # Assign a positive score for a valid action
            taken_actions.append(action)
        else:
            print(f"The action '{action}' has already been taken for the incident '{incident.name}', step {step}.")
            action_successes.append(False)
            scores.append(0)  # No score for a repeated valid action

    return all(action_successes), sum(scores), actions_options, selected_actions, taken_actions, total_time, total_cost, consequences

def evaluate_result(incident, action_success, consequences, company):
    if action_success:
        print(f"You have successfully managed the step of {incident.name}. The impact has been mitigated.")
        print(f"Consequences: {', '.join(consequences)}")
        for consequence in consequences:
            if consequence == "Partial containment":
                company.reputation += 5
                company.financials -= 5
            elif consequence == "Identify the source":
                company.reputation += 10
                company.financials += 5
            elif consequence == "Data restoration":
                company.reputation += 15
                company.financials += 10
    else:
        print(f"You have not effectively managed the step of {incident.name}. The impact persists.")
        print(f"Consequences: {', '.join(consequences)}")
        company.reputation -= 10
        company.financials -= 10
