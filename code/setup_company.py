import random
from models import Company

def setup_company(company_config, randomize=False):
    print("Company Setup")
    
    if randomize:
        name = "Random Company " + str(random.randint(1, 100))
    else:
        name = input("Company Name: ")
    
    # Company Size
    size_options = [item['Option'] for item in company_config if item['Field'] == 'Company Size']
    if randomize:
        size = random.choice(size_options)
    else:
        print("Company Size:")
        for i, size in enumerate(size_options, 1):
            print(f"{i}. {size}")
        while True:
            try:
                size = size_options[int(input("Select the size (1, 2, 3, ...): ")) - 1]
                break
            except (IndexError, ValueError):
                print("Invalid input. Please select a valid option.")
    
    # Industry
    industry_options = [item['Option'] for item in company_config if item['Field'] == 'Industry']
    if randomize:
        industry = random.choice(industry_options)
    else:
        print("Industry:")
        for i, industry in enumerate(industry_options, 1):
            print(f"{i}. {industry}")
        while True:
            try:
                industry = industry_options[int(input("Select the industry (1, 2, 3, ...): ")) - 1]
                break
            except (IndexError, ValueError):
                print("Invalid input. Please select a valid option.")
    
    # Infrastructure
    if randomize:
        infrastructure = {
            "servers": random.randint(1, 20),
            "IoT devices": random.randint(1, 50),
            "cloud services": random.choice(["AWS", "Azure", "Google Cloud", "IBM Cloud", "Oracle Cloud"]),
            "databases": random.choice(["SQL", "NoSQL", "Mixed"]),
            "security software": random.choice(["Norton", "McAfee", "Kaspersky", "Bitdefender"])
        }
    else:
        infrastructure = {
            "servers": int(input("Number of servers: ")),
            "IoT devices": int(input("Number of IoT devices: ")),
            "cloud services": input("Cloud services (AWS, Azure, Google Cloud, etc.): "),
            "databases": input("Types of databases (SQL, NoSQL, etc.): "),
            "security software": input("Security software used: ")
        }
    
    # Security Policies
    policies_options = [item['Option'] for item in company_config if item['Field'] == 'Security Policies']
    if randomize:
        policies = random.sample(policies_options, k=random.randint(1, len(policies_options)))
    else:
        print("Security Policies (select multiple, separated by commas):")
        for i, policy in enumerate(policies_options, 1):
            print(f"{i}. {policy}")
        while True:
            try:
                selected_policies = input("Select policies (1, 2, 3, ...): ").split(",")
                policies = [policies_options[int(policy.strip()) - 1] for policy in selected_policies]
                break
            except (IndexError, ValueError):
                print("Invalid input. Please select valid options.")
    
    # Compliance and Regulations
    compliance_options = [item['Option'] for item in company_config if item['Field'] == 'Compliance and Regulations']
    if randomize:
        compliance = random.sample(compliance_options, k=random.randint(1, len(compliance_options)))
    else:
        print("Compliance and Regulations (select multiple, separated by commas):")
        for i, compliance in enumerate(compliance_options, 1):
            print(f"{i}. {compliance}")
        while True:
            try:
                selected_compliance = input("Select regulations (1, 2, 3, ...): ").split(",")
                compliance = [compliance_options[int(comp.strip()) - 1] for comp in selected_compliance]
                break
            except (IndexError, ValueError):
                print("Invalid input. Please select valid options.")
    
    return Company(name, size, industry, infrastructure, policies, compliance)
