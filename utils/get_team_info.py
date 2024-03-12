import os
import sys
import traceback
from turtle import update
from numpy import save
import requests
import re
from bs4 import BeautifulSoup

from slugify import slugify

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from teams.utils.get_imgs import download_image
from teams.utils.passToFloat import pass_to_float
from teams.utils.slugfy import *
from teams.utils.sql_commands import *


players_link = []
teams_link_error = ""
players_link_error = ""


def get_player_img(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        
        div = soup.find("div", class_="data-header__profile-container")
        img = div.find("img").get("src")
        
        if img:
            return img
        
        else:
            return ""
        
    else:
        return ""

def get_players(url, slug, team_id = 0):
    global teams_link_error, players_link_error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            team = {}
            header = soup.find("header", "data-header")
            header_li = header.find("div", "data-header__details").find_all("ul", "data-header__items")[1].find_all("li", "data-header__label")[1]
            stadium = {}
            stadium['name'] = header_li.find("a").text.strip()
            stadium['link'] = "https://www.transfermarkt.com.br"+header_li.find("a").get("href")
            stadium_id = select_rows("MAX(id)", "stadiums_stadium")[0][0]
            
            if not stadium_id:
                stadium_id = 0
                
            print(stadium_id)
            insert_rows("stadiums_stadium", "(id, name, link)", f"""
                            (
                                "{stadium_id + 1}",
                                "{stadium['name']}",
                                "{stadium['link']}"
                            )""")
            
            
            
            
            update_rows("teams_team", f"id_stadium_id = '{stadium_id}'", f"id = {team_id}")
            
            
            div = soup.find("div", class_="data-header__profile-container")
            main = soup.find("main")
            team["img"] = div.find("img").get("src")

            download_image(team["img"], f"{slug}{team_id}.png")

            
            try:
                table = main.find("div", class_="responsive-table")
                trs = table.find_all("tr")
                
                for tr in trs:
                    tr_table = tr.find("table")
                    if tr_table:
                        try:
                            player = {}
                            player["name"] = tr_table.find("td", "hauptlink").text.strip()
                            player["link"] = tr_table.find("a").get("href")
                            player["img"] = get_player_img("https://www.transfermarkt.com.br"+player["link"])
                            player["pos"] = tr_table.find_all('tr')[1].text.strip()
                            player["id_team_id"] = team_id
                            player["slug"] = slugify(player["name"])
                            player["num"] = tr.find_all("td", "zentriert")[0].text.strip()
                            player["birthdate"] = tr.find_all("td", "zentriert")[1].text.strip()
                            player["country_flag"] = tr.find_all("td", "zentriert")[2].find("img").get("src")
                            player["country_name"] = tr.find_all("td", "zentriert")[2].find("img").get("title")
                            player["value_market"] = pass_to_float(tr.find("td", "rechts").text.strip())
                            
                            
                            insert_rows("players_player", "(name, slug, img, link, pos, id_team_id, num, birthdate, country_flag, country_name, value_market)", f"""
                            (
                                "{player['name']}",
                                "{player['slug']}",
                                "{player['img']}",
                                "{player['link']}",
                                "{player['pos']}",
                                "{player['id_team_id']}",
                                "{player['num']}",
                                "{player['birthdate']}",
                                "{player['country_flag']}",
                                "{player['country_name']}",
                                "{player['value_market']}"
                            )""")
                            
                        except Exception as e:
                            players_link_error += """
                                {link}
                            """
                        
                            print(e)
            except Exception as e:
                # Handling the exception
                print("An error occurred:", e)
                traceback.print_exc()
                teams_link_error += """
                    {link}
                """
        except Exception as e:
            # Handling the exception
            print("An error occurred:", e)
            traceback.print_exc()
      
    





    

def get_stadium(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        



teams = select_rows("teams_team.id, teams_team.slug, teams_team.link ,teams_team.name", """teams_team
LEFT JOIN players_player ON teams_team.id = players_player.id_team_id
GROUP BY teams_team.id, teams_team.name
HAVING COUNT(players_player.id) = 0 """)


    
for team in teams:
    id = team[0]
    slug = team[1]
    link = team[2]
    link = link.replace("br//", "/")
    link = link.replace("saison_id/2023", "")
    name = team[3]
    print(link, slug, id)
    get_players(link, slug, id)
    print(f"Jogadores do { name } adicionados")
    
    

    
    
