from time import sleep
from sql_commands import select_rows, update_rows


players = select_rows("p.id, p.name, p.birthdate, t.name", "players_player as p INNER JOIN teams_team as t ON p.id_team_id = t.id; ")

for player in players:
    player_id = player[0]
    player_name = player[1]
    team_name = player[3]
