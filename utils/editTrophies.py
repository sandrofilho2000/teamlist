from xxlimited import new
from sql_commands import select_rows, update_rows


trophies = select_rows("id, season", "team_trophy where season like '%/%' ")

for trophy in trophies:
    id = trophy[0]
    season = trophy[1]
    
    if len(season) == 5:
        new_season = season.split("/")
        new_season = f"20{new_season[0]}/{new_season[1]}"
        update_rows("team_trophy", f"season = '{new_season}'", f"id = {id}")
        print(id, new_season)