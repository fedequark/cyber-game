import random
from models import Player, Team

def setup_player(player_config, randomize=False):
    players = []
    if randomize:
        player_config_sample = random.sample(player_config, k=min(3, len(player_config)))  # Seleccionar aleatoriamente hasta 3 jugadores
    else:
        player_config_sample = player_config
    
    for player_data in player_config_sample:
        name = player_data.get('Name', 'Unknown')
        role = player_data.get('Role', 'Unknown')
        skills = player_data.get('Skills', '')
        
        if skills:
            skills = skills.split(', ')
        else:
            skills = []

        players.append(Player(name, role, skills))
    
    return Team(players)
