
import os
import sys
import sqlite3
from sqlite3 import Error


root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)




        
      
conn = sqlite3.connect(r"C:\xampp\htdocs\Not legacy\Python\Futeapp\db.sqlite3")
cur = conn.cursor()



def select_rows(query):
    global cur
    rows = cur.fetchall()
    conn.close()
    return rows
  
  
teams = select_rows("""SELECT teams_team.id, teams_team.slug, teams_team.link
FROM teams_team
    LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
    WHERE teams_team.name LIKE 'a%' 
    GROUP BY teams_team.id, teams_team.name
    HAVING COUNT(players_player.id) < 12;
""")


for team in teams:
    print(team)