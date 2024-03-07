import os
import sys

root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

import traceback
import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures

from slugify import slugify
from passToFloat import pass_to_float

from sql_commands import insert_rows, select_rows, update_rows




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
    
    

def get_players(link, team_id = 0, players=[], id_country_id = 0, country_flag="", country_name = "", team_name=""):
    global teams_link_error, players_link_error
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    response = requests.get(link, headers=headers)

    if response.status_code == 200:
        try:
            soup = BeautifulSoup(response.content, "html.parser")
            main = soup.find("main")
                        
            try:
                table = main.find("div", class_="responsive-table")
                trs = table.find_all("tr")
                
                for tr in trs:
                    tr_table = tr.find("table")
                    if tr_table:
                        try:
                            player = {}
                            player["name"] = tr_table.find("td", "hauptlink").text.strip()
                            
                            if(player["name"] not in players):

                                player["link"] = tr_table.find("a").get("href")
                                player["img"] = get_player_img("https://www.transfermarkt.com.br"+player["link"])
                                player["pos"] = tr_table.find_all('tr')[1].text.strip()
                                player["id_team_id"] = team_id
                                player["id_country_id"] = id_country_id
                                player["slug"] = slugify(player["name"])
                                player["num"] = tr.find_all("td", "zentriert")[0].text.strip()
                                player["birth"] = tr.find_all("td", "zentriert")[1].text.strip()
                                player["value_market"] = pass_to_float(tr.find("td", "rechts").text.strip())
                                
                                insert_rows("players_player", "(name, slug, img, link, pos, id_country_id, id_team_id, num, birth, country_flag, country_name, value_market)", f"""
                                (
                                    "{player['name']}",
                                    "{player['slug']}",
                                    "{player['img']}",
                                    "{player['link']}",
                                    "{player['pos']}",
                                    "{player['id_country_id']}",
                                    "{player['id_team_id']}",
                                    "{player['num']}",
                                    "{player['birth']}",
                                    "{country_flag}",
                                    "{country_name}",
                                    "{player['value_market']}"
                                )""")
                                
                                print("\t", player["name"], "adicionado")

                            
                            else:
                                print("")
                                
                        except Exception as e:
                            players_link_error += """
                                {link}
                            """
                        
                            print("An error occurred:", e)
                            traceback.print_exc()
            
                    print(f"Jogadores do { team_name } adicionados\n\n")

            except Exception as e:
                # Handling the exception
                print("An error occurred:", e)
                traceback.print_exc()
                
                
            try:
                trophies_link = main.find("div", "data-header__badge-container").find("a").get("href")
                if trophies_link:
                    trophies_link = "https://www.transfermarkt.com.br"+trophies_link
                    update_rows("teams_team", f"trophies_link='{trophies_link}'", f"id='{team_id}'" )

            except:
                print("ERRO AO ATUALIZAR CLUBE")
                pass 

        except Exception as e:
            # Handling the exception
            print("An error occurred:", e)
            traceback.print_exc()
      
    





    

        







def get_players_by_letter(letter):
    teams = select_rows("id, link, name, id_country_id, country_img, country_name", f"teams_team")
    
    try:
        for team in teams:
            players_sql = select_rows("name", f"players_player where id_team_id = '{team[0]}'")
            if(len(players_sql) < 20):
            
                id = team[0]
                link = team[1].replace(".br//", ".br/")
                name = team[2]
                id_country_id = team[3]
                country_flag = team[4]
                country_name = team[5]
                
                players = []
                
                for player in players_sql:
                    players.append(player[0])
                    
                get_players(link, id, players, id_country_id,country_flag, country_name, name)
    except:
        print("Error")
        
        
       

functions_to_run = [
    (get_players_by_letter, "a")
]

with concurrent.futures.ThreadPoolExecutor(max_workers=27) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func, param) for func, param in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]