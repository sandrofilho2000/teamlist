from sql_commands import select_rows, update_rows


trophies = select_rows("id, season", "team_trophy where season like '% %'")

for trophy in trophies:
    print(trophy[1].strip())
    update_rows("team_trophy", f"season = {trophy[1].strip()}", f"id={trophy[0]}")