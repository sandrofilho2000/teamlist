import os
import sys


root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from teams.utils.get_team_info import get_players
from teams.utils.sql_commands import select_rows


def get_players_letter():
    teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) > 10""")
    
    print(teams)
    
"""     for team in teams:
        id = team[0]
        slug = team[1]
        link = team[2]
        link = link.replace("br//", "/")
        link = link.replace("saison_id/2023", "")
        name = team[3]
        print(f"Adicionando jogadores do { name } ")
        get_players(link, slug, id)
        print(f"Jogadores do { name } adicionados") """
 
 
teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
GROUP BY teams_team.id, teams_team.name
HAVING COUNT(players_player.id) = 0""")

print(teams)