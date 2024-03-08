import traceback
from turtle import update
from numpy import insert
import requests
import re
from bs4 import BeautifulSoup
import concurrent.futures

from slugify import slugify
from passToFloat import pass_to_float

from sql_commands import insert_rows, select_rows, update_rows
from slugfy import slugfy


trophies_added = []
trophy_id = 0

def get_trophies(letter):
    global trophy_id
    
    teams = select_rows("id, trophies_link, name", f"teams_team where trophies_link is not null and name like '{letter}%' and trophies_link != ''")


    for team in teams:
        id = team[0]
        link = team[1]
        team_name = team[2]

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        try:
            response = requests.get(link, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                div = soup.find("div", "large-8")
                trophies_box = div.find_all("div", "box")
                for trophy_box in trophies_box:
                    trophy_name = trophy_box.find("h2").text
                    trophy_name = trophy_name.split("x")[1]
                    trophy_name = trophy_name.replace("Vencedor", "").replace("Campeão de", "").replace("Campeão da", "").replace("Winner", "").strip()
                    trophy_slug = slugfy(trophy_name)
                    trophy_img = trophy_box.find("img").get("src")
                    
                    trophie_added = select_rows("count(*)", "trophies_trophy where img = '{trophy_img}'")
                    if trophie_added[0][0] == 0:
                        trophy_id += 1
                        insert_rows("trophies_trophy", "(id, name, slug, img)", f"""
                                (
                                    "{trophy_id}",
                                    "{trophy_name}",
                                    "{trophy_slug}",
                                    "{trophy_img}"
                                )
                        """)
                                                
                    trophy_seasons = trophy_box.find("div", "erfolg_infotext_box").text
                    trophy_seasons = trophy_seasons.split(",")
                    

                    for trophy_season in trophy_seasons:
                        if trophy_season:
                            insert_rows("team_trophy", "(id_team_id, season, trophy_img)", f"""
                                    (
                                        "{id}",
                                        "{trophy_season.strip()}",
                                        "{trophy_img}"
                                    )
                            """)
                        
                        
                    
        except Exception as e:
            print(e)     
                      
        print(f"Taças de {team_name} adicionadas\n\n\n")
        
        


functions_to_run = []               
                
import string
for letter in string.ascii_lowercase:
    # Add tuple with get_players function and current letter as parameter to the list
    functions_to_run.append((get_trophies, letter))


with concurrent.futures.ThreadPoolExecutor(max_workers=27) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func, param) for func, param in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]