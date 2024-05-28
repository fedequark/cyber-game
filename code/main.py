from read_csv import read_csv
from setup_company import setup_company
from setup_player import setup_player
from present_incident import present_incident
from take_action import take_action, evaluate_result, load_valid_actions
from models import Company, Player, Team

def generate_report_to_file(company, team, score, incident_history):
    report = []
    report.append("\n--- Final Report ---")
    report.append(f"Company: {company.name}")
    report.append(f"Size: {company.size}")
    report.append(f"Industry: {company.industry}")
    report.append(f"Infrastructure: {company.infrastructure}")
    report.append(f"Security Policies: {company.policies}")
    report.append(f"Compliance and Regulations: {company.compliance}")
    report.append("Player Profiles:")
    for player in team.players:
        report.append(f"Name: {player.name}, Role: {player.role}, Skills: {', '.join(player.skills)}")
    report.append(f"Final Score: {score}")
    report.append(f"Final Reputation: {company.reputation}")
    report.append(f"Final Financials: {company.financials}")
    report.append("Incident History:")
    for record in incident_history:
        report.append(f"Incident: {record['Incident']}, Step: {record['Step']}, Action Taken: {record['Action Taken']}, Result: {record['Result']}, Time: {record['Time']}, Resource Cost: {record['Resource Cost']}, Consequences: {record['Consequences']}")
    report.append("\n--- End of Report ---")
    
    with open("incident_report.txt", "w") as file:
        for line in report:
            file.write(line + "\n")

def print_successful_history(successful_history):
    print("\n--- Successful Actions History ---")
    for record in successful_history:
        print(f"Incident: {record['Incident']}, Step: {record['Step']}, Action Taken: {record['Action Taken']}, Result: {record['Result']}, Consequences: {record['Consequences']}")
    print("\n--- End of Successful Actions History ---")

def main():
    # Read CSV files
    company_config = read_csv('company_config.csv')
    player_config = read_csv('player_config.csv')
    incidents = read_csv('incidents.csv')
    actions = read_csv('actions.csv')
    valid_actions = load_valid_actions('incident_action_mapping.csv')
    
    # Offer random parameters
    random_choice = input("Do you want to use random parameters for the company and player? (1: yes, 2: no): ")
    randomize = random_choice == '1'
    
    # Setup company and player
    company = setup_company(company_config, randomize=randomize)
    team = setup_player(player_config, randomize=randomize)
    
    # Display company and player profiles
    print("\n--- Company Profile ---")
    print(f"Name: {company.name}")
    print(f"Size: {company.size}")
    print(f"Industry: {company.industry}")
    print(f"Infrastructure: {company.infrastructure}")
    print(f"Security Policies: {company.policies}")
    print(f"Compliance and Regulations: {company.compliance}")
    
    print("\n--- Player Profiles ---")
    for player in team.players:
        print(f"Name: {player.name}")
        print(f"Role: {player.role}")
        print(f"Skills: {', '.join(player.skills)}\n")
    
    score = 0
    incident_history = []
    successful_history = []
    while company.resources['financial'] > 0 and company.resources['human'] > 0 and company.resources['technological'] > 0:
        incident = present_incident(incidents)
        if not incident:
            print("No more incidents to handle.")
            break

        for step in range(1, 4):  # Assuming each incident has exactly 3 steps
            taken_actions = []
            while len(taken_actions) < len(valid_actions[incident.name][str(step)]):
                if any(res <= 0 for res in company.resources.values()):
                    print("Resources depleted. Game over.")
                    break

                action_success, action_score, actions_options, selected_actions, taken_actions, action_time, resource_cost, consequences = take_action(incident, step, team, actions, valid_actions, taken_actions, company.resources)
                evaluate_result(incident, action_success, consequences, company)
                score += action_score
                for res, cost in resource_cost.items():
                    company.resources[res] -= cost
                incident.time_taken += action_time
                
                # Save to incident history
                for action_index in selected_actions:
                    result = "Successful" if action_success else "Failed"
                    incident_history.append({
                        "Incident": incident.name,
                        "Step": step,
                        "Action Taken": actions_options[action_index],
                        "Result": result,
                        "Time": action_time,
                        "Resource Cost": str(resource_cost),
                        "Consequences": ', '.join(consequences)
                    })
                    # Save only successful actions to the successful history
                    if result == "Successful":
                        successful_history.append({
                            "Incident": incident.name,
                            "Step": step,
                            "Action Taken": actions_options[action_index],
                            "Result": result,
                            "Consequences": ', '.join(consequences)
                        })
                
                print(f"Current Score: {score}")
                print(f"Remaining Resources: {company.resources}")
                print(f"Reputation: {company.reputation}")
                print(f"Financials: {company.financials}")
        
        if any(res <= 0 for res in company.resources.values()):
            print("Resources depleted. Game over.")
            break

        print(f"Completed all actions for {incident.name}.")
        continue_game = input("Do you want to continue with the next incident? (1: yes, 2: no): ")
        if continue_game != '1':
            break
    
    # Generate final report to file
    generate_report_to_file(company, team, score, incident_history)
    
    # Print successful history to screen
    print_successful_history(successful_history)

if __name__ == "__main__":
    main()
