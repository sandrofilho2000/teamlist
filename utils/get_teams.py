import os
import sys
import requests
import re
from bs4 import BeautifulSoup

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)




teams_link =[]

sql_teams_command = """
DROP TABLE teams_team ;
CREATE TABLE teams_team (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        slug VARCHAR(255) NOT NULL,
        link VARCHAR(255) NOT NULL,
        small_img VARCHAR(255) NOT NULL,
        average_market_value REAL,
        total_market_value REAL,
        country_name VARCHAR(255) NOT NULL,
        country_img VARCHAR(255) NOT NULL
);

INSERT INTO teams_team (id, name, slug, link, small_img, average_market_value, total_market_value, country_name, country_img)
VALUES 

"""

sql_leagues_teams_command = """
DROP TABLE leagues_teams ;
CREATE TABLE leagues_teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_league INTEGER,
    id_team INTEGER,
    FOREIGN KEY (id_league) REFERENCES leagues_league(id),
    FOREIGN KEY (id_team) REFERENCES teams_team(id)
);

INSERT INTO leagues_teams (id_league, id_team)
VALUES 

"""

    

def get_team(url, id, country_name , country_img, id_league):
    global sql_leagues_teams_command
    global sql_teams_command
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    

            
            
        

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        div = soup.find("div", class_="responsive-table")
        table = div.find("table")
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")
        
        for tr in trs:
            id+=1
            
            try:
                
                team = {}
                team['id'] = id
                team['name'] = tr.find("td", class_="hauptlink no-border-links").text.strip()
                team['slug'] = slugfy(team["name"])
                team['link'] = "https://www.transfermarkt.com.br/" + tr.find("a").get("href")
                team['small_img'] = tr.find("img", class_="tiny_wappen").get("src")
                team['average_market_value'] = pass_to_float(tr.find_all("td", class_="rechts")[0].text.strip())
                team['total_market_value'] = pass_to_float(tr.find_all("td", class_="rechts")[1].text.strip())
                team['country_name'] = country_name
                team['country_img'] = country_img
            
                if team['link'] not in teams_link:
                    teams_link.append(team['link'])
                    sql_teams_command += f"""
                    
                            (
                            '{team["id"]}',
                            '{team["name"]}',
                            '{team["slug"]}',
                            '{team["link"]}',
                            '{team["small_img"]}',
                            '{team["average_market_value"]}',
                            '{team["total_market_value"]}',
                            '{team["country_name"]}',
                            '{team["country_img"]}'
                            ) ,               
                        """

                    print(f'Equipe {team["name"]} Adicionada!') 
                    
                sql_leagues_teams_command += f"""
                        (
                        '{id_league}',
                        '{team["id"]}'
                        ) ,               
                    """
            except:
                print("Element not found")




leagues = select_rows("id, name, link, country_name, country_img", "leagues_league")

id = 0

for league in leagues:    
    id_league = league[0]
    link = league[2]
    country_name = league[3]
    country_img = league[4]
    
    teams = get_team(link, id, country_name, country_img, id_league)
    id = len(teams_link)



teams_file = "teams.sql"
with open(teams_file, "w", encoding="utf-8") as file:
    file.write(sql_teams_command)

teams_file = "leagues_team.sql"
with open(teams_file, "w", encoding="utf-8") as file:
    file.write(sql_leagues_teams_command)