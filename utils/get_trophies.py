import math
import random
from uu import Error
import concurrent.futures
from slugify import slugify
from sql_commands import insert_rows, select_rows, update_rows
import requests
import re
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

def get_trophies(link, team_id):
    trophy_id = select_rows("max(id)", "trophies_trophy")[0][0]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(link, headers=headers)
    

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        div = soup.find("div", "large-8")
        trophies_box = div.find_all("div", "box")
        
        for trophy_box in trophies_box:
            trophy_img = trophy_box.find("img").get("src")
            trophie_added = select_rows("count(*)", f"team_trophy where trophy_img = '{trophy_img}'")
            
            if trophie_added[0][0] == 0:
                trophy_name = trophy_box.find("h2").text
                trophy_name = trophy_name.split("x")[1]
                trophy_name = trophy_name.replace("Vencedor", "").replace("Campeão de", "").replace("Campeão da", "").replace("Winner", "").strip()
                trophy_slug = slugify(trophy_name)
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
                                "{team_id}",
                                "{trophy_season.strip()}",
                                "{trophy_img}"
                            )
                    """)
                    
                    
                
  
                    
    

def get_trophy_count(letter):
    
    teams = select_rows("id, name, trophies_link", f"teams_team where trophies_link is not null and trophies_link != '' and name like '%{letter}%'")

    for team in teams:
        team_id = team[0]
        team_name = team[1]
        trophies_link = team[2]

        trophies_count = 0
        
        trophies = select_rows(f"""tt.id_trophy_id,
            COUNT(tt.id_trophy_id) AS trophy_count,
            tr.img""", f"""
            team_trophy AS tt
            JOIN trophies_trophy AS tr ON tt.id_trophy_id = tr.id
            WHERE tt.id_team_id = {team_id}
            GROUP BY tt.id_trophy_id, tr.img;""")
        
        for trophy in trophies:
            trophies_count += int(trophy[1])
                
        response = requests.get(trophies_link, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            boxes = soup.find_all("div", "erfolg_infotext_box")
            count = 0
            for box in boxes:
                count += len(box.text.split(","))
                
            if trophies_count < count:
                get_trophies(trophies_link, team_id)
                
            else:
                print("TODOS OS TÍTULOS FORAM ADICIONADOS")
                



    
    
    
functions_to_run = []               
                
import string
for letter in string.ascii_lowercase:
    # Add tuple with get_players function and current letter as parameter to the list
    functions_to_run.append((get_trophy_count, letter))


with concurrent.futures.ThreadPoolExecutor(max_workers=27) as executor:
    # Submit each function to the executor
    futures = [executor.submit(func, param) for func, param in functions_to_run]

    # Wait for all functions to complete
    concurrent.futures.wait(futures)

    # Optionally, retrieve the results if the functions return anything
    results = [future.result() for future in futures]

    
