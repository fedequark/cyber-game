class Company:
    def __init__(self, name, size, industry, infrastructure, policies, compliance):
        self.name = name
        self.size = size
        self.industry = industry
        self.infrastructure = infrastructure
        self.policies = policies
        self.compliance = compliance
        self.resources = {'financial': 100, 'human': 50, 'technological': 30}  # Diferentes tipos de recursos
        self.reputation = 100  # Initial reputation score
        self.financials = 100  # Initial financial health

class Player:
    def __init__(self, name, role, skills):
        self.name = name
        self.role = role
        self.skills = skills

class Team:
    def __init__(self, players):
        self.players = players

class Incident:
    def __init__(self, name, description, impact, steps):
        self.name = name
        self.description = description
        self.impact = impact
        self.steps = steps
        self.current_step = 1
        self.time_taken = 0
        self.substeps = []  # List to hold substeps for each step
        self.consequences = []  # List to hold consequences of actions

class Action:
    def __init__(self, name, description, time, resource_cost):
        self.name = name
        self.description = description
        self.time = time
        self.resource_cost = resource_cost
